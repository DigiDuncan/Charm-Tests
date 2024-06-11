"""
This type stub file was generated by pyright.
"""

from ctypes import Structure, c_int, c_uint32, c_void_p

lib = ...
if lib is None:
    lib = ...
ca = ...
class AudioStreamPacketDescription(Structure):
    _fields_ = ...


class AudioStreamBasicDescription(Structure):
    _fields_ = ...
    def __repr__(self): # -> str:
        ...
    


class AudioBuffer(Structure):
    _fields_ = ...


class AudioBufferList(Structure):
    _fields_ = ...


kCFURLPOSIXPathStyle = ...
ExtAudioFilePropertyID = c_uint32
OSStatus = c_int
ExtAudioFileRef = c_void_p
AudioFileTypeID = c_uint32
AudioFileID = c_void_p
AudioFile_ReadProc = ...
AudioFile_GetSizeProc = ...
kCFAllocatorDefault = ...
def c_literal(literal): # -> int:
    """Example 'xyz' -> 7895418.
    Used for some CoreAudio constants."""
    ...

kAudioFilePropertyMagicCookieData = ...
kExtAudioFileProperty_FileDataFormat = ...
kExtAudioFileProperty_ClientDataFormat = ...
kExtAudioFileProperty_FileLengthFrames = ...
kAudioFormatLinearPCM = ...
kAudioFormatFlagIsFloat = ...
kAudioFormatFlagIsBigEndian = ...
kAudioFormatFlagIsSignedInteger = ...
kAudioFormatFlagIsPacked = ...
kAudioFormatFlagsNativeEndian = ...
kAudioFormatFlagsCanonical = ...
kAudioQueueProperty_MagicCookie = ...
kAudio_UnimplementedError = ...
kAudio_FileNotFoundError = ...
kAudio_ParamError = ...
kAudio_MemFullError = ...
kAudioFileUnspecifiedError = ...
kAudioFileUnsupportedFileTypeError = ...
kAudioFileUnsupportedDataFormatError = ...
kAudioFileUnsupportedPropertyError = ...
kAudioFileBadPropertySizeError = ...
kAudioFilePermissionsError = ...
kAudioFileNotOptimizedError = ...
kAudioFileInvalidChunkError = ...
kAudioFileDoesNotAllow64BitDataSizeError = ...
kAudioFileInvalidPacketOffsetError = ...
kAudioFileInvalidFileError = ...
kAudioFileOperationNotSupportedError = ...
kAudioFileNotOpenError = ...
kAudioFileEndOfFileError = ...
kAudioFilePositionError = ...
kAudioFileFileNotFoundError = ...
err_str_db = ...
def err_check(err): # -> None:
    ...

