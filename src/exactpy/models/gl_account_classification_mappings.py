from exactpy.models import ExactOnlineBaseModel
from exactpy.types import GUID


class GLAccountClassificationMappings(ExactOnlineBaseModel):
    id: GUID
    classification: GUID
    classification_code: str | None = None
    classification_description: str | None = None
    division: int | None = None
    gl__account: GUID
    gl__account_code: str | None = None
    gl__account_description: str | None = None
    gl__scheme_code: str | None = None
    gl__scheme_description: str | None = None
    gl__scheme_id: GUID
