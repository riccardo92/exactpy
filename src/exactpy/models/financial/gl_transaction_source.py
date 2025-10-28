from exactpy.models.base import ExactOnlineBaseModel


class GLTransactionSourceModel(ExactOnlineBaseModel):
    id: int | None = None
    description: str | None = None
    description_suffix: str | None = None
