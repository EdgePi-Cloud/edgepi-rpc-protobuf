# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: din.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tdin.proto\x12\rEdgePiRPC_DIN\"B\n\x06\x44inPin\x12,\n\x07\x64in_pin\x18\x01 \x01(\x0e\x32\x16.EdgePiRPC_DIN.DinPinsH\x00\x88\x01\x01\x42\n\n\x08_din_pin\"/\n\x05State\x12\x17\n\nstate_bool\x18\x01 \x01(\x08H\x00\x88\x01\x01\x42\r\n\x0b_state_bool*Y\n\x07\x44inPins\x12\x08\n\x04\x44IN1\x10\x00\x12\x08\n\x04\x44IN2\x10\x01\x12\x08\n\x04\x44IN3\x10\x02\x12\x08\n\x04\x44IN4\x10\x03\x12\x08\n\x04\x44IN5\x10\x04\x12\x08\n\x04\x44IN6\x10\x05\x12\x08\n\x04\x44IN7\x10\x06\x12\x08\n\x04\x44IN8\x10\x07\x32P\n\nDinService\x12\x42\n\x13\x64igital_input_state\x12\x15.EdgePiRPC_DIN.DinPin\x1a\x14.EdgePiRPC_DIN.StateB\x03\x90\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'din_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_DINPINS']._serialized_start=145
  _globals['_DINPINS']._serialized_end=234
  _globals['_DINPIN']._serialized_start=28
  _globals['_DINPIN']._serialized_end=94
  _globals['_STATE']._serialized_start=96
  _globals['_STATE']._serialized_end=143
  _globals['_DINSERVICE']._serialized_start=236
  _globals['_DINSERVICE']._serialized_end=316
_builder.BuildServices(DESCRIPTOR, 'din_pb2', _globals)
# @@protoc_insertion_point(module_scope)
