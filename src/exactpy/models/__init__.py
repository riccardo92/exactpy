from pydantic import AliasGenerator, BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal


class ExactOnlineBaseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(serialization_alias=to_pascal)
    )
