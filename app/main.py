import time
from concurrent import futures
import grpc
import location_pb2
import location_pb2_grpc
import location_service
from datetime import datetime


class LocationServicer(location_pb2_grpc.LocationServiceServicer):

    def create(self, request, context):
        timestamp_dt = datetime.fromtimestamp(request.creation_time.seconds + request.creation_time.nanos / 1e9)
        timestamp_st = timestamp_dt.strftime('%Y-%m-%d %H:%M:%S.%f')

        request_value = {
            "person_id": request.person_id,
            "longitude": str(request.longitude),
            "latitude": str(request.latitude),
            "creation_time": timestamp_st
        }

        result_from_db = location_service.LocationService.create(request_value)

        print("result_from_db= ", result_from_db)

        return location_pb2.LocationMessageResponse(
            id=result_from_db.id,
            person_id=result_from_db.person_id,
            coordinate=str(result_from_db.coordinate),
            creation_time=result_from_db.creation_time)

    def retrieve(self, request, context):
        result_from_db = location_service.LocationService.retrieve(request.id)

        if result_from_db:
            return location_pb2.LocationMessageResponse(
                id=result_from_db.id,
                person_id=result_from_db.person_id,
                coordinate=str(result_from_db.coordinate),
                creation_time=result_from_db.creation_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            )


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
