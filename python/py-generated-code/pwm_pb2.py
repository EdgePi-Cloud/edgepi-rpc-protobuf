# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pwm.proto
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
  name='pwm.proto',
  package='EdgePiRPC_PWM',
  syntax='proto3',
  serialized_options=b'\220\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tpwm.proto\x12\rEdgePiRPC_PWM\".\n\nSuccessMsg\x12\x14\n\x07\x63ontent\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_content\"\xd0\x01\n\x06\x43onfig\x12/\n\x08\x63onf_arg\x18\x01 \x03(\x0b\x32\x1d.EdgePiRPC_PWM.Config.ConfArg\x1a\x94\x01\n\x07\x43onfArg\x12)\n\x07pwm_num\x18\x02 \x01(\x0e\x32\x16.EdgePiRPC_PWM.PWMPinsH\x00\x12\x13\n\tfrequency\x18\x03 \x01(\x02H\x00\x12\x14\n\nduty_cycle\x18\x04 \x01(\x02H\x00\x12+\n\x08polarity\x18\x05 \x01(\x0e\x32\x17.EdgePiRPC_PWM.PolarityH\x00\x42\x06\n\x04\x65num\"?\n\x03PWM\x12,\n\x07pwm_num\x18\x01 \x01(\x0e\x32\x16.EdgePiRPC_PWM.PWMPinsH\x00\x88\x01\x01\x42\n\n\x08_pwm_num\"4\n\x0cGetFrequency\x12\x16\n\tfrequency\x18\x01 \x01(\x02H\x00\x88\x01\x01\x42\x0c\n\n_frequency\"6\n\x0cGetDutyCycle\x12\x17\n\nduty_cycle\x18\x01 \x01(\x02H\x00\x88\x01\x01\x42\r\n\x0b_duty_cycle\".\n\nGetEnabled\x12\x14\n\x07\x65nabled\x18\x01 \x01(\x08H\x00\x88\x01\x01\x42\n\n\x08_enabled\"J\n\x0bGetPolarity\x12.\n\x08polarity\x18\x01 \x01(\x0e\x32\x17.EdgePiRPC_PWM.PolarityH\x00\x88\x01\x01\x42\x0b\n\t_polarity*$\n\x08Polarity\x12\n\n\x06NORMAL\x10\x00\x12\x0c\n\x08INVERSED\x10\x01*\x1d\n\x07PWMPins\x12\x08\n\x04PWM1\x10\x00\x12\x08\n\x04PWM2\x10\x01\x32\xb5\x04\n\nPWMService\x12>\n\nset_config\x12\x15.EdgePiRPC_PWM.Config\x1a\x19.EdgePiRPC_PWM.SuccessMsg\x12\x39\n\x08init_pwm\x12\x12.EdgePiRPC_PWM.PWM\x1a\x19.EdgePiRPC_PWM.SuccessMsg\x12@\n\rget_frequency\x12\x12.EdgePiRPC_PWM.PWM\x1a\x1b.EdgePiRPC_PWM.GetFrequency\x12\x41\n\x0eget_duty_cycle\x12\x12.EdgePiRPC_PWM.PWM\x1a\x1b.EdgePiRPC_PWM.GetDutyCycle\x12>\n\x0cget_polarity\x12\x12.EdgePiRPC_PWM.PWM\x1a\x1a.EdgePiRPC_PWM.GetPolarity\x12\x37\n\x06\x65nable\x12\x12.EdgePiRPC_PWM.PWM\x1a\x19.EdgePiRPC_PWM.SuccessMsg\x12\x38\n\x07\x64isable\x12\x12.EdgePiRPC_PWM.PWM\x1a\x19.EdgePiRPC_PWM.SuccessMsg\x12<\n\x0bget_enabled\x12\x12.EdgePiRPC_PWM.PWM\x1a\x19.EdgePiRPC_PWM.GetEnabled\x12\x36\n\x05\x63lose\x12\x12.EdgePiRPC_PWM.PWM\x1a\x19.EdgePiRPC_PWM.SuccessMsgB\x03\x90\x01\x01\x62\x06proto3'
)

_POLARITY = _descriptor.EnumDescriptor(
  name='Polarity',
  full_name='EdgePiRPC_PWM.Polarity',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVERSED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=586,
  serialized_end=622,
)
_sym_db.RegisterEnumDescriptor(_POLARITY)

Polarity = enum_type_wrapper.EnumTypeWrapper(_POLARITY)
_PWMPINS = _descriptor.EnumDescriptor(
  name='PWMPins',
  full_name='EdgePiRPC_PWM.PWMPins',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PWM1', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PWM2', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=624,
  serialized_end=653,
)
_sym_db.RegisterEnumDescriptor(_PWMPINS)

PWMPins = enum_type_wrapper.EnumTypeWrapper(_PWMPINS)
NORMAL = 0
INVERSED = 1
PWM1 = 0
PWM2 = 1



_SUCCESSMSG = _descriptor.Descriptor(
  name='SuccessMsg',
  full_name='EdgePiRPC_PWM.SuccessMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='EdgePiRPC_PWM.SuccessMsg.content', index=0,
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
      name='_content', full_name='EdgePiRPC_PWM.SuccessMsg._content',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=28,
  serialized_end=74,
)


_CONFIG_CONFARG = _descriptor.Descriptor(
  name='ConfArg',
  full_name='EdgePiRPC_PWM.Config.ConfArg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pwm_num', full_name='EdgePiRPC_PWM.Config.ConfArg.pwm_num', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='EdgePiRPC_PWM.Config.ConfArg.frequency', index=1,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duty_cycle', full_name='EdgePiRPC_PWM.Config.ConfArg.duty_cycle', index=2,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='polarity', full_name='EdgePiRPC_PWM.Config.ConfArg.polarity', index=3,
      number=5, type=14, cpp_type=8, label=1,
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
      name='enum', full_name='EdgePiRPC_PWM.Config.ConfArg.enum',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=137,
  serialized_end=285,
)

_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='EdgePiRPC_PWM.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='conf_arg', full_name='EdgePiRPC_PWM.Config.conf_arg', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CONFIG_CONFARG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=285,
)


_PWM = _descriptor.Descriptor(
  name='PWM',
  full_name='EdgePiRPC_PWM.PWM',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pwm_num', full_name='EdgePiRPC_PWM.PWM.pwm_num', index=0,
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
      name='_pwm_num', full_name='EdgePiRPC_PWM.PWM._pwm_num',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=287,
  serialized_end=350,
)


_GETFREQUENCY = _descriptor.Descriptor(
  name='GetFrequency',
  full_name='EdgePiRPC_PWM.GetFrequency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frequency', full_name='EdgePiRPC_PWM.GetFrequency.frequency', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
      name='_frequency', full_name='EdgePiRPC_PWM.GetFrequency._frequency',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=352,
  serialized_end=404,
)


_GETDUTYCYCLE = _descriptor.Descriptor(
  name='GetDutyCycle',
  full_name='EdgePiRPC_PWM.GetDutyCycle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='duty_cycle', full_name='EdgePiRPC_PWM.GetDutyCycle.duty_cycle', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
      name='_duty_cycle', full_name='EdgePiRPC_PWM.GetDutyCycle._duty_cycle',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=406,
  serialized_end=460,
)


_GETENABLED = _descriptor.Descriptor(
  name='GetEnabled',
  full_name='EdgePiRPC_PWM.GetEnabled',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='EdgePiRPC_PWM.GetEnabled.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
      name='_enabled', full_name='EdgePiRPC_PWM.GetEnabled._enabled',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=462,
  serialized_end=508,
)


_GETPOLARITY = _descriptor.Descriptor(
  name='GetPolarity',
  full_name='EdgePiRPC_PWM.GetPolarity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='polarity', full_name='EdgePiRPC_PWM.GetPolarity.polarity', index=0,
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
      name='_polarity', full_name='EdgePiRPC_PWM.GetPolarity._polarity',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=510,
  serialized_end=584,
)

_SUCCESSMSG.oneofs_by_name['_content'].fields.append(
  _SUCCESSMSG.fields_by_name['content'])
_SUCCESSMSG.fields_by_name['content'].containing_oneof = _SUCCESSMSG.oneofs_by_name['_content']
_CONFIG_CONFARG.fields_by_name['pwm_num'].enum_type = _PWMPINS
_CONFIG_CONFARG.fields_by_name['polarity'].enum_type = _POLARITY
_CONFIG_CONFARG.containing_type = _CONFIG
_CONFIG_CONFARG.oneofs_by_name['enum'].fields.append(
  _CONFIG_CONFARG.fields_by_name['pwm_num'])
_CONFIG_CONFARG.fields_by_name['pwm_num'].containing_oneof = _CONFIG_CONFARG.oneofs_by_name['enum']
_CONFIG_CONFARG.oneofs_by_name['enum'].fields.append(
  _CONFIG_CONFARG.fields_by_name['frequency'])
_CONFIG_CONFARG.fields_by_name['frequency'].containing_oneof = _CONFIG_CONFARG.oneofs_by_name['enum']
_CONFIG_CONFARG.oneofs_by_name['enum'].fields.append(
  _CONFIG_CONFARG.fields_by_name['duty_cycle'])
_CONFIG_CONFARG.fields_by_name['duty_cycle'].containing_oneof = _CONFIG_CONFARG.oneofs_by_name['enum']
_CONFIG_CONFARG.oneofs_by_name['enum'].fields.append(
  _CONFIG_CONFARG.fields_by_name['polarity'])
_CONFIG_CONFARG.fields_by_name['polarity'].containing_oneof = _CONFIG_CONFARG.oneofs_by_name['enum']
_CONFIG.fields_by_name['conf_arg'].message_type = _CONFIG_CONFARG
_PWM.fields_by_name['pwm_num'].enum_type = _PWMPINS
_PWM.oneofs_by_name['_pwm_num'].fields.append(
  _PWM.fields_by_name['pwm_num'])
_PWM.fields_by_name['pwm_num'].containing_oneof = _PWM.oneofs_by_name['_pwm_num']
_GETFREQUENCY.oneofs_by_name['_frequency'].fields.append(
  _GETFREQUENCY.fields_by_name['frequency'])
_GETFREQUENCY.fields_by_name['frequency'].containing_oneof = _GETFREQUENCY.oneofs_by_name['_frequency']
_GETDUTYCYCLE.oneofs_by_name['_duty_cycle'].fields.append(
  _GETDUTYCYCLE.fields_by_name['duty_cycle'])
_GETDUTYCYCLE.fields_by_name['duty_cycle'].containing_oneof = _GETDUTYCYCLE.oneofs_by_name['_duty_cycle']
_GETENABLED.oneofs_by_name['_enabled'].fields.append(
  _GETENABLED.fields_by_name['enabled'])
_GETENABLED.fields_by_name['enabled'].containing_oneof = _GETENABLED.oneofs_by_name['_enabled']
_GETPOLARITY.fields_by_name['polarity'].enum_type = _POLARITY
_GETPOLARITY.oneofs_by_name['_polarity'].fields.append(
  _GETPOLARITY.fields_by_name['polarity'])
_GETPOLARITY.fields_by_name['polarity'].containing_oneof = _GETPOLARITY.oneofs_by_name['_polarity']
DESCRIPTOR.message_types_by_name['SuccessMsg'] = _SUCCESSMSG
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['PWM'] = _PWM
DESCRIPTOR.message_types_by_name['GetFrequency'] = _GETFREQUENCY
DESCRIPTOR.message_types_by_name['GetDutyCycle'] = _GETDUTYCYCLE
DESCRIPTOR.message_types_by_name['GetEnabled'] = _GETENABLED
DESCRIPTOR.message_types_by_name['GetPolarity'] = _GETPOLARITY
DESCRIPTOR.enum_types_by_name['Polarity'] = _POLARITY
DESCRIPTOR.enum_types_by_name['PWMPins'] = _PWMPINS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SuccessMsg = _reflection.GeneratedProtocolMessageType('SuccessMsg', (_message.Message,), {
  'DESCRIPTOR' : _SUCCESSMSG,
  '__module__' : 'pwm_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_PWM.SuccessMsg)
  })
_sym_db.RegisterMessage(SuccessMsg)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {

  'ConfArg' : _reflection.GeneratedProtocolMessageType('ConfArg', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_CONFARG,
    '__module__' : 'pwm_pb2'
    # @@protoc_insertion_point(class_scope:EdgePiRPC_PWM.Config.ConfArg)
    })
  ,
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'pwm_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_PWM.Config)
  })
_sym_db.RegisterMessage(Config)
_sym_db.RegisterMessage(Config.ConfArg)

PWM = _reflection.GeneratedProtocolMessageType('PWM', (_message.Message,), {
  'DESCRIPTOR' : _PWM,
  '__module__' : 'pwm_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_PWM.PWM)
  })
_sym_db.RegisterMessage(PWM)

GetFrequency = _reflection.GeneratedProtocolMessageType('GetFrequency', (_message.Message,), {
  'DESCRIPTOR' : _GETFREQUENCY,
  '__module__' : 'pwm_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_PWM.GetFrequency)
  })
_sym_db.RegisterMessage(GetFrequency)

GetDutyCycle = _reflection.GeneratedProtocolMessageType('GetDutyCycle', (_message.Message,), {
  'DESCRIPTOR' : _GETDUTYCYCLE,
  '__module__' : 'pwm_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_PWM.GetDutyCycle)
  })
_sym_db.RegisterMessage(GetDutyCycle)

GetEnabled = _reflection.GeneratedProtocolMessageType('GetEnabled', (_message.Message,), {
  'DESCRIPTOR' : _GETENABLED,
  '__module__' : 'pwm_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_PWM.GetEnabled)
  })
_sym_db.RegisterMessage(GetEnabled)

GetPolarity = _reflection.GeneratedProtocolMessageType('GetPolarity', (_message.Message,), {
  'DESCRIPTOR' : _GETPOLARITY,
  '__module__' : 'pwm_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_PWM.GetPolarity)
  })
_sym_db.RegisterMessage(GetPolarity)


DESCRIPTOR._options = None

_PWMSERVICE = _descriptor.ServiceDescriptor(
  name='PWMService',
  full_name='EdgePiRPC_PWM.PWMService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=656,
  serialized_end=1221,
  methods=[
  _descriptor.MethodDescriptor(
    name='set_config',
    full_name='EdgePiRPC_PWM.PWMService.set_config',
    index=0,
    containing_service=None,
    input_type=_CONFIG,
    output_type=_SUCCESSMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='init_pwm',
    full_name='EdgePiRPC_PWM.PWMService.init_pwm',
    index=1,
    containing_service=None,
    input_type=_PWM,
    output_type=_SUCCESSMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_frequency',
    full_name='EdgePiRPC_PWM.PWMService.get_frequency',
    index=2,
    containing_service=None,
    input_type=_PWM,
    output_type=_GETFREQUENCY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_duty_cycle',
    full_name='EdgePiRPC_PWM.PWMService.get_duty_cycle',
    index=3,
    containing_service=None,
    input_type=_PWM,
    output_type=_GETDUTYCYCLE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_polarity',
    full_name='EdgePiRPC_PWM.PWMService.get_polarity',
    index=4,
    containing_service=None,
    input_type=_PWM,
    output_type=_GETPOLARITY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='enable',
    full_name='EdgePiRPC_PWM.PWMService.enable',
    index=5,
    containing_service=None,
    input_type=_PWM,
    output_type=_SUCCESSMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='disable',
    full_name='EdgePiRPC_PWM.PWMService.disable',
    index=6,
    containing_service=None,
    input_type=_PWM,
    output_type=_SUCCESSMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_enabled',
    full_name='EdgePiRPC_PWM.PWMService.get_enabled',
    index=7,
    containing_service=None,
    input_type=_PWM,
    output_type=_GETENABLED,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='close',
    full_name='EdgePiRPC_PWM.PWMService.close',
    index=8,
    containing_service=None,
    input_type=_PWM,
    output_type=_SUCCESSMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PWMSERVICE)

DESCRIPTOR.services_by_name['PWMService'] = _PWMSERVICE

PWMService = service_reflection.GeneratedServiceType('PWMService', (_service.Service,), dict(
  DESCRIPTOR = _PWMSERVICE,
  __module__ = 'pwm_pb2'
  ))

PWMService_Stub = service_reflection.GeneratedServiceStubType('PWMService_Stub', (PWMService,), dict(
  DESCRIPTOR = _PWMSERVICE,
  __module__ = 'pwm_pb2'
  ))


# @@protoc_insertion_point(module_scope)
