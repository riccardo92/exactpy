from exactpy.models.base import ExactOnlineBaseModel


class GLTransactionType(ExactOnlineBaseModel):
    id: int | None = None
    description: str | None = None
    description_suffix: str | None = None
