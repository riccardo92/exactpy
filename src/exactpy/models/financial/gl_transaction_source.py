from exactpy.models.base import ExactOnlineBaseModel


class GLTransactionSource(ExactOnlineBaseModel):
    id: int | None = None
    description: str | None = None
    description_suffix: str | None = None
