from exactpy.models.base import ExactOnlineBaseModel


class GLTransactionTypeModel(ExactOnlineBaseModel):
    id: int | None = None
    description: str | None = None
    description_suffix: str | None = None
