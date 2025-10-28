from pydantic import AliasGenerator, BaseModel, ConfigDict

from exactpy.alias_generators import special_snake_to_pascal


class ExactOnlineBaseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(alias=special_snake_to_pascal),
        validate_by_alias=True,
        use_enum_values=True,
    )

    # Indicates what field is used as primary key
    _pk: str | None = None
