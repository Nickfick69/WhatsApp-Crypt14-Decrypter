"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import C14_cipher_version_pb2 as C14__cipher__version__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10C14_cipher.proto\x1a\x18C14_cipher_version.proto"U\n\nC14_cipher\x12\x13\n\x0bkey_version\x18\x02 \x01(\x0c\x12\x13\n\x0bserver_salt\x18\x03 \x01(\x0c\x12\x11\n\tgoogle_id\x18\x04 \x01(\x0c\x12\n\n\x02IV\x18\x05 \x01(\x0cb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'C14_cipher_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_C14_CIPHER']._serialized_start = 46
    _globals['_C14_CIPHER']._serialized_end = 131