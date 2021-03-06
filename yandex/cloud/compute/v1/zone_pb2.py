# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/zone.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/compute/v1/zone.proto',
  package='yandex.cloud.compute.v1',
  syntax='proto3',
  serialized_options=_b('ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'),
  serialized_pb=_b('\n\"yandex/cloud/compute/v1/zone.proto\x12\x17yandex.cloud.compute.v1\"\x8f\x01\n\x04Zone\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tregion_id\x18\x02 \x01(\t\x12\x34\n\x06status\x18\x03 \x01(\x0e\x32$.yandex.cloud.compute.v1.Zone.Status\"2\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x06\n\x02UP\x10\x01\x12\x08\n\x04\x44OWN\x10\x02\x42\x45ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')
)



_ZONE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.compute.v1.Zone.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWN', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=157,
  serialized_end=207,
)
_sym_db.RegisterEnumDescriptor(_ZONE_STATUS)


_ZONE = _descriptor.Descriptor(
  name='Zone',
  full_name='yandex.cloud.compute.v1.Zone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.compute.v1.Zone.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region_id', full_name='yandex.cloud.compute.v1.Zone.region_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.compute.v1.Zone.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ZONE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=207,
)

_ZONE.fields_by_name['status'].enum_type = _ZONE_STATUS
_ZONE_STATUS.containing_type = _ZONE
DESCRIPTOR.message_types_by_name['Zone'] = _ZONE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Zone = _reflection.GeneratedProtocolMessageType('Zone', (_message.Message,), dict(
  DESCRIPTOR = _ZONE,
  __module__ = 'yandex.cloud.compute.v1.zone_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.Zone)
  ))
_sym_db.RegisterMessage(Zone)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
