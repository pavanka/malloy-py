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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aservices/v1/compiler.proto\x12\x12malloy.services.v1\"\xf9\x02\n\x0e\x43ompileRequest\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\'.malloy.services.v1.CompileRequest.Type\x12\x35\n\x08\x64ocument\x18\x02 \x01(\x0b\x32#.malloy.services.v1.CompileDocument\x12\x37\n\nreferences\x18\x03 \x03(\x0b\x32#.malloy.services.v1.CompileDocument\x12\x0e\n\x06schema\x18\x04 \x01(\t\x12=\n\x11sql_block_schemas\x18\x05 \x03(\x0b\x32\".malloy.services.v1.SqlBlockSchema\x12\r\n\x05query\x18\x06 \x01(\t\x12\x13\n\x0bnamed_query\x18\x07 \x01(\t\"M\n\x04Type\x12\x0b\n\x07\x43OMPILE\x10\x00\x12\x0e\n\nREFERENCES\x10\x01\x12\x11\n\rTABLE_SCHEMAS\x10\x02\x12\x15\n\x11SQL_BLOCK_SCHEMAS\x10\x03\"-\n\x0f\x43ompileResponse\x12\r\n\x05model\x18\x01 \x01(\t\x12\x0b\n\x03sql\x18\x02 \x01(\t\"/\n\x0f\x43ompileDocument\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"=\n\x0bTableSchema\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\nconnection\x18\x02 \x01(\t\x12\r\n\x05table\x18\x03 \x01(\t\"\xd0\x02\n\x0f\x43ompilerRequest\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32(.malloy.services.v1.CompilerRequest.Type\x12\x13\n\x0bimport_urls\x18\x02 \x03(\t\x12\x36\n\rtable_schemas\x18\x03 \x03(\x0b\x32\x1f.malloy.services.v1.TableSchema\x12/\n\tsql_block\x18\x04 \x01(\x0b\x32\x1c.malloy.services.v1.SqlBlock\x12\x12\n\nconnection\x18\x05 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x63 \x01(\t\"b\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06IMPORT\x10\x01\x12\x11\n\rTABLE_SCHEMAS\x10\x02\x12\x15\n\x11SQL_BLOCK_SCHEMAS\x10\x03\x12\x0c\n\x08\x43OMPLETE\x10\x04\x12\t\n\x05\x45RROR\x10\x05\"9\n\x08SqlBlock\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03sql\x18\x02 \x01(\t\x12\x12\n\nconnection\x18\x03 \x01(\t\";\n\x0eSqlBlockSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03sql\x18\x02 \x01(\t\x12\x0e\n\x06schema\x18\x03 \x01(\t2\xc0\x01\n\x08\x43ompiler\x12T\n\x07\x43ompile\x12\".malloy.services.v1.CompileRequest\x1a#.malloy.services.v1.CompileResponse\"\x00\x12^\n\rCompileStream\x12\".malloy.services.v1.CompileRequest\x1a#.malloy.services.v1.CompilerRequest\"\x00(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.v1.compiler_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPILEREQUEST._serialized_start=51
  _COMPILEREQUEST._serialized_end=428
  _COMPILEREQUEST_TYPE._serialized_start=351
  _COMPILEREQUEST_TYPE._serialized_end=428
  _COMPILERESPONSE._serialized_start=430
  _COMPILERESPONSE._serialized_end=475
  _COMPILEDOCUMENT._serialized_start=477
  _COMPILEDOCUMENT._serialized_end=524
  _TABLESCHEMA._serialized_start=526
  _TABLESCHEMA._serialized_end=587
  _COMPILERREQUEST._serialized_start=590
  _COMPILERREQUEST._serialized_end=926
  _COMPILERREQUEST_TYPE._serialized_start=828
  _COMPILERREQUEST_TYPE._serialized_end=926
  _SQLBLOCK._serialized_start=928
  _SQLBLOCK._serialized_end=985
  _SQLBLOCKSCHEMA._serialized_start=987
  _SQLBLOCKSCHEMA._serialized_end=1046
  _COMPILER._serialized_start=1049
  _COMPILER._serialized_end=1241
# @@protoc_insertion_point(module_scope)
