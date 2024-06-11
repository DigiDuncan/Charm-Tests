"""
This type stub file was generated by pyright.
"""

import ctypes
import pyglet.libs.x11.xlib
import pyglet.gl.glx
from ctypes import *

"""Wrapper for http://oss.sgi.com/projects/ogl-sample/ABI/glxext.h

Generated by tools/gengl.py.
Do not modify this file.
"""
if not hasattr(ctypes, 'c_int64'):
    c_int64 = ...
    c_uint64 = ...
GLX_GLXEXT_VERSION = ...
GLX_SAMPLE_BUFFERS_ARB = ...
GLX_SAMPLES_ARB = ...
GLX_CONTEXT_ALLOW_BUFFER_BYTE_ORDER_MISMATCH_ARB = ...
GLX_RGBA_FLOAT_TYPE_ARB = ...
GLX_RGBA_FLOAT_BIT_ARB = ...
GLX_FRAMEBUFFER_SRGB_CAPABLE_ARB = ...
GLX_CONTEXT_DEBUG_BIT_ARB = ...
GLX_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB = ...
GLX_CONTEXT_MAJOR_VERSION_ARB = ...
GLX_CONTEXT_MINOR_VERSION_ARB = ...
GLX_CONTEXT_FLAGS_ARB = ...
GLX_CONTEXT_CORE_PROFILE_BIT_ARB = ...
GLX_CONTEXT_COMPATIBILITY_PROFILE_BIT_ARB = ...
GLX_CONTEXT_PROFILE_MASK_ARB = ...
GLX_CONTEXT_ROBUST_ACCESS_BIT_ARB = ...
GLX_LOSE_CONTEXT_ON_RESET_ARB = ...
GLX_CONTEXT_RESET_NOTIFICATION_STRATEGY_ARB = ...
GLX_NO_RESET_NOTIFICATION_ARB = ...
GLX_SAMPLE_BUFFERS_SGIS = ...
GLX_SAMPLES_SGIS = ...
GLX_X_VISUAL_TYPE_EXT = ...
GLX_TRANSPARENT_TYPE_EXT = ...
GLX_TRANSPARENT_INDEX_VALUE_EXT = ...
GLX_TRANSPARENT_RED_VALUE_EXT = ...
GLX_TRANSPARENT_GREEN_VALUE_EXT = ...
GLX_TRANSPARENT_BLUE_VALUE_EXT = ...
GLX_TRANSPARENT_ALPHA_VALUE_EXT = ...
GLX_NONE_EXT = ...
GLX_TRUE_COLOR_EXT = ...
GLX_DIRECT_COLOR_EXT = ...
GLX_PSEUDO_COLOR_EXT = ...
GLX_STATIC_COLOR_EXT = ...
GLX_GRAY_SCALE_EXT = ...
GLX_STATIC_GRAY_EXT = ...
GLX_TRANSPARENT_RGB_EXT = ...
GLX_TRANSPARENT_INDEX_EXT = ...
GLX_VISUAL_CAVEAT_EXT = ...
GLX_SLOW_VISUAL_EXT = ...
GLX_NON_CONFORMANT_VISUAL_EXT = ...
GLX_SHARE_CONTEXT_EXT = ...
GLX_VISUAL_ID_EXT = ...
GLX_SCREEN_EXT = ...
GLX_WINDOW_BIT_SGIX = ...
GLX_PIXMAP_BIT_SGIX = ...
GLX_RGBA_BIT_SGIX = ...
GLX_COLOR_INDEX_BIT_SGIX = ...
GLX_DRAWABLE_TYPE_SGIX = ...
GLX_RENDER_TYPE_SGIX = ...
GLX_X_RENDERABLE_SGIX = ...
GLX_FBCONFIG_ID_SGIX = ...
GLX_RGBA_TYPE_SGIX = ...
GLX_COLOR_INDEX_TYPE_SGIX = ...
GLX_PBUFFER_BIT_SGIX = ...
GLX_BUFFER_CLOBBER_MASK_SGIX = ...
GLX_FRONT_LEFT_BUFFER_BIT_SGIX = ...
GLX_FRONT_RIGHT_BUFFER_BIT_SGIX = ...
GLX_BACK_LEFT_BUFFER_BIT_SGIX = ...
GLX_BACK_RIGHT_BUFFER_BIT_SGIX = ...
GLX_AUX_BUFFERS_BIT_SGIX = ...
GLX_DEPTH_BUFFER_BIT_SGIX = ...
GLX_STENCIL_BUFFER_BIT_SGIX = ...
GLX_ACCUM_BUFFER_BIT_SGIX = ...
GLX_SAMPLE_BUFFERS_BIT_SGIX = ...
GLX_MAX_PBUFFER_WIDTH_SGIX = ...
GLX_MAX_PBUFFER_HEIGHT_SGIX = ...
GLX_MAX_PBUFFER_PIXELS_SGIX = ...
GLX_OPTIMAL_PBUFFER_WIDTH_SGIX = ...
GLX_OPTIMAL_PBUFFER_HEIGHT_SGIX = ...
GLX_PRESERVED_CONTENTS_SGIX = ...
GLX_LARGEST_PBUFFER_SGIX = ...
GLX_WIDTH_SGIX = ...
GLX_HEIGHT_SGIX = ...
GLX_EVENT_MASK_SGIX = ...
GLX_DAMAGED_SGIX = ...
GLX_SAVED_SGIX = ...
GLX_WINDOW_SGIX = ...
GLX_PBUFFER_SGIX = ...
GLX_SYNC_FRAME_SGIX = ...
GLX_SYNC_SWAP_SGIX = ...
GLX_DIGITAL_MEDIA_PBUFFER_SGIX = ...
GLX_BLENDED_RGBA_SGIS = ...
GLX_MULTISAMPLE_SUB_RECT_WIDTH_SGIS = ...
GLX_MULTISAMPLE_SUB_RECT_HEIGHT_SGIS = ...
GLX_SAMPLE_BUFFERS_3DFX = ...
GLX_SAMPLES_3DFX = ...
GLX_3DFX_WINDOW_MODE_MESA = ...
GLX_3DFX_FULLSCREEN_MODE_MESA = ...
GLX_VISUAL_SELECT_GROUP_SGIX = ...
GLX_SWAP_METHOD_OML = ...
GLX_SWAP_EXCHANGE_OML = ...
GLX_SWAP_COPY_OML = ...
GLX_SWAP_UNDEFINED_OML = ...
GLX_FLOAT_COMPONENTS_NV = ...
GLX_HYPERPIPE_PIPE_NAME_LENGTH_SGIX = ...
GLX_BAD_HYPERPIPE_CONFIG_SGIX = ...
GLX_BAD_HYPERPIPE_SGIX = ...
GLX_HYPERPIPE_DISPLAY_PIPE_SGIX = ...
GLX_HYPERPIPE_RENDER_PIPE_SGIX = ...
GLX_PIPE_RECT_SGIX = ...
GLX_PIPE_RECT_LIMITS_SGIX = ...
GLX_HYPERPIPE_STEREO_SGIX = ...
GLX_HYPERPIPE_PIXEL_AVERAGE_SGIX = ...
GLX_HYPERPIPE_ID_SGIX = ...
GLX_RGBA_UNSIGNED_FLOAT_TYPE_EXT = ...
GLX_RGBA_UNSIGNED_FLOAT_BIT_EXT = ...
GLX_FRAMEBUFFER_SRGB_CAPABLE_EXT = ...
GLX_TEXTURE_1D_BIT_EXT = ...
GLX_TEXTURE_2D_BIT_EXT = ...
GLX_TEXTURE_RECTANGLE_BIT_EXT = ...
GLX_BIND_TO_TEXTURE_RGB_EXT = ...
GLX_BIND_TO_TEXTURE_RGBA_EXT = ...
GLX_BIND_TO_MIPMAP_TEXTURE_EXT = ...
GLX_BIND_TO_TEXTURE_TARGETS_EXT = ...
GLX_Y_INVERTED_EXT = ...
GLX_TEXTURE_FORMAT_EXT = ...
GLX_TEXTURE_TARGET_EXT = ...
GLX_MIPMAP_TEXTURE_EXT = ...
GLX_TEXTURE_FORMAT_NONE_EXT = ...
GLX_TEXTURE_FORMAT_RGB_EXT = ...
GLX_TEXTURE_FORMAT_RGBA_EXT = ...
GLX_TEXTURE_1D_EXT = ...
GLX_TEXTURE_2D_EXT = ...
GLX_TEXTURE_RECTANGLE_EXT = ...
GLX_FRONT_LEFT_EXT = ...
GLX_FRONT_RIGHT_EXT = ...
GLX_BACK_LEFT_EXT = ...
GLX_BACK_RIGHT_EXT = ...
GLX_FRONT_EXT = ...
GLX_BACK_EXT = ...
GLX_AUX0_EXT = ...
GLX_AUX1_EXT = ...
GLX_AUX2_EXT = ...
GLX_AUX3_EXT = ...
GLX_AUX4_EXT = ...
GLX_AUX5_EXT = ...
GLX_AUX6_EXT = ...
GLX_AUX7_EXT = ...
GLX_AUX8_EXT = ...
GLX_AUX9_EXT = ...
GLX_NUM_VIDEO_SLOTS_NV = ...
GLX_VIDEO_OUT_COLOR_NV = ...
GLX_VIDEO_OUT_ALPHA_NV = ...
GLX_VIDEO_OUT_DEPTH_NV = ...
GLX_VIDEO_OUT_COLOR_AND_ALPHA_NV = ...
GLX_VIDEO_OUT_COLOR_AND_DEPTH_NV = ...
GLX_VIDEO_OUT_FRAME_NV = ...
GLX_VIDEO_OUT_FIELD_1_NV = ...
GLX_VIDEO_OUT_FIELD_2_NV = ...
GLX_VIDEO_OUT_STACKED_FIELDS_1_2_NV = ...
GLX_VIDEO_OUT_STACKED_FIELDS_2_1_NV = ...
GLX_DEVICE_ID_NV = ...
GLX_UNIQUE_ID_NV = ...
GLX_NUM_VIDEO_CAPTURE_SLOTS_NV = ...
GLX_SWAP_INTERVAL_EXT = ...
GLX_MAX_SWAP_INTERVAL_EXT = ...
GLX_BUFFER_SWAP_COMPLETE_INTEL_MASK = ...
GLX_EXCHANGE_COMPLETE_INTEL = ...
GLX_COPY_COMPLETE_INTEL = ...
GLX_FLIP_COMPLETE_INTEL = ...
GLX_COVERAGE_SAMPLES_NV = ...
GLX_COLOR_SAMPLES_NV = ...
GLX_GPU_VENDOR_AMD = ...
GLX_GPU_RENDERER_STRING_AMD = ...
GLX_GPU_OPENGL_VERSION_STRING_AMD = ...
GLX_GPU_FASTEST_TARGET_GPUS_AMD = ...
GLX_GPU_RAM_AMD = ...
GLX_GPU_CLOCK_AMD = ...
GLX_GPU_NUM_PIPES_AMD = ...
GLX_GPU_NUM_SIMD_AMD = ...
GLX_GPU_NUM_RB_AMD = ...
GLX_GPU_NUM_SPI_AMD = ...
GLX_CONTEXT_ES2_PROFILE_BIT_EXT = ...
XID = pyglet.libs.x11.xlib.XID
GLXVideoSourceSGIX = XID
GLXFBConfigIDSGIX = XID
class struct___GLXFBConfigRec(Structure):
    __slots__ = ...


class struct___GLXFBConfigRec(Structure):
    __slots__ = ...


GLXFBConfigSGIX = ...
GLXPbufferSGIX = XID
class struct_anon_106(Structure):
    __slots__ = ...


Display = pyglet.libs.x11.xlib.Display
GLXDrawable = pyglet.gl.glx.GLXDrawable
GLXBufferClobberEventSGIX = struct_anon_106
GLXVideoDeviceNV = c_uint
GLXVideoCaptureDeviceNV = XID
GLX_ARB_multisample = ...
GLX_ARB_fbconfig_float = ...
GLX_ARB_framebuffer_sRGB = ...
GLX_ARB_create_context = ...
GLXContext = pyglet.gl.glx.GLXContext
GLXFBConfig = pyglet.gl.glx.GLXFBConfig
glXCreateContextAttribsARB = ...
PFNGLXCREATECONTEXTATTRIBSARBPROC = ...
GLX_ARB_create_context_profile = ...
GLX_ARB_create_context_robustness = ...
GLX_SGIS_multisample = ...
GLX_EXT_visual_info = ...
GLX_SGI_swap_control = ...
glXSwapIntervalSGI = ...
PFNGLXSWAPINTERVALSGIPROC = ...
GLX_SGI_video_sync = ...
glXGetVideoSyncSGI = ...
glXWaitVideoSyncSGI = ...
PFNGLXGETVIDEOSYNCSGIPROC = ...
PFNGLXWAITVIDEOSYNCSGIPROC = ...
GLX_SGI_make_current_read = ...
glXMakeCurrentReadSGI = ...
glXGetCurrentReadDrawableSGI = ...
PFNGLXMAKECURRENTREADSGIPROC = ...
PFNGLXGETCURRENTREADDRAWABLESGIPROC = ...
GLX_SGIX_video_source = ...
GLX_EXT_visual_rating = ...
GLX_EXT_import_context = ...
glXGetCurrentDisplayEXT = ...
glXQueryContextInfoEXT = ...
GLXContextID = pyglet.gl.glx.GLXContextID
glXGetContextIDEXT = ...
glXImportContextEXT = ...
glXFreeContextEXT = ...
PFNGLXGETCURRENTDISPLAYEXTPROC = ...
PFNGLXQUERYCONTEXTINFOEXTPROC = ...
PFNGLXGETCONTEXTIDEXTPROC = ...
PFNGLXIMPORTCONTEXTEXTPROC = ...
PFNGLXFREECONTEXTEXTPROC = ...
GLX_SGIX_fbconfig = ...
glXGetFBConfigAttribSGIX = ...
glXChooseFBConfigSGIX = ...
GLXPixmap = pyglet.gl.glx.GLXPixmap
Pixmap = pyglet.libs.x11.xlib.Pixmap
glXCreateGLXPixmapWithConfigSGIX = ...
glXCreateContextWithConfigSGIX = ...
XVisualInfo = pyglet.libs.x11.xlib.XVisualInfo
glXGetVisualFromFBConfigSGIX = ...
glXGetFBConfigFromVisualSGIX = ...
PFNGLXGETFBCONFIGATTRIBSGIXPROC = ...
PFNGLXCHOOSEFBCONFIGSGIXPROC = ...
PFNGLXCREATEGLXPIXMAPWITHCONFIGSGIXPROC = ...
PFNGLXCREATECONTEXTWITHCONFIGSGIXPROC = ...
PFNGLXGETVISUALFROMFBCONFIGSGIXPROC = ...
PFNGLXGETFBCONFIGFROMVISUALSGIXPROC = ...
GLX_SGIX_pbuffer = ...
glXCreateGLXPbufferSGIX = ...
glXDestroyGLXPbufferSGIX = ...
glXQueryGLXPbufferSGIX = ...
glXSelectEventSGIX = ...
glXGetSelectedEventSGIX = ...
PFNGLXCREATEGLXPBUFFERSGIXPROC = ...
PFNGLXDESTROYGLXPBUFFERSGIXPROC = ...
PFNGLXQUERYGLXPBUFFERSGIXPROC = ...
PFNGLXSELECTEVENTSGIXPROC = ...
PFNGLXGETSELECTEDEVENTSGIXPROC = ...
GLX_SGI_cushion = ...
Window = pyglet.libs.x11.xlib.Window
glXCushionSGI = ...
PFNGLXCUSHIONSGIPROC = ...
GLX_SGIX_video_resize = ...
glXBindChannelToWindowSGIX = ...
glXChannelRectSGIX = ...
glXQueryChannelRectSGIX = ...
glXQueryChannelDeltasSGIX = ...
GLenum = c_uint
glXChannelRectSyncSGIX = ...
PFNGLXBINDCHANNELTOWINDOWSGIXPROC = ...
PFNGLXCHANNELRECTSGIXPROC = ...
PFNGLXQUERYCHANNELRECTSGIXPROC = ...
PFNGLXQUERYCHANNELDELTASSGIXPROC = ...
PFNGLXCHANNELRECTSYNCSGIXPROC = ...
GLX_SGIX_dmbuffer = ...
GLX_SGIX_swap_group = ...
glXJoinSwapGroupSGIX = ...
PFNGLXJOINSWAPGROUPSGIXPROC = ...
GLX_SGIX_swap_barrier = ...
glXBindSwapBarrierSGIX = ...
glXQueryMaxSwapBarriersSGIX = ...
PFNGLXBINDSWAPBARRIERSGIXPROC = ...
PFNGLXQUERYMAXSWAPBARRIERSSGIXPROC = ...
GLX_SUN_get_transparent_index = ...
glXGetTransparentIndexSUN = ...
PFNGLXGETTRANSPARENTINDEXSUNPROC = ...
GLX_MESA_copy_sub_buffer = ...
glXCopySubBufferMESA = ...
PFNGLXCOPYSUBBUFFERMESAPROC = ...
GLX_MESA_pixmap_colormap = ...
Colormap = pyglet.libs.x11.xlib.Colormap
glXCreateGLXPixmapMESA = ...
PFNGLXCREATEGLXPIXMAPMESAPROC = ...
GLX_MESA_release_buffers = ...
glXReleaseBuffersMESA = ...
PFNGLXRELEASEBUFFERSMESAPROC = ...
GLX_MESA_set_3dfx_mode = ...
glXSet3DfxModeMESA = ...
PFNGLXSET3DFXMODEMESAPROC = ...
GLX_SGIX_visual_select_group = ...
GLX_OML_swap_method = ...
GLX_OML_sync_control = ...
glXGetSyncValuesOML = ...
glXGetMscRateOML = ...
glXSwapBuffersMscOML = ...
glXWaitForMscOML = ...
glXWaitForSbcOML = ...
PFNGLXGETSYNCVALUESOMLPROC = ...
PFNGLXGETMSCRATEOMLPROC = ...
PFNGLXSWAPBUFFERSMSCOMLPROC = ...
PFNGLXWAITFORMSCOMLPROC = ...
PFNGLXWAITFORSBCOMLPROC = ...
GLX_NV_float_buffer = ...
GLX_SGIX_hyperpipe = ...
class struct_anon_107(Structure):
    __slots__ = ...


GLXHyperpipeNetworkSGIX = struct_anon_107
class struct_anon_108(Structure):
    __slots__ = ...


GLXHyperpipeConfigSGIX = struct_anon_108
class struct_anon_109(Structure):
    __slots__ = ...


GLXPipeRect = struct_anon_109
class struct_anon_110(Structure):
    __slots__ = ...


GLXPipeRectLimits = struct_anon_110
glXQueryHyperpipeNetworkSGIX = ...
glXHyperpipeConfigSGIX = ...
glXQueryHyperpipeConfigSGIX = ...
glXDestroyHyperpipeConfigSGIX = ...
glXBindHyperpipeSGIX = ...
glXQueryHyperpipeBestAttribSGIX = ...
glXHyperpipeAttribSGIX = ...
glXQueryHyperpipeAttribSGIX = ...
PFNGLXQUERYHYPERPIPENETWORKSGIXPROC = ...
PFNGLXHYPERPIPECONFIGSGIXPROC = ...
PFNGLXQUERYHYPERPIPECONFIGSGIXPROC = ...
PFNGLXDESTROYHYPERPIPECONFIGSGIXPROC = ...
PFNGLXBINDHYPERPIPESGIXPROC = ...
PFNGLXQUERYHYPERPIPEBESTATTRIBSGIXPROC = ...
PFNGLXHYPERPIPEATTRIBSGIXPROC = ...
PFNGLXQUERYHYPERPIPEATTRIBSGIXPROC = ...
GLX_MESA_agp_offset = ...
glXGetAGPOffsetMESA = ...
PFNGLXGETAGPOFFSETMESAPROC = ...
GLX_EXT_fbconfig_packed_float = ...
GLX_EXT_framebuffer_sRGB = ...
GLX_EXT_texture_from_pixmap = ...
glXBindTexImageEXT = ...
glXReleaseTexImageEXT = ...
PFNGLXBINDTEXIMAGEEXTPROC = ...
PFNGLXRELEASETEXIMAGEEXTPROC = ...
GLX_NV_present_video = ...
glXEnumerateVideoDevicesNV = ...
glXBindVideoDeviceNV = ...
PFNGLXENUMERATEVIDEODEVICESNVPROC = ...
PFNGLXBINDVIDEODEVICENVPROC = ...
GLX_NV_video_output = ...
glXGetVideoDeviceNV = ...
glXReleaseVideoDeviceNV = ...
GLXPbuffer = pyglet.gl.glx.GLXPbuffer
glXBindVideoImageNV = ...
glXReleaseVideoImageNV = ...
GLboolean = c_ubyte
glXSendPbufferToVideoNV = ...
glXGetVideoInfoNV = ...
PFNGLXGETVIDEODEVICENVPROC = ...
PFNGLXRELEASEVIDEODEVICENVPROC = ...
PFNGLXBINDVIDEOIMAGENVPROC = ...
PFNGLXRELEASEVIDEOIMAGENVPROC = ...
PFNGLXSENDPBUFFERTOVIDEONVPROC = ...
PFNGLXGETVIDEOINFONVPROC = ...
GLX_NV_swap_group = ...
GLuint = c_uint
glXJoinSwapGroupNV = ...
glXBindSwapBarrierNV = ...
glXQuerySwapGroupNV = ...
glXQueryMaxSwapGroupsNV = ...
glXQueryFrameCountNV = ...
glXResetFrameCountNV = ...
PFNGLXJOINSWAPGROUPNVPROC = ...
PFNGLXBINDSWAPBARRIERNVPROC = ...
PFNGLXQUERYSWAPGROUPNVPROC = ...
PFNGLXQUERYMAXSWAPGROUPSNVPROC = ...
PFNGLXQUERYFRAMECOUNTNVPROC = ...
PFNGLXRESETFRAMECOUNTNVPROC = ...
GLX_NV_video_capture = ...
glXBindVideoCaptureDeviceNV = ...
glXEnumerateVideoCaptureDevicesNV = ...
glXLockVideoCaptureDeviceNV = ...
glXQueryVideoCaptureDeviceNV = ...
glXReleaseVideoCaptureDeviceNV = ...
PFNGLXBINDVIDEOCAPTUREDEVICENVPROC = ...
PFNGLXENUMERATEVIDEOCAPTUREDEVICESNVPROC = ...
PFNGLXLOCKVIDEOCAPTUREDEVICENVPROC = ...
PFNGLXQUERYVIDEOCAPTUREDEVICENVPROC = ...
PFNGLXRELEASEVIDEOCAPTUREDEVICENVPROC = ...
GLX_EXT_swap_control = ...
glXSwapIntervalEXT = ...
PFNGLXSWAPINTERVALEXTPROC = ...
GLX_NV_copy_image = ...
GLint = c_int
GLsizei = c_int
glXCopyImageSubDataNV = ...
PFNGLXCOPYIMAGESUBDATANVPROC = ...
GLX_INTEL_swap_event = ...
GLX_NV_multisample_coverage = ...
__all__ = ['GLX_GLXEXT_VERSION', 'GLX_SAMPLE_BUFFERS_ARB', 'GLX_SAMPLES_ARB', 'GLX_CONTEXT_ALLOW_BUFFER_BYTE_ORDER_MISMATCH_ARB', 'GLX_RGBA_FLOAT_TYPE_ARB', 'GLX_RGBA_FLOAT_BIT_ARB', 'GLX_FRAMEBUFFER_SRGB_CAPABLE_ARB', 'GLX_CONTEXT_DEBUG_BIT_ARB', 'GLX_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB', 'GLX_CONTEXT_MAJOR_VERSION_ARB', 'GLX_CONTEXT_MINOR_VERSION_ARB', 'GLX_CONTEXT_FLAGS_ARB', 'GLX_CONTEXT_CORE_PROFILE_BIT_ARB', 'GLX_CONTEXT_COMPATIBILITY_PROFILE_BIT_ARB', 'GLX_CONTEXT_PROFILE_MASK_ARB', 'GLX_CONTEXT_ROBUST_ACCESS_BIT_ARB', 'GLX_LOSE_CONTEXT_ON_RESET_ARB', 'GLX_CONTEXT_RESET_NOTIFICATION_STRATEGY_ARB', 'GLX_NO_RESET_NOTIFICATION_ARB', 'GLX_SAMPLE_BUFFERS_SGIS', 'GLX_SAMPLES_SGIS', 'GLX_X_VISUAL_TYPE_EXT', 'GLX_TRANSPARENT_TYPE_EXT', 'GLX_TRANSPARENT_INDEX_VALUE_EXT', 'GLX_TRANSPARENT_RED_VALUE_EXT', 'GLX_TRANSPARENT_GREEN_VALUE_EXT', 'GLX_TRANSPARENT_BLUE_VALUE_EXT', 'GLX_TRANSPARENT_ALPHA_VALUE_EXT', 'GLX_NONE_EXT', 'GLX_TRUE_COLOR_EXT', 'GLX_DIRECT_COLOR_EXT', 'GLX_PSEUDO_COLOR_EXT', 'GLX_STATIC_COLOR_EXT', 'GLX_GRAY_SCALE_EXT', 'GLX_STATIC_GRAY_EXT', 'GLX_TRANSPARENT_RGB_EXT', 'GLX_TRANSPARENT_INDEX_EXT', 'GLX_VISUAL_CAVEAT_EXT', 'GLX_SLOW_VISUAL_EXT', 'GLX_NON_CONFORMANT_VISUAL_EXT', 'GLX_SHARE_CONTEXT_EXT', 'GLX_VISUAL_ID_EXT', 'GLX_SCREEN_EXT', 'GLX_WINDOW_BIT_SGIX', 'GLX_PIXMAP_BIT_SGIX', 'GLX_RGBA_BIT_SGIX', 'GLX_COLOR_INDEX_BIT_SGIX', 'GLX_DRAWABLE_TYPE_SGIX', 'GLX_RENDER_TYPE_SGIX', 'GLX_X_RENDERABLE_SGIX', 'GLX_FBCONFIG_ID_SGIX', 'GLX_RGBA_TYPE_SGIX', 'GLX_COLOR_INDEX_TYPE_SGIX', 'GLX_PBUFFER_BIT_SGIX', 'GLX_BUFFER_CLOBBER_MASK_SGIX', 'GLX_FRONT_LEFT_BUFFER_BIT_SGIX', 'GLX_FRONT_RIGHT_BUFFER_BIT_SGIX', 'GLX_BACK_LEFT_BUFFER_BIT_SGIX', 'GLX_BACK_RIGHT_BUFFER_BIT_SGIX', 'GLX_AUX_BUFFERS_BIT_SGIX', 'GLX_DEPTH_BUFFER_BIT_SGIX', 'GLX_STENCIL_BUFFER_BIT_SGIX', 'GLX_ACCUM_BUFFER_BIT_SGIX', 'GLX_SAMPLE_BUFFERS_BIT_SGIX', 'GLX_MAX_PBUFFER_WIDTH_SGIX', 'GLX_MAX_PBUFFER_HEIGHT_SGIX', 'GLX_MAX_PBUFFER_PIXELS_SGIX', 'GLX_OPTIMAL_PBUFFER_WIDTH_SGIX', 'GLX_OPTIMAL_PBUFFER_HEIGHT_SGIX', 'GLX_PRESERVED_CONTENTS_SGIX', 'GLX_LARGEST_PBUFFER_SGIX', 'GLX_WIDTH_SGIX', 'GLX_HEIGHT_SGIX', 'GLX_EVENT_MASK_SGIX', 'GLX_DAMAGED_SGIX', 'GLX_SAVED_SGIX', 'GLX_WINDOW_SGIX', 'GLX_PBUFFER_SGIX', 'GLX_SYNC_FRAME_SGIX', 'GLX_SYNC_SWAP_SGIX', 'GLX_DIGITAL_MEDIA_PBUFFER_SGIX', 'GLX_BLENDED_RGBA_SGIS', 'GLX_MULTISAMPLE_SUB_RECT_WIDTH_SGIS', 'GLX_MULTISAMPLE_SUB_RECT_HEIGHT_SGIS', 'GLX_SAMPLE_BUFFERS_3DFX', 'GLX_SAMPLES_3DFX', 'GLX_3DFX_WINDOW_MODE_MESA', 'GLX_3DFX_FULLSCREEN_MODE_MESA', 'GLX_VISUAL_SELECT_GROUP_SGIX', 'GLX_SWAP_METHOD_OML', 'GLX_SWAP_EXCHANGE_OML', 'GLX_SWAP_COPY_OML', 'GLX_SWAP_UNDEFINED_OML', 'GLX_FLOAT_COMPONENTS_NV', 'GLX_HYPERPIPE_PIPE_NAME_LENGTH_SGIX', 'GLX_BAD_HYPERPIPE_CONFIG_SGIX', 'GLX_BAD_HYPERPIPE_SGIX', 'GLX_HYPERPIPE_DISPLAY_PIPE_SGIX', 'GLX_HYPERPIPE_RENDER_PIPE_SGIX', 'GLX_PIPE_RECT_SGIX', 'GLX_PIPE_RECT_LIMITS_SGIX', 'GLX_HYPERPIPE_STEREO_SGIX', 'GLX_HYPERPIPE_PIXEL_AVERAGE_SGIX', 'GLX_HYPERPIPE_ID_SGIX', 'GLX_RGBA_UNSIGNED_FLOAT_TYPE_EXT', 'GLX_RGBA_UNSIGNED_FLOAT_BIT_EXT', 'GLX_FRAMEBUFFER_SRGB_CAPABLE_EXT', 'GLX_TEXTURE_1D_BIT_EXT', 'GLX_TEXTURE_2D_BIT_EXT', 'GLX_TEXTURE_RECTANGLE_BIT_EXT', 'GLX_BIND_TO_TEXTURE_RGB_EXT', 'GLX_BIND_TO_TEXTURE_RGBA_EXT', 'GLX_BIND_TO_MIPMAP_TEXTURE_EXT', 'GLX_BIND_TO_TEXTURE_TARGETS_EXT', 'GLX_Y_INVERTED_EXT', 'GLX_TEXTURE_FORMAT_EXT', 'GLX_TEXTURE_TARGET_EXT', 'GLX_MIPMAP_TEXTURE_EXT', 'GLX_TEXTURE_FORMAT_NONE_EXT', 'GLX_TEXTURE_FORMAT_RGB_EXT', 'GLX_TEXTURE_FORMAT_RGBA_EXT', 'GLX_TEXTURE_1D_EXT', 'GLX_TEXTURE_2D_EXT', 'GLX_TEXTURE_RECTANGLE_EXT', 'GLX_FRONT_LEFT_EXT', 'GLX_FRONT_RIGHT_EXT', 'GLX_BACK_LEFT_EXT', 'GLX_BACK_RIGHT_EXT', 'GLX_FRONT_EXT', 'GLX_BACK_EXT', 'GLX_AUX0_EXT', 'GLX_AUX1_EXT', 'GLX_AUX2_EXT', 'GLX_AUX3_EXT', 'GLX_AUX4_EXT', 'GLX_AUX5_EXT', 'GLX_AUX6_EXT', 'GLX_AUX7_EXT', 'GLX_AUX8_EXT', 'GLX_AUX9_EXT', 'GLX_NUM_VIDEO_SLOTS_NV', 'GLX_VIDEO_OUT_COLOR_NV', 'GLX_VIDEO_OUT_ALPHA_NV', 'GLX_VIDEO_OUT_DEPTH_NV', 'GLX_VIDEO_OUT_COLOR_AND_ALPHA_NV', 'GLX_VIDEO_OUT_COLOR_AND_DEPTH_NV', 'GLX_VIDEO_OUT_FRAME_NV', 'GLX_VIDEO_OUT_FIELD_1_NV', 'GLX_VIDEO_OUT_FIELD_2_NV', 'GLX_VIDEO_OUT_STACKED_FIELDS_1_2_NV', 'GLX_VIDEO_OUT_STACKED_FIELDS_2_1_NV', 'GLX_DEVICE_ID_NV', 'GLX_UNIQUE_ID_NV', 'GLX_NUM_VIDEO_CAPTURE_SLOTS_NV', 'GLX_SWAP_INTERVAL_EXT', 'GLX_MAX_SWAP_INTERVAL_EXT', 'GLX_BUFFER_SWAP_COMPLETE_INTEL_MASK', 'GLX_EXCHANGE_COMPLETE_INTEL', 'GLX_COPY_COMPLETE_INTEL', 'GLX_FLIP_COMPLETE_INTEL', 'GLX_COVERAGE_SAMPLES_NV', 'GLX_COLOR_SAMPLES_NV', 'GLX_GPU_VENDOR_AMD', 'GLX_GPU_RENDERER_STRING_AMD', 'GLX_GPU_OPENGL_VERSION_STRING_AMD', 'GLX_GPU_FASTEST_TARGET_GPUS_AMD', 'GLX_GPU_RAM_AMD', 'GLX_GPU_CLOCK_AMD', 'GLX_GPU_NUM_PIPES_AMD', 'GLX_GPU_NUM_SIMD_AMD', 'GLX_GPU_NUM_RB_AMD', 'GLX_GPU_NUM_SPI_AMD', 'GLX_CONTEXT_ES2_PROFILE_BIT_EXT', 'GLXVideoSourceSGIX', 'GLXFBConfigIDSGIX', 'GLXFBConfigSGIX', 'GLXPbufferSGIX', 'GLXBufferClobberEventSGIX', 'GLXVideoDeviceNV', 'GLXVideoCaptureDeviceNV', 'GLX_ARB_multisample', 'GLX_ARB_fbconfig_float', 'GLX_ARB_framebuffer_sRGB', 'GLX_ARB_create_context', 'glXCreateContextAttribsARB', 'PFNGLXCREATECONTEXTATTRIBSARBPROC', 'GLX_ARB_create_context_profile', 'GLX_ARB_create_context_robustness', 'GLX_SGIS_multisample', 'GLX_EXT_visual_info', 'GLX_SGI_swap_control', 'glXSwapIntervalSGI', 'PFNGLXSWAPINTERVALSGIPROC', 'GLX_SGI_video_sync', 'glXGetVideoSyncSGI', 'glXWaitVideoSyncSGI', 'PFNGLXGETVIDEOSYNCSGIPROC', 'PFNGLXWAITVIDEOSYNCSGIPROC', 'GLX_SGI_make_current_read', 'glXMakeCurrentReadSGI', 'glXGetCurrentReadDrawableSGI', 'PFNGLXMAKECURRENTREADSGIPROC', 'PFNGLXGETCURRENTREADDRAWABLESGIPROC', 'GLX_SGIX_video_source', 'GLX_EXT_visual_rating', 'GLX_EXT_import_context', 'glXGetCurrentDisplayEXT', 'glXQueryContextInfoEXT', 'glXGetContextIDEXT', 'glXImportContextEXT', 'glXFreeContextEXT', 'PFNGLXGETCURRENTDISPLAYEXTPROC', 'PFNGLXQUERYCONTEXTINFOEXTPROC', 'PFNGLXGETCONTEXTIDEXTPROC', 'PFNGLXIMPORTCONTEXTEXTPROC', 'PFNGLXFREECONTEXTEXTPROC', 'GLX_SGIX_fbconfig', 'glXGetFBConfigAttribSGIX', 'glXChooseFBConfigSGIX', 'glXCreateGLXPixmapWithConfigSGIX', 'glXCreateContextWithConfigSGIX', 'glXGetVisualFromFBConfigSGIX', 'glXGetFBConfigFromVisualSGIX', 'PFNGLXGETFBCONFIGATTRIBSGIXPROC', 'PFNGLXCHOOSEFBCONFIGSGIXPROC', 'PFNGLXCREATEGLXPIXMAPWITHCONFIGSGIXPROC', 'PFNGLXCREATECONTEXTWITHCONFIGSGIXPROC', 'PFNGLXGETVISUALFROMFBCONFIGSGIXPROC', 'PFNGLXGETFBCONFIGFROMVISUALSGIXPROC', 'GLX_SGIX_pbuffer', 'glXCreateGLXPbufferSGIX', 'glXDestroyGLXPbufferSGIX', 'glXQueryGLXPbufferSGIX', 'glXSelectEventSGIX', 'glXGetSelectedEventSGIX', 'PFNGLXCREATEGLXPBUFFERSGIXPROC', 'PFNGLXDESTROYGLXPBUFFERSGIXPROC', 'PFNGLXQUERYGLXPBUFFERSGIXPROC', 'PFNGLXSELECTEVENTSGIXPROC', 'PFNGLXGETSELECTEDEVENTSGIXPROC', 'GLX_SGI_cushion', 'glXCushionSGI', 'PFNGLXCUSHIONSGIPROC', 'GLX_SGIX_video_resize', 'glXBindChannelToWindowSGIX', 'glXChannelRectSGIX', 'glXQueryChannelRectSGIX', 'glXQueryChannelDeltasSGIX', 'glXChannelRectSyncSGIX', 'PFNGLXBINDCHANNELTOWINDOWSGIXPROC', 'PFNGLXCHANNELRECTSGIXPROC', 'PFNGLXQUERYCHANNELRECTSGIXPROC', 'PFNGLXQUERYCHANNELDELTASSGIXPROC', 'PFNGLXCHANNELRECTSYNCSGIXPROC', 'GLX_SGIX_dmbuffer', 'GLX_SGIX_swap_group', 'glXJoinSwapGroupSGIX', 'PFNGLXJOINSWAPGROUPSGIXPROC', 'GLX_SGIX_swap_barrier', 'glXBindSwapBarrierSGIX', 'glXQueryMaxSwapBarriersSGIX', 'PFNGLXBINDSWAPBARRIERSGIXPROC', 'PFNGLXQUERYMAXSWAPBARRIERSSGIXPROC', 'GLX_SUN_get_transparent_index', 'glXGetTransparentIndexSUN', 'PFNGLXGETTRANSPARENTINDEXSUNPROC', 'GLX_MESA_copy_sub_buffer', 'glXCopySubBufferMESA', 'PFNGLXCOPYSUBBUFFERMESAPROC', 'GLX_MESA_pixmap_colormap', 'glXCreateGLXPixmapMESA', 'PFNGLXCREATEGLXPIXMAPMESAPROC', 'GLX_MESA_release_buffers', 'glXReleaseBuffersMESA', 'PFNGLXRELEASEBUFFERSMESAPROC', 'GLX_MESA_set_3dfx_mode', 'glXSet3DfxModeMESA', 'PFNGLXSET3DFXMODEMESAPROC', 'GLX_SGIX_visual_select_group', 'GLX_OML_swap_method', 'GLX_OML_sync_control', 'glXGetSyncValuesOML', 'glXGetMscRateOML', 'glXSwapBuffersMscOML', 'glXWaitForMscOML', 'glXWaitForSbcOML', 'PFNGLXGETSYNCVALUESOMLPROC', 'PFNGLXGETMSCRATEOMLPROC', 'PFNGLXSWAPBUFFERSMSCOMLPROC', 'PFNGLXWAITFORMSCOMLPROC', 'PFNGLXWAITFORSBCOMLPROC', 'GLX_NV_float_buffer', 'GLX_SGIX_hyperpipe', 'GLXHyperpipeNetworkSGIX', 'GLXHyperpipeConfigSGIX', 'GLXPipeRect', 'GLXPipeRectLimits', 'glXQueryHyperpipeNetworkSGIX', 'glXHyperpipeConfigSGIX', 'glXQueryHyperpipeConfigSGIX', 'glXDestroyHyperpipeConfigSGIX', 'glXBindHyperpipeSGIX', 'glXQueryHyperpipeBestAttribSGIX', 'glXHyperpipeAttribSGIX', 'glXQueryHyperpipeAttribSGIX', 'PFNGLXQUERYHYPERPIPENETWORKSGIXPROC', 'PFNGLXHYPERPIPECONFIGSGIXPROC', 'PFNGLXQUERYHYPERPIPECONFIGSGIXPROC', 'PFNGLXDESTROYHYPERPIPECONFIGSGIXPROC', 'PFNGLXBINDHYPERPIPESGIXPROC', 'PFNGLXQUERYHYPERPIPEBESTATTRIBSGIXPROC', 'PFNGLXHYPERPIPEATTRIBSGIXPROC', 'PFNGLXQUERYHYPERPIPEATTRIBSGIXPROC', 'GLX_MESA_agp_offset', 'glXGetAGPOffsetMESA', 'PFNGLXGETAGPOFFSETMESAPROC', 'GLX_EXT_fbconfig_packed_float', 'GLX_EXT_framebuffer_sRGB', 'GLX_EXT_texture_from_pixmap', 'glXBindTexImageEXT', 'glXReleaseTexImageEXT', 'PFNGLXBINDTEXIMAGEEXTPROC', 'PFNGLXRELEASETEXIMAGEEXTPROC', 'GLX_NV_present_video', 'glXEnumerateVideoDevicesNV', 'glXBindVideoDeviceNV', 'PFNGLXENUMERATEVIDEODEVICESNVPROC', 'PFNGLXBINDVIDEODEVICENVPROC', 'GLX_NV_video_output', 'glXGetVideoDeviceNV', 'glXReleaseVideoDeviceNV', 'glXBindVideoImageNV', 'glXReleaseVideoImageNV', 'glXSendPbufferToVideoNV', 'glXGetVideoInfoNV', 'PFNGLXGETVIDEODEVICENVPROC', 'PFNGLXRELEASEVIDEODEVICENVPROC', 'PFNGLXBINDVIDEOIMAGENVPROC', 'PFNGLXRELEASEVIDEOIMAGENVPROC', 'PFNGLXSENDPBUFFERTOVIDEONVPROC', 'PFNGLXGETVIDEOINFONVPROC', 'GLX_NV_swap_group', 'glXJoinSwapGroupNV', 'glXBindSwapBarrierNV', 'glXQuerySwapGroupNV', 'glXQueryMaxSwapGroupsNV', 'glXQueryFrameCountNV', 'glXResetFrameCountNV', 'PFNGLXJOINSWAPGROUPNVPROC', 'PFNGLXBINDSWAPBARRIERNVPROC', 'PFNGLXQUERYSWAPGROUPNVPROC', 'PFNGLXQUERYMAXSWAPGROUPSNVPROC', 'PFNGLXQUERYFRAMECOUNTNVPROC', 'PFNGLXRESETFRAMECOUNTNVPROC', 'GLX_NV_video_capture', 'glXBindVideoCaptureDeviceNV', 'glXEnumerateVideoCaptureDevicesNV', 'glXLockVideoCaptureDeviceNV', 'glXQueryVideoCaptureDeviceNV', 'glXReleaseVideoCaptureDeviceNV', 'PFNGLXBINDVIDEOCAPTUREDEVICENVPROC', 'PFNGLXENUMERATEVIDEOCAPTUREDEVICESNVPROC', 'PFNGLXLOCKVIDEOCAPTUREDEVICENVPROC', 'PFNGLXQUERYVIDEOCAPTUREDEVICENVPROC', 'PFNGLXRELEASEVIDEOCAPTUREDEVICENVPROC', 'GLX_EXT_swap_control', 'glXSwapIntervalEXT', 'PFNGLXSWAPINTERVALEXTPROC', 'GLX_NV_copy_image', 'glXCopyImageSubDataNV', 'PFNGLXCOPYIMAGESUBDATANVPROC', 'GLX_INTEL_swap_event', 'GLX_NV_multisample_coverage']
