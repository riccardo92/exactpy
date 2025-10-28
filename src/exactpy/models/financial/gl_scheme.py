from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    GUID,
    ExactUnixTimestamp,
)


class GLSchemeModel(ExactOnlineBaseModel):
    _pk = "id"
    id: GUID
    code: str | None = None
    created: ExactUnixTimestamp
    creator: GUID
    creator_full_name: str | None = None
    description: str | None = None
    division: int | None = None
    main: int | None = None
    modified: ExactUnixTimestamp
    modifier: GUID
    modifier_full_name: str | None = None
    target_namespace: str | None = None
