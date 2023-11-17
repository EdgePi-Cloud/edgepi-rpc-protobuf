# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: adc.proto
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
  name='adc.proto',
  package='EdgePiRPC_ADC',
  syntax='proto3',
  serialized_options=b'\220\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tadc.proto\x12\rEdgePiRPC_ADC\"\n\n\x08\x45mptyMsg\".\n\nSuccessMsg\x12\x14\n\x07\x63ontent\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_content\"9\n\x0bVoltageRead\x12\x19\n\x0cvoltage_read\x18\x01 \x01(\x02H\x00\x88\x01\x01\x42\x0f\n\r_voltage_read\"\xb2\x03\n\x06\x43onfig\x12/\n\x08\x63onf_arg\x18\x01 \x03(\x0b\x32\x1d.EdgePiRPC_ADC.Config.ConfArg\x1a\xf6\x02\n\x07\x43onfArg\x12\x32\n\x0f\x61\x64\x63_1_analog_in\x18\x02 \x01(\x0e\x32\x17.EdgePiRPC_ADC.AnalogInH\x00\x12\x36\n\x0f\x61\x64\x63_1_data_rate\x18\x03 \x01(\x0e\x32\x1b.EdgePiRPC_ADC.ADC1DataRateH\x00\x12\x32\n\x0f\x61\x64\x63_2_analog_in\x18\x04 \x01(\x0e\x32\x17.EdgePiRPC_ADC.AnalogInH\x00\x12\x36\n\x0f\x61\x64\x63_2_data_rate\x18\x05 \x01(\x0e\x32\x1b.EdgePiRPC_ADC.ADC2DataRateH\x00\x12\x30\n\x0b\x66ilter_mode\x18\x06 \x01(\x0e\x32\x19.EdgePiRPC_ADC.FilterModeH\x00\x12\x32\n\x0f\x63onversion_mode\x18\x07 \x01(\x0e\x32\x17.EdgePiRPC_ADC.ConvModeH\x00\x12%\n\x1boverride_updates_validation\x18\x08 \x01(\x08H\x00\x42\x06\n\x04\x65num\"z\n\nDiffConfig\x12+\n\x07\x61\x64\x63_num\x18\x01 \x01(\x0e\x32\x15.EdgePiRPC_ADC.ADCNumH\x00\x88\x01\x01\x12*\n\x04\x64iff\x18\x02 \x01(\x0e\x32\x17.EdgePiRPC_ADC.DiffModeH\x01\x88\x01\x01\x42\n\n\x08_adc_numB\x07\n\x05_diff\"f\n\tRtdConfig\x12\x14\n\x07set_rtd\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12+\n\x07\x61\x64\x63_num\x18\x02 \x01(\x0e\x32\x15.EdgePiRPC_ADC.ADCNumH\x01\x88\x01\x01\x42\n\n\x08_set_rtdB\n\n\x08_adc_num\")\n\x0bTempReading\x12\x11\n\x04temp\x18\x01 \x01(\x02H\x00\x88\x01\x01\x42\x07\n\x05_temp\">\n\x03\x41\x44\x43\x12+\n\x07\x61\x64\x63_num\x18\x01 \x01(\x0e\x32\x15.EdgePiRPC_ADC.ADCNumH\x00\x88\x01\x01\x42\n\n\x08_adc_num*q\n\x08\x41nalogIn\x12\x08\n\x04\x41IN1\x10\x00\x12\x08\n\x04\x41IN2\x10\x01\x12\x08\n\x04\x41IN3\x10\x02\x12\x08\n\x04\x41IN4\x10\x03\x12\x08\n\x04\x41IN5\x10\x04\x12\x08\n\x04\x41IN6\x10\x05\x12\x08\n\x04\x41IN7\x10\x06\x12\x08\n\x04\x41IN8\x10\x07\x12\n\n\x06\x41INCOM\x10\x08\x12\t\n\x05\x46LOAT\x10\t*\xe6\x01\n\x0c\x41\x44\x43\x31\x44\x61taRate\x12\x0b\n\x07SPS_2P5\x10\x00\x12\t\n\x05SPS_5\x10\x01\x12\x0b\n\x07SPS_10_\x10\x02\x12\x0c\n\x08SPS_16P6\x10\x03\x12\n\n\x06SPS_20\x10\x04\x12\n\n\x06SPS_50\x10\x05\x12\n\n\x06SPS_60\x10\x06\x12\x0c\n\x08SPS_100_\x10\x07\x12\x0c\n\x08SPS_400_\x10\x08\x12\x0c\n\x08SPS_1200\x10\t\x12\x0c\n\x08SPS_2400\x10\n\x12\x0c\n\x08SPS_4800\x10\x0b\x12\x0c\n\x08SPS_7200\x10\x0c\x12\r\n\tSPS_14400\x10\r\x12\r\n\tSPS_19200\x10\x0e\x12\r\n\tSPS_38400\x10\x0f*A\n\x0c\x41\x44\x43\x32\x44\x61taRate\x12\n\n\x06SPS_10\x10\x00\x12\x0b\n\x07SPS_100\x10\x01\x12\x0b\n\x07SPS_400\x10\x03\x12\x0b\n\x07SPS_800\x10\x04*A\n\nFilterMode\x12\t\n\x05SINC1\x10\x00\x12\t\n\x05SINC2\x10\x01\x12\t\n\x05SINC3\x10\x02\x12\t\n\x05SINC4\x10\x03\x12\x07\n\x03\x46IR\x10\x04*%\n\x08\x43onvMode\x12\x0e\n\nCONTINUOUS\x10\x00\x12\t\n\x05PULSE\x10\x01*\x1e\n\x06\x41\x44\x43Num\x12\t\n\x05\x41\x44\x43_1\x10\x00\x12\t\n\x05\x41\x44\x43_2\x10\x01*H\n\x08\x44iffMode\x12\n\n\x06\x44IFF_1\x10\x00\x12\n\n\x06\x44IFF_2\x10\x01\x12\n\n\x06\x44IFF_3\x10\x02\x12\n\n\x06\x44IFF_4\x10\x03\x12\x0c\n\x08\x44IFF_OFF\x10\x04\x32\xfd\x04\n\nAdcService\x12>\n\nset_config\x12\x15.EdgePiRPC_ADC.Config\x1a\x19.EdgePiRPC_ADC.SuccessMsg\x12\x44\n\rsingle_sample\x12\x17.EdgePiRPC_ADC.EmptyMsg\x1a\x1a.EdgePiRPC_ADC.VoltageRead\x12K\n\x13select_differential\x12\x19.EdgePiRPC_ADC.DiffConfig\x1a\x19.EdgePiRPC_ADC.SuccessMsg\x12>\n\x07set_rtd\x12\x18.EdgePiRPC_ADC.RtdConfig\x1a\x19.EdgePiRPC_ADC.SuccessMsg\x12H\n\x11single_sample_rtd\x12\x17.EdgePiRPC_ADC.EmptyMsg\x1a\x1a.EdgePiRPC_ADC.TempReading\x12\x42\n\x11start_conversions\x12\x12.EdgePiRPC_ADC.ADC\x1a\x19.EdgePiRPC_ADC.SuccessMsg\x12\x41\n\x10stop_conversions\x12\x12.EdgePiRPC_ADC.ADC\x1a\x19.EdgePiRPC_ADC.SuccessMsg\x12>\n\x0cread_voltage\x12\x12.EdgePiRPC_ADC.ADC\x1a\x1a.EdgePiRPC_ADC.VoltageRead\x12K\n\x14read_rtd_temperature\x12\x17.EdgePiRPC_ADC.EmptyMsg\x1a\x1a.EdgePiRPC_ADC.TempReadingB\x03\x90\x01\x01\x62\x06proto3'
)

_ANALOGIN = _descriptor.EnumDescriptor(
  name='AnalogIn',
  full_name='EdgePiRPC_ADC.AnalogIn',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AIN1', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AIN2', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AIN3', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AIN4', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AIN5', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AIN6', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AIN7', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AIN8', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AINCOM', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=919,
  serialized_end=1032,
)
_sym_db.RegisterEnumDescriptor(_ANALOGIN)

AnalogIn = enum_type_wrapper.EnumTypeWrapper(_ANALOGIN)
_ADC1DATARATE = _descriptor.EnumDescriptor(
  name='ADC1DataRate',
  full_name='EdgePiRPC_ADC.ADC1DataRate',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPS_2P5', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_5', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_10_', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_16P6', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_20', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_50', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_60', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_100_', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_400_', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_1200', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_2400', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_4800', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_7200', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_14400', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_19200', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_38400', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1035,
  serialized_end=1265,
)
_sym_db.RegisterEnumDescriptor(_ADC1DATARATE)

ADC1DataRate = enum_type_wrapper.EnumTypeWrapper(_ADC1DATARATE)
_ADC2DATARATE = _descriptor.EnumDescriptor(
  name='ADC2DataRate',
  full_name='EdgePiRPC_ADC.ADC2DataRate',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPS_10', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_100', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_400', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPS_800', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1267,
  serialized_end=1332,
)
_sym_db.RegisterEnumDescriptor(_ADC2DATARATE)

ADC2DataRate = enum_type_wrapper.EnumTypeWrapper(_ADC2DATARATE)
_FILTERMODE = _descriptor.EnumDescriptor(
  name='FilterMode',
  full_name='EdgePiRPC_ADC.FilterMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SINC1', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SINC2', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SINC3', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SINC4', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1334,
  serialized_end=1399,
)
_sym_db.RegisterEnumDescriptor(_FILTERMODE)

FilterMode = enum_type_wrapper.EnumTypeWrapper(_FILTERMODE)
_CONVMODE = _descriptor.EnumDescriptor(
  name='ConvMode',
  full_name='EdgePiRPC_ADC.ConvMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONTINUOUS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PULSE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1401,
  serialized_end=1438,
)
_sym_db.RegisterEnumDescriptor(_CONVMODE)

ConvMode = enum_type_wrapper.EnumTypeWrapper(_CONVMODE)
_ADCNUM = _descriptor.EnumDescriptor(
  name='ADCNum',
  full_name='EdgePiRPC_ADC.ADCNum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADC_1', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADC_2', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1440,
  serialized_end=1470,
)
_sym_db.RegisterEnumDescriptor(_ADCNUM)

ADCNum = enum_type_wrapper.EnumTypeWrapper(_ADCNUM)
_DIFFMODE = _descriptor.EnumDescriptor(
  name='DiffMode',
  full_name='EdgePiRPC_ADC.DiffMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIFF_1', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIFF_2', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIFF_3', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIFF_4', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIFF_OFF', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1472,
  serialized_end=1544,
)
_sym_db.RegisterEnumDescriptor(_DIFFMODE)

DiffMode = enum_type_wrapper.EnumTypeWrapper(_DIFFMODE)
AIN1 = 0
AIN2 = 1
AIN3 = 2
AIN4 = 3
AIN5 = 4
AIN6 = 5
AIN7 = 6
AIN8 = 7
AINCOM = 8
FLOAT = 9
SPS_2P5 = 0
SPS_5 = 1
SPS_10_ = 2
SPS_16P6 = 3
SPS_20 = 4
SPS_50 = 5
SPS_60 = 6
SPS_100_ = 7
SPS_400_ = 8
SPS_1200 = 9
SPS_2400 = 10
SPS_4800 = 11
SPS_7200 = 12
SPS_14400 = 13
SPS_19200 = 14
SPS_38400 = 15
SPS_10 = 0
SPS_100 = 1
SPS_400 = 3
SPS_800 = 4
SINC1 = 0
SINC2 = 1
SINC3 = 2
SINC4 = 3
FIR = 4
CONTINUOUS = 0
PULSE = 1
ADC_1 = 0
ADC_2 = 1
DIFF_1 = 0
DIFF_2 = 1
DIFF_3 = 2
DIFF_4 = 3
DIFF_OFF = 4



_EMPTYMSG = _descriptor.Descriptor(
  name='EmptyMsg',
  full_name='EdgePiRPC_ADC.EmptyMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=28,
  serialized_end=38,
)


_SUCCESSMSG = _descriptor.Descriptor(
  name='SuccessMsg',
  full_name='EdgePiRPC_ADC.SuccessMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='EdgePiRPC_ADC.SuccessMsg.content', index=0,
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
      name='_content', full_name='EdgePiRPC_ADC.SuccessMsg._content',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=40,
  serialized_end=86,
)


_VOLTAGEREAD = _descriptor.Descriptor(
  name='VoltageRead',
  full_name='EdgePiRPC_ADC.VoltageRead',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='voltage_read', full_name='EdgePiRPC_ADC.VoltageRead.voltage_read', index=0,
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
      name='_voltage_read', full_name='EdgePiRPC_ADC.VoltageRead._voltage_read',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=88,
  serialized_end=145,
)


_CONFIG_CONFARG = _descriptor.Descriptor(
  name='ConfArg',
  full_name='EdgePiRPC_ADC.Config.ConfArg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='adc_1_analog_in', full_name='EdgePiRPC_ADC.Config.ConfArg.adc_1_analog_in', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adc_1_data_rate', full_name='EdgePiRPC_ADC.Config.ConfArg.adc_1_data_rate', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adc_2_analog_in', full_name='EdgePiRPC_ADC.Config.ConfArg.adc_2_analog_in', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adc_2_data_rate', full_name='EdgePiRPC_ADC.Config.ConfArg.adc_2_data_rate', index=3,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter_mode', full_name='EdgePiRPC_ADC.Config.ConfArg.filter_mode', index=4,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='conversion_mode', full_name='EdgePiRPC_ADC.Config.ConfArg.conversion_mode', index=5,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='override_updates_validation', full_name='EdgePiRPC_ADC.Config.ConfArg.override_updates_validation', index=6,
      number=8, type=8, cpp_type=7, label=1,
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
      name='enum', full_name='EdgePiRPC_ADC.Config.ConfArg.enum',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=208,
  serialized_end=582,
)

_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='EdgePiRPC_ADC.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='conf_arg', full_name='EdgePiRPC_ADC.Config.conf_arg', index=0,
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
  serialized_start=148,
  serialized_end=582,
)


_DIFFCONFIG = _descriptor.Descriptor(
  name='DiffConfig',
  full_name='EdgePiRPC_ADC.DiffConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='adc_num', full_name='EdgePiRPC_ADC.DiffConfig.adc_num', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='diff', full_name='EdgePiRPC_ADC.DiffConfig.diff', index=1,
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
      name='_adc_num', full_name='EdgePiRPC_ADC.DiffConfig._adc_num',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_diff', full_name='EdgePiRPC_ADC.DiffConfig._diff',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=584,
  serialized_end=706,
)


_RTDCONFIG = _descriptor.Descriptor(
  name='RtdConfig',
  full_name='EdgePiRPC_ADC.RtdConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='set_rtd', full_name='EdgePiRPC_ADC.RtdConfig.set_rtd', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adc_num', full_name='EdgePiRPC_ADC.RtdConfig.adc_num', index=1,
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
      name='_set_rtd', full_name='EdgePiRPC_ADC.RtdConfig._set_rtd',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_adc_num', full_name='EdgePiRPC_ADC.RtdConfig._adc_num',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=708,
  serialized_end=810,
)


_TEMPREADING = _descriptor.Descriptor(
  name='TempReading',
  full_name='EdgePiRPC_ADC.TempReading',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='temp', full_name='EdgePiRPC_ADC.TempReading.temp', index=0,
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
      name='_temp', full_name='EdgePiRPC_ADC.TempReading._temp',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=812,
  serialized_end=853,
)


_ADC = _descriptor.Descriptor(
  name='ADC',
  full_name='EdgePiRPC_ADC.ADC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='adc_num', full_name='EdgePiRPC_ADC.ADC.adc_num', index=0,
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
      name='_adc_num', full_name='EdgePiRPC_ADC.ADC._adc_num',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=855,
  serialized_end=917,
)

_SUCCESSMSG.oneofs_by_name['_content'].fields.append(
  _SUCCESSMSG.fields_by_name['content'])
_SUCCESSMSG.fields_by_name['content'].containing_oneof = _SUCCESSMSG.oneofs_by_name['_content']
_VOLTAGEREAD.oneofs_by_name['_voltage_read'].fields.append(
  _VOLTAGEREAD.fields_by_name['voltage_read'])
_VOLTAGEREAD.fields_by_name['voltage_read'].containing_oneof = _VOLTAGEREAD.oneofs_by_name['_voltage_read']
_CONFIG_CONFARG.fields_by_name['adc_1_analog_in'].enum_type = _ANALOGIN
_CONFIG_CONFARG.fields_by_name['adc_1_data_rate'].enum_type = _ADC1DATARATE
_CONFIG_CONFARG.fields_by_name['adc_2_analog_in'].enum_type = _ANALOGIN
_CONFIG_CONFARG.fields_by_name['adc_2_data_rate'].enum_type = _ADC2DATARATE
_CONFIG_CONFARG.fields_by_name['filter_mode'].enum_type = _FILTERMODE
_CONFIG_CONFARG.fields_by_name['conversion_mode'].enum_type = _CONVMODE
_CONFIG_CONFARG.containing_type = _CONFIG
_CONFIG_CONFARG.oneofs_by_name['enum'].fields.append(
  _CONFIG_CONFARG.fields_by_name['adc_1_analog_in'])
_CONFIG_CONFARG.fields_by_name['adc_1_analog_in'].containing_oneof = _CONFIG_CONFARG.oneofs_by_name['enum']
_CONFIG_CONFARG.oneofs_by_name['enum'].fields.append(
  _CONFIG_CONFARG.fields_by_name['adc_1_data_rate'])
_CONFIG_CONFARG.fields_by_name['adc_1_data_rate'].containing_oneof = _CONFIG_CONFARG.oneofs_by_name['enum']
_CONFIG_CONFARG.oneofs_by_name['enum'].fields.append(
  _CONFIG_CONFARG.fields_by_name['adc_2_analog_in'])
_CONFIG_CONFARG.fields_by_name['adc_2_analog_in'].containing_oneof = _CONFIG_CONFARG.oneofs_by_name['enum']
_CONFIG_CONFARG.oneofs_by_name['enum'].fields.append(
  _CONFIG_CONFARG.fields_by_name['adc_2_data_rate'])
_CONFIG_CONFARG.fields_by_name['adc_2_data_rate'].containing_oneof = _CONFIG_CONFARG.oneofs_by_name['enum']
_CONFIG_CONFARG.oneofs_by_name['enum'].fields.append(
  _CONFIG_CONFARG.fields_by_name['filter_mode'])
_CONFIG_CONFARG.fields_by_name['filter_mode'].containing_oneof = _CONFIG_CONFARG.oneofs_by_name['enum']
_CONFIG_CONFARG.oneofs_by_name['enum'].fields.append(
  _CONFIG_CONFARG.fields_by_name['conversion_mode'])
_CONFIG_CONFARG.fields_by_name['conversion_mode'].containing_oneof = _CONFIG_CONFARG.oneofs_by_name['enum']
_CONFIG_CONFARG.oneofs_by_name['enum'].fields.append(
  _CONFIG_CONFARG.fields_by_name['override_updates_validation'])
_CONFIG_CONFARG.fields_by_name['override_updates_validation'].containing_oneof = _CONFIG_CONFARG.oneofs_by_name['enum']
_CONFIG.fields_by_name['conf_arg'].message_type = _CONFIG_CONFARG
_DIFFCONFIG.fields_by_name['adc_num'].enum_type = _ADCNUM
_DIFFCONFIG.fields_by_name['diff'].enum_type = _DIFFMODE
_DIFFCONFIG.oneofs_by_name['_adc_num'].fields.append(
  _DIFFCONFIG.fields_by_name['adc_num'])
_DIFFCONFIG.fields_by_name['adc_num'].containing_oneof = _DIFFCONFIG.oneofs_by_name['_adc_num']
_DIFFCONFIG.oneofs_by_name['_diff'].fields.append(
  _DIFFCONFIG.fields_by_name['diff'])
_DIFFCONFIG.fields_by_name['diff'].containing_oneof = _DIFFCONFIG.oneofs_by_name['_diff']
_RTDCONFIG.fields_by_name['adc_num'].enum_type = _ADCNUM
_RTDCONFIG.oneofs_by_name['_set_rtd'].fields.append(
  _RTDCONFIG.fields_by_name['set_rtd'])
_RTDCONFIG.fields_by_name['set_rtd'].containing_oneof = _RTDCONFIG.oneofs_by_name['_set_rtd']
_RTDCONFIG.oneofs_by_name['_adc_num'].fields.append(
  _RTDCONFIG.fields_by_name['adc_num'])
_RTDCONFIG.fields_by_name['adc_num'].containing_oneof = _RTDCONFIG.oneofs_by_name['_adc_num']
_TEMPREADING.oneofs_by_name['_temp'].fields.append(
  _TEMPREADING.fields_by_name['temp'])
_TEMPREADING.fields_by_name['temp'].containing_oneof = _TEMPREADING.oneofs_by_name['_temp']
_ADC.fields_by_name['adc_num'].enum_type = _ADCNUM
_ADC.oneofs_by_name['_adc_num'].fields.append(
  _ADC.fields_by_name['adc_num'])
_ADC.fields_by_name['adc_num'].containing_oneof = _ADC.oneofs_by_name['_adc_num']
DESCRIPTOR.message_types_by_name['EmptyMsg'] = _EMPTYMSG
DESCRIPTOR.message_types_by_name['SuccessMsg'] = _SUCCESSMSG
DESCRIPTOR.message_types_by_name['VoltageRead'] = _VOLTAGEREAD
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['DiffConfig'] = _DIFFCONFIG
DESCRIPTOR.message_types_by_name['RtdConfig'] = _RTDCONFIG
DESCRIPTOR.message_types_by_name['TempReading'] = _TEMPREADING
DESCRIPTOR.message_types_by_name['ADC'] = _ADC
DESCRIPTOR.enum_types_by_name['AnalogIn'] = _ANALOGIN
DESCRIPTOR.enum_types_by_name['ADC1DataRate'] = _ADC1DATARATE
DESCRIPTOR.enum_types_by_name['ADC2DataRate'] = _ADC2DATARATE
DESCRIPTOR.enum_types_by_name['FilterMode'] = _FILTERMODE
DESCRIPTOR.enum_types_by_name['ConvMode'] = _CONVMODE
DESCRIPTOR.enum_types_by_name['ADCNum'] = _ADCNUM
DESCRIPTOR.enum_types_by_name['DiffMode'] = _DIFFMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyMsg = _reflection.GeneratedProtocolMessageType('EmptyMsg', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYMSG,
  '__module__' : 'adc_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_ADC.EmptyMsg)
  })
_sym_db.RegisterMessage(EmptyMsg)

SuccessMsg = _reflection.GeneratedProtocolMessageType('SuccessMsg', (_message.Message,), {
  'DESCRIPTOR' : _SUCCESSMSG,
  '__module__' : 'adc_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_ADC.SuccessMsg)
  })
_sym_db.RegisterMessage(SuccessMsg)

VoltageRead = _reflection.GeneratedProtocolMessageType('VoltageRead', (_message.Message,), {
  'DESCRIPTOR' : _VOLTAGEREAD,
  '__module__' : 'adc_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_ADC.VoltageRead)
  })
_sym_db.RegisterMessage(VoltageRead)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {

  'ConfArg' : _reflection.GeneratedProtocolMessageType('ConfArg', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_CONFARG,
    '__module__' : 'adc_pb2'
    # @@protoc_insertion_point(class_scope:EdgePiRPC_ADC.Config.ConfArg)
    })
  ,
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'adc_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_ADC.Config)
  })
_sym_db.RegisterMessage(Config)
_sym_db.RegisterMessage(Config.ConfArg)

DiffConfig = _reflection.GeneratedProtocolMessageType('DiffConfig', (_message.Message,), {
  'DESCRIPTOR' : _DIFFCONFIG,
  '__module__' : 'adc_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_ADC.DiffConfig)
  })
_sym_db.RegisterMessage(DiffConfig)

RtdConfig = _reflection.GeneratedProtocolMessageType('RtdConfig', (_message.Message,), {
  'DESCRIPTOR' : _RTDCONFIG,
  '__module__' : 'adc_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_ADC.RtdConfig)
  })
_sym_db.RegisterMessage(RtdConfig)

TempReading = _reflection.GeneratedProtocolMessageType('TempReading', (_message.Message,), {
  'DESCRIPTOR' : _TEMPREADING,
  '__module__' : 'adc_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_ADC.TempReading)
  })
_sym_db.RegisterMessage(TempReading)

ADC = _reflection.GeneratedProtocolMessageType('ADC', (_message.Message,), {
  'DESCRIPTOR' : _ADC,
  '__module__' : 'adc_pb2'
  # @@protoc_insertion_point(class_scope:EdgePiRPC_ADC.ADC)
  })
_sym_db.RegisterMessage(ADC)


DESCRIPTOR._options = None

_ADCSERVICE = _descriptor.ServiceDescriptor(
  name='AdcService',
  full_name='EdgePiRPC_ADC.AdcService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1547,
  serialized_end=2184,
  methods=[
  _descriptor.MethodDescriptor(
    name='set_config',
    full_name='EdgePiRPC_ADC.AdcService.set_config',
    index=0,
    containing_service=None,
    input_type=_CONFIG,
    output_type=_SUCCESSMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='single_sample',
    full_name='EdgePiRPC_ADC.AdcService.single_sample',
    index=1,
    containing_service=None,
    input_type=_EMPTYMSG,
    output_type=_VOLTAGEREAD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='select_differential',
    full_name='EdgePiRPC_ADC.AdcService.select_differential',
    index=2,
    containing_service=None,
    input_type=_DIFFCONFIG,
    output_type=_SUCCESSMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='set_rtd',
    full_name='EdgePiRPC_ADC.AdcService.set_rtd',
    index=3,
    containing_service=None,
    input_type=_RTDCONFIG,
    output_type=_SUCCESSMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='single_sample_rtd',
    full_name='EdgePiRPC_ADC.AdcService.single_sample_rtd',
    index=4,
    containing_service=None,
    input_type=_EMPTYMSG,
    output_type=_TEMPREADING,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='start_conversions',
    full_name='EdgePiRPC_ADC.AdcService.start_conversions',
    index=5,
    containing_service=None,
    input_type=_ADC,
    output_type=_SUCCESSMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='stop_conversions',
    full_name='EdgePiRPC_ADC.AdcService.stop_conversions',
    index=6,
    containing_service=None,
    input_type=_ADC,
    output_type=_SUCCESSMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='read_voltage',
    full_name='EdgePiRPC_ADC.AdcService.read_voltage',
    index=7,
    containing_service=None,
    input_type=_ADC,
    output_type=_VOLTAGEREAD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='read_rtd_temperature',
    full_name='EdgePiRPC_ADC.AdcService.read_rtd_temperature',
    index=8,
    containing_service=None,
    input_type=_EMPTYMSG,
    output_type=_TEMPREADING,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADCSERVICE)

DESCRIPTOR.services_by_name['AdcService'] = _ADCSERVICE

AdcService = service_reflection.GeneratedServiceType('AdcService', (_service.Service,), dict(
  DESCRIPTOR = _ADCSERVICE,
  __module__ = 'adc_pb2'
  ))

AdcService_Stub = service_reflection.GeneratedServiceStubType('AdcService_Stub', (AdcService,), dict(
  DESCRIPTOR = _ADCSERVICE,
  __module__ = 'adc_pb2'
  ))


# @@protoc_insertion_point(module_scope)