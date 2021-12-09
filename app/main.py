from concurrent import futures
import time
import grpc
import location_pb2
import location_pb2_grpc


class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Retrieve(self, request, context):

        locationmsg = location_pb2.LocationMessage(
            id=53,
            person_id=8,
            coordinate="010100000097FDBAD39D925EC0D00A0C59DDC64240",
            creation_time="2021-11-07 14:30:53.096698"
        )
        return locationmsg


server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)
server.add_insecure_port("[::]:5006")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
