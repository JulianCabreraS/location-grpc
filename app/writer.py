import grpc
import location_pb2
import location_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
import datetime


# Writer for the gRPC
channel = grpc.insecure_channel("127.0.0.1:5006", options=(('grpc.enable_http_proxy', 0),))
stub = location_pb2_grpc.LocationServiceStub(channel)


timestamp = Timestamp()
now = datetime.datetime.now()
timestamp.FromDatetime(now)

location_req = location_pb2.LocationMessage(
    person_id=10,
    longitude=-79.52,
    latitude=36.78,
    creation_time=timestamp
)

response = stub.create(location_req)
print("response after callling stub.Create ...", response)
