from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    GUID,
    BlockingStatusEnum,
    DivisionStatusEnum,
    ExactUnixTimestamp,
)
from exactpy.utils.fields import GenericField


class DivisionModel(ExactOnlineBaseModel):
    _pk = "code"
    code: int
    address_line1: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    address_line2: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    address_line3: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    archive_date: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    blocking_status: BlockingStatusEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    business_type_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    business_type_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    chamber_of_commerce_establishment: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    chamber_of_commerce_number: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    city: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    # TODO
    # class_01
    # class_02
    # class_03
    # class_04
    # class_05
    company_size_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    company_size_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    country: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    created: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    creator: GUID = GenericField(iceberg_type="string", spark_type="string")
    creator_full_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    currency: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    current: bool | None = None
    customer: GUID = GenericField(iceberg_type="string", spark_type="string")
    customer_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    customer_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    datev_accountant_number: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    datev_client_number: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    division_hr__link_unlink_date: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    division_move_date: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    email: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    fax: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    hid: int | None = GenericField(iceberg_type="long", spark_type="long", default=None)
    is_dossier_division: bool | None = None
    is_hr__division: bool | None = None
    is_main_division: bool | None = None
    is_practice_division: bool | None = None
    legislation: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    modified: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    modifier: GUID = GenericField(iceberg_type="string", spark_type="string")
    modifier_full_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    ob__number: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    phone: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    postcode: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    sbi_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    sbi_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    sector_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    sector_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    share_capital: float | None = GenericField(
        iceberg_type="float", spark_type="float", default=None
    )
    siret_number: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    start_date: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    state: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    status: DivisionStatusEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    subsector_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    subsector_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    tax_office_number: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    tax_reference_number: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    template_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    vat__number: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    website: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
