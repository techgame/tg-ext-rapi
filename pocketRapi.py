##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
##~ Copyright (C) 2002-2005  TechGame Networks, LLC.              ##
##~                                                               ##
##~ This library is free software; you can redistribute it        ##
##~ and/or modify it under the terms of the BSD style License as  ##
##~ found in the LICENSE file included with this distribution.    ##
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import StringIO
from ctypes import windll, FormatError, sizeof, byref 
from ctypes import c_buffer, c_ulong, c_char, c_wchar, Structure, POINTER

from ceFile import CEFile

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Constants / Variables / Etc. 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

INVALID_HANDLE_VALUE        = -1

GENERIC_EXECUTE             = 0x20000000
GENERIC_WRITE               = 0x40000000
GENERIC_READ                =-0x80000000

CREATE_NEW                  = 0x1
CREATE_ALWAYS               = 0x2
OPEN_EXISTING               = 0x3
OPEN_ALWAYS                 = 0x4

FILE_SHARE_READ             = 0x1
FILE_SHARE_WRITE            = 0x2
FILE_SHARE_DELETE           = 0x4

FILE_FLAG_POSIX_SEMANTICS   = 0x01000000
FILE_FLAG_BACKUP_SEMANTICS  = 0x02000000
FILE_FLAG_DELETE_ON_CLOSE   = 0x04000000
FILE_FLAG_SEQUENTIAL_SCAN   = 0x08000000
FILE_FLAG_RANDOM_ACCESS     = 0x10000000
FILE_FLAG_NO_BUFFERING      = 0x20000000
FILE_FLAG_OVERLAPPED        = 0x40000000
FILE_FLAG_WRITE_THROUGH     =-0x80000000

FILE_ATTRIBUTE_READONLY     = 0x0001
FILE_ATTRIBUTE_HIDDEN       = 0x0002
FILE_ATTRIBUTE_SYSTEM       = 0x0004
FILE_ATTRIBUTE_DIRECTORY    = 0x0010
FILE_ATTRIBUTE_ARCHIVE      = 0x0020
FILE_ATTRIBUTE_NORMAL       = 0x0080
FILE_ATTRIBUTE_TEMPORARY    = 0x0100
FILE_ATTRIBUTE_COMPRESSED   = 0x0800
FILE_ATTRIBUTE_OFFLINE      = 0x1000

FAF_ATTRIBUTES               = 0x00000001;
FAF_CREATION_TIME            = 0x00000002;
FAF_LASTACCESS_TIME          = 0x00000004;
FAF_LASTWRITE_TIME           = 0x00000008;
FAF_SIZE_HIGH                = 0x00000010;
FAF_SIZE_LOW                 = 0x00000020;
FAF_OID                      = 0x00000040;
FAF_NAME                     = 0x00000080;

FAF_FLAG_COUNT               = 8;

FAF_ATTRIB_CHILDREN          = 0x00001000;
FAF_ATTRIB_NO_HIDDEN         = 0x00002000;
FAF_FOLDERS_ONLY             = 0x00004000;
FAF_NO_HIDDEN_SYS_ROMMODULES = 0x00008000;

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Definitions 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MAX_PATH = 260

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class RAPIINIT(Structure):
    _fields_ = [
        ('cbSize', c_ulong),
        ('heRapiInitEvent', c_ulong),
        ('hrRapiInit', c_ulong), ]

class FILETIME(Structure):
    _fields_ = [
        ('nTimeHigh', c_ulong),
        ('nTimeLow', c_ulong), ]

class CE_FIND_DATA(Structure):
    _fields_ = [
        ('dwFileAttributes', c_ulong),
        ('ftCreationTime', FILETIME),
        ('dwLastAccessTime', FILETIME),
        ('dwLastWriteTime', FILETIME),
        ('nFileSizeHigh', c_ulong),
        ('nFileSizeLow', c_ulong),
        ('dwOID', c_ulong),
        ('cFileName', c_wchar*MAX_PATH), ]

class PROCESS_INFORMATION(Structure):
    _fields_ = [
        ('hProcess', c_ulong), 
        ('hThread', c_ulong), 
        ('dwProcessId', c_ulong), 
        ('dwThreadId', c_ulong), ]

class CEFileEx(CEFile): 
    raiseErrors = False

class PocketRapi(object):
    blockSize=65536
    _rapiReady = False
    _heRapiInitEvent = None
    raiseErrors = False
    CEFile = CEFileEx

    def __init__(self, blocking=False):
        self._loadRapiMethods()
        if blocking is not None:
            self.init(blocking)

    def __nonzero__(self):
        return self.isReady()

    def init(self, blocking=False):
        if blocking:
            self._rapiReady = (self._CeRapiInit_() == 0) # S_OK == 0
            return self._rapiReady

        self._rapiReady = None
        args = RAPIINIT()
        args.cbSize = sizeof(args)
        self._CeRapiInitEx_(byref(args))
        if args.hrRapiInit == 0: # S_OK
            self._heRapiInitEvent = args.heRapiInitEvent
            return True
        else: return False

    _isCELoaded = False
    @classmethod
    def _loadRapiMethods(klass):
        if klass._isCELoaded:
            return True
        rapi = windll.rapi

        klass._CeGetLastError = staticmethod(rapi.CeGetLastError)

        def CeErrorCheck(result, cfunc, args):
            ceErrorNo = rapi.CeGetLastError()
            if ceErrorNo and ceErrorNo != 183:
                if klass.raiseErrors:
                    raise OSError('%s %d (0x%x)' % (FormatError(ceErrorNo), ceErrorNo, ceErrorNo))
                else:
                    print OSError('%s %d (0x%x)' % (FormatError(ceErrorNo), ceErrorNo, ceErrorNo))
            return result

        klass._CeCloseHandle_ = staticmethod(rapi.CeCloseHandle)
        klass._CeCloseHandle_.errcheck = CeErrorCheck

        klass._CeCreateDirectory_ = staticmethod(rapi.CeCreateDirectory)
        klass._CeCreateDirectory_.errcheck = CeErrorCheck

        klass._CeCreateFile_ = staticmethod(rapi.CeCreateFile)
        klass._CeCreateFile_.errcheck = CeErrorCheck

        klass._CeCreateProcess_ = staticmethod(rapi.CeCreateProcess)
        klass._CeCreateProcess_.errcheck = CeErrorCheck

        klass._CeDeleteFile_ = staticmethod(rapi.CeDeleteFile)
        klass._CeDeleteFile_.errcheck = CeErrorCheck

        klass._CeFindAllFiles_ = staticmethod(rapi.CeFindAllFiles)
        klass._CeFindAllFiles_.errcheck = CeErrorCheck

        klass._CeGetFileAttributes_ = staticmethod(rapi.CeGetFileAttributes)
        #klass._CeGetFileAttributes_.errcheck = CeErrorCheck

        klass._CeRapiFreeBuffer_ = staticmethod(rapi.CeRapiFreeBuffer)
        klass._CeRapiFreeBuffer_.errcheck = CeErrorCheck

        klass._CeRapiGetError_ = staticmethod(rapi.CeRapiGetError)
        klass._CeRapiGetError_.errcheck = CeErrorCheck

        klass._CeRapiInit_ = staticmethod(rapi.CeRapiInit)
        klass._CeRapiInit_.errcheck = CeErrorCheck

        klass._CeRapiInitEx_ = staticmethod(rapi.CeRapiInitEx)
        #klass._CeRapiInitEx_.errcheck = CeErrorCheck

        klass._CeRapiUninit_ = staticmethod(rapi.CeRapiUninit)
        #klass._CeRapiUninit_.errcheck = CeErrorCheck

        klass._CeReadFile_ = staticmethod(rapi.CeReadFile)
        klass._CeReadFile_.errcheck = CeErrorCheck

        klass._CeRemoveDirectory_ = staticmethod(rapi.CeRemoveDirectory)
        klass._CeRemoveDirectory_.errcheck = CeErrorCheck

        klass._CeWriteFile_ = staticmethod(rapi.CeWriteFile)
        klass._CeWriteFile_.errcheck = CeErrorCheck

        klass._isCELoaded = True
        return True

    def isReady(self, timeout=0):
        if not self._rapiReady and self._heRapiInitEvent:
            self.waitForInit(timeout)
        return bool(self._rapiReady)

    def waitForInit(self, timeout=0):
        if not self._heRapiInitEvent:
            raise OSError("Event not initialized")

        miliseconds = min(0, max(int(timeout*1000), 0x7fffffff))
        events = (c_ulong*1)(self._heRapiInitEvent)
        waitResult = self.user32().MsgWaitForMultipleObjects(len(events), events, False, miliseconds, 0)

        if waitResult == 0:
            self._heRapiInitEvent = None
            self._rapiReady = True
        return self._rapiReady

    def uninit(self):
        self._CeRapiUninit_()
        self._rapiReady = False

    def getRapiError(self):
        return self._CeGetLastError_() or None
    def getRapiErrorStr(self):
        return FormatError(self.getRapiError())

    def joinPath(self, *args):
        args = filter(None, args)
        return '\\'.join(args or '')

    @staticmethod
    def user32(): 
        return windll.user32

    @staticmethod
    def rapi(): 
        return windll.rapi

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def rmFile(self, path):
        return self._CeDeleteFile_(unicode(path))

    def makeDirs(self, path):
        pathParts = path.replace('/', '\\').split('\\')
        partialPath = ''
        for part in pathParts:
            if partialPath:
                partialPath += '\\' + part
            else: partialPath = part
            if not self.exists(partialPath):
                self.mkDir(partialPath)
        return path
    def mkDir(self, path):
        return self._CeCreateDirectory_(unicode(path), None)
    def rmDir(self, path):
        return self._CeRemoveDirectory_(unicode(path))
    def rmTree(self, path):
        for entry in self.listFiles(path):
            if self.isFile(entry):
                self.rmFile(entry)
            elif self.isDir(entry):
                self.rmTree(entry)
            #else: # what the heck is it?
        self.rmDir(path)

    #~ List Utilities ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _joinPathsList(self, path, pathList, hasAttrs=False, keepAttrs=True):
        if hasAttrs:
            if keepAttrs:
                return [(self.joinPath(path, p[0]),) + p[1:] for p in pathList]
            else:
                return [self.joinPath(path, p[0]) for p in pathList]
        else:
            return [self.joinPath(path, p) for p in pathList]

    def list(self, path='', incAttrs=False):
        listing = self.findFiles(self.joinPath(path, '*'), incAttrs)
        return self._joinPathsList(path, listing, incAttrs)

    def listWithMask(self, path='', mask=-1, incAttrs=False):
        listing = self.findFilesWithMask(self.joinPath(path, '*'), mask, True)
        return self._joinPathsList(path, listing, True, incAttrs)

    def listFiles(self, path='', incAttrs=False):
        return self.list(path, incAttrs)

    def listDirs(self, path='', incAttrs=False):
        return self.listWithMask(path, FILE_ATTRIBUTE_DIRECTORY, incAttrs)

    def listTemporaryItems(self, path='', incAttrs=False):
        return self.listWithMask(path, FILE_ATTRIBUTE_TEMPORARY, incAttrs)

    def findFilesWithMask(self, path, mask, incAttrs=False):
        for f, a in self.findFiles(path, FAF_ATTRIBUTES):
            if a & mask > 0:
                if incAttrs:
                    yield f, a
                else:
                    yield f

    def findFiles(self, path, incAttrs=False):
        mask = FAF_NAME  # Fill in the filename field
        if incAttrs is True:
            mask |= FAF_ATTRIBUTES # fill in the attribute field
            mask |= FAF_SIZE_LOW | FAF_SIZE_HIGH
        elif incAttrs > 0:
            mask |= incAttrs

        result = []
        nCount = c_ulong(0)
        answer = POINTER(CE_FIND_DATA*32767)()
        try:
            self._CeFindAllFiles_(unicode(path), mask, byref(nCount), byref(answer))

            if answer:
                answer = answer[0] # deref the pointer
                for i in xrange(nCount.value):
                    a = answer[i]
                    if incAttrs:
                        r = [a.cFileName]
                        if mask & (FAF_SIZE_HIGH|FAF_SIZE_LOW):
                            r.append((a.nFileSizeHigh << 32) | a.nFileSizeLow)
                        if mask & FAF_ATTRIBUTES:
                            r.append(a.dwFileAttributes)
                        result.append(tuple(r))
                    else:
                        result.append(a.cFileName)
        finally:
            # free the memory they allocated for us
            if answer:
                self._CeRapiFreeBuffer_(byref(answer))
        return result
    
    def copyFileToDevice(self, hostFile, toPath,):
        if isinstance(hostFile, (str, unicode)):
            hostFile = open(hostFile, 'rb')

        #HANDLE CeCreateFile(
        #            LPCWSTR lpFileName, 
        #            DWORD dwDesiredAccess, 
        #            DWORD dwShareMode, 
        #            LPSECURITY_ATTRIBUTES lpSecurityAttributes, 
        #            DWORD dwCreationDisposition, 
        #            DWORD dwFlagsAndAttributes, 
        #            HANDLE hTemplateFile); 

        hceFile = self._CeCreateFile_(unicode(toPath), GENERIC_WRITE, FILE_SHARE_READ, None, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, 0)
        if hceFile == INVALID_HANDLE_VALUE:
            raise OSError("Error creating file on the device")

        try:
            dwWritten = c_ulong(0)
            data = hostFile.read(self.blockSize)
            while data:
                while dwWritten.value < len(data):
                    dwWritten.value = 0
                    self._CeWriteFile_(hceFile, data, len(data), byref(dwWritten), None)
                    data = data[dwWritten.value:]

                dwWritten.value = 0
                data = hostFile.read(self.blockSize)
        finally:
            self._CeCloseHandle_(hceFile)

    def getAttrs(self, path):
        result = self._CeGetFileAttributes_(unicode(path))
        if result == -1: 
            return None
        else: return result
    def exists(self, path):
        return self.getAttrs(path) is not None
    def dirExists(self, path):
        #return self.isDir(path)
        self.isDir(path)
        return self.exists(path)
    def fileExists(self, path):
        #return self.isFile(path)
        self.isFile(path)
        return self.exists(path)
    def isDir(self, path):
        attr = self.getAttrs(path)
        if attr is None:
            return None
        return attr and (attr & FILE_ATTRIBUTE_DIRECTORY)
    def isFile(self, path):
        attr = self.getAttrs(path)
        if attr is None:
            return None
        return attr and not (attr & FILE_ATTRIBUTE_DIRECTORY)

    def fileSize(self, path):
        for each in self.findFiles(path, True):
            return each[1]
        return None

    def readFile(self, fromPath):
        hostFile = StringIO.StringIO()
        self.copyFileFromDevice(fromPath, hostFile)
        hostFile.seek(0)
        return hostFile

    def copyFileFromDevice(self, fromPath, hostFile):
        if isinstance(hostFile, (str, unicode)):
            hostFile = open(hostFile, 'wb')

        hceFile = self._CeCreateFile_(unicode(fromPath), GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, 0)
        if hceFile == INVALID_HANDLE_VALUE:
            raise OSError("Error opening the file on the device for reading")

        try:
            dwRead = c_ulong(1)
            data = (self.blockSize * c_char)()
            
            while dwRead.value:
                dwRead.value = 0
                self._CeReadFile_(hceFile, data, len(data), byref(dwRead), None)
                hostFile.write(data.raw[:dwRead.value])
        finally:
            self._CeCloseHandle_(hceFile)
        return hostFile
    
    def openFile(self, name, mode='rU', buffering=None):
        return self.CEFile(name, mode, buffering)

    def popenDevice(self, path, commandLine=u''):
        processInfo = PROCESS_INFORMATION()
        result = bool(self._CeCreateProcess_(unicode(path), unicode(commandLine), None, None, False, 0, None, None, None, byref(processInfo)))
        return result

