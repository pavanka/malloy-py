# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/v1/compiler.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aservices/v1/compiler.proto\x12\x12malloy.services.v1\"\xa6\x04\n\x0e\x43ompileRequest\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\'.malloy.services.v1.CompileRequest.Type\x12\x35\n\x04mode\x18\x02 \x01(\x0e\x32\'.malloy.services.v1.CompileRequest.Mode\x12\x35\n\x08\x64ocument\x18\x03 \x01(\x0b\x32#.malloy.services.v1.CompileDocument\x12\x37\n\nreferences\x18\x04 \x03(\x0b\x32#.malloy.services.v1.CompileDocument\x12\x0e\n\x06schema\x18\x05 \x01(\t\x12=\n\x11sql_block_schemas\x18\x06 \x03(\x0b\x32\".malloy.services.v1.SqlBlockSchema\x12\r\n\x05query\x18\x07 \x01(\t\x12\x13\n\x0bnamed_query\x18\x08 \x01(\t\x12\x35\n\x0cquery_result\x18\t \x01(\x0b\x32\x1f.malloy.services.v1.QueryResult\"Z\n\x04Type\x12\x0b\n\x07\x43OMPILE\x10\x00\x12\x0e\n\nREFERENCES\x10\x01\x12\x11\n\rTABLE_SCHEMAS\x10\x02\x12\x15\n\x11SQL_BLOCK_SCHEMAS\x10\x03\x12\x0b\n\x07RESULTS\x10\x04\"0\n\x04Mode\x12\x16\n\x12\x43OMPILE_AND_RENDER\x10\x00\x12\x10\n\x0c\x43OMPILE_ONLY\x10\x01\"/\n\x0bQueryResult\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\x12\n\ntotal_rows\x18\x02 \x01(\x05\"-\n\x0f\x43ompileResponse\x12\r\n\x05model\x18\x01 \x01(\t\x12\x0b\n\x03sql\x18\x02 \x01(\t\"/\n\x0f\x43ompileDocument\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"=\n\x0bTableSchema\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\nconnection\x18\x02 \x01(\t\x12\r\n\x05table\x18\x03 \x01(\t\"\xf1\x02\n\x0f\x43ompilerRequest\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32(.malloy.services.v1.CompilerRequest.Type\x12\x13\n\x0bimport_urls\x18\x02 \x03(\t\x12\x36\n\rtable_schemas\x18\x03 \x03(\x0b\x32\x1f.malloy.services.v1.TableSchema\x12/\n\tsql_block\x18\x04 \x01(\x0b\x32\x1c.malloy.services.v1.SqlBlock\x12\x12\n\nconnection\x18\x05 \x01(\t\x12\x16\n\x0erender_content\x18\x06 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x63 \x01(\t\"k\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06IMPORT\x10\x01\x12\x11\n\rTABLE_SCHEMAS\x10\x02\x12\x15\n\x11SQL_BLOCK_SCHEMAS\x10\x03\x12\x0c\n\x08\x43OMPLETE\x10\x04\x12\t\n\x05\x45RROR\x10\x05\x12\x07\n\x03RUN\x10\x06\"9\n\x08SqlBlock\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03sql\x18\x02 \x01(\t\x12\x12\n\nconnection\x18\x03 \x01(\t\";\n\x0eSqlBlockSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03sql\x18\x02 \x01(\t\x12\x0e\n\x06schema\x18\x03 \x01(\t2\xc0\x01\n\x08\x43ompiler\x12T\n\x07\x43ompile\x12\".malloy.services.v1.CompileRequest\x1a#.malloy.services.v1.CompileResponse\"\x00\x12^\n\rCompileStream\x12\".malloy.services.v1.CompileRequest\x1a#.malloy.services.v1.CompilerRequest\"\x00(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.v1.compiler_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPILEREQUEST._serialized_start=51
  _COMPILEREQUEST._serialized_end=601
  _COMPILEREQUEST_TYPE._serialized_start=461
  _COMPILEREQUEST_TYPE._serialized_end=551
  _COMPILEREQUEST_MODE._serialized_start=553
  _COMPILEREQUEST_MODE._serialized_end=601
  _QUERYRESULT._serialized_start=603
  _QUERYRESULT._serialized_end=650
  _COMPILERESPONSE._serialized_start=652
  _COMPILERESPONSE._serialized_end=697
  _COMPILEDOCUMENT._serialized_start=699
  _COMPILEDOCUMENT._serialized_end=746
  _TABLESCHEMA._serialized_start=748
  _TABLESCHEMA._serialized_end=809
  _COMPILERREQUEST._serialized_start=812
  _COMPILERREQUEST._serialized_end=1181
  _COMPILERREQUEST_TYPE._serialized_start=1074
  _COMPILERREQUEST_TYPE._serialized_end=1181
  _SQLBLOCK._serialized_start=1183
  _SQLBLOCK._serialized_end=1240
  _SQLBLOCKSCHEMA._serialized_start=1242
  _SQLBLOCKSCHEMA._serialized_end=1301
  _COMPILER._serialized_start=1304
  _COMPILER._serialized_end=1496
# @@protoc_insertion_point(module_scope)
