
import collections
import time
from concurrent import futures

import grpc

import dynamic_ks_pb2
import dynamic_ks_pb2_grpc


class DKeystoreServer(dynamic_ks_pb2_grpc.DynamicKSServicer):

    def __init__(self):
        self.ks = collections.defaultdict()

    def setKey(self, request, context):
        print('/set', request)
        self.ks[request.key] = request.value
        print(self.ks)
        return dynamic_ks_pb2.response(status=True)
    
    def getKey(self, request, context):
        print('/get', request)
        return dynamic_ks_pb2.value(value=self.ks.get(request.key))
        

def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dynamic_ks_pb2_grpc.add_DynamicKSServicer_to_server(DKeystoreServer(), server)

    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':

    serve()
