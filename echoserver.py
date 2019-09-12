import echoserver_pb2
import echoserver_pb2_grpc
from concurrent import futures
import grpc
import time

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class EchoServer(echoserver_pb2_grpc.EchoServerServicer):

    def Echo(self, request, context):
        return echoserver_pb2.EchoResponse(message=request.message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    echoserver_pb2_grpc.add_EchoServerServicer_to_server(EchoServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
