"""
This type stub file was generated by pyright.
"""

"""Load application resources from a known path.

Loading resources by specifying relative paths to filenames is often
problematic in Python, as the working directory is not necessarily the same
directory as the application's script files.

This module allows applications to specify a search path for resources.
Relative paths are taken to be relative to the application's ``__main__``
module. ZIP files can appear on the path; they will be searched inside.  The
resource module also behaves as expected when applications are bundled using
Freezers such as PyInstaller, py2exe, py2app, etc..

In addition to providing file references (with the :py:func:`file` function),
the resource module also contains convenience functions for loading images,
textures, fonts, media and documents.

3rd party modules or packages not bound to a specific application should
construct their own :py:class:`Loader` instance and override the path to use the
resources in the module's directory.

Path format
^^^^^^^^^^^

The resource path :py:attr:`path` (see also :py:meth:`Loader.__init__` and
:py:meth:`Loader.path`)
is a list of locations to search for resources.  Locations are searched in the
order given in the path.  If a location is not valid (for example, if the
directory does not exist), it is skipped.

Locations in the path beginning with an "at" symbol (''@'') specify
Python packages.  Other locations specify a ZIP archive or directory on the
filesystem.  Locations that are not absolute are assumed to be relative to the
script home.  Some examples::

    # Search just the `res` directory, assumed to be located alongside the
    # main script file.
    path = ['res']

    # Search the directory containing the module `levels.level1`, followed
    # by the `res/images` directory.
    path = ['@levels.level1', 'res/images']

Paths are always **case-sensitive** and **forward slashes are always used**
as path separators, even in cases when the filesystem or platform does not do this.
This avoids a common programmer error when porting applications between platforms.

The default path is ``['.']``.  If you modify the path, you must call
:py:func:`reindex`.

.. versionadded:: 1.1
"""
class ResourceNotFoundException(Exception):
    """The named resource was not found on the search path."""
    def __init__(self, name) -> None:
        ...
    


class UndetectableShaderType(Exception):
    """The type of the Shader source could not be identified."""
    def __init__(self, name) -> None:
        ...
    


def get_script_home(): # -> Any | str:
    """Get the directory containing the program entry module.

    For ordinary Python scripts, this is the directory containing the
    ``__main__`` module.  For executables created with py2exe the result is
    the directory containing the running executable file.  For OS X bundles
    created using Py2App the result is the Resources directory within the
    running bundle.

    If none of the above cases apply and the file for ``__main__`` cannot
    be determined the working directory is returned.

    When the script is being run by a Python profiler, this function
    may return the directory where the profiler is running instead of
    the directory of the real script. To workaround this behaviour the
    full path to the real script can be specified in :py:attr:`pyglet.resource.path`.

    :rtype: str
    """
    ...

def get_settings_path(name): # -> str:
    """Get a directory to save user preferences.

    Different platforms have different conventions for where to save user
    preferences, saved games, and settings.  This function implements those
    conventions.  Note that the returned path may not exist: applications
    should use ``os.makedirs`` to construct it if desired.

    On Linux, a directory `name` in the user's configuration directory is
    returned (usually under ``~/.config``).

    On Windows (including under Cygwin) the `name` directory in the user's
    ``Application Settings`` directory is returned.

    On Mac OS X the `name` directory under ``~/Library/Application Support``
    is returned.

    :Parameters:
        `name` : str
            The name of the application.

    :rtype: str
    """
    ...

def get_data_path(name): # -> str:
    """Get a directory to save user data.

    For a Posix or Linux based system many distributions have a separate
    directory to store user data for a specific application and this 
    function returns the path to that location.  Note that the returned 
    path may not exist: applications should use ``os.makedirs`` to 
    construct it if desired.

    On Linux, a directory `name` in the user's data directory is returned 
    (usually under ``~/.local/share``).

    On Windows (including under Cygwin) the `name` directory in the user's
    ``Application Settings`` directory is returned.

    On Mac OS X the `name` directory under ``~/Library/Application Support``
    is returned.

    :Parameters:
        `name` : str
            The name of the application.

    :rtype: str
    """
    ...

class Location:
    """Abstract resource location.

    Given a location, a file can be loaded from that location with the `open`
    method.  This provides a convenient way to specify a path to load files
    from, and not necessarily have that path reside on the filesystem.
    """
    def open(self, filename, mode=...):
        """Open a file at this location.

        :Parameters:
            `filename` : str
                The filename to open.  Absolute paths are not supported.
                Relative paths are not supported by most locations (you
                should specify only a filename with no path component).
            `mode` : str
                The file mode to open with.  Only files opened on the
                filesystem make use of this parameter; others ignore it.

        :rtype: file object
        """
        ...
    


class FileLocation(Location):
    """Location on the filesystem.
    """
    def __init__(self, filepath) -> None:
        """Create a location given a relative or absolute path.

        :Parameters:
            `filepath` : str
                Path on the filesystem.
        """
        ...
    
    def open(self, filename, mode=...): # -> IO[Any]:
        ...
    


class ZIPLocation(Location):
    """Location within a ZIP file.
    """
    def __init__(self, zip, dir) -> None:
        """Create a location given an open ZIP file and a path within that
        file.

        :Parameters:
            `zip` : ``zipfile.ZipFile``
                An open ZIP file from the ``zipfile`` module.
            `dir` : str
                A path within that ZIP file.  Can be empty to specify files at
                the top level of the ZIP file.

        """
        ...
    
    def open(self, filename, mode=...): # -> BytesIO:
        ...
    


class URLLocation(Location):
    """Location on the network.

    This class uses the ``urlparse`` and ``urllib2`` modules to open files on
    the network given a URL.
    """
    def __init__(self, base_url) -> None:
        """Create a location given a base URL.

        :Parameters:
            `base_url` : str
                URL string to prepend to filenames.

        """
        ...
    
    def open(self, filename, mode=...): # -> _UrlopenRet:
        ...
    


class Loader:
    """Load program resource files from disk.

    The loader contains a search path which can include filesystem
    directories, ZIP archives and Python packages.

    :Ivariables:
        `path` : list of str
            List of search locations.  After modifying the path you must
            call the `reindex` method.
        `script_home` : str
            Base resource location, defaulting to the location of the
            application script.

    """
    def __init__(self, path=..., script_home=...) -> None:
        """Create a loader for the given path.

        If no path is specified it defaults to ``['.']``; that is, just the
        program directory.

        See the module documentation for details on the path format.

        :Parameters:
            `path` : list of str
                List of locations to search for resources.
            `script_home` : str
                Base location of relative files.  Defaults to the result of
                `get_script_home`.

        """
        ...
    
    def reindex(self): # -> None:
        """Refresh the file index.

        You must call this method if `path` is changed or the filesystem
        layout changes.
        """
        ...
    
    def file(self, name, mode=...):
        """Load a resource.

        :Parameters:
            `name` : str
                Filename of the resource to load.
            `mode` : str
                Combination of ``r``, ``w``, ``a``, ``b`` and ``t`` characters
                with the meaning as for the builtin ``open`` function.

        :rtype: file object
        """
        ...
    
    def location(self, name):
        """Get the location of a resource.

        This method is useful for opening files referenced from a resource.
        For example, an HTML file loaded as a resource might reference some
        images.  These images should be located relative to the HTML file, not
        looked up individually in the loader's path.

        :Parameters:
            `name` : str
                Filename of the resource to locate.

        :rtype: `Location`
        """
        ...
    
    def add_font(self, name): # -> None:
        """Add a font resource to the application.

        Fonts not installed on the system must be added to pyglet before they
        can be used with `font.load`.  Although the font is added with
        its filename using this function, it is loaded by specifying its
        family name.  For example::

            resource.add_font('action_man.ttf')
            action_man = font.load('Action Man')

        :Parameters:
            `name` : str
                Filename of the font resource to add.

        """
        ...
    
    def image(self, name, flip_x=..., flip_y=..., rotate=..., atlas=..., border=...): # -> TextureRegion:
        """Load an image with optional transformation.

        This is similar to `texture`, except the resulting image will be
        packed into a :py:class:`~pyglet.image.atlas.TextureBin` if it is an appropriate size for packing.
        This is more efficient than loading images into separate textures.

        :Parameters:
            `name` : str
                Filename of the image source to load.
            `flip_x` : bool
                If True, the returned image will be flipped horizontally.
            `flip_y` : bool
                If True, the returned image will be flipped vertically.
            `rotate` : int
                The returned image will be rotated clockwise by the given
                number of degrees (a multiple of 90).
            `atlas` : bool
                If True, the image will be loaded into an atlas managed by
                pyglet. If atlas loading is not appropriate for specific
                texturing reasons (e.g. border control is required) then set
                this argument to False.
            `border` : int
                Leaves specified pixels of blank space around each image in
                an atlas, which may help reduce texture bleeding.

        :rtype: `Texture`
        :return: A complete texture if the image is large or not in an atlas,
            otherwise a :py:class:`~pyglet.image.TextureRegion` of a texture atlas.
        """
        ...
    
    def animation(self, name, flip_x=..., flip_y=..., rotate=..., border=...):
        """Load an animation with optional transformation.

        Animations loaded from the same source but with different
        transformations will use the same textures.

        :Parameters:
            `name` : str
                Filename of the animation source to load.
            `flip_x` : bool
                If True, the returned image will be flipped horizontally.
            `flip_y` : bool
                If True, the returned image will be flipped vertically.
            `rotate` : int
                The returned image will be rotated clockwise by the given
                number of degrees (a multiple of 90).
            `border` : int
                Leaves specified pixels of blank space around each image in
                an atlas, which may help reduce texture bleeding.
                
        :rtype: :py:class:`~pyglet.image.Animation`
        """
        ...
    
    def get_cached_image_names(self): # -> list[Any]:
        """Get a list of image filenames that have been cached.

        This is useful for debugging and profiling only.

        :rtype: list
        :return: List of str
        """
        ...
    
    def get_cached_animation_names(self): # -> list[Any]:
        """Get a list of animation filenames that have been cached.

        This is useful for debugging and profiling only.

        :rtype: list
        :return: List of str
        """
        ...
    
    def get_texture_bins(self): # -> list[Any]:
        """Get a list of texture bins in use.

        This is useful for debugging and profiling only.

        :rtype: list
        :return: List of :py:class:`~pyglet.image.atlas.TextureBin`
        """
        ...
    
    def media(self, name, streaming=...):
        """Load a sound or video resource.

        The meaning of `streaming` is as for `media.load`.  Compressed
        sources cannot be streamed (that is, video and compressed audio
        cannot be streamed from a ZIP archive).

        :Parameters:
            `name` : str
                Filename of the media source to load.
            `streaming` : bool
                True if the source should be streamed from disk, False if
                it should be entirely decoded into memory immediately.

        :rtype: `media.Source`
        """
        ...
    
    def texture(self, name):
        """Load a texture.

        The named image will be loaded as a single OpenGL texture.  If the
        dimensions of the image are not powers of 2 a :py:class:`~pyglet.image.TextureRegion` will
        be returned.

        :Parameters:
            `name` : str
                Filename of the image resource to load.

        :rtype: `Texture`
        """
        ...
    
    def model(self, name, batch=...):
        """Load a 3D model.

        :Parameters:
            `name` : str
                Filename of the 3D model to load.
            `batch` : Batch or None
                An optional Batch instance to add this model to.

        :rtype: `Model`
        """
        ...
    
    def html(self, name): # -> FormattedDocument | UnformattedDocument:
        """Load an HTML document.

        :Parameters:
            `name` : str
                Filename of the HTML resource to load.

        :rtype: `FormattedDocument`
        """
        ...
    
    def attributed(self, name): # -> FormattedDocument | UnformattedDocument:
        """Load an attributed text document.

        See `pyglet.text.formats.attributed` for details on this format.

        :Parameters:
            `name` : str
                Filename of the attribute text resource to load.

        :rtype: `FormattedDocument`
        """
        ...
    
    def text(self, name): # -> FormattedDocument | UnformattedDocument:
        """Load a plain text document.

        :Parameters:
            `name` : str
                Filename of the plain text resource to load.

        :rtype: `UnformattedDocument`
        """
        ...
    
    def shader(self, name, shader_type=...): # -> Shader:
        """Load a Shader object.

        :Parameters:
            `name` : str
                Filename of the Shader source to load.
            `shader_type` : str
                A hint for the type of shader, such as 'vertex', 'fragment', etc.
                Not required if your shader has a standard file extension.

        :rtype: A compiled `Shader` object.
        """
        ...
    
    def get_cached_texture_names(self): # -> list[Any]:
        """Get the names of textures currently cached.

        :rtype: list of str
        """
        ...
    


path = ...
class _DefaultLoader(Loader):
    @property
    def path(self): # -> list[Any]:
        ...
    
    @path.setter
    def path(self, value): # -> None:
        ...
    


_default_loader = ...
reindex = ...
file = ...
location = ...
add_font = ...
image = ...
animation = ...
model = ...
media = ...
texture = ...
html = ...
attributed = ...
text = ...
shader = ...
get_cached_texture_names = ...
get_cached_image_names = ...
get_cached_animation_names = ...
get_texture_bins = ...
