import logging

from typing import Dict
from models import Location
from geoalchemy2.functions import ST_Point
from database import db

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("location_service")


class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        with db.Session() as dbs:
            attr = {"id": location_id}
            location = db.s.first(Location, **attr)
            db.s.flush()
            db.s.commit()
            dbs.close()
            return location

    @staticmethod
    def create(location: Dict):
        location_object = Location()
        location_object.person_id = location["person_id"]
        location_object.creation_time = location["creation_time"]
        location_object.coordinate = ST_Point(location["latitude"], location["longitude"])

        with db.Session() as dbs:
            db.s.add(location_object)
            db.s.flush()
            db.s.commit()
            dbs.close()
