"""
This type stub file was generated by pyright.
"""

import ctypes
from pyglet.image.codecs import ImageDecoder

"""Decoder for BMP files.

Currently supports version 3 and 4 bitmaps with BI_RGB and BI_BITFIELDS
encoding.  Alpha channel is supported for 32-bit BI_RGB only.
"""
BYTE = ctypes.c_ubyte
WORD = ctypes.c_uint16
DWORD = ctypes.c_uint32
LONG = ctypes.c_int32
FXPT2DOT30 = ctypes.c_uint32
BI_RGB = ...
BI_RLE8 = ...
BI_RLE4 = ...
BI_BITFIELDS = ...
class BITMAPFILEHEADER(ctypes.LittleEndianStructure):
    _pack_ = ...
    _fields_ = ...


class BITMAPINFOHEADER(ctypes.LittleEndianStructure):
    _pack_ = ...
    _fields_ = ...


CIEXYZTRIPLE = ...
class BITMAPV4HEADER(ctypes.LittleEndianStructure):
    _pack_ = ...
    _fields_ = ...


class RGBFields(ctypes.LittleEndianStructure):
    _pack_ = ...
    _fields_ = ...


class RGBQUAD(ctypes.LittleEndianStructure):
    _pack_ = ...
    _fields_ = ...
    def __repr__(self): # -> LiteralString:
        ...
    


def ptr_add(ptr, offset): # -> _Pointer[Any]:
    ...

def to_ctypes(buffer, offset, type):
    ...

class BMPImageDecoder(ImageDecoder):
    def get_file_extensions(self): # -> list[str]:
        ...
    
    def decode(self, filename, file):
        ...
    


def decode_1bit(bits, palette, width, height, pitch, pitch_sign): # -> ImageData:
    ...

def decode_4bit(bits, palette, width, height, pitch, pitch_sign): # -> ImageData:
    ...

def decode_8bit(bits, palette, width, height, pitch, pitch_sign): # -> ImageData:
    ...

def decode_24bit(bits, palette, width, height, pitch, pitch_sign): # -> ImageData:
    ...

def decode_32bit_rgb(bits, palette, width, height, pitch, pitch_sign): # -> ImageData:
    ...

def get_shift(mask): # -> tuple[Literal[0], int] | tuple[int, Literal[0]] | Literal[0]:
    ...

def decode_bitfields(bits, r_mask, g_mask, b_mask, width, height, pitch, pitch_sign): # -> ImageData:
    ...

def get_decoders(): # -> list[BMPImageDecoder]:
    ...

def get_encoders(): # -> list[Any]:
    ...

