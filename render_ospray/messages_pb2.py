# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0emessages.proto\"-\n\rClientMessage\"\x1c\n\x04Type\x12\x14\n\x10\x43\x41NCEL_RENDERING\x10\x00\"\x91\x01\n\x0cRenderResult\x12 \n\x04type\x18\x01 \x01(\x0e\x32\x12.RenderResult.Type\x12\x0e\n\x06sample\x18\x02 \x01(\r\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12\x11\n\tfile_size\x18\x04 \x01(\r\")\n\x04Type\x12\t\n\x05\x46RAME\x10\x00\x12\x0c\n\x08\x43\x41NCELED\x10\x01\x12\x08\n\x04\x44ONE\x10\x02\"f\n\x0cSceneElement\x12 \n\x04type\x18\x01 \x01(\x0e\x32\x12.SceneElement.Type\x12\x0c\n\x04name\x18\x02 \x01(\t\"&\n\x04Type\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04MESH\x10\x01\x12\n\n\x06VOLUME\x10\x02\"\xcb\x01\n\x08MeshInfo\x12\r\n\x05\x66lags\x18\x01 \x01(\r\x12\x14\n\x0cobject2world\x18\x02 \x03(\x02\x12\x12\n\nproperties\x18\x03 \x01(\t\x12\x13\n\x0bobject_name\x18\x04 \x01(\t\x12\x11\n\tmesh_name\x18\x05 \x01(\t\x12\x14\n\x0cnum_vertices\x18\x06 \x01(\r\x12\x15\n\rnum_triangles\x18\x07 \x01(\r\"1\n\x05\x46lags\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07NORMALS\x10\x01\x12\x11\n\rVERTEX_COLORS\x10\x02\"m\n\nVolumeInfo\x12\r\n\x05\x66lags\x18\x01 \x01(\r\x12\x14\n\x0cobject2world\x18\x02 \x03(\x02\x12\x12\n\nproperties\x18\x03 \x01(\t\x12\x13\n\x0bobject_name\x18\x04 \x01(\t\x12\x11\n\tmesh_name\x18\x05 \x01(\t\"B\n\rImageSettings\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\x12\n\npercentage\x18\x03 \x01(\r\"\x85\x01\n\x0e\x43\x61meraSettings\x12\x10\n\x08position\x18\x01 \x03(\x02\x12\x10\n\x08view_dir\x18\x02 \x03(\x02\x12\x0e\n\x06up_dir\x18\x03 \x03(\x02\x12\r\n\x05\x66ov_y\x18\x04 \x01(\x02\x12\x1a\n\x12\x64of_focus_distance\x18\x05 \x01(\x02\x12\x14\n\x0c\x64of_aperture\x18\x06 \x01(\x02\"z\n\x0eRenderSettings\x12\x10\n\x08renderer\x18\x01 \x01(\t\x12\x0f\n\x07samples\x18\x02 \x01(\r\x12\x12\n\nao_samples\x18\x03 \x01(\r\x12\x18\n\x10\x62\x61\x63kground_color\x18\x04 \x03(\x02\x12\x17\n\x0fshadows_enabled\x18\x05 \x01(\x08\"\xb7\x02\n\x05Light\x12\x19\n\x04type\x18\x01 \x01(\x0e\x32\x0b.Light.Type\x12\x14\n\x0cobject2world\x18\x02 \x03(\x02\x12\r\n\x05\x63olor\x18\x03 \x03(\x02\x12\x11\n\tintensity\x18\x04 \x01(\x02\x12\x0f\n\x07visible\x18\x05 \x01(\x08\x12\x11\n\tdirection\x18\x06 \x03(\x02\x12\x18\n\x10\x61ngular_diameter\x18\x07 \x01(\x02\x12\x10\n\x08position\x18\x08 \x03(\x02\x12\x0e\n\x06radius\x18\t \x01(\x02\x12\x15\n\ropening_angle\x18\n \x01(\x02\x12\x16\n\x0epenumbra_angle\x18\x0b \x01(\x02\x12\r\n\x05\x65\x64ge1\x18\x0c \x03(\x02\x12\r\n\x05\x65\x64ge2\x18\r \x03(\x02\".\n\x04Type\x12\t\n\x05POINT\x10\x00\x12\x07\n\x03SUN\x10\x01\x12\x08\n\x04SPOT\x10\x02\x12\x08\n\x04\x41REA\x10\x03\"Y\n\rLightSettings\x12\x19\n\x11\x61mbient_intensity\x18\x01 \x01(\x02\x12\x15\n\rambient_color\x18\x02 \x03(\x02\x12\x16\n\x06lights\x18\x03 \x03(\x0b\x32\x06.Light\"P\n\x10VolumeLoadResult\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04hash\x18\x03 \x01(\t\x12\x0c\n\x04\x62\x62ox\x18\x04 \x03(\x02\x62\x06proto3')
)



_CLIENTMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='ClientMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CANCEL_RENDERING', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=35,
  serialized_end=63,
)
_sym_db.RegisterEnumDescriptor(_CLIENTMESSAGE_TYPE)

_RENDERRESULT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='RenderResult.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FRAME', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=170,
  serialized_end=211,
)
_sym_db.RegisterEnumDescriptor(_RENDERRESULT_TYPE)

_SCENEELEMENT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='SceneElement.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLUME', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=277,
  serialized_end=315,
)
_sym_db.RegisterEnumDescriptor(_SCENEELEMENT_TYPE)

_MESHINFO_FLAGS = _descriptor.EnumDescriptor(
  name='Flags',
  full_name='MeshInfo.Flags',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORMALS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERTEX_COLORS', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=472,
  serialized_end=521,
)
_sym_db.RegisterEnumDescriptor(_MESHINFO_FLAGS)

_LIGHT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Light.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POINT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPOT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AREA', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1228,
  serialized_end=1274,
)
_sym_db.RegisterEnumDescriptor(_LIGHT_TYPE)


_CLIENTMESSAGE = _descriptor.Descriptor(
  name='ClientMessage',
  full_name='ClientMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLIENTMESSAGE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=63,
)


_RENDERRESULT = _descriptor.Descriptor(
  name='RenderResult',
  full_name='RenderResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='RenderResult.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sample', full_name='RenderResult.sample', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='RenderResult.file_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_size', full_name='RenderResult.file_size', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RENDERRESULT_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=211,
)


_SCENEELEMENT = _descriptor.Descriptor(
  name='SceneElement',
  full_name='SceneElement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='SceneElement.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='SceneElement.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCENEELEMENT_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=315,
)


_MESHINFO = _descriptor.Descriptor(
  name='MeshInfo',
  full_name='MeshInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flags', full_name='MeshInfo.flags', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object2world', full_name='MeshInfo.object2world', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='MeshInfo.properties', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_name', full_name='MeshInfo.object_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mesh_name', full_name='MeshInfo.mesh_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_vertices', full_name='MeshInfo.num_vertices', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_triangles', full_name='MeshInfo.num_triangles', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESHINFO_FLAGS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=318,
  serialized_end=521,
)


_VOLUMEINFO = _descriptor.Descriptor(
  name='VolumeInfo',
  full_name='VolumeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flags', full_name='VolumeInfo.flags', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object2world', full_name='VolumeInfo.object2world', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='VolumeInfo.properties', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_name', full_name='VolumeInfo.object_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mesh_name', full_name='VolumeInfo.mesh_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=523,
  serialized_end=632,
)


_IMAGESETTINGS = _descriptor.Descriptor(
  name='ImageSettings',
  full_name='ImageSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='ImageSettings.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='ImageSettings.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='percentage', full_name='ImageSettings.percentage', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=634,
  serialized_end=700,
)


_CAMERASETTINGS = _descriptor.Descriptor(
  name='CameraSettings',
  full_name='CameraSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='CameraSettings.position', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view_dir', full_name='CameraSettings.view_dir', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='up_dir', full_name='CameraSettings.up_dir', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fov_y', full_name='CameraSettings.fov_y', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dof_focus_distance', full_name='CameraSettings.dof_focus_distance', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dof_aperture', full_name='CameraSettings.dof_aperture', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=703,
  serialized_end=836,
)


_RENDERSETTINGS = _descriptor.Descriptor(
  name='RenderSettings',
  full_name='RenderSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='renderer', full_name='RenderSettings.renderer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='samples', full_name='RenderSettings.samples', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ao_samples', full_name='RenderSettings.ao_samples', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='background_color', full_name='RenderSettings.background_color', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shadows_enabled', full_name='RenderSettings.shadows_enabled', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=838,
  serialized_end=960,
)


_LIGHT = _descriptor.Descriptor(
  name='Light',
  full_name='Light',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Light.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object2world', full_name='Light.object2world', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='Light.color', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intensity', full_name='Light.intensity', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visible', full_name='Light.visible', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='Light.direction', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_diameter', full_name='Light.angular_diameter', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='Light.position', index=7,
      number=8, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius', full_name='Light.radius', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opening_angle', full_name='Light.opening_angle', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='penumbra_angle', full_name='Light.penumbra_angle', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edge1', full_name='Light.edge1', index=11,
      number=12, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edge2', full_name='Light.edge2', index=12,
      number=13, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LIGHT_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=963,
  serialized_end=1274,
)


_LIGHTSETTINGS = _descriptor.Descriptor(
  name='LightSettings',
  full_name='LightSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ambient_intensity', full_name='LightSettings.ambient_intensity', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ambient_color', full_name='LightSettings.ambient_color', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lights', full_name='LightSettings.lights', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1276,
  serialized_end=1365,
)


_VOLUMELOADRESULT = _descriptor.Descriptor(
  name='VolumeLoadResult',
  full_name='VolumeLoadResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='VolumeLoadResult.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='VolumeLoadResult.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='VolumeLoadResult.hash', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bbox', full_name='VolumeLoadResult.bbox', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1367,
  serialized_end=1447,
)

_CLIENTMESSAGE_TYPE.containing_type = _CLIENTMESSAGE
_RENDERRESULT.fields_by_name['type'].enum_type = _RENDERRESULT_TYPE
_RENDERRESULT_TYPE.containing_type = _RENDERRESULT
_SCENEELEMENT.fields_by_name['type'].enum_type = _SCENEELEMENT_TYPE
_SCENEELEMENT_TYPE.containing_type = _SCENEELEMENT
_MESHINFO_FLAGS.containing_type = _MESHINFO
_LIGHT.fields_by_name['type'].enum_type = _LIGHT_TYPE
_LIGHT_TYPE.containing_type = _LIGHT
_LIGHTSETTINGS.fields_by_name['lights'].message_type = _LIGHT
DESCRIPTOR.message_types_by_name['ClientMessage'] = _CLIENTMESSAGE
DESCRIPTOR.message_types_by_name['RenderResult'] = _RENDERRESULT
DESCRIPTOR.message_types_by_name['SceneElement'] = _SCENEELEMENT
DESCRIPTOR.message_types_by_name['MeshInfo'] = _MESHINFO
DESCRIPTOR.message_types_by_name['VolumeInfo'] = _VOLUMEINFO
DESCRIPTOR.message_types_by_name['ImageSettings'] = _IMAGESETTINGS
DESCRIPTOR.message_types_by_name['CameraSettings'] = _CAMERASETTINGS
DESCRIPTOR.message_types_by_name['RenderSettings'] = _RENDERSETTINGS
DESCRIPTOR.message_types_by_name['Light'] = _LIGHT
DESCRIPTOR.message_types_by_name['LightSettings'] = _LIGHTSETTINGS
DESCRIPTOR.message_types_by_name['VolumeLoadResult'] = _VOLUMELOADRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientMessage = _reflection.GeneratedProtocolMessageType('ClientMessage', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTMESSAGE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ClientMessage)
  ))
_sym_db.RegisterMessage(ClientMessage)

RenderResult = _reflection.GeneratedProtocolMessageType('RenderResult', (_message.Message,), dict(
  DESCRIPTOR = _RENDERRESULT,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:RenderResult)
  ))
_sym_db.RegisterMessage(RenderResult)

SceneElement = _reflection.GeneratedProtocolMessageType('SceneElement', (_message.Message,), dict(
  DESCRIPTOR = _SCENEELEMENT,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:SceneElement)
  ))
_sym_db.RegisterMessage(SceneElement)

MeshInfo = _reflection.GeneratedProtocolMessageType('MeshInfo', (_message.Message,), dict(
  DESCRIPTOR = _MESHINFO,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:MeshInfo)
  ))
_sym_db.RegisterMessage(MeshInfo)

VolumeInfo = _reflection.GeneratedProtocolMessageType('VolumeInfo', (_message.Message,), dict(
  DESCRIPTOR = _VOLUMEINFO,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:VolumeInfo)
  ))
_sym_db.RegisterMessage(VolumeInfo)

ImageSettings = _reflection.GeneratedProtocolMessageType('ImageSettings', (_message.Message,), dict(
  DESCRIPTOR = _IMAGESETTINGS,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ImageSettings)
  ))
_sym_db.RegisterMessage(ImageSettings)

CameraSettings = _reflection.GeneratedProtocolMessageType('CameraSettings', (_message.Message,), dict(
  DESCRIPTOR = _CAMERASETTINGS,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:CameraSettings)
  ))
_sym_db.RegisterMessage(CameraSettings)

RenderSettings = _reflection.GeneratedProtocolMessageType('RenderSettings', (_message.Message,), dict(
  DESCRIPTOR = _RENDERSETTINGS,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:RenderSettings)
  ))
_sym_db.RegisterMessage(RenderSettings)

Light = _reflection.GeneratedProtocolMessageType('Light', (_message.Message,), dict(
  DESCRIPTOR = _LIGHT,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Light)
  ))
_sym_db.RegisterMessage(Light)

LightSettings = _reflection.GeneratedProtocolMessageType('LightSettings', (_message.Message,), dict(
  DESCRIPTOR = _LIGHTSETTINGS,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:LightSettings)
  ))
_sym_db.RegisterMessage(LightSettings)

VolumeLoadResult = _reflection.GeneratedProtocolMessageType('VolumeLoadResult', (_message.Message,), dict(
  DESCRIPTOR = _VOLUMELOADRESULT,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:VolumeLoadResult)
  ))
_sym_db.RegisterMessage(VolumeLoadResult)


# @@protoc_insertion_point(module_scope)