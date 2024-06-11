"""
This type stub file was generated by pyright.
"""

import ctypes
from OpenGL import arrays, platform as _p
from OpenGL.raw.GL import _errors, _types as _cs
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

'''Autogenerated by xml_generate script, do not edit!'''
_EXTENSION_NAME = ...
GL_BUFFER = ...
GL_BUFFER_KHR = ...
GL_CONTEXT_FLAG_DEBUG_BIT = ...
GL_CONTEXT_FLAG_DEBUG_BIT_KHR = ...
GL_DEBUG_CALLBACK_FUNCTION = ...
GL_DEBUG_CALLBACK_FUNCTION_KHR = ...
GL_DEBUG_CALLBACK_USER_PARAM = ...
GL_DEBUG_CALLBACK_USER_PARAM_KHR = ...
GL_DEBUG_GROUP_STACK_DEPTH = ...
GL_DEBUG_GROUP_STACK_DEPTH_KHR = ...
GL_DEBUG_LOGGED_MESSAGES = ...
GL_DEBUG_LOGGED_MESSAGES_KHR = ...
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH = ...
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_KHR = ...
GL_DEBUG_OUTPUT = ...
GL_DEBUG_OUTPUT_KHR = ...
GL_DEBUG_OUTPUT_SYNCHRONOUS = ...
GL_DEBUG_OUTPUT_SYNCHRONOUS_KHR = ...
GL_DEBUG_SEVERITY_HIGH = ...
GL_DEBUG_SEVERITY_HIGH_KHR = ...
GL_DEBUG_SEVERITY_LOW = ...
GL_DEBUG_SEVERITY_LOW_KHR = ...
GL_DEBUG_SEVERITY_MEDIUM = ...
GL_DEBUG_SEVERITY_MEDIUM_KHR = ...
GL_DEBUG_SEVERITY_NOTIFICATION = ...
GL_DEBUG_SEVERITY_NOTIFICATION_KHR = ...
GL_DEBUG_SOURCE_API = ...
GL_DEBUG_SOURCE_API_KHR = ...
GL_DEBUG_SOURCE_APPLICATION = ...
GL_DEBUG_SOURCE_APPLICATION_KHR = ...
GL_DEBUG_SOURCE_OTHER = ...
GL_DEBUG_SOURCE_OTHER_KHR = ...
GL_DEBUG_SOURCE_SHADER_COMPILER = ...
GL_DEBUG_SOURCE_SHADER_COMPILER_KHR = ...
GL_DEBUG_SOURCE_THIRD_PARTY = ...
GL_DEBUG_SOURCE_THIRD_PARTY_KHR = ...
GL_DEBUG_SOURCE_WINDOW_SYSTEM = ...
GL_DEBUG_SOURCE_WINDOW_SYSTEM_KHR = ...
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR = ...
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_KHR = ...
GL_DEBUG_TYPE_ERROR = ...
GL_DEBUG_TYPE_ERROR_KHR = ...
GL_DEBUG_TYPE_MARKER = ...
GL_DEBUG_TYPE_MARKER_KHR = ...
GL_DEBUG_TYPE_OTHER = ...
GL_DEBUG_TYPE_OTHER_KHR = ...
GL_DEBUG_TYPE_PERFORMANCE = ...
GL_DEBUG_TYPE_PERFORMANCE_KHR = ...
GL_DEBUG_TYPE_POP_GROUP = ...
GL_DEBUG_TYPE_POP_GROUP_KHR = ...
GL_DEBUG_TYPE_PORTABILITY = ...
GL_DEBUG_TYPE_PORTABILITY_KHR = ...
GL_DEBUG_TYPE_PUSH_GROUP = ...
GL_DEBUG_TYPE_PUSH_GROUP_KHR = ...
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR = ...
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_KHR = ...
GL_DISPLAY_LIST = ...
GL_MAX_DEBUG_GROUP_STACK_DEPTH = ...
GL_MAX_DEBUG_GROUP_STACK_DEPTH_KHR = ...
GL_MAX_DEBUG_LOGGED_MESSAGES = ...
GL_MAX_DEBUG_LOGGED_MESSAGES_KHR = ...
GL_MAX_DEBUG_MESSAGE_LENGTH = ...
GL_MAX_DEBUG_MESSAGE_LENGTH_KHR = ...
GL_MAX_LABEL_LENGTH = ...
GL_MAX_LABEL_LENGTH_KHR = ...
GL_PROGRAM = ...
GL_PROGRAM_KHR = ...
GL_PROGRAM_PIPELINE = ...
GL_PROGRAM_PIPELINE_KHR = ...
GL_QUERY = ...
GL_QUERY_KHR = ...
GL_SAMPLER = ...
GL_SAMPLER_KHR = ...
GL_SHADER = ...
GL_SHADER_KHR = ...
GL_STACK_OVERFLOW = ...
GL_STACK_OVERFLOW_KHR = ...
GL_STACK_UNDERFLOW = ...
GL_STACK_UNDERFLOW_KHR = ...
GL_VERTEX_ARRAY = ...
GL_VERTEX_ARRAY_KHR = ...
@_f
@_p.types(None, _cs.GLDEBUGPROC, ctypes.c_void_p)
def glDebugMessageCallback(callback, userParam): # -> None:
    ...

@_f
@_p.types(None, _cs.GLDEBUGPROCKHR, ctypes.c_void_p)
def glDebugMessageCallbackKHR(callback, userParam): # -> None:
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLenum, _cs.GLsizei, arrays.GLuintArray, _cs.GLboolean)
def glDebugMessageControl(source, type, severity, count, ids, enabled): # -> None:
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLenum, _cs.GLsizei, arrays.GLuintArray, _cs.GLboolean)
def glDebugMessageControlKHR(source, type, severity, count, ids, enabled): # -> None:
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLuint, _cs.GLenum, _cs.GLsizei, arrays.GLcharArray)
def glDebugMessageInsert(source, type, id, severity, length, buf): # -> None:
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLuint, _cs.GLenum, _cs.GLsizei, arrays.GLcharArray)
def glDebugMessageInsertKHR(source, type, id, severity, length, buf): # -> None:
    ...

@_f
@_p.types(_cs.GLuint, _cs.GLuint, _cs.GLsizei, arrays.GLuintArray, arrays.GLuintArray, arrays.GLuintArray, arrays.GLuintArray, arrays.GLsizeiArray, arrays.GLcharArray)
def glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog): # -> None:
    ...

@_f
@_p.types(_cs.GLuint, _cs.GLuint, _cs.GLsizei, arrays.GLuintArray, arrays.GLuintArray, arrays.GLuintArray, arrays.GLuintArray, arrays.GLsizeiArray, arrays.GLcharArray)
def glGetDebugMessageLogKHR(count, bufSize, sources, types, ids, severities, lengths, messageLog): # -> None:
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLcharArray)
def glGetObjectLabel(identifier, name, bufSize, length, label): # -> None:
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLcharArray)
def glGetObjectLabelKHR(identifier, name, bufSize, length, label): # -> None:
    ...

@_f
@_p.types(None, ctypes.c_void_p, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLcharArray)
def glGetObjectPtrLabel(ptr, bufSize, length, label): # -> None:
    ...

@_f
@_p.types(None, ctypes.c_void_p, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLcharArray)
def glGetObjectPtrLabelKHR(ptr, bufSize, length, label): # -> None:
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLvoidpArray)
def glGetPointerv(pname, params): # -> None:
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLvoidpArray)
def glGetPointervKHR(pname, params): # -> None:
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint, _cs.GLsizei, arrays.GLcharArray)
def glObjectLabel(identifier, name, length, label): # -> None:
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint, _cs.GLsizei, arrays.GLcharArray)
def glObjectLabelKHR(identifier, name, length, label): # -> None:
    ...

@_f
@_p.types(None, ctypes.c_void_p, _cs.GLsizei, arrays.GLcharArray)
def glObjectPtrLabel(ptr, length, label): # -> None:
    ...

@_f
@_p.types(None, ctypes.c_void_p, _cs.GLsizei, arrays.GLcharArray)
def glObjectPtrLabelKHR(ptr, length, label): # -> None:
    ...

@_f
@_p.types(None)
def glPopDebugGroup(): # -> None:
    ...

@_f
@_p.types(None)
def glPopDebugGroupKHR(): # -> None:
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint, _cs.GLsizei, arrays.GLcharArray)
def glPushDebugGroup(source, id, length, message): # -> None:
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint, _cs.GLsizei, arrays.GLcharArray)
def glPushDebugGroupKHR(source, id, length, message): # -> None:
    ...
