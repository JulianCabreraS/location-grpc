import grpc
import location_pb2
import location_pb2_grpc


# Reader for the gRPC
channel = grpc.insecure_channel("127.0.0.1:30006", options=(('grpc.enable_http_proxy', 0),))
stub = location_pb2_grpc.LocationServiceStub(channel)

request = location_pb2.MessageRequest(id=51)
response = stub.retrieve(request)
print("Location retrieved: ...", response)
