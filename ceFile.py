#!/usr/bin/env python
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

import os
from ctypes import windll, FormatError, sizeof, byref 
from ctypes import c_buffer, c_ulong, c_char, c_wchar, Structure, POINTER

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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ WinCE File-like object
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class CEFile(object):
    name = None
    mode = None
    closed = True
    newlines = None
    softspace = 0
    raiseErrors = True

    _flagShare = FILE_SHARE_READ
    _flagAttribute = FILE_ATTRIBUTE_NORMAL
    _flagWriteThrough = 0

    def __init__(self, name, mode='rU', buffering=None):
        self._loadRapiMethods()

        mode = mode.lower()
        self.name = name
        self.mode = mode
        if buffering == 0:
            self._flagWriteThrough = 1

        if 'u' in mode: 
            self.newlines = ['\r\n']

        if 'a' in mode:
            openMethod = self._openAppend
            fileAccessMode = GENERIC_WRITE
        elif 'w' in mode:
            openMethod = self._openWrite
            fileAccessMode = GENERIC_WRITE
        elif 'r' in mode:
            openMethod = self._openRead
            fileAccessMode = GENERIC_READ

        if '+' in mode: 
            fileAccessMode = GENERIC_READ | GENERIC_WRITE

        self._handle = openMethod(name, fileAccessMode)
        self.closed = False

    def __repr__(self):
        return "<%s.%s '%s', mode '%s' at 0x%x>" % (
                self.__class__.__module__, self.__class__.__name__,
                self.name, self.mode, id(self))

    _isCELoaded = False
    @classmethod
    def _loadRapiMethods(klass):
        if klass._isCELoaded:
            return True
        rapi = windll.rapi

        klass._CeGetLastError_ = staticmethod(rapi.CeGetLastError)

        def CeErrorCheck(result, cfunc, args):
            ceErrorNo = klass._CeGetLastError_()
            if ceErrorNo and ceErrorNo != 183:
                if klass.raiseErrors:
                    raise IOError('%s %d (0x%x)' % (FormatError(ceErrorNo), ceErrorNo, ceErrorNo))
                else:
                    print IOError('%s %d (0x%x)' % (FormatError(ceErrorNo), ceErrorNo, ceErrorNo))
            return result

        klass._CeCreateFile_ = staticmethod(rapi.CeCreateFile)
        klass._CeCreateFile_.errcheck = CeErrorCheck

        klass._CeCloseHandle_ = staticmethod(rapi.CeCloseHandle)
        klass._CeCloseHandle_.errcheck = CeErrorCheck

        klass._CeSetFilePointer_ = staticmethod(rapi.CeSetFilePointer)
        klass._CeSetFilePointer_.errcheck = CeErrorCheck

        klass._CeGetFileSize_ = staticmethod(rapi.CeGetFileSize)
        klass._CeGetFileSize_.errcheck = CeErrorCheck

        klass._CeReadFile_ = staticmethod(rapi.CeReadFile)
        klass._CeReadFile_.errcheck = CeErrorCheck

        klass._CeWriteFile_ = staticmethod(rapi.CeWriteFile)
        klass._CeWriteFile_.errcheck = CeErrorCheck

        klass._CeSetEndOfFile_ = staticmethod(rapi.CeSetEndOfFile)
        klass._CeSetEndOfFile_.errcheck = CeErrorCheck

        klass._isCELoaded = True
        return True

    def _openRead(self, name, fileAccessMode=GENERIC_READ):
        hceFile = self._CeCreateFile_(
                unicode(name),
                fileAccessMode,
                self._flagShare,
                None,
                OPEN_EXISTING,
                self._flagAttribute,
                self._flagWriteThrough and FILE_FLAG_WRITE_THROUGH or 0)
        if hceFile == INVALID_HANDLE_VALUE:
            raise IOError("Error opening the file on the device for reading")
        return hceFile
    def _openAppend(self, name, fileAccessMode=GENERIC_WRITE):
        hceFile = self._CeCreateFile_(
                unicode(name),
                fileAccessMode, 
                self._flagShare,
                None,
                OPEN_ALWAYS,
                self._flagAttribute,
                self._flagWriteThrough and FILE_FLAG_WRITE_THROUGH or 0)
        if hceFile == INVALID_HANDLE_VALUE:
            raise IOError("Error opening file on the device for appending")
        return hceFile
    def _openWrite(self, name, fileAccessMode=GENERIC_WRITE):
        hceFile = self._CeCreateFile_(
                unicode(name),
                GENERIC_WRITE,
                self._flagShare,
                None,
                CREATE_ALWAYS,
                self._flagAttribute,
                self._flagWriteThrough and FILE_FLAG_WRITE_THROUGH or 0)
        if hceFile == INVALID_HANDLE_VALUE:
            raise IOError("Error opening file on the device for writing")
        return hceFile

    def close(self):
        self._CeCloseHandle_(self._getHandle())
        self._handle = None
        self.closed = True

    def isatty(self):
        return False
    def fileno(self):
        return None

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def tell(self):
        return self.seek(0, 1)
    def seek(self, pos, whence=0):
        result = self._CeSetFilePointer_(self._getHandle(), pos, None, whence)
        if result == 0xffffffff:
            raise IOError('CE Seek Error')
        return result

    def flush(self,):
        pass

    def read(self, count=None):
        handle = self._getHandle()
        if count is None:
            count = self._CeGetFileSize_(handle, None)
        data = c_buffer(count)
        dwRead = c_ulong(0)
        self._CeReadFile_(handle, data, len(data), byref(dwRead), None)
        data = data[:dwRead.value]

        if self.newlines:
            for n in self.newlines:
                data = data.replace(n, '\n')
        return data

    def writelines(self, lines):
        for line in lines:
            self.write(line + '\n') 

    def write(self, data):
        if not data: return
        dwWritten = c_ulong(0)
        self._CeWriteFile_(self._getHandle(), data, len(data), byref(dwWritten), None)

    def truncate(self, size=None):
        self._CeSetEndOfFile_(self._getHandle())

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _getHandle(self):
        handle = self._handle
        if handle is None or self.closed:
            raise IOError("CE file handle is closed")
        return handle
        

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Main 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__=='__main__':
    from pocketRapi import PocketRapi
    pr = PocketRapi()
    f = CEFile('/testfile.txt', 'a+u')
    print repr(f.read())
    print >> f, 'test string!'
    print >> f, 'left',
    print >> f, 'right'

    print f.tell(), f.seek(0)
    print repr(f.read())
    print f.seek(0), f.seek(0, 2)
    print repr(f.read())
    f.close()


