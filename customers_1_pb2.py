# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: customers_1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63ustomers_1.proto\"\xa1\x03\n\x13\x43ustomers_1_Message\x12\x0b\n\x03_id\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\r\x12\x0c\n\x04guid\x18\x03 \x01(\t\x12\x10\n\x08isActive\x18\x04 \x01(\x08\x12\x0b\n\x03\x61ge\x18\x05 \x01(\r\x12\x10\n\x08\x65yeColor\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x0e\n\x06gender\x18\x08 \x01(\t\x12\x0f\n\x07\x63ompany\x18\t \x01(\t\x12\r\n\x05\x65mail\x18\n \x01(\t\x12\r\n\x05phone\x18\x0b \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x0c \x01(\t\x12\r\n\x05\x61\x62out\x18\r \x01(\t\x12\x12\n\nregistered\x18\x0e \x01(\t\x12\x10\n\x08latitude\x18\x0f \x01(\x02\x12\x11\n\tlongitude\x18\x10 \x01(\x02\x12\x0c\n\x04tags\x18\x11 \x03(\t\x12-\n\x07\x66riends\x18\x12 \x03(\x0b\x32\x1c.Customers_1_Message.Friends\x12\x10\n\x08greeting\x18\x13 \x01(\t\x12\x15\n\rfavoriteFruit\x18\x14 \x01(\t\x1a#\n\x07\x46riends\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t')



_CUSTOMERS_1_MESSAGE = DESCRIPTOR.message_types_by_name['Customers_1_Message']
_CUSTOMERS_1_MESSAGE_FRIENDS = _CUSTOMERS_1_MESSAGE.nested_types_by_name['Friends']
Customers_1_Message = _reflection.GeneratedProtocolMessageType('Customers_1_Message', (_message.Message,), {

  'Friends' : _reflection.GeneratedProtocolMessageType('Friends', (_message.Message,), {
    'DESCRIPTOR' : _CUSTOMERS_1_MESSAGE_FRIENDS,
    '__module__' : 'customers_1_pb2'
    # @@protoc_insertion_point(class_scope:Customers_1_Message.Friends)
    })
  ,
  'DESCRIPTOR' : _CUSTOMERS_1_MESSAGE,
  '__module__' : 'customers_1_pb2'
  # @@protoc_insertion_point(class_scope:Customers_1_Message)
  })
_sym_db.RegisterMessage(Customers_1_Message)
_sym_db.RegisterMessage(Customers_1_Message.Friends)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CUSTOMERS_1_MESSAGE._serialized_start=22
  _CUSTOMERS_1_MESSAGE._serialized_end=439
  _CUSTOMERS_1_MESSAGE_FRIENDS._serialized_start=404
  _CUSTOMERS_1_MESSAGE_FRIENDS._serialized_end=439
# @@protoc_insertion_point(module_scope)