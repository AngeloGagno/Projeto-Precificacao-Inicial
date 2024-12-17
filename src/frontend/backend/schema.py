from pydantic import BaseModel, PositiveInt,StringConstraints,PositiveFloat
from typing_extensions import Annotated

class Acc_Price(BaseModel):
    name: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,  
            to_upper=True,       
            min_length=1,       
        ),
    ]
    price: PositiveFloat
    tier: PositiveInt
    min_price: PositiveFloat
    base_price: PositiveFloat

