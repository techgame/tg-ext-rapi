#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from _ctypes_rapi import *
from ctypes.wintypes import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Code generated from:
#~   "inc/rapi.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class _CE_FIND_DATA(Structure):
    _fields_ = [
        ("dwFileAttributes", DWORD),
        ("ftCreationTime", FILETIME),
        ("ftLastAccessTime", FILETIME),
        ("ftLastWriteTime", FILETIME),
        ("nFileSizeHigh", DWORD),
        ("nFileSizeLow", DWORD),
        ("dwOID", DWORD),
        ("cFileName", (4160*WCHAR)),
        ]

#~ line: 34, skipped: 9 ~~~~~~

# typedef CE_FIND_DATA
CE_FIND_DATA = _CE_FIND_DATA
# typedef LPCE_FIND_DATA
LPCE_FIND_DATA = POINTER(_CE_FIND_DATA)

# typedef LPLPCE_FIND_DATA
LPLPCE_FIND_DATA = POINTER(POINTER(CE_FIND_DATA))

#~ line: 90, skipped: 54 ~~~~~~

class tagRAPISTREAMFLAG(c_int):
    '''enum tagRAPISTREAMFLAG''' 
    STREAM_TIMEOUT_READ = 0
    lookup = {
        0: "STREAM_TIMEOUT_READ",
        }
    rlookup = dict([(v,k) for k,v in lookup.items()])
    
    def __repr__(self): return str(self)
    def __str__(self): 
        return self.lookup.get(self.value) or str(self.value)
    

# typedef RAPISTREAMFLAG
RAPISTREAMFLAG = tagRAPISTREAMFLAG

IRAPIStream = c_void_p # Structure with empty _fields_

#~ line: 119, skipped: 23 ~~~~~~

class STORE_INFORMATION(Structure):
    _fields_ = [
        ("dwStoreSize", DWORD),
        ("dwFreeSize", DWORD),
        ]

# typedef LPSTORE_INFORMATION
LPSTORE_INFORMATION = POINTER(STORE_INFORMATION)

# typedef CEPROPID as c_ulong for absent DWORD
CEPROPID = c_ulong

#~ line: 128, skipped: 4 ~~~~~~

# typedef CEOID as c_ulong for absent DWORD
CEOID = c_ulong
# typedef PCEOID
PCEOID = POINTER(CEOID)

class _CEGUID(Structure):
    _fields_ = [
        ("Data1", DWORD),
        ("Data2", DWORD),
        ("Data3", DWORD),
        ("Data4", DWORD),
        ]

#~ line: 136, skipped: 5 ~~~~~~

# typedef CEGUID
CEGUID = _CEGUID
# typedef PCEGUID
PCEGUID = POINTER(CEGUID)

#~ line: 149, skipped: 12 ~~~~~~

class _CENOTIFYREQUEST(Structure):
    _fields_ = [
        ("dwSize", DWORD),
        ("hwnd", HWND),
        ("dwFlags", DWORD),
        ("hHeap", HANDLE),
        ("dwParam", DWORD),
        ]

#~ line: 155, skipped: 6 ~~~~~~

# typedef CENOTIFYREQUEST
CENOTIFYREQUEST = _CENOTIFYREQUEST

class _CEFILEINFO(Structure):
    _fields_ = [
        ("dwAttributes", DWORD),
        ("oidParent", CEOID),
        ("szFileName", (4160*WCHAR)),
        ("ftLastChanged", FILETIME),
        ("dwLength", DWORD),
        ]

#~ line: 164, skipped: 6 ~~~~~~

# typedef CEFILEINFO
CEFILEINFO = _CEFILEINFO

class _CEDIRINFO(Structure):
    _fields_ = [
        ("dwAttributes", DWORD),
        ("oidParent", CEOID),
        ("szDirName", (4160*WCHAR)),
        ]

#~ line: 170, skipped: 4 ~~~~~~

# typedef CEDIRINFO
CEDIRINFO = _CEDIRINFO

class _CERECORDINFO(Structure):
    _fields_ = [
        ("oidParent", CEOID),
        ]

# typedef CERECORDINFO
CERECORDINFO = _CERECORDINFO

#~ line: 181, skipped: 7 ~~~~~~

class _SORTORDERSPEC(Structure):
    _fields_ = [
        ("propid", CEPROPID),
        ("dwFlags", DWORD),
        ]

# typedef SORTORDERSPEC
SORTORDERSPEC = _SORTORDERSPEC

#~ line: 198, skipped: 14 ~~~~~~

class _CEDBASEINFO(Structure):
    _fields_ = [
        ("dwFlags", DWORD),
        ("szDbaseName", (512*WCHAR)),
        ("dwDbaseType", DWORD),
        ("wNumRecords", WORD),
        ("wNumSortOrder", WORD),
        ("dwSize", DWORD),
        ("ftLastModified", FILETIME),
        ("rgSortSpecs", (256*SORTORDERSPEC)),
        ]

#~ line: 207, skipped: 9 ~~~~~~

# typedef CEDBASEINFO
CEDBASEINFO = _CEDBASEINFO

class _CEDB_FIND_DATA(Structure):
    _fields_ = [
        ("OidDb", CEOID),
        ("DbInfo", CEDBASEINFO),
        ]

# typedef CEDB_FIND_DATA
CEDB_FIND_DATA = _CEDB_FIND_DATA

# typedef LPLPCEDB_FIND_DATA
LPLPCEDB_FIND_DATA = POINTER(POINTER(CEDB_FIND_DATA))

#~ line: 222, skipped: 8 ~~~~~~

class _CEOIDINFO_Union(Union):
    _fields_ = [
        ("infFile", CEFILEINFO),
        ("infDirectory", CEDIRINFO),
        ("infDatabase", CEDBASEINFO),
        ("infRecord", CERECORDINFO),
        ]

class _CEOIDINFO(Structure):
    _fields_ = [
        ("wObjType", WORD),
        ("wPad", WORD),
        ("_u", _CEOIDINFO_Union),
        ]
    _anonymous_ = ('_u',)

#~ line: 231, skipped: 6 ~~~~~~

# typedef CEOIDINFO
CEOIDINFO = _CEOIDINFO

#~ line: 244, skipped: 13 ~~~~~~

class _CEBLOB(Structure):
    _fields_ = [
        ("dwCount", DWORD),
        ("lpb", LPBYTE),
        ]

# typedef CEBLOB
CEBLOB = _CEBLOB

#~ line: 259, skipped: 12 ~~~~~~

class _CEVALUNION(Union):
    _fields_ = [
        ("iVal", c_short),
        ("uiVal", USHORT),
        ("lVal", c_long),
        ("ulVal", DWORD),
        ("filetime", FILETIME),
        ("lpwstr", LPWSTR),
        ("blob", CEBLOB),
        ("boolVal", BOOL),
        ("dblVal", c_double),
        ]

#~ line: 269, skipped: 10 ~~~~~~

# typedef CEVALUNION
CEVALUNION = _CEVALUNION

#~ line: 273, skipped: 4 ~~~~~~

class _CEPROPVAL(Structure):
    _fields_ = [
        ("propid", CEPROPID),
        ("wLenData", WORD),
        ("wFlags", WORD),
        ("val", CEVALUNION),
        ]

#~ line: 278, skipped: 5 ~~~~~~

# typedef CEPROPVAL
CEPROPVAL = _CEPROPVAL

#~ line: 297, skipped: 19 ~~~~~~

class _CEOSVERSIONINFO(Structure):
    _fields_ = [
        ("dwOSVersionInfoSize", DWORD),
        ("dwMajorVersion", DWORD),
        ("dwMinorVersion", DWORD),
        ("dwBuildNumber", DWORD),
        ("dwPlatformId", DWORD),
        ("szCSDVersion", (2048*WCHAR)),
        ]

#~ line: 304, skipped: 7 ~~~~~~

# typedef LPCEOSVERSIONINFO
LPCEOSVERSIONINFO = POINTER(_CEOSVERSIONINFO)

#~ line: 322, skipped: 18 ~~~~~~

class _SYSTEM_POWER_STATUS_EX(Structure):
    _fields_ = [
        ("ACLineStatus", BYTE),
        ("BatteryFlag", BYTE),
        ("BatteryLifePercent", BYTE),
        ("Reserved1", BYTE),
        ("BatteryLifeTime", DWORD),
        ("BatteryFullLifeTime", DWORD),
        ("Reserved2", BYTE),
        ("BackupBatteryFlag", BYTE),
        ("BackupBatteryLifePercent", BYTE),
        ("Reserved3", BYTE),
        ("BackupBatteryLifeTime", DWORD),
        ("BackupBatteryFullLifeTime", DWORD),
        ]

#~ line: 335, skipped: 13 ~~~~~~

# typedef PSYSTEM_POWER_STATUS_EX
PSYSTEM_POWER_STATUS_EX = POINTER(_SYSTEM_POWER_STATUS_EX)

#~ line: 345, skipped: 10 ~~~~~~

class _RAPIINIT(Structure):
    _fields_ = [
        ("cbSize", DWORD),
        ("heRapiInit", HANDLE),
        ("hrRapiInit", HRESULT),
        ]

#~ line: 349, skipped: 4 ~~~~~~

# typedef RAPIINIT
RAPIINIT = _RAPIINIT

@bind(HRESULT, [POINTER(RAPIINIT)])
def CeRapiInitEx(arg_0, _api_=None): 
    """CeRapiInitEx(arg_0)
    
        arg_0 : POINTER(RAPIINIT)
    """
    return _api_(arg_0)
    
@bind(HRESULT, [])
def CeRapiInit(_api_=None): 
    """CeRapiInit()
    
        
    """
    return _api_()
    
@bind(HRESULT, [])
def CeRapiUninit(_api_=None): 
    """CeRapiUninit()
    
        
    """
    return _api_()
    
@bind(HRESULT, [])
def CeRapiGetError(_api_=None): 
    """CeRapiGetError()
    
        
    """
    return _api_()
    
@bind(HRESULT, [LPVOID])
def CeRapiFreeBuffer(arg_0, _api_=None): 
    """CeRapiFreeBuffer(arg_0)
    
        arg_0 : LPVOID
    """
    return _api_(arg_0)
    
@bind(HRESULT, [LPCWSTR, LPCWSTR, DWORD, POINTER(c_ubyte), POINTER(c_ulong), POINTER(POINTER(c_ubyte)), POINTER(POINTER(IRAPIStream)), DWORD])
def CeRapiInvoke(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7, _api_=None): 
    """CeRapiInvoke(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7)
    
        arg_0 : LPCWSTR
        arg_1 : LPCWSTR
        arg_2 : DWORD
        arg_3 : POINTER(c_ubyte)
        arg_4 : POINTER(c_ulong)
        arg_5 : POINTER(POINTER(c_ubyte))
        arg_6 : POINTER(POINTER(IRAPIStream))
        arg_7 : DWORD
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7)
    

@bind(CEOID, [LPWSTR, DWORD, WORD, POINTER(SORTORDERSPEC)])
def CeCreateDatabase(arg_0, arg_1, arg_2, arg_3, _api_=None): 
    """CeCreateDatabase(arg_0, arg_1, arg_2, arg_3)
    
        arg_0 : LPWSTR
        arg_1 : DWORD
        arg_2 : WORD
        arg_3 : POINTER(SORTORDERSPEC)
    """
    return _api_(arg_0, arg_1, arg_2, arg_3)
    
@bind(BOOL, [CEOID])
def CeDeleteDatabase(arg_0, _api_=None): 
    """CeDeleteDatabase(arg_0)
    
        arg_0 : CEOID
    """
    return _api_(arg_0)
    
@bind(BOOL, [HANDLE, CEOID])
def CeDeleteRecord(arg_0, arg_1, _api_=None): 
    """CeDeleteRecord(arg_0, arg_1)
    
        arg_0 : HANDLE
        arg_1 : CEOID
    """
    return _api_(arg_0, arg_1)
    
@bind(HANDLE, [DWORD])
def CeFindFirstDatabase(arg_0, _api_=None): 
    """CeFindFirstDatabase(arg_0)
    
        arg_0 : DWORD
    """
    return _api_(arg_0)
    
@bind(CEOID, [HANDLE])
def CeFindNextDatabase(arg_0, _api_=None): 
    """CeFindNextDatabase(arg_0)
    
        arg_0 : HANDLE
    """
    return _api_(arg_0)
    
@bind(BOOL, [CEOID, POINTER(CEOIDINFO)])
def CeOidGetInfo(arg_0, arg_1, _api_=None): 
    """CeOidGetInfo(arg_0, arg_1)
    
        arg_0 : CEOID
        arg_1 : POINTER(CEOIDINFO)
    """
    return _api_(arg_0, arg_1)
    
@bind(HANDLE, [PCEOID, LPWSTR, CEPROPID, DWORD, HWND])
def CeOpenDatabase(arg_0, arg_1, arg_2, arg_3, arg_4, _api_=None): 
    """CeOpenDatabase(arg_0, arg_1, arg_2, arg_3, arg_4)
    
        arg_0 : PCEOID
        arg_1 : LPWSTR
        arg_2 : CEPROPID
        arg_3 : DWORD
        arg_4 : HWND
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4)
    
@bind(CEOID, [HANDLE, DWORD, LPWORD, POINTER(CEPROPID), POINTER(LPBYTE), LPDWORD])
def CeReadRecordProps(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, _api_=None): 
    """CeReadRecordProps(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5)
    
        arg_0 : HANDLE
        arg_1 : DWORD
        arg_2 : LPWORD
        arg_3 : POINTER(CEPROPID)
        arg_4 : POINTER(LPBYTE)
        arg_5 : LPDWORD
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5)
    
@bind(CEOID, [HANDLE, DWORD, DWORD, LPDWORD])
def CeSeekDatabase(arg_0, arg_1, arg_2, arg_3, _api_=None): 
    """CeSeekDatabase(arg_0, arg_1, arg_2, arg_3)
    
        arg_0 : HANDLE
        arg_1 : DWORD
        arg_2 : DWORD
        arg_3 : LPDWORD
    """
    return _api_(arg_0, arg_1, arg_2, arg_3)
    
@bind(BOOL, [CEOID, POINTER(CEDBASEINFO)])
def CeSetDatabaseInfo(arg_0, arg_1, _api_=None): 
    """CeSetDatabaseInfo(arg_0, arg_1)
    
        arg_0 : CEOID
        arg_1 : POINTER(CEDBASEINFO)
    """
    return _api_(arg_0, arg_1)
    

@bind(HANDLE, [LPCWSTR, LPCE_FIND_DATA])
def CeFindFirstFile(arg_0, arg_1, _api_=None): 
    """CeFindFirstFile(arg_0, arg_1)
    
        arg_0 : LPCWSTR
        arg_1 : LPCE_FIND_DATA
    """
    return _api_(arg_0, arg_1)
    
@bind(BOOL, [HANDLE, LPCE_FIND_DATA])
def CeFindNextFile(arg_0, arg_1, _api_=None): 
    """CeFindNextFile(arg_0, arg_1)
    
        arg_0 : HANDLE
        arg_1 : LPCE_FIND_DATA
    """
    return _api_(arg_0, arg_1)
    
@bind(BOOL, [HANDLE])
def CeFindClose(arg_0, _api_=None): 
    """CeFindClose(arg_0)
    
        arg_0 : HANDLE
    """
    return _api_(arg_0)
    
@bind(DWORD, [LPCWSTR])
def CeGetFileAttributes(arg_0, _api_=None): 
    """CeGetFileAttributes(arg_0)
    
        arg_0 : LPCWSTR
    """
    return _api_(arg_0)
    
@bind(BOOL, [LPCWSTR, DWORD])
def CeSetFileAttributes(arg_0, arg_1, _api_=None): 
    """CeSetFileAttributes(arg_0, arg_1)
    
        arg_0 : LPCWSTR
        arg_1 : DWORD
    """
    return _api_(arg_0, arg_1)
    
@bind(HANDLE, [LPCWSTR, DWORD, DWORD, LPSECURITY_ATTRIBUTES, DWORD, DWORD, HANDLE])
def CeCreateFile(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, _api_=None): 
    """CeCreateFile(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6)
    
        arg_0 : LPCWSTR
        arg_1 : DWORD
        arg_2 : DWORD
        arg_3 : LPSECURITY_ATTRIBUTES
        arg_4 : DWORD
        arg_5 : DWORD
        arg_6 : HANDLE
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6)
    
@bind(BOOL, [HANDLE, LPVOID, DWORD, LPDWORD, LPOVERLAPPED])
def CeReadFile(arg_0, arg_1, arg_2, arg_3, arg_4, _api_=None): 
    """CeReadFile(arg_0, arg_1, arg_2, arg_3, arg_4)
    
        arg_0 : HANDLE
        arg_1 : LPVOID
        arg_2 : DWORD
        arg_3 : LPDWORD
        arg_4 : LPOVERLAPPED
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4)
    
@bind(BOOL, [HANDLE, LPCVOID, DWORD, LPDWORD, LPOVERLAPPED])
def CeWriteFile(arg_0, arg_1, arg_2, arg_3, arg_4, _api_=None): 
    """CeWriteFile(arg_0, arg_1, arg_2, arg_3, arg_4)
    
        arg_0 : HANDLE
        arg_1 : LPCVOID
        arg_2 : DWORD
        arg_3 : LPDWORD
        arg_4 : LPOVERLAPPED
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4)
    
@bind(BOOL, [HANDLE])
def CeCloseHandle(arg_0, _api_=None): 
    """CeCloseHandle(arg_0)
    
        arg_0 : HANDLE
    """
    return _api_(arg_0)
    
@bind(BOOL, [LPCWSTR, DWORD, LPDWORD, LPLPCE_FIND_DATA])
def CeFindAllFiles(arg_0, arg_1, arg_2, arg_3, _api_=None): 
    """CeFindAllFiles(arg_0, arg_1, arg_2, arg_3)
    
        arg_0 : LPCWSTR
        arg_1 : DWORD
        arg_2 : LPDWORD
        arg_3 : LPLPCE_FIND_DATA
    """
    return _api_(arg_0, arg_1, arg_2, arg_3)
    
@bind(BOOL, [DWORD, WORD, LPWORD, LPLPCEDB_FIND_DATA])
def CeFindAllDatabases(arg_0, arg_1, arg_2, arg_3, _api_=None): 
    """CeFindAllDatabases(arg_0, arg_1, arg_2, arg_3)
    
        arg_0 : DWORD
        arg_1 : WORD
        arg_2 : LPWORD
        arg_3 : LPLPCEDB_FIND_DATA
    """
    return _api_(arg_0, arg_1, arg_2, arg_3)
    
@bind(DWORD, [])
def CeGetLastError(_api_=None): 
    """CeGetLastError()
    
        
    """
    return _api_()
    
@bind(DWORD, [HANDLE, LONG, PLONG, DWORD])
def CeSetFilePointer(arg_0, arg_1, arg_2, arg_3, _api_=None): 
    """CeSetFilePointer(arg_0, arg_1, arg_2, arg_3)
    
        arg_0 : HANDLE
        arg_1 : LONG
        arg_2 : PLONG
        arg_3 : DWORD
    """
    return _api_(arg_0, arg_1, arg_2, arg_3)
    
@bind(BOOL, [HANDLE])
def CeSetEndOfFile(arg_0, _api_=None): 
    """CeSetEndOfFile(arg_0)
    
        arg_0 : HANDLE
    """
    return _api_(arg_0)
    
@bind(BOOL, [LPCWSTR, LPSECURITY_ATTRIBUTES])
def CeCreateDirectory(arg_0, arg_1, _api_=None): 
    """CeCreateDirectory(arg_0, arg_1)
    
        arg_0 : LPCWSTR
        arg_1 : LPSECURITY_ATTRIBUTES
    """
    return _api_(arg_0, arg_1)
    
@bind(BOOL, [LPCWSTR])
def CeRemoveDirectory(arg_0, _api_=None): 
    """CeRemoveDirectory(arg_0)
    
        arg_0 : LPCWSTR
    """
    return _api_(arg_0)
    
@bind(BOOL, [LPCWSTR, LPCWSTR, LPSECURITY_ATTRIBUTES, LPSECURITY_ATTRIBUTES, BOOL, DWORD, LPVOID, LPWSTR, LPSTARTUPINFO, LPPROCESS_INFORMATION])
def CeCreateProcess(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7, arg_8, arg_9, _api_=None): 
    """CeCreateProcess(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7, arg_8, arg_9)
    
        arg_0 : LPCWSTR
        arg_1 : LPCWSTR
        arg_2 : LPSECURITY_ATTRIBUTES
        arg_3 : LPSECURITY_ATTRIBUTES
        arg_4 : BOOL
        arg_5 : DWORD
        arg_6 : LPVOID
        arg_7 : LPWSTR
        arg_8 : LPSTARTUPINFO
        arg_9 : LPPROCESS_INFORMATION
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7, arg_8, arg_9)
    
@bind(BOOL, [LPCWSTR, LPCWSTR])
def CeMoveFile(arg_0, arg_1, _api_=None): 
    """CeMoveFile(arg_0, arg_1)
    
        arg_0 : LPCWSTR
        arg_1 : LPCWSTR
    """
    return _api_(arg_0, arg_1)
    
@bind(BOOL, [LPCWSTR, LPCWSTR, BOOL])
def CeCopyFile(arg_0, arg_1, arg_2, _api_=None): 
    """CeCopyFile(arg_0, arg_1, arg_2)
    
        arg_0 : LPCWSTR
        arg_1 : LPCWSTR
        arg_2 : BOOL
    """
    return _api_(arg_0, arg_1, arg_2)
    
@bind(BOOL, [LPCWSTR])
def CeDeleteFile(arg_0, _api_=None): 
    """CeDeleteFile(arg_0)
    
        arg_0 : LPCWSTR
    """
    return _api_(arg_0)
    
@bind(DWORD, [HANDLE, LPDWORD])
def CeGetFileSize(arg_0, arg_1, _api_=None): 
    """CeGetFileSize(arg_0, arg_1)
    
        arg_0 : HANDLE
        arg_1 : LPDWORD
    """
    return _api_(arg_0, arg_1)
    
@bind(LONG, [HKEY, LPCWSTR, DWORD, REGSAM, PHKEY])
def CeRegOpenKeyEx(arg_0, arg_1, arg_2, arg_3, arg_4, _api_=None): 
    """CeRegOpenKeyEx(arg_0, arg_1, arg_2, arg_3, arg_4)
    
        arg_0 : HKEY
        arg_1 : LPCWSTR
        arg_2 : DWORD
        arg_3 : REGSAM
        arg_4 : PHKEY
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4)
    
@bind(LONG, [HKEY, DWORD, LPWSTR, LPDWORD, LPDWORD, LPWSTR, LPDWORD, PFILETIME])
def CeRegEnumKeyEx(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7, _api_=None): 
    """CeRegEnumKeyEx(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7)
    
        arg_0 : HKEY
        arg_1 : DWORD
        arg_2 : LPWSTR
        arg_3 : LPDWORD
        arg_4 : LPDWORD
        arg_5 : LPWSTR
        arg_6 : LPDWORD
        arg_7 : PFILETIME
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7)
    
@bind(LONG, [HKEY, LPCWSTR, DWORD, LPWSTR, DWORD, REGSAM, LPSECURITY_ATTRIBUTES, PHKEY, LPDWORD])
def CeRegCreateKeyEx(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7, arg_8, _api_=None): 
    """CeRegCreateKeyEx(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7, arg_8)
    
        arg_0 : HKEY
        arg_1 : LPCWSTR
        arg_2 : DWORD
        arg_3 : LPWSTR
        arg_4 : DWORD
        arg_5 : REGSAM
        arg_6 : LPSECURITY_ATTRIBUTES
        arg_7 : PHKEY
        arg_8 : LPDWORD
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7, arg_8)
    
@bind(LONG, [HKEY])
def CeRegCloseKey(arg_0, _api_=None): 
    """CeRegCloseKey(arg_0)
    
        arg_0 : HKEY
    """
    return _api_(arg_0)
    
@bind(LONG, [HKEY, LPCWSTR])
def CeRegDeleteKey(arg_0, arg_1, _api_=None): 
    """CeRegDeleteKey(arg_0, arg_1)
    
        arg_0 : HKEY
        arg_1 : LPCWSTR
    """
    return _api_(arg_0, arg_1)
    
@bind(LONG, [HKEY, DWORD, LPWSTR, LPDWORD, LPDWORD, LPDWORD, LPBYTE, LPDWORD])
def CeRegEnumValue(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7, _api_=None): 
    """CeRegEnumValue(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7)
    
        arg_0 : HKEY
        arg_1 : DWORD
        arg_2 : LPWSTR
        arg_3 : LPDWORD
        arg_4 : LPDWORD
        arg_5 : LPDWORD
        arg_6 : LPBYTE
        arg_7 : LPDWORD
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7)
    
@bind(LONG, [HKEY, LPCWSTR])
def CeRegDeleteValue(arg_0, arg_1, _api_=None): 
    """CeRegDeleteValue(arg_0, arg_1)
    
        arg_0 : HKEY
        arg_1 : LPCWSTR
    """
    return _api_(arg_0, arg_1)
    
@bind(LONG, [HKEY, LPWSTR, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, PFILETIME])
def CeRegQueryInfoKey(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7, arg_8, arg_9, arg_10, arg_11, _api_=None): 
    """CeRegQueryInfoKey(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7, arg_8, arg_9, arg_10, arg_11)
    
        arg_0 : HKEY
        arg_1 : LPWSTR
        arg_2 : LPDWORD
        arg_3 : LPDWORD
        arg_4 : LPDWORD
        arg_5 : LPDWORD
        arg_6 : LPDWORD
        arg_7 : LPDWORD
        arg_8 : LPDWORD
        arg_9 : LPDWORD
        arg_10 : LPDWORD
        arg_11 : PFILETIME
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7, arg_8, arg_9, arg_10, arg_11)
    
@bind(LONG, [HKEY, LPCWSTR, LPDWORD, LPDWORD, LPBYTE, LPDWORD])
def CeRegQueryValueEx(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, _api_=None): 
    """CeRegQueryValueEx(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5)
    
        arg_0 : HKEY
        arg_1 : LPCWSTR
        arg_2 : LPDWORD
        arg_3 : LPDWORD
        arg_4 : LPBYTE
        arg_5 : LPDWORD
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5)
    
@bind(LONG, [HKEY, LPCWSTR, DWORD, DWORD, LPBYTE, DWORD])
def CeRegSetValueEx(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, _api_=None): 
    """CeRegSetValueEx(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5)
    
        arg_0 : HKEY
        arg_1 : LPCWSTR
        arg_2 : DWORD
        arg_3 : DWORD
        arg_4 : LPBYTE
        arg_5 : DWORD
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5)
    
@bind(BOOL, [LPSTORE_INFORMATION])
def CeGetStoreInformation(arg_0, _api_=None): 
    """CeGetStoreInformation(arg_0)
    
        arg_0 : LPSTORE_INFORMATION
    """
    return _api_(arg_0)
    
@bind(INT, [INT])
def CeGetSystemMetrics(arg_0, _api_=None): 
    """CeGetSystemMetrics(arg_0)
    
        arg_0 : INT
    """
    return _api_(arg_0)
    
@bind(INT, [INT])
def CeGetDesktopDeviceCaps(arg_0, _api_=None): 
    """CeGetDesktopDeviceCaps(arg_0)
    
        arg_0 : INT
    """
    return _api_(arg_0)
    
@bind(None, [LPSYSTEM_INFO])
def CeGetSystemInfo(arg_0, _api_=None): 
    """CeGetSystemInfo(arg_0)
    
        arg_0 : LPSYSTEM_INFO
    """
    return _api_(arg_0)
    
@bind(DWORD, [LPWSTR, LPWSTR])
def CeSHCreateShortcut(arg_0, arg_1, _api_=None): 
    """CeSHCreateShortcut(arg_0, arg_1)
    
        arg_0 : LPWSTR
        arg_1 : LPWSTR
    """
    return _api_(arg_0, arg_1)
    
@bind(BOOL, [LPWSTR, LPWSTR, INT])
def CeSHGetShortcutTarget(arg_0, arg_1, arg_2, _api_=None): 
    """CeSHGetShortcutTarget(arg_0, arg_1, arg_2)
    
        arg_0 : LPWSTR
        arg_1 : LPWSTR
        arg_2 : INT
    """
    return _api_(arg_0, arg_1, arg_2)
    
@bind(BOOL, [LPWSTR])
def CeCheckPassword(arg_0, _api_=None): 
    """CeCheckPassword(arg_0)
    
        arg_0 : LPWSTR
    """
    return _api_(arg_0)
    
@bind(BOOL, [HANDLE, LPFILETIME, LPFILETIME, LPFILETIME])
def CeGetFileTime(arg_0, arg_1, arg_2, arg_3, _api_=None): 
    """CeGetFileTime(arg_0, arg_1, arg_2, arg_3)
    
        arg_0 : HANDLE
        arg_1 : LPFILETIME
        arg_2 : LPFILETIME
        arg_3 : LPFILETIME
    """
    return _api_(arg_0, arg_1, arg_2, arg_3)
    
@bind(BOOL, [HANDLE, LPFILETIME, LPFILETIME, LPFILETIME])
def CeSetFileTime(arg_0, arg_1, arg_2, arg_3, _api_=None): 
    """CeSetFileTime(arg_0, arg_1, arg_2, arg_3)
    
        arg_0 : HANDLE
        arg_1 : LPFILETIME
        arg_2 : LPFILETIME
        arg_3 : LPFILETIME
    """
    return _api_(arg_0, arg_1, arg_2, arg_3)
    
@bind(BOOL, [LPCEOSVERSIONINFO])
def CeGetVersionEx(arg_0, _api_=None): 
    """CeGetVersionEx(arg_0)
    
        arg_0 : LPCEOSVERSIONINFO
    """
    return _api_(arg_0)
    
@bind(HWND, [HWND, UINT])
def CeGetWindow(arg_0, arg_1, _api_=None): 
    """CeGetWindow(arg_0, arg_1)
    
        arg_0 : HWND
        arg_1 : UINT
    """
    return _api_(arg_0, arg_1)
    
@bind(LONG, [HWND, c_int])
def CeGetWindowLong(arg_0, arg_1, _api_=None): 
    """CeGetWindowLong(arg_0, arg_1)
    
        arg_0 : HWND
        arg_1 : c_int
    """
    return _api_(arg_0, arg_1)
    
@bind(c_int, [HWND, LPWSTR, c_int])
def CeGetWindowText(arg_0, arg_1, arg_2, _api_=None): 
    """CeGetWindowText(arg_0, arg_1, arg_2)
    
        arg_0 : HWND
        arg_1 : LPWSTR
        arg_2 : c_int
    """
    return _api_(arg_0, arg_1, arg_2)
    
@bind(c_int, [HWND, LPWSTR, c_int])
def CeGetClassName(arg_0, arg_1, arg_2, _api_=None): 
    """CeGetClassName(arg_0, arg_1, arg_2)
    
        arg_0 : HWND
        arg_1 : LPWSTR
        arg_2 : c_int
    """
    return _api_(arg_0, arg_1, arg_2)
    
@bind(None, [LPMEMORYSTATUS])
def CeGlobalMemoryStatus(arg_0, _api_=None): 
    """CeGlobalMemoryStatus(arg_0)
    
        arg_0 : LPMEMORYSTATUS
    """
    return _api_(arg_0)
    
@bind(BOOL, [PSYSTEM_POWER_STATUS_EX, BOOL])
def CeGetSystemPowerStatusEx(arg_0, arg_1, _api_=None): 
    """CeGetSystemPowerStatusEx(arg_0, arg_1)
    
        arg_0 : PSYSTEM_POWER_STATUS_EX
        arg_1 : BOOL
    """
    return _api_(arg_0, arg_1)
    
@bind(DWORD, [DWORD, LPWSTR])
def CeGetTempPath(arg_0, arg_1, _api_=None): 
    """CeGetTempPath(arg_0, arg_1)
    
        arg_0 : DWORD
        arg_1 : LPWSTR
    """
    return _api_(arg_0, arg_1)
    
@bind(DWORD, [c_int, DWORD, LPWSTR])
def CeGetSpecialFolderPath(arg_0, arg_1, arg_2, _api_=None): 
    """CeGetSpecialFolderPath(arg_0, arg_1, arg_2)
    
        arg_0 : c_int
        arg_1 : DWORD
        arg_2 : LPWSTR
    """
    return _api_(arg_0, arg_1, arg_2)
    
@bind(HANDLE, [PCEGUID, DWORD])
def CeFindFirstDatabaseEx(arg_0, arg_1, _api_=None): 
    """CeFindFirstDatabaseEx(arg_0, arg_1)
    
        arg_0 : PCEGUID
        arg_1 : DWORD
    """
    return _api_(arg_0, arg_1)
    
@bind(CEOID, [HANDLE, PCEGUID])
def CeFindNextDatabaseEx(arg_0, arg_1, _api_=None): 
    """CeFindNextDatabaseEx(arg_0, arg_1)
    
        arg_0 : HANDLE
        arg_1 : PCEGUID
    """
    return _api_(arg_0, arg_1)
    
@bind(CEOID, [PCEGUID, POINTER(CEDBASEINFO)])
def CeCreateDatabaseEx(arg_0, arg_1, _api_=None): 
    """CeCreateDatabaseEx(arg_0, arg_1)
    
        arg_0 : PCEGUID
        arg_1 : POINTER(CEDBASEINFO)
    """
    return _api_(arg_0, arg_1)
    
@bind(BOOL, [PCEGUID, CEOID, POINTER(CEDBASEINFO)])
def CeSetDatabaseInfoEx(arg_0, arg_1, arg_2, _api_=None): 
    """CeSetDatabaseInfoEx(arg_0, arg_1, arg_2)
    
        arg_0 : PCEGUID
        arg_1 : CEOID
        arg_2 : POINTER(CEDBASEINFO)
    """
    return _api_(arg_0, arg_1, arg_2)
    
@bind(HANDLE, [PCEGUID, PCEOID, LPWSTR, CEPROPID, DWORD, POINTER(CENOTIFYREQUEST)])
def CeOpenDatabaseEx(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, _api_=None): 
    """CeOpenDatabaseEx(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5)
    
        arg_0 : PCEGUID
        arg_1 : PCEOID
        arg_2 : LPWSTR
        arg_3 : CEPROPID
        arg_4 : DWORD
        arg_5 : POINTER(CENOTIFYREQUEST)
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5)
    
@bind(BOOL, [PCEGUID, CEOID])
def CeDeleteDatabaseEx(arg_0, arg_1, _api_=None): 
    """CeDeleteDatabaseEx(arg_0, arg_1)
    
        arg_0 : PCEGUID
        arg_1 : CEOID
    """
    return _api_(arg_0, arg_1)
    
@bind(CEOID, [HANDLE, DWORD, LPWORD, POINTER(CEPROPID), POINTER(LPBYTE), LPDWORD, HANDLE])
def CeReadRecordPropsEx(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, _api_=None): 
    """CeReadRecordPropsEx(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6)
    
        arg_0 : HANDLE
        arg_1 : DWORD
        arg_2 : LPWORD
        arg_3 : POINTER(CEPROPID)
        arg_4 : POINTER(LPBYTE)
        arg_5 : LPDWORD
        arg_6 : HANDLE
    """
    return _api_(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6)
    
@bind(CEOID, [HANDLE, CEOID, WORD, POINTER(CEPROPVAL)])
def CeWriteRecordProps(arg_0, arg_1, arg_2, arg_3, _api_=None): 
    """CeWriteRecordProps(arg_0, arg_1, arg_2, arg_3)
    
        arg_0 : HANDLE
        arg_1 : CEOID
        arg_2 : WORD
        arg_3 : POINTER(CEPROPVAL)
    """
    return _api_(arg_0, arg_1, arg_2, arg_3)
    
@bind(BOOL, [PCEGUID, LPWSTR, DWORD])
def CeMountDBVol(arg_0, arg_1, arg_2, _api_=None): 
    """CeMountDBVol(arg_0, arg_1, arg_2)
    
        arg_0 : PCEGUID
        arg_1 : LPWSTR
        arg_2 : DWORD
    """
    return _api_(arg_0, arg_1, arg_2)
    
@bind(BOOL, [PCEGUID])
def CeUnmountDBVol(arg_0, _api_=None): 
    """CeUnmountDBVol(arg_0)
    
        arg_0 : PCEGUID
    """
    return _api_(arg_0)
    
@bind(BOOL, [PCEGUID])
def CeFlushDBVol(arg_0, _api_=None): 
    """CeFlushDBVol(arg_0)
    
        arg_0 : PCEGUID
    """
    return _api_(arg_0)
    
@bind(BOOL, [PCEGUID, LPWSTR, DWORD])
def CeEnumDBVolumes(arg_0, arg_1, arg_2, _api_=None): 
    """CeEnumDBVolumes(arg_0, arg_1, arg_2)
    
        arg_0 : PCEGUID
        arg_1 : LPWSTR
        arg_2 : DWORD
    """
    return _api_(arg_0, arg_1, arg_2)
    
@bind(BOOL, [PCEGUID, CEOID, POINTER(CEOIDINFO)])
def CeOidGetInfoEx(arg_0, arg_1, arg_2, _api_=None): 
    """CeOidGetInfoEx(arg_0, arg_1, arg_2)
    
        arg_0 : PCEGUID
        arg_1 : CEOID
        arg_2 : POINTER(CEOIDINFO)
    """
    return _api_(arg_0, arg_1, arg_2)
    


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ End of code generated from:
#~   "inc/rapi.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

