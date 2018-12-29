# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: insult-jmk.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='insult-jmk.proto',
  package='insultJMK',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10insult-jmk.proto\x12\tinsultJMK\"\x1d\n\rInsultRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\x0eInsultResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2N\n\x08Insulter\x12\x42\n\tGetInsult\x12\x18.insultJMK.InsultRequest\x1a\x19.insultJMK.InsultResponse\"\x00\x62\x06proto3')
)




_INSULTREQUEST = _descriptor.Descriptor(
  name='InsultRequest',
  full_name='insultJMK.InsultRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='insultJMK.InsultRequest.name', index=0,
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
  serialized_start=31,
  serialized_end=60,
)


_INSULTRESPONSE = _descriptor.Descriptor(
  name='InsultResponse',
  full_name='insultJMK.InsultResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='insultJMK.InsultResponse.message', index=0,
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
  serialized_start=62,
  serialized_end=95,
)

DESCRIPTOR.message_types_by_name['InsultRequest'] = _INSULTREQUEST
DESCRIPTOR.message_types_by_name['InsultResponse'] = _INSULTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InsultRequest = _reflection.GeneratedProtocolMessageType('InsultRequest', (_message.Message,), dict(
  DESCRIPTOR = _INSULTREQUEST,
  __module__ = 'insult_jmk_pb2'
  # @@protoc_insertion_point(class_scope:insultJMK.InsultRequest)
  ))
_sym_db.RegisterMessage(InsultRequest)

InsultResponse = _reflection.GeneratedProtocolMessageType('InsultResponse', (_message.Message,), dict(
  DESCRIPTOR = _INSULTRESPONSE,
  __module__ = 'insult_jmk_pb2'
  # @@protoc_insertion_point(class_scope:insultJMK.InsultResponse)
  ))
_sym_db.RegisterMessage(InsultResponse)



_INSULTER = _descriptor.ServiceDescriptor(
  name='Insulter',
  full_name='insultJMK.Insulter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=97,
  serialized_end=175,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetInsult',
    full_name='insultJMK.Insulter.GetInsult',
    index=0,
    containing_service=None,
    input_type=_INSULTREQUEST,
    output_type=_INSULTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_INSULTER)

DESCRIPTOR.services_by_name['Insulter'] = _INSULTER

# @@protoc_insertion_point(module_scope)