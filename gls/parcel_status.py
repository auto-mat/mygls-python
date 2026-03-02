import datetime

from pydantic.dataclasses import dataclass


@dataclass
class ParcelStatus:
    DepotCity: str
    DepotNumber: str
    StatusCode: str
    StatusDate: str
    StatusDescription: str
    StatusInfo: str
