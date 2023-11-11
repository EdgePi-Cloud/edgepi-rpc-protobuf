# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dout.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dout.proto',
  package='EdgePiRPC_Dout',
  syntax='proto3',
  serialized_options=b'\220\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ndout.proto\x12\x0e\x45\x64gePiRPC_Dout\"\x87\x01\n\x0bPinAndState\x12/\n\x08\x64out_pin\x18\x01 \x01(\x0e\x32\x18.EdgePiRPC_Dout.DoutPinsH\x00\x88\x01\x01\x12\x30\n\x05state\x18\x02 \x01(\x0e\x32\x1c.EdgePiRPC_Dout.DoutTriStateH\x01\x88\x01\x01\x42\x0b\n\t_dout_pinB\x08\n\x06_state\"G\n\x07\x44outPin\x12/\n\x08\x64out_pin\x18\x01 \x01(\x0e\x32\x18.EdgePiRPC_Dout.DoutPinsH\x00\x88\x01\x01\x42\x0b\n\t_dout_pin\"C\n\x05State\x12\x30\n\x05state\x18\x01 \x01(\x0e\x32\x1c.EdgePiRPC_Dout.DoutTriStateH\x00\x88\x01\x01\x42\x08\n\x06_state\".\n\nSuccessMsg\x12\x14\n\x07\x63ontent\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_content*b\n\x08\x44outPins\x12\t\n\x05\x44OUT1\x10\x00\x12\t\n\x05\x44OUT2\x10\x01\x12\t\n\x05\x44OUT3\x10\x02\x12\t\n\x05\x44OUT4\x10\x03\x12\t\n\x05\x44OUT5\x10\x04\x12\t\n\x05\x44OUT6\x10\x05\x12\t\n\x05\x44OUT7\x10\x06\x12\t\n\x05\x44OUT8\x10\x07*+\n\x0c\x44outTriState\x12\x08\n\x04HI_Z\x10\x00\x12\x08\n\x04HIGH\x10\x01\x12\x07\n\x03LOW\x10\x02\x32\x95\x01\n\x0b\x44outService\x12I\n\x0eset_dout_state\x12\x1b.EdgePiRPC_Dout.PinAndState\x1a\x1a.EdgePiRPC_Dout.SuccessMsg\x12;\n\tget_state\x12\x17.EdgePiRPC_Dout.DoutPin\x1a\x15.EdgePiRPC_Dout.StateB\x03\x90\x01\x01\x62\x06proto3'
)

_DOUTPINS = _descriptor.EnumDescriptor(
  name='DoutPins',
  full_name='EdgePiRPC_Dout.DoutPins',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DOUT1', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUT2', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUT3', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUT4', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUT5', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUT6', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUT7', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUT8', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=358,
  serialized_end=456,
)
_sym_db.RegisterEnumDescriptor(_DOUTPINS)

DoutPins = enum_type_wrapper.EnumTypeWrapper(_DOUTPINS)
_DOUTTRISTATE = _descriptor.EnumDescriptor(
  name='DoutTriState',
  full_name='EdgePiRPC_Dout.DoutTriState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HI_Z', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HIGH', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOW', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=458,
  serialized_end=501,
)
_sym_db.RegisterEnumDescriptor(_DOUTTRISTATE)

DoutTriState = enum_type_wrapper.EnumTypeWrapper(_DOUTTRISTATE)
DOUT1 = 0
DOUT2 = 1
DOUT3 = 2
DOUT4 = 3
DOUT5 = 4
DOUT6 = 5
DOUT7 = 6
DOUT8 = 7
HI_Z = 0
HIGH = 1
LOW = 2



_PINANDSTATE = _descriptor.Descriptor(
  name='PinAndState',
  full_name='EdgePiRPC_Dout.PinAndState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dout_pin', full_name='EdgePiRPC_Dout.PinAndState.dout_pin', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='EdgePiRPC_Dout.PinAndState.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='_dout_pin', full_name='EdgePiRPC_Dout.PinAndState._dout_pin',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_state', full_name='EdgePiRPC_Dout.PinAndState._state',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=31,
  serialized_end=166,
)


_DOUTPIN = _descriptor.Descriptor(
  name='DoutPin',
  full_name='EdgePiRPC_Dout.DoutPin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dout_pin', full_name='EdgePiRPC_Dout.DoutPin.dout_pin', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='_dout_pin', full_name='EdgePiRPC_Dout.DoutPin._dout_pin',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=168,
  serialized_end=239,
)


_STATE = _descriptor.Descriptor(
  name='State',
  full_name='EdgePiRPC_Dout.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='EdgePiRPC_Dout.State.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='_state', full_name='EdgePiRPC_Dout.State._state',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=241,
  serialized_end=308,
)


_SUCCESSMSG = _descriptor.Descriptor(
  name='SuccessMsg',
  full_name='EdgePiRPC_Dout.SuccessMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='EdgePiRPC_Dout.SuccessMsg.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='_content', full_name='EdgePiRPC_Dout.SuccessMsg._content',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=310,
  serialized_end=356,
)

_PINANDSTATE.fields_by_name['dout_pin'].enum_type = _DOUTPINS
_PINANDSTATE.fields_by_name['state'].enum_type = _DOUTTRISTATE
_PINANDSTATE.oneofs_by_name['_dout_pin'].fields.append(
  _PINANDSTATE.fields_by_name['dout_pin'])
_PINANDSTATE.fields_by_name['dout_pin'].containing_oneof = _PINANDSTATE.oneofs_by_name['_dout_pin']
_PINANDSTATE.oneofs_by_name['_state'].fields.append(
  _PINANDSTATE.fields_by_name['state'])
_PINANDSTATE.fields_by_name['state'].containing_oneof = _PINANDSTATE.oneofs_by_name['_state']
_DOUTPIN.fields_by_name['dout_pin'].enum_type = _DOUTPINS
_DOUTPIN.oneofs_by_name['_dout_pin'].fields.append(
  _DOUTPIN.fields_by_name['dout_pin'])
_DOUTPIN.fields_by_name['dout_pin'].containing_oneof = _DOUTPIN.oneofs_by_name['_dout_pin']
_STATE.fields_by_name['state'].enum_type = _DOUTTRISTATE
_STATE.oneofs_by_name['_state'].fields.append(
  _STATE.fields_by_name['state'])
_STATE.fields_by_name['state'].containing_oneof = _STATE.oneofs_by_name['_state']
_SUCCESSMSG.oneofs_by_name['_content'].fields.append(
  _SUCCESSMSG.fields_by_name['content'])
_SUCCESSMSG.fields_by_name['content'].containing_oneof = _SUCCESSMSG.oneofs_by_name['_content']
DESCRIPTOR.message_types_by_name['PinAndState'] = _PINANDSTATE
DESCRIPTOR.message_types_by_name['DoutPin'] = _DOUTPIN
DESCRIPTOR.message_types_by_name['State'] = _STATE
DESCRIPTOR.message_types_by_name['SuccessMsg'] = _SUCCESSMSG
DESCRIPTOR.enum_types_by_name['DoutPins'] = _DOUTPINS
DESCRIPTOR.enum_types_by_name['DoutTriState'] = _DOUTTRISTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PinAndState = _reflection.GeneratedProtocolMessageType('PinAndState', (_message.Message,), {
  'DESCRIPTOR' : _PINANDSTATE,
  '__module__' : 'dout_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_Dout.PinAndState)
  })
_sym_db.RegisterMessage(PinAndState)

DoutPin = _reflection.GeneratedProtocolMessageType('DoutPin', (_message.Message,), {
  'DESCRIPTOR' : _DOUTPIN,
  '__module__' : 'dout_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_Dout.DoutPin)
  })
_sym_db.RegisterMessage(DoutPin)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
  'DESCRIPTOR' : _STATE,
  '__module__' : 'dout_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_Dout.State)
  })
_sym_db.RegisterMessage(State)

SuccessMsg = _reflection.GeneratedProtocolMessageType('SuccessMsg', (_message.Message,), {
  'DESCRIPTOR' : _SUCCESSMSG,
  '__module__' : 'dout_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_Dout.SuccessMsg)
  })
_sym_db.RegisterMessage(SuccessMsg)


DESCRIPTOR._options = None

_DOUTSERVICE = _descriptor.ServiceDescriptor(
  name='DoutService',
  full_name='EdgePiRPC_Dout.DoutService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=504,
  serialized_end=653,
  methods=[
  _descriptor.MethodDescriptor(
    name='set_dout_state',
    full_name='EdgePiRPC_Dout.DoutService.set_dout_state',
    index=0,
    containing_service=None,
    input_type=_PINANDSTATE,
    output_type=_SUCCESSMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_state',
    full_name='EdgePiRPC_Dout.DoutService.get_state',
    index=1,
    containing_service=None,
    input_type=_DOUTPIN,
    output_type=_STATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DOUTSERVICE)

DESCRIPTOR.services_by_name['DoutService'] = _DOUTSERVICE

DoutService = service_reflection.GeneratedServiceType('DoutService', (_service.Service,), dict(
  DESCRIPTOR = _DOUTSERVICE,
  __module__ = 'dout_pb2'
  ))

DoutService_Stub = service_reflection.GeneratedServiceStubType('DoutService_Stub', (DoutService,), dict(
  DESCRIPTOR = _DOUTSERVICE,
  __module__ = 'dout_pb2'
  ))


# @@protoc_insertion_point(module_scope)
