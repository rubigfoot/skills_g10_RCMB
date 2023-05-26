from pydantic import BaseModel
from typing import List

class IrisSchema(BaseModel):

    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    class Config:
        schema_extra = {
            "example":{
                "sepal_length": 3,
                "sepal_width": 4,
                "petal_length": 5,
                "petal_width": 10
            }
        }


    data:List[List[float]]

