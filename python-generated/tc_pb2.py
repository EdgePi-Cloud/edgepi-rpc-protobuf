# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc_module/protos/tc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1arpc_module/protos/tc.proto\x12\x0c\x45\x64gePiRPC_TC\"\n\n\x08\x45mptyMsg\".\n\nSuccessMsg\x12\x14\n\x07\x63ontent\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_content\"S\n\x0bTempReading\x12\x14\n\x07\x63j_temp\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x15\n\x08lin_temp\x18\x02 \x01(\x02H\x01\x88\x01\x01\x42\n\n\x08_cj_tempB\x0b\n\t_lin_temp\"v\n\x06\x43Jtemp\x12\x14\n\x07\x63j_temp\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x35\n\x10\x63j_temp_decimals\x18\x02 \x01(\x0e\x32\x16.EdgePiRPC_TC.DecBits6H\x01\x88\x01\x01\x42\n\n\x08_cj_tempB\x13\n\x11_cj_temp_decimals\"@\n\x0c\x46ilterFaults\x12\x1c\n\x0f\x66ilter_at_fault\x18\x01 \x01(\x08H\x00\x88\x01\x01\x42\x12\n\x10_filter_at_fault\"\x86\x01\n\x06\x46\x61ults\x12)\n\x05\x66\x61ult\x18\x01 \x03(\x0b\x32\x1a.EdgePiRPC_TC.Faults.Fault\x1aQ\n\x05\x46\x61ult\x12\x10\n\x08\x61t_fault\x18\x02 \x01(\x08\x12\x0f\n\x07\x65rr_msg\x18\x03 \x01(\t\x12\x12\n\nfault_type\x18\x04 \x01(\t\x12\x11\n\tis_masked\x18\x05 \x01(\x08\"\x82\t\n\x06\x43onfig\x12.\n\x08\x63onf_arg\x18\x01 \x03(\x0b\x32\x1c.EdgePiRPC_TC.Config.ConfArg\x1a\xc7\x08\n\x07\x43onfArg\x12\x31\n\x0f\x63onversion_mode\x18\x02 \x01(\x0e\x32\x16.EdgePiRPC_TC.ConvModeH\x00\x12:\n\x11open_circuit_mode\x18\x03 \x01(\x0e\x32\x1d.EdgePiRPC_TC.OpenCircuitModeH\x00\x12\x32\n\x12\x63old_junction_mode\x18\x04 \x01(\x0e\x32\x14.EdgePiRPC_TC.CJModeH\x00\x12-\n\nfault_mode\x18\x05 \x01(\x0e\x32\x17.EdgePiRPC_TC.FaultModeH\x00\x12:\n\x11noise_filter_mode\x18\x06 \x01(\x0e\x32\x1d.EdgePiRPC_TC.NoiseFilterModeH\x00\x12-\n\x0c\x61verage_mode\x18\x07 \x01(\x0e\x32\x15.EdgePiRPC_TC.AvgModeH\x00\x12\'\n\x07tc_type\x18\x08 \x01(\x0e\x32\x14.EdgePiRPC_TC.TCTypeH\x00\x12\x31\n\x0cvoltage_mode\x18\t \x01(\x0e\x32\x19.EdgePiRPC_TC.VoltageModeH\x00\x12\x30\n\x0c\x63j_high_mask\x18\n \x01(\x0e\x32\x18.EdgePiRPC_TC.CJHighMaskH\x00\x12.\n\x0b\x63j_low_mask\x18\x0b \x01(\x0e\x32\x17.EdgePiRPC_TC.CJLowMaskH\x00\x12\x30\n\x0ctc_high_mask\x18\x0c \x01(\x0e\x32\x18.EdgePiRPC_TC.TCHighMaskH\x00\x12.\n\x0btc_low_mask\x18\r \x01(\x0e\x32\x17.EdgePiRPC_TC.TCLowMaskH\x00\x12+\n\tovuv_mask\x18\x0e \x01(\x0e\x32\x16.EdgePiRPC_TC.OvuvMaskH\x00\x12+\n\topen_mask\x18\x0f \x01(\x0e\x32\x16.EdgePiRPC_TC.OpenMaskH\x00\x12\x1b\n\x11\x63j_high_threshold\x18\x10 \x01(\x05H\x00\x12\x1a\n\x10\x63j_low_threshold\x18\x11 \x01(\x05H\x00\x12\x1b\n\x11lt_high_threshold\x18\x12 \x01(\x05H\x00\x12<\n\x1alt_high_threshold_decimals\x18\x13 \x01(\x0e\x32\x16.EdgePiRPC_TC.DecBits4H\x00\x12\x1a\n\x10lt_low_threshold\x18\x14 \x01(\x05H\x00\x12;\n\x19lt_low_threshold_decimals\x18\x15 \x01(\x0e\x32\x16.EdgePiRPC_TC.DecBits4H\x00\x12\x13\n\tcj_offset\x18\x16 \x01(\x05H\x00\x12\x34\n\x12\x63j_offset_decimals\x18\x17 \x01(\x0e\x32\x16.EdgePiRPC_TC.DecBits4H\x00\x12\x11\n\x07\x63j_temp\x18\x18 \x01(\x05H\x00\x12\x32\n\x10\x63j_temp_decimals\x18\x19 \x01(\x0e\x32\x16.EdgePiRPC_TC.DecBits6H\x00\x42\x06\n\x04\x65num* \n\x08\x43onvMode\x12\n\n\x06SINGLE\x10\x00\x12\x08\n\x04\x41UTO\x10\x01*k\n\x0fOpenCircuitMode\x12\x0c\n\x08\x44ISABLED\x10\x00\x12\x17\n\x13LOW_INPUT_IMPEDANCE\x10\x01\x12\x17\n\x13MED_INPUT_IMPEDANCE\x10\x02\x12\x18\n\x14HIGH_INPUT_IMPEDANCE\x10\x03*!\n\x06\x43JMode\x12\n\n\x06\x45NABLE\x10\x00\x12\x0b\n\x07\x44ISABLE\x10\x01**\n\tFaultMode\x12\x0e\n\nCOMPARATOR\x10\x00\x12\r\n\tINTERRUPT\x10\x01*\'\n\x0fNoiseFilterMode\x12\t\n\x05HZ_60\x10\x00\x12\t\n\x05HZ_50\x10\x01*A\n\x07\x41vgMode\x12\t\n\x05\x41VG_1\x10\x00\x12\t\n\x05\x41VG_2\x10\x01\x12\t\n\x05\x41VG_4\x10\x02\x12\t\n\x05\x41VG_8\x10\x03\x12\n\n\x06\x41VG_16\x10\x04*h\n\x06TCType\x12\n\n\x06TYPE_B\x10\x00\x12\n\n\x06TYPE_E\x10\x01\x12\n\n\x06TYPE_J\x10\x02\x12\n\n\x06TYPE_K\x10\x03\x12\n\n\x06TYPE_N\x10\x04\x12\n\n\x06TYPE_R\x10\x05\x12\n\n\x06TYPE_S\x10\x06\x12\n\n\x06TYPE_T\x10\x07*&\n\x0bVoltageMode\x12\n\n\x06GAIN_8\x10\x00\x12\x0b\n\x07GAIN_32\x10\x01*5\n\nCJHighMask\x12\x12\n\x0e\x43JHIGH_MASK_ON\x10\x00\x12\x13\n\x0f\x43JHIGH_MASK_OFF\x10\x01*2\n\tCJLowMask\x12\x11\n\rCJLOW_MASK_ON\x10\x00\x12\x12\n\x0e\x43JLOW_MASK_OFF\x10\x01*5\n\nTCHighMask\x12\x12\n\x0eTCHIGH_MASK_ON\x10\x00\x12\x13\n\x0fTCHIGH_MASK_OFF\x10\x01*2\n\tTCLowMask\x12\x11\n\rTCLOW_MASK_ON\x10\x00\x12\x12\n\x0eTCLOW_MASK_OFF\x10\x01*/\n\x08OvuvMask\x12\x10\n\x0cOVUV_MASK_ON\x10\x00\x12\x11\n\rOVUV_MASK_OFF\x10\x01*/\n\x08OpenMask\x12\x10\n\x0cOPEN_MASK_ON\x10\x00\x12\x11\n\rOPEN_MASK_OFF\x10\x01*\xca\x01\n\x08\x44\x65\x63\x42its4\x12\x06\n\x02P0\x10\x00\x12\x08\n\x04P0_5\x10\x01\x12\t\n\x05P0_75\x10\x02\x12\n\n\x06P0_875\x10\x03\x12\x0b\n\x07P0_9375\x10\x04\x12\x0b\n\x07P0_4375\x10\x05\x12\x0b\n\x07P0_1875\x10\x06\x12\x0b\n\x07P0_0625\x10\x07\x12\x0b\n\x07P0_5625\x10\x08\x12\x0b\n\x07P0_8125\x10\t\x12\x0b\n\x07P0_6875\x10\n\x12\t\n\x05P0_25\x10\x0b\x12\n\n\x06P0_125\x10\x0c\x12\n\n\x06P0_625\x10\r\x12\x0b\n\x07P0_3125\x10\x0e\x12\n\n\x06P0_375\x10\x0f*\x9a\x07\n\x08\x44\x65\x63\x42its6\x12\x07\n\x03P0_\x10\x00\x12\r\n\tP0_015625\x10\x01\x12\x0c\n\x08P0_03125\x10\x02\x12\r\n\tP0_046875\x10\x03\x12\x0c\n\x08P0_0625_\x10\x04\x12\r\n\tP0_078125\x10\x05\x12\x0c\n\x08P0_09375\x10\x06\x12\r\n\tP0_109375\x10\x07\x12\x0b\n\x07P0_125_\x10\x08\x12\r\n\tP0_140625\x10\t\x12\x0c\n\x08P0_15625\x10\n\x12\r\n\tP0_171875\x10\x0b\x12\x0c\n\x08P0_1875_\x10\x0c\x12\r\n\tP0_203125\x10\r\x12\x0c\n\x08P0_21875\x10\x0e\x12\r\n\tP0_234375\x10\x0f\x12\n\n\x06P0_25_\x10\x10\x12\r\n\tP0_265625\x10\x11\x12\x0c\n\x08P0_28125\x10\x12\x12\r\n\tP0_296875\x10\x13\x12\x0c\n\x08P0_3125_\x10\x14\x12\r\n\tP0_328125\x10\x15\x12\x0c\n\x08P0_34375\x10\x16\x12\r\n\tP0_359375\x10\x17\x12\x0b\n\x07P0_375_\x10\x18\x12\r\n\tP0_390625\x10\x19\x12\x0c\n\x08P0_40625\x10\x1a\x12\r\n\tP0_421875\x10\x1b\x12\x0c\n\x08P0_4375_\x10\x1c\x12\r\n\tP0_453125\x10\x1d\x12\x0c\n\x08P0_46875\x10\x1e\x12\r\n\tP0_484375\x10\x1f\x12\t\n\x05P0_5_\x10 \x12\r\n\tP0_515625\x10!\x12\x0c\n\x08P0_53125\x10\"\x12\r\n\tP0_546875\x10#\x12\x0c\n\x08P0_5625_\x10$\x12\r\n\tP0_578125\x10%\x12\x0c\n\x08P0_59375\x10&\x12\r\n\tP0_609375\x10\'\x12\x0b\n\x07P0_625_\x10(\x12\r\n\tP0_640625\x10)\x12\x0c\n\x08P0_65625\x10*\x12\r\n\tP0_671875\x10+\x12\x0c\n\x08P0_6875_\x10,\x12\r\n\tP0_703125\x10-\x12\x0c\n\x08P0_71875\x10.\x12\r\n\tP0_734375\x10/\x12\n\n\x06P0_75_\x10\x30\x12\r\n\tP0_765625\x10\x31\x12\x0c\n\x08P0_78125\x10\x32\x12\r\n\tP0_796875\x10\x33\x12\x0c\n\x08P0_8125_\x10\x34\x12\r\n\tP0_828125\x10\x35\x12\x0c\n\x08P0_84375\x10\x36\x12\r\n\tP0_859375\x10\x37\x12\x0b\n\x07P0_875_\x10\x38\x12\r\n\tP0_890625\x10\x39\x12\x0c\n\x08P0_90625\x10:\x12\r\n\tP0_921875\x10;\x12\x0c\n\x08P0_9375_\x10<\x12\r\n\tP0_953125\x10=\x12\x0c\n\x08P0_96875\x10>\x12\r\n\tP0_984375\x10?2\xed\x03\n\tTcService\x12<\n\nset_config\x12\x14.EdgePiRPC_TC.Config\x1a\x18.EdgePiRPC_TC.SuccessMsg\x12\x42\n\rsingle_sample\x12\x16.EdgePiRPC_TC.EmptyMsg\x1a\x19.EdgePiRPC_TC.TempReading\x12\x46\n\x11read_temperatures\x12\x16.EdgePiRPC_TC.EmptyMsg\x1a\x19.EdgePiRPC_TC.TempReading\x12@\n\x0c\x63lear_faults\x12\x16.EdgePiRPC_TC.EmptyMsg\x1a\x18.EdgePiRPC_TC.SuccessMsg\x12?\n\x0bread_faults\x12\x1a.EdgePiRPC_TC.FilterFaults\x1a\x14.EdgePiRPC_TC.Faults\x12\x43\n\x0freset_registers\x12\x16.EdgePiRPC_TC.EmptyMsg\x1a\x18.EdgePiRPC_TC.SuccessMsg\x12N\n\x1coverwrite_cold_junction_temp\x12\x14.EdgePiRPC_TC.CJtemp\x1a\x18.EdgePiRPC_TC.SuccessMsgB\x03\x90\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rpc_module.protos.tc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\220\001\001'
  _globals['_CONVMODE']._serialized_start=1669
  _globals['_CONVMODE']._serialized_end=1701
  _globals['_OPENCIRCUITMODE']._serialized_start=1703
  _globals['_OPENCIRCUITMODE']._serialized_end=1810
  _globals['_CJMODE']._serialized_start=1812
  _globals['_CJMODE']._serialized_end=1845
  _globals['_FAULTMODE']._serialized_start=1847
  _globals['_FAULTMODE']._serialized_end=1889
  _globals['_NOISEFILTERMODE']._serialized_start=1891
  _globals['_NOISEFILTERMODE']._serialized_end=1930
  _globals['_AVGMODE']._serialized_start=1932
  _globals['_AVGMODE']._serialized_end=1997
  _globals['_TCTYPE']._serialized_start=1999
  _globals['_TCTYPE']._serialized_end=2103
  _globals['_VOLTAGEMODE']._serialized_start=2105
  _globals['_VOLTAGEMODE']._serialized_end=2143
  _globals['_CJHIGHMASK']._serialized_start=2145
  _globals['_CJHIGHMASK']._serialized_end=2198
  _globals['_CJLOWMASK']._serialized_start=2200
  _globals['_CJLOWMASK']._serialized_end=2250
  _globals['_TCHIGHMASK']._serialized_start=2252
  _globals['_TCHIGHMASK']._serialized_end=2305
  _globals['_TCLOWMASK']._serialized_start=2307
  _globals['_TCLOWMASK']._serialized_end=2357
  _globals['_OVUVMASK']._serialized_start=2359
  _globals['_OVUVMASK']._serialized_end=2406
  _globals['_OPENMASK']._serialized_start=2408
  _globals['_OPENMASK']._serialized_end=2455
  _globals['_DECBITS4']._serialized_start=2458
  _globals['_DECBITS4']._serialized_end=2660
  _globals['_DECBITS6']._serialized_start=2663
  _globals['_DECBITS6']._serialized_end=3585
  _globals['_EMPTYMSG']._serialized_start=44
  _globals['_EMPTYMSG']._serialized_end=54
  _globals['_SUCCESSMSG']._serialized_start=56
  _globals['_SUCCESSMSG']._serialized_end=102
  _globals['_TEMPREADING']._serialized_start=104
  _globals['_TEMPREADING']._serialized_end=187
  _globals['_CJTEMP']._serialized_start=189
  _globals['_CJTEMP']._serialized_end=307
  _globals['_FILTERFAULTS']._serialized_start=309
  _globals['_FILTERFAULTS']._serialized_end=373
  _globals['_FAULTS']._serialized_start=376
  _globals['_FAULTS']._serialized_end=510
  _globals['_FAULTS_FAULT']._serialized_start=429
  _globals['_FAULTS_FAULT']._serialized_end=510
  _globals['_CONFIG']._serialized_start=513
  _globals['_CONFIG']._serialized_end=1667
  _globals['_CONFIG_CONFARG']._serialized_start=572
  _globals['_CONFIG_CONFARG']._serialized_end=1667
  _globals['_TCSERVICE']._serialized_start=3588
  _globals['_TCSERVICE']._serialized_end=4081
_builder.BuildServices(DESCRIPTOR, 'rpc_module.protos.tc_pb2', _globals)
# @@protoc_insertion_point(module_scope)
