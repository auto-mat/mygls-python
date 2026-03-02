from pydantic.dataclasses import dataclass


@dataclass
class ParcelProperty:
    PackageType: int
    Height: int
    Length: int
    Width: int
    Weight: float
