from pydantic import BaseModel

class heartuser(BaseModel):
    age: int
    sex: int
    cp: int
    trtbps: int
    chol: int
    fbs: int
    restecg: int
    thalachh: int
    exng: int
    oldpeak: float
    slp: int
    caa: int
    thal: int