import datetime

from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class ParcelStatus:
    DepotCity: Optional[str]
    DepotNumber: Optional[str]
    StatusCode: str
    StatusDate: str
    StatusDescription: str
    StatusInfo: str
