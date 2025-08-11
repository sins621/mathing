from base import AutoField, BaseModel, TextField


class PracticeRegime(BaseModel):
    id = AutoField()
    regime_name = TextField()
