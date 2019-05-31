# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dynamic_ks.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dynamic_ks.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x64ynamic_ks.proto\"%\n\x07request\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x1a\n\x08response\x12\x0e\n\x06status\x18\x01 \x01(\x08\"\x12\n\x03key\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x16\n\x05value\x12\r\n\x05value\x18\x01 \x01(\t2F\n\tDynamicKS\x12\x1f\n\x06setKey\x12\x08.request\x1a\t.response\"\x00\x12\x18\n\x06getKey\x12\x04.key\x1a\x06.value\"\x00\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='request',
  full_name='request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='request.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='request.value', index=1,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=57,
)


_RESPONSE = _descriptor.Descriptor(
  name='response',
  full_name='response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='response.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=59,
  serialized_end=85,
)


_KEY = _descriptor.Descriptor(
  name='key',
  full_name='key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='key.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=87,
  serialized_end=105,
)


_VALUE = _descriptor.Descriptor(
  name='value',
  full_name='value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='value.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=107,
  serialized_end=129,
)

DESCRIPTOR.message_types_by_name['request'] = _REQUEST
DESCRIPTOR.message_types_by_name['response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['key'] = _KEY
DESCRIPTOR.message_types_by_name['value'] = _VALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

request = _reflection.GeneratedProtocolMessageType('request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'dynamic_ks_pb2'
  # @@protoc_insertion_point(class_scope:request)
  ))
_sym_db.RegisterMessage(request)

response = _reflection.GeneratedProtocolMessageType('response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dynamic_ks_pb2'
  # @@protoc_insertion_point(class_scope:response)
  ))
_sym_db.RegisterMessage(response)

key = _reflection.GeneratedProtocolMessageType('key', (_message.Message,), dict(
  DESCRIPTOR = _KEY,
  __module__ = 'dynamic_ks_pb2'
  # @@protoc_insertion_point(class_scope:key)
  ))
_sym_db.RegisterMessage(key)

value = _reflection.GeneratedProtocolMessageType('value', (_message.Message,), dict(
  DESCRIPTOR = _VALUE,
  __module__ = 'dynamic_ks_pb2'
  # @@protoc_insertion_point(class_scope:value)
  ))
_sym_db.RegisterMessage(value)



_DYNAMICKS = _descriptor.ServiceDescriptor(
  name='DynamicKS',
  full_name='DynamicKS',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=131,
  serialized_end=201,
  methods=[
  _descriptor.MethodDescriptor(
    name='setKey',
    full_name='DynamicKS.setKey',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getKey',
    full_name='DynamicKS.getKey',
    index=1,
    containing_service=None,
    input_type=_KEY,
    output_type=_VALUE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DYNAMICKS)

DESCRIPTOR.services_by_name['DynamicKS'] = _DYNAMICKS

# @@protoc_insertion_point(module_scope)