import argparse
import grpc
import echoserver_pb2
import echoserver_pb2_grpc

parser = argparse.ArgumentParser()
parser.add_argument("message")
args = parser.parse_args()

channel = grpc.insecure_channel('localhost:50051')
stub = echoserver_pb2_grpc.EchoServerStub(channel)
response = stub.Echo(echoserver_pb2.EchoRequest(message=args.message))

print("EchoServer responded: %s" % response.message)
