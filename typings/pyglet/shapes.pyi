"""
This type stub file was generated by pyright.
"""

from abc import ABC
from pyglet.graphics import Group

"""2D shapes.

This module provides classes for a variety of simplistic 2D shapes,
such as Rectangles, Circles, and Lines. These shapes are made
internally from OpenGL primitives, and provide excellent performance
when drawn as part of a :py:class:`~pyglet.graphics.Batch`.
Convenience methods are provided for positioning, changing color
and opacity, and rotation (where applicable). To create more
complex shapes than what is provided here, the lower level
graphics API is more appropriate. See the :ref:`guide_graphics`
for more details. You can also use the ``in`` operator to check
whether a point is inside a shape.

A simple example of drawing shapes::

    import pyglet
    from pyglet import shapes

    window = pyglet.window.Window(960, 540)
    batch = pyglet.graphics.Batch()

    circle = shapes.Circle(700, 150, 100, color=(50, 225, 30), batch=batch)
    square = shapes.Rectangle(200, 200, 200, 200, color=(55, 55, 255), batch=batch)
    rectangle = shapes.Rectangle(250, 300, 400, 200, color=(255, 22, 20), batch=batch)
    rectangle.opacity = 128
    rectangle.rotation = 33
    line = shapes.Line(100, 100, 100, 200, thickness=19, batch=batch)
    line2 = shapes.Line(150, 150, 444, 111, thickness=4, color=(200, 20, 20), batch=batch)
    star = shapes.Star(800, 400, 60, 40, num_spikes=20, color=(255, 255, 0), batch=batch)

    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    pyglet.app.run()


.. note:: Some Shapes, such as Lines and Triangles, have multiple coordinates.
          If you update the x, y coordinate, this will also affect the secondary
          coordinates. This allows you to move the shape without affecting it's
          overall dimensions.

.. versionadded:: 1.5.4
"""
vertex_source = ...
fragment_source = ...
def get_default_shader():
    ...

class _ShapeGroup(Group):
    """Shared Shape rendering Group.

    The group is automatically coalesced with other shape groups
    sharing the same parent group and blend parameters.
    """
    def __init__(self, blend_src, blend_dest, program, parent=...) -> None:
        """Create a Shape group.

        The group is created internally. Usually you do not
        need to explicitly create it.

        :Parameters:
            `blend_src` : int
                OpenGL blend source mode; for example,
                ``GL_SRC_ALPHA``.
            `blend_dest` : int
                OpenGL blend destination mode; for example,
                ``GL_ONE_MINUS_SRC_ALPHA``.
            `program` : `~pyglet.graphics.shader.ShaderProgram`
                The ShaderProgram to use.
            `parent` : `~pyglet.graphics.Group`
                Optional parent group.
        """
        ...
    
    def set_state(self): # -> None:
        ...
    
    def unset_state(self): # -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


class ShapeBase(ABC):
    """Base class for all shape objects.

    A number of default shapes are provided in this module. Curves are
    approximated using multiple vertices.

    If you need shapes or functionality not provided in this module,
    you can write your own custom subclass of `ShapeBase` by using
    the provided shapes as reference.
    """
    _rgba = ...
    _rotation = ...
    _visible = ...
    _x = ...
    _y = ...
    _anchor_x = ...
    _anchor_y = ...
    _batch = ...
    _group = ...
    _num_verts = ...
    _vertex_list = ...
    _draw_mode = ...
    group_class = _ShapeGroup
    def __del__(self): # -> None:
        ...
    
    def __contains__(self, point):
        """Test whether a point is inside a shape."""
        ...
    
    @property
    def rotation(self) -> float:
        """Clockwise rotation of the shape in degrees.

        It will be rotated about its (anchor_x, anchor_y) position,
        which defaults to the first vertex point of the shape.

        For most shapes, this is the lower left corner. The shapes
        below default to the points their ``radius`` values are
        measured from:

            * :py:class:`.Circle`
            * :py:class:`.Ellipse`
            * :py:class:`.Arc`
            * :py:class:`.Sector`
            * :py:class:`.Star`
        """
        ...
    
    @rotation.setter
    def rotation(self, rotation: float) -> None:
        ...
    
    def draw(self): # -> None:
        """Draw the shape at its current position.

        Using this method is not recommended. Instead, add the
        shape to a `pyglet.graphics.Batch` for efficient rendering.
        """
        ...
    
    def delete(self): # -> None:
        """Force immediate removal of the shape from video memory.

        It is recommended to call this whenever you delete a shape,
        as the Python garbage collector will not necessarily call the
        finalizer as soon as the sprite falls out of scope.
        """
        ...
    
    @property
    def x(self): # -> int:
        """X coordinate of the shape.

        :type: int or float
        """
        ...
    
    @x.setter
    def x(self, value): # -> None:
        ...
    
    @property
    def y(self): # -> int:
        """Y coordinate of the shape.

        :type: int or float
        """
        ...
    
    @y.setter
    def y(self, value): # -> None:
        ...
    
    @property
    def position(self): # -> tuple[int | Any, int | Any]:
        """The (x, y) coordinates of the shape, as a tuple.

        :Parameters:
            `x` : int or float
                X coordinate of the sprite.
            `y` : int or float
                Y coordinate of the sprite.
        """
        ...
    
    @position.setter
    def position(self, values): # -> None:
        ...
    
    @property
    def anchor_x(self): # -> int:
        """The X coordinate of the anchor point

        :type: int or float
        """
        ...
    
    @anchor_x.setter
    def anchor_x(self, value): # -> None:
        ...
    
    @property
    def anchor_y(self): # -> int:
        """The Y coordinate of the anchor point

        :type: int or float
        """
        ...
    
    @anchor_y.setter
    def anchor_y(self, value): # -> None:
        ...
    
    @property
    def anchor_position(self): # -> tuple[int | Any, int | Any]:
        """The (x, y) coordinates of the anchor point, as a tuple.

        :Parameters:
            `x` : int or float
                X coordinate of the anchor point.
            `y` : int or float
                Y coordinate of the anchor point.
        """
        ...
    
    @anchor_position.setter
    def anchor_position(self, values): # -> None:
        ...
    
    @property
    def color(self): # -> tuple[Literal[255], Literal[255], Literal[255], Literal[255]] | tuple[Any, Any, Any, Any] | tuple[Any, Any, Any, Any | Literal[255]] | tuple[*tuple[Any | Literal[255], ...], Any]:
        """The shape's color as an RGBA tuple.

        The color is stored as an RGBA tuple of integers in the
        following order: '(red, green, blue, alpha)'. Each channel
        is between 0 (unsaturated) and 255 (saturated).

        You can set the color with either of the following:

        1. An RGBA tuple of integers '(red, green, blue, alpha)'
        2. An RGB tuple of integers '(red, green, blue)'

        In the latter case, the shape's current alpha value will be
        preserved. Each color component must be in the range 0 (dark)
        to 255 (saturated).

        :type: (int, int, int, int)
        """
        ...
    
    @color.setter
    def color(self, values): # -> None:
        ...
    
    @property
    def opacity(self): # -> Literal[255]:
        """Blend opacity.

        This property sets the alpha component of the color of the shape.
        With the default blend mode (see the constructor), this allows the
        shape to be drawn with fractional opacity, blending with the
        background.

        An opacity of 255 (the default) has no effect.  An opacity of 128
        will make the shape appear translucent.

        :type: int
        """
        ...
    
    @opacity.setter
    def opacity(self, value): # -> None:
        ...
    
    @property
    def visible(self): # -> bool:
        """True if the shape will be drawn.

        :type: bool
        """
        ...
    
    @visible.setter
    def visible(self, value): # -> None:
        ...
    
    @property
    def group(self): # -> None:
        """User assigned :class:`Group` object."""
        ...
    
    @group.setter
    def group(self, group): # -> None:
        ...
    
    @property
    def batch(self): # -> None:
        """User assigned :class:`Batch` object."""
        ...
    
    @batch.setter
    def batch(self, batch): # -> None:
        ...
    


class Arc(ShapeBase):
    def __init__(self, x, y, radius, segments=..., angle=..., start_angle=..., closed=..., thickness=..., color=..., batch=..., group=...) -> None:
        """Create an Arc.

        The Arc's anchor point (x, y) defaults to its center.

        :Parameters:
            `x` : float
                X coordinate of the circle.
            `y` : float
                Y coordinate of the circle.
            `radius` : float
                The desired radius.
            `segments` : int
                You can optionally specify how many distinct line segments
                the arc should be made from. If not specified it will be
                automatically calculated using the formula:
                `max(14, int(radius / 1.25))`.
            `angle` : float
                The angle of the arc, in degrees. Defaults to 360.0, which is
                a full circle.
            `start_angle` : float
                The start angle of the arc, in degrees. Defaults to 0.
            `closed` : bool
                If True, the ends of the arc will be connected with a line.
                defaults to False.
            `thickness` : float
                The desired thickness of the lines used for the arc.
            `color` : (int, int, int, int)
                The RGB or RGBA color of the arc, specified as a
                tuple of 3 or 4 ints in the range of 0-255. RGB colors
                will be treated as having opacity of 255.
            `batch` : `~pyglet.graphics.Batch`
                Optional batch to add the circle to.
            `group` : `~pyglet.graphics.Group`
                Optional parent group of the circle.
        """
        ...
    
    @property
    def radius(self): # -> Any:
        """The radius of the arc.

        :type: float
        """
        ...
    
    @radius.setter
    def radius(self, value): # -> None:
        ...
    
    @property
    def thickness(self): # -> int:
        ...
    
    @thickness.setter
    def thickness(self, thickness): # -> None:
        ...
    
    @property
    def angle(self): # -> int:
        """The angle of the arc, in degrees.

        :type: float
        """
        ...
    
    @angle.setter
    def angle(self, value): # -> None:
        ...
    
    @property
    def start_angle(self): # -> int:
        """The start angle of the arc, in degrees.

        :type: float
        """
        ...
    
    @start_angle.setter
    def start_angle(self, angle): # -> None:
        ...
    


class BezierCurve(ShapeBase):
    def __init__(self, *points, t=..., segments=..., thickness=..., color=..., batch=..., group=...) -> None:
        """Create a Bézier curve.

        The curve's anchor point (x, y) defaults to its first control point.

        :Parameters:
            `points` : List[[int, int]]
                Control points of the curve. Points can be specified as multiple
                lists or tuples of point pairs. Ex. (0,0), (2,3), (1,9)
            `t` : float
                Draw `100*t` percent of the curve. 0.5 means the curve
                is half drawn and 1.0 means draw the whole curve.
            `segments` : int
                You can optionally specify how many line segments the
                curve should be made from.
            `thickness` : float
                The desired thickness of the lines used for the curve.
            `color` : (int, int, int, int)
                The RGB or RGBA color of the curve, specified as a
                tuple of 3 or 4 ints in the range of 0-255. RGB colors
                will be treated as having an opacity of 255.
            `batch` : `~pyglet.graphics.Batch`
                Optional batch to add the curve to.
            `group` : `~pyglet.graphics.Group`
                Optional parent group of the curve.
        """
        ...
    
    @property
    def points(self): # -> list[Any]:
        """Control points of the curve.

        :type: List[[int, int]]
        """
        ...
    
    @points.setter
    def points(self, value): # -> None:
        ...
    
    @property
    def t(self): # -> float:
        """Draw `100*t` percent of the curve.

        :type: float
        """
        ...
    
    @t.setter
    def t(self, value): # -> None:
        ...
    
    @property
    def thickness(self): # -> int:
        ...
    
    @thickness.setter
    def thickness(self, thickness): # -> None:
        ...
    


class Circle(ShapeBase):
    def __init__(self, x, y, radius, segments=..., color=..., batch=..., group=...) -> None:
        """Create a circle.

        The circle's anchor point (x, y) defaults to the center of the circle.

        :Parameters:
            `x` : float
                X coordinate of the circle.
            `y` : float
                Y coordinate of the circle.
            `radius` : float
                The desired radius.
            `segments` : int
                You can optionally specify how many distinct triangles
                the circle should be made from. If not specified it will
                be automatically calculated using the formula:
                `max(14, int(radius / 1.25))`.
            `color` : (int, int, int, int)
                The RGB or RGBA color of the circle, specified as a
                tuple of 3 or 4 ints in the range of 0-255. RGB colors
                will be treated as having an opacity of 255.
            `batch` : `~pyglet.graphics.Batch`
                Optional batch to add the circle to.
            `group` : `~pyglet.graphics.Group`
                Optional parent group of the circle.
        """
        ...
    
    def __contains__(self, point): # -> bool:
        ...
    
    @property
    def radius(self): # -> Any:
        """The radius of the circle.

        :type: float
        """
        ...
    
    @radius.setter
    def radius(self, value): # -> None:
        ...
    


class Ellipse(ShapeBase):
    def __init__(self, x, y, a, b, segments=..., color=..., batch=..., group=...) -> None:
        """Create an ellipse.

        The ellipse's anchor point (x, y) defaults to the center of the ellipse.

        :Parameters:
            `x` : float
                X coordinate of the ellipse.
            `y` : float
                Y coordinate of the ellipse.
            `a` : float
                Semi-major axes of the ellipse.
            `b`: float
                Semi-minor axes of the ellipse.
            `color` : (int, int, int, int)
                The RGB or RGBA color of the ellipse, specified as a
                tuple of 3 or 4 ints in the range of 0-255. RGB colors
                will be treated as having an opacity of 255.
            `batch` : `~pyglet.graphics.Batch`
                Optional batch to add the circle to.
            `group` : `~pyglet.graphics.Group`
                Optional parent group of the circle.
        """
        ...
    
    def __contains__(self, point): # -> bool:
        ...
    
    @property
    def a(self): # -> Any:
        """The semi-major axes of the ellipse.

        :type: float
        """
        ...
    
    @a.setter
    def a(self, value): # -> None:
        ...
    
    @property
    def b(self): # -> Any:
        """The semi-minor axes of the ellipse.

        :type: float
        """
        ...
    
    @b.setter
    def b(self, value): # -> None:
        ...
    


class Sector(ShapeBase):
    def __init__(self, x, y, radius, segments=..., angle=..., start_angle=..., color=..., batch=..., group=...) -> None:
        """Create a Sector of a circle.

                The sector's anchor point (x, y) defaults to the center of the circle.

                :Parameters:
                    `x` : float
                        X coordinate of the sector.
                    `y` : float
                        Y coordinate of the sector.
                    `radius` : float
                        The desired radius.
                    `segments` : int
                        You can optionally specify how many distinct triangles
                        the sector should be made from. If not specified it will
                        be automatically calculated using the formula:
                        `max(14, int(radius / 1.25))`.
                    `angle` : float
                        The angle of the sector, in degrees. Defaults to 360.0,
                        which is a full circle.
                    `start_angle` : float
                        The start angle of the sector, in degrees. Defaults to 0.
                    `color` : (int, int, int, int)
                        The RGB or RGBA color of the circle, specified as a
                        tuple of 3 or 4 ints in the range of 0-255. RGB colors
                        will be treated as having an opacity of 255.
                    `batch` : `~pyglet.graphics.Batch`
                        Optional batch to add the sector to.
                    `group` : `~pyglet.graphics.Group`
                        Optional parent group of the sector.
                """
        ...
    
    def __contains__(self, point): # -> bool:
        ...
    
    @property
    def angle(self): # -> float:
        """The angle of the sector, in degrees.

        :type: float
        """
        ...
    
    @angle.setter
    def angle(self, value): # -> None:
        ...
    
    @property
    def start_angle(self): # -> int:
        """The start angle of the sector, in degrees.

        :type: float
        """
        ...
    
    @start_angle.setter
    def start_angle(self, angle): # -> None:
        ...
    
    @property
    def radius(self): # -> Any:
        """The radius of the sector.

        :type: float
        """
        ...
    
    @radius.setter
    def radius(self, value): # -> None:
        ...
    


class Line(ShapeBase):
    def __init__(self, x, y, x2, y2, thickness=..., color=..., batch=..., group=...) -> None:
        """Create a line.

        The line's anchor point defaults to the center of the line's
        thickness on the X axis, and the Y axis.

        :Parameters:
            `x` : float
                The first X coordinate of the line.
            `y` : float
                The first Y coordinate of the line.
            `x2` : float
                The second X coordinate of the line.
            `y2` : float
                The second Y coordinate of the line.
            `thickness` : float
                The desired thickness of the line.
            `color` : (int, int, int, int)
                The RGB or RGBA color of the line, specified as a
                tuple of 3 or 4 ints in the range of 0-255. RGB colors
                will be treated as having an opacity of 255.
            `batch` : `~pyglet.graphics.Batch`
                Optional batch to add the line to.
            `group` : `~pyglet.graphics.Group`
                Optional parent group of the line.
        """
        ...
    
    def __contains__(self, point): # -> Literal[False]:
        ...
    
    @property
    def thickness(self): # -> int:
        ...
    
    @thickness.setter
    def thickness(self, thickness): # -> None:
        ...
    
    @property
    def x2(self): # -> Any:
        """Second X coordinate of the shape.

        :type: int or float
        """
        ...
    
    @x2.setter
    def x2(self, value): # -> None:
        ...
    
    @property
    def y2(self): # -> Any:
        """Second Y coordinate of the shape.

        :type: int or float
        """
        ...
    
    @y2.setter
    def y2(self, value): # -> None:
        ...
    


class Rectangle(ShapeBase):
    def __init__(self, x, y, width, height, color=..., batch=..., group=...) -> None:
        """Create a rectangle or square.

        The rectangle's anchor point defaults to the (x, y) coordinates,
        which are at the bottom left.

        :Parameters:
            `x` : float
                The X coordinate of the rectangle.
            `y` : float
                The Y coordinate of the rectangle.
            `width` : float
                The width of the rectangle.
            `height` : float
                The height of the rectangle.
            `color` : (int, int, int, int)
                The RGB or RGBA color of the circle, specified as a
                tuple of 3 or 4 ints in the range of 0-255. RGB colors
                will be treated as having an opacity of 255.
            `batch` : `~pyglet.graphics.Batch`
                Optional batch to add the rectangle to.
            `group` : `~pyglet.graphics.Group`
                Optional parent group of the rectangle.
        """
        ...
    
    def __contains__(self, point):
        ...
    
    @property
    def width(self): # -> Any:
        """The width of the rectangle.

        :type: float
        """
        ...
    
    @width.setter
    def width(self, value): # -> None:
        ...
    
    @property
    def height(self): # -> Any:
        """The height of the rectangle.

        :type: float
        """
        ...
    
    @height.setter
    def height(self, value): # -> None:
        ...
    


class BorderedRectangle(ShapeBase):
    def __init__(self, x, y, width, height, border=..., color=..., border_color=..., batch=..., group=...) -> None:
        """Create a rectangle or square.

        The rectangle's anchor point defaults to the (x, y) coordinates,
        which are at the bottom left.

        :Parameters:
            `x` : float
                The X coordinate of the rectangle.
            `y` : float
                The Y coordinate of the rectangle.
            `width` : float
                The width of the rectangle.
            `height` : float
                The height of the rectangle.
            `border` : float
                The thickness of the border.
            `color` : (int, int, int, int)
                The RGB or RGBA fill color of the rectangle, specified
                as a tuple of 3 or 4 ints in the range of 0-255. RGB
                colors will be treated as having an opacity of 255.
            `border_color` : (int, int, int, int)
                The RGB or RGBA fill color of the border, specified
                as a tuple of 3 or 4 ints in the range of 0-255. RGB
                colors will be treated as having an opacity of 255.

                The alpha values must match if you pass RGBA values to
                both this argument and `border_color`. If they do not,
                a `ValueError` will be raised informing you of the
                ambiguity.
            `batch` : `~pyglet.graphics.Batch`
                Optional batch to add the rectangle to.
            `group` : `~pyglet.graphics.Group`
                Optional parent group of the rectangle.
        """
        ...
    
    def __contains__(self, point):
        ...
    
    @property
    def border(self): # -> int:
        """The border width of the rectangle.

        :return: float
        """
        ...
    
    @border.setter
    def border(self, width): # -> None:
        ...
    
    @property
    def width(self): # -> Any:
        """The width of the rectangle.

        :type: float
        """
        ...
    
    @width.setter
    def width(self, value): # -> None:
        ...
    
    @property
    def height(self): # -> Any:
        """The height of the rectangle.

        :type: float
        """
        ...
    
    @height.setter
    def height(self, value): # -> None:
        ...
    
    @property
    def border_color(self): # -> tuple[Any, Any, Any, Any | Literal[255]]:
        """The rectangle's border color.

        This property sets the color of the border of a bordered rectangle.

        The color is specified as an RGB tuple of integers '(red, green, blue)'
        or an RGBA tuple of integers '(red, green, blue, alpha)`. Setting the
        alpha on this property will change the alpha of the entire shape,
        including both the fill and the border.

        Each color component must be in the range 0 (dark) to 255 (saturated).

        :type: (int, int, int, int)
        """
        ...
    
    @border_color.setter
    def border_color(self, values): # -> None:
        ...
    
    @property
    def color(self): # -> tuple[Any, Any, Any, Any | Literal[255]] | tuple[Any, Any, Any, Any]:
        """The rectangle's fill color.

        This property sets the color of the inside of a bordered rectangle.

        The color is specified as an RGB tuple of integers '(red, green, blue)'
        or an RGBA tuple of integers '(red, green, blue, alpha)`. Setting the
        alpha on this property will change the alpha of the entire shape,
        including both the fill and the border.

        Each color component must be in the range 0 (dark) to 255 (saturated).

        :type: (int, int, int, int)
        """
        ...
    
    @color.setter
    def color(self, values): # -> None:
        ...
    


class Box(ShapeBase):
    def __init__(self, x, y, width, height, thickness=..., color=..., batch=..., group=...) -> None:
        """Create an unfilled rectangular shape, with optional thickness.

        The box's anchor point defaults to the (x, y) coordinates,
        which are at the bottom left.
        Changing the thickness of the box will extend the walls inward;
        the outward dimesions will not be affected.

        :Parameters:
            `x` : float
                The X coordinate of the box.
            `y` : float
                The Y coordinate of the box.
            `width` : float
                The width of the box.
            `height` : float
                The height of the box.
            `thickness` : float
                The thickness of the lines that make up the box.
            `color` : (int, int, int, int)
                The RGB or RGBA color of the box, specified as a tuple
                of 3 or 4 ints in the range of 0-255. RGB colors will
                be treated as having an opacity of 255.
            `batch` : `~pyglet.graphics.Batch`
                Optional batch to add the box to.
            `group` : `~pyglet.graphics.Group`
                Optional parent group of the box.
        """
        ...
    
    def __contains__(self, point):
        ...
    
    @property
    def width(self): # -> Any:
        """The width of the Box.

        :type: float
        """
        ...
    
    @width.setter
    def width(self, value): # -> None:
        ...
    
    @property
    def height(self): # -> Any:
        """The height of the Box.

        :type: float
        """
        ...
    
    @height.setter
    def height(self, value): # -> None:
        ...
    


class Triangle(ShapeBase):
    def __init__(self, x, y, x2, y2, x3, y3, color=..., batch=..., group=...) -> None:
        """Create a triangle.

        The triangle's anchor point defaults to the first vertex point.

        :Parameters:
            `x` : float
                The first X coordinate of the triangle.
            `y` : float
                The first Y coordinate of the triangle.
            `x2` : float
                The second X coordinate of the triangle.
            `y2` : float
                The second Y coordinate of the triangle.
            `x3` : float
                The third X coordinate of the triangle.
            `y3` : float
                The third Y coordinate of the triangle.
            `color` : (int, int, int, int)
                The RGB or RGBA color of the triangle, specified as a
                tuple of 3 or 4 ints in the range of 0-255. RGB colors
                will be treated as having an opacity of 255.
            `batch` : `~pyglet.graphics.Batch`
                Optional batch to add the triangle to.
            `group` : `~pyglet.graphics.Group`
                Optional parent group of the triangle.
        """
        ...
    
    def __contains__(self, point): # -> bool:
        ...
    
    @property
    def x2(self):
        """Second X coordinate of the shape.

        :type: int or float
        """
        ...
    
    @x2.setter
    def x2(self, value): # -> None:
        ...
    
    @property
    def y2(self):
        """Second Y coordinate of the shape.

        :type: int or float
        """
        ...
    
    @y2.setter
    def y2(self, value): # -> None:
        ...
    
    @property
    def x3(self):
        """Third X coordinate of the shape.

        :type: int or float
        """
        ...
    
    @x3.setter
    def x3(self, value): # -> None:
        ...
    
    @property
    def y3(self):
        """Third Y coordinate of the shape.

        :type: int or float
        """
        ...
    
    @y3.setter
    def y3(self, value): # -> None:
        ...
    


class Star(ShapeBase):
    def __init__(self, x, y, outer_radius, inner_radius, num_spikes, rotation=..., color=..., batch=..., group=...) -> None:
        """Create a star.

        The star's anchor point (x, y) defaults to the center of the star.

        :Parameters:
            `x` : float
                The X coordinate of the star.
            `y` : float
                The Y coordinate of the star.
            `outer_radius` : float
                The desired outer radius of the star.
            `inner_radius` : float
                The desired inner radius of the star.
            `num_spikes` : float
                The desired number of spikes of the star.
            `rotation` : float
                The rotation of the star in degrees. A rotation of 0 degrees
                will result in one spike lining up with the X axis in
                positive direction.
            `color` : (int, int, int)
                The RGB or RGBA color of the star, specified as a
                tuple of 3 or 4 ints in the range of 0-255. RGB colors
                will be treated as having an opacity of 255.
            `batch` : `~pyglet.graphics.Batch`
                Optional batch to add the star to.
            `group` : `~pyglet.graphics.Group`
                Optional parent group of the star.
        """
        ...
    
    def __contains__(self, point):
        ...
    
    @property
    def outer_radius(self): # -> Any:
        """The outer radius of the star."""
        ...
    
    @outer_radius.setter
    def outer_radius(self, value): # -> None:
        ...
    
    @property
    def inner_radius(self): # -> Any:
        """The inner radius of the star."""
        ...
    
    @inner_radius.setter
    def inner_radius(self, value): # -> None:
        ...
    
    @property
    def num_spikes(self): # -> Any:
        """Number of spikes of the star."""
        ...
    
    @num_spikes.setter
    def num_spikes(self, value): # -> None:
        ...
    


class Polygon(ShapeBase):
    def __init__(self, *coordinates, color=..., batch=..., group=...) -> None:
        """Create a convex polygon.

        The polygon's anchor point defaults to the first vertex point.

        :Parameters:
            `coordinates` : List[[int, int]]
                The coordinates for each point in the polygon.
            `color` : (int, int, int, int)
                The RGB or RGBA color of the polygon, specified as a
                tuple of 3 or 4 ints in the range of 0-255. RGB colors
                will be treated as having an opacity of 255.
            `batch` : `~pyglet.graphics.Batch`
                Optional batch to add the polygon to.
            `group` : `~pyglet.graphics.Group`
                Optional parent group of the polygon.
        """
        ...
    
    def __contains__(self, point): # -> bool:
        ...
    


class MultiLine(ShapeBase):
    def __init__(self, *coordinates, closed=..., thickness=..., color=..., batch=..., group=...) -> None:
        """Create multiple connected lines from a sequence of coordinates

        The shape's anchor point defaults to the first vertex point.

        :Parameters:
            `coordinates` : List[[int, int]]
                The coordinates for each point in the shape.
            `closed` : bool
                If True, the first and last coordinate will be connected with a line.
                defaults to False.
            `thickness` : float
                The desired thickness of the line segments.
            `color` : (int, int, int, int)
                The RGB or RGBA color of the shape, specified as a
                tuple of 3 or 4 ints in the range of 0-255. RGB colors
                will be treated as having an opacity of 255.
            `batch` : `~pyglet.graphics.Batch`
                Optional batch to add the shape to.
            `group` : `~pyglet.graphics.Group`
                Optional parent group of the shape.
        """
        ...
    
    @property
    def thickness(self): # -> int:
        ...
    
    @thickness.setter
    def thickness(self, thickness): # -> None:
        ...
    


__all__ = ('Arc', 'Box', 'BezierCurve', 'Circle', 'Ellipse', 'Line', 'MultiLine', 'Rectangle', 'BorderedRectangle', 'Triangle', 'Star', 'Polygon', 'Sector', 'ShapeBase')
