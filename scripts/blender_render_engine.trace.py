# Sources based on https://docs.blender.org/api/blender2.8/bpy.types.RenderEngine.html
# blender -P blender_render_engine.trace.py  -p 900 1000 3000 1500 
import bpy
import bgl
from mathutils import Vector

import math, time
import numpy

t0 = time.time()

def log(s):
    t = '%.6f' % (time.time() - t0)
    print('%s | %s' % (t, s))
    

class CustomRenderEngine(bpy.types.RenderEngine):
    # These three members are used by blender to set up the
    # RenderEngine; define its internal name, visible name and capabilities.
    bl_idname = "CUSTOM"
    bl_label = "Custom"
    bl_use_preview = True
    bl_use_eevee_viewport = True
    bl_use_shading_nodes_custom = False     # Default: True

    # Init is called whenever a new render engine instance is created. Multiple
    # instances may exist at the same time, for example for a viewport and final
    # render.
    def __init__(self):
        print('-' * 40)
        log('RENDER ENGINE __init__()')
        print('-' * 40)
        print()
        
        self.scene_data = None
        self.draw_data = None
        
        self.render_count = 0
        self.draw_count = 0
        self.update_count = 0
        self.dimensions = None

    # When the render engine instance is destroyed, this is called. Clean up any
    # render engine data here, for example stopping running render threads.
    def __del__(self):
        print('-' * 40)
        log('RENDER ENGINE __del__()')
        print('-' * 40)
        print()

    # This is the method called by Blender for both final renders (F12) and
    # small preview for materials, world and lights.
    def render(self, depsgraph):
        
        self.render_count += 1
        
        print('-' * 40)
        log('render #%d' % self.render_count)
        print('-' * 40)
        
        scene = depsgraph.scene
        scale = scene.render.resolution_percentage / 100.0
        self.size_x = int(scene.render.resolution_x * scale)
        self.size_y = int(scene.render.resolution_y * scale)

        # Fill the render result with a flat color. The framebuffer is
        # defined as a list of pixels, each pixel itself being a list of
        # R,G,B,A values.
        if self.is_preview:
            color = [0.1, 0.2, 0.1, 1.0]
        else:
            color = [0.2, 0.1, 0.1, 1.0]

        pixel_count = self.size_x * self.size_y
        rect = [color] * pixel_count

        # Here we write the pixel values to the RenderResult
        result = self.begin_result(0, 0, self.size_x, self.size_y)
        layer = result.layers[0].passes["Combined"]
        layer.rect = rect
        self.end_result(result)
        
        print()

    # For viewport renders, this method gets called once at the start and
    # whenever the scene or 3D viewport changes. This method is where data
    # should be read from Blender in the same thread. Typically a render
    # thread will be started to do the work while keeping Blender responsive.
    def view_update(self, context, depsgraph):
        
        self.update_count += 1
        
        print('-' * 40)
        log('view_update #%d' % self.update_count)
        print('-' * 40)
        
        # The first call to view_update will not list any object updates,
        # so the full scene has to be synced using depsgraph.object_instances
        
        print('object_instances: %d objects' % len(depsgraph.object_instances))
        
        region = context.region
        view3d = context.space_data
        scene = depsgraph.scene
        
        # Get viewport dimensions
        dimensions = region.width, region.height
                
        types = ['ACTION', 'ARMATURE', 'BRUSH', 'CAMERA', 'CACHEFILE', 'CURVE', 'FONT', 'GREASEPENCIL', 'COLLECTION', 'IMAGE', 'KEY', 'LIGHT', 'LIBRARY', 'LINESTYLE', 'LATTICE', 'MASK', 'MATERIAL', 'META', 'MESH', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'LIGHT_PROBE', 'SCENE', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'WINDOWMANAGER', 'WORLD', 'WORKSPACE']
        for t in types:
            if depsgraph.id_type_updated(t):
                print("Type %s updated" % t)

        print()
        
        for update in depsgraph.updates:
            print('Datablock "%s" updated (%s)' % (update.id.name, type(update.id)))
            if update.is_updated_geometry:
                print('-- geometry was updated')
            if update.is_updated_transform:
                print('-- transform was updated')
                
        print()

    # For viewport renders, this method is called whenever Blender redraws
    # the 3D viewport. The renderer is expected to quickly draw the render
    # with OpenGL, and not perform other expensive work.
    # Blender will draw overlays for selection and editing on top of the
    # rendered image automatically.
    def view_draw(self, context, depsgraph):
        
        # See https://github.com/LuxCoreRender/BlendLuxCore/blob/master/draw/viewport.py

        self.draw_count += 1
        
        print('-' * 40)
        log('view_draw #%d' % self.draw_count)
        print('-' * 40)
        
        region = context.region
        assert region.type == 'WINDOW'        
        assert context.space_data.type == 'VIEW_3D'
        
        region_data = context.region_data
        space_data = context.space_data
        
        scene = context.scene
        
        # view clipping has no effect on these matrices
        print('window_matrix')
        print(region_data.window_matrix)
        print('perspective_matrix')
        print(region_data.perspective_matrix)    # = window * view
        print('view_matrix')
        print(region_data.view_matrix)
        # view_matrix = identity when in top view.
        # view_matrix = model-view matrix,  i.e. world to camera
        
        print('region_data:')
        print('view_perspective', region_data.view_perspective) # PERSP (regular 3D view not tied to camera), CAMERA (view from camera) or ORTHO (one of top, etc)
        print('view_location', region_data.view_location)       # View pivot point
        print('view_distance', region_data.view_distance)       # Distance to view location
        print('view_rotation', region_data.view_rotation)       # Quat
        print('view_camera_offset', list(region_data.view_camera_offset))
        print('view_camera_zoom', region_data.view_camera_zoom)
        print('is_perspective %d' % region_data.is_perspective)
        
        cam_xform = region_data.view_matrix.inverted()
        location = cam_xform.translation
        position = list(location)
        view_dir = list(cam_xform @ Vector((0, 0, -1)) - location)
        up_dir = list(cam_xform @ Vector((0, 1, 0)) - location)
        print('derived camera:')
        print('position', position)
        print('view_dir', view_dir)
        print('up_dir', up_dir)

        # view3d.perspective_matrix = window_matrix * view_matrix
        perspective_matrix = region_data.perspective_matrix
        
        print('space_data:')
        print('camera', space_data.camera)
        camobj = space_data.camera
        camdata = camobj.data
        print('... shift', camdata.shift_x, camdata.shift_y)
        print('use_local_camera', space_data.use_local_camera)  # No relation to camera view yes/no
        print('lens', space_data.lens)                          # Always set to viewport lens setting, even when in camera view
        print('clip_start', space_data.clip_start)
                      
        scene = depsgraph.scene

        # Get viewport dimensions
        dimensions = region.width, region.height
        
        if dimensions != self.dimensions:
            print('Dimensions changed to %d x %d' % dimensions)
            self.dimensions = dimensions        
            
        print('aspect (dims) %.3f' % (self.dimensions[0]/self.dimensions[1]))
        print('aspect (window matrix) %.3f' % (region_data.window_matrix[1][1] / region_data.window_matrix[0][0]))
        
        # Bind shader that converts from scene linear to display space,
        bgl.glEnable(bgl.GL_BLEND)
        bgl.glBlendFunc(bgl.GL_ONE, bgl.GL_ONE_MINUS_SRC_ALPHA);
        self.bind_display_space_shader(scene)

        if not self.draw_data or self.draw_data.dimensions != dimensions:
            self.draw_data = CustomDrawData(dimensions)

        self.draw_data.draw()

        self.unbind_display_space_shader()
        bgl.glDisable(bgl.GL_BLEND)
        
        print()
        


class CustomDrawData:
    def __init__(self, dimensions):
        log('CustomDrawData.__init__()')
        
        # Generate dummy float image buffer
        self.dimensions = dimensions
        width, height = dimensions
        
        pixels = numpy.full(width*height*4, 0.3, dtype=numpy.float32)
        #pixels = [0.1, 0.2, 0.1, 1.0] * width * height
        pixels = bgl.Buffer(bgl.GL_FLOAT, width * height * 4, pixels)

        # Generate texture
        self.texture = bgl.Buffer(bgl.GL_INT, 1)
        bgl.glGenTextures(1, self.texture)
        bgl.glActiveTexture(bgl.GL_TEXTURE0)
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, self.texture[0])
        bgl.glTexImage2D(bgl.GL_TEXTURE_2D, 0, bgl.GL_RGBA16F, width, height, 0, bgl.GL_RGBA, bgl.GL_FLOAT, pixels)
        bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MIN_FILTER, bgl.GL_LINEAR)
        bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MAG_FILTER, bgl.GL_LINEAR)
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, 0)

        # Bind shader that converts from scene linear to display space,
        # use the scene's color management settings.
        shader_program = bgl.Buffer(bgl.GL_INT, 1)
        bgl.glGetIntegerv(bgl.GL_CURRENT_PROGRAM, shader_program);

        # Generate vertex array
        self.vertex_array = bgl.Buffer(bgl.GL_INT, 1)
        bgl.glGenVertexArrays(1, self.vertex_array)
        bgl.glBindVertexArray(self.vertex_array[0])

        texturecoord_location = bgl.glGetAttribLocation(shader_program[0], "texCoord");
        position_location = bgl.glGetAttribLocation(shader_program[0], "pos");

        bgl.glEnableVertexAttribArray(texturecoord_location);
        bgl.glEnableVertexAttribArray(position_location);

        # Generate geometry buffers for drawing textured quad
        position = [0.0, 0.0, width, 0.0, width, height, 0.0, height]
        position = bgl.Buffer(bgl.GL_FLOAT, len(position), position)
        texcoord = [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0]
        texcoord = bgl.Buffer(bgl.GL_FLOAT, len(texcoord), texcoord)

        self.vertex_buffer = bgl.Buffer(bgl.GL_INT, 2)

        bgl.glGenBuffers(2, self.vertex_buffer)
        bgl.glBindBuffer(bgl.GL_ARRAY_BUFFER, self.vertex_buffer[0])
        bgl.glBufferData(bgl.GL_ARRAY_BUFFER, 32, position, bgl.GL_STATIC_DRAW)
        bgl.glVertexAttribPointer(position_location, 2, bgl.GL_FLOAT, bgl.GL_FALSE, 0, None)

        bgl.glBindBuffer(bgl.GL_ARRAY_BUFFER, self.vertex_buffer[1])
        bgl.glBufferData(bgl.GL_ARRAY_BUFFER, 32, texcoord, bgl.GL_STATIC_DRAW)
        bgl.glVertexAttribPointer(texturecoord_location, 2, bgl.GL_FLOAT, bgl.GL_FALSE, 0, None)

        bgl.glBindBuffer(bgl.GL_ARRAY_BUFFER, 0)
        bgl.glBindVertexArray(0)

    def __del__(self):
        log('CustomDrawData.__del__()')
        
        bgl.glDeleteBuffers(2, self.vertex_buffer)
        bgl.glDeleteVertexArrays(1, self.vertex_array)
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, 0)
        bgl.glDeleteTextures(1, self.texture)

    def draw(self):
        log('CustomDrawData.draw()')
        
        bgl.glActiveTexture(bgl.GL_TEXTURE0)
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, self.texture[0])
        bgl.glBindVertexArray(self.vertex_array[0])
        bgl.glDrawArrays(bgl.GL_TRIANGLE_FAN, 0, 4);
        bgl.glBindVertexArray(0)
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, 0)


# RenderEngines also need to tell UI Panels that they are compatible with.
# We recommend to enable all panels marked as BLENDER_RENDER, and then
# exclude any panels that are replaced by custom panels registered by the
# render engine, or that are not supported.
def get_panels():
    exclude_panels = {
        'VIEWLAYER_PT_filter',
        'VIEWLAYER_PT_layer_passes',
        'WORLD_PT_context_world',
    }

    panels = []
    for panel in bpy.types.Panel.__subclasses__():
        if hasattr(panel, 'COMPAT_ENGINES') and 'BLENDER_RENDER' in panel.COMPAT_ENGINES:
            if panel.__name__ not in exclude_panels:
                panels.append(panel)

    return panels

def register():
    # Register the RenderEngine
    bpy.utils.register_class(CustomRenderEngine)

    for panel in get_panels():
        panel.COMPAT_ENGINES.add('CUSTOM')

def unregister():
    bpy.utils.unregister_class(CustomRenderEngine)

    for panel in get_panels():
        if 'CUSTOM' in panel.COMPAT_ENGINES:
            panel.COMPAT_ENGINES.remove('CUSTOM')


if __name__ == "__main__":
    register()
