import grpc

import dynamic_ks_pb2
import dynamic_ks_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')

stub = dynamic_ks_pb2_grpc.DynamicKSStub(channel)

request = dynamic_ks_pb2.request(key='foo', value='bar')
response = stub.setKey(request)
print(response)

key_request = dynamic_ks_pb2.key(key='foo')
response = stub.getKey(key_request)
print(response)

key_request = dynamic_ks_pb2.key(key='fooX')
response = stub.getKey(key_request)
print(response)