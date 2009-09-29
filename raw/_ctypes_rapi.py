#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from ctypes import *
import _ctypes_support

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Definitions 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

rapiLib = _ctypes_support.loadFirstLibrary('rapi')

errorFuncNames = set(['CeRapiGetError', 'CeGetLastError'])
errorSkipNames = set([])

def cleanupNamespace(namespace):
    _ctypes_support.scrubNamespace(namespace, globals())

def checkRapiError(ftError, func, args):
    code = GetLastError()
    if code != 0:
        raise WinError(code)
    return ftError

def _getErrorCheckForFn(fn, restype):
    if fn.__name__ in errorSkipNames:
        return None

    return checkRapiError

def bind(restype, argtypes, errcheck=None):
    def bindFuncTypes(fn):
        fnErrCheck = errcheck
        if errcheck is None:
            fnErrCheck = _getErrorCheckForFn(fn, restype)

        return _ctypes_support.attachToLibFn(fn, restype, argtypes, fnErrCheck, rapiLib)
    return bindFuncTypes

