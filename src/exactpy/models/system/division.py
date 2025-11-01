from sparkdantic import SparkField

from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    GUID,
    BlockingStatusEnum,
    DivisionStatusEnum,
    ExactUnixTimestamp,
)


class DivisionModel(ExactOnlineBaseModel):
    _pk = "code"
    code: int
    address_line1: str | None = None
    address_line2: str | None = None
    address_line3: str | None = None
    archive_date: ExactUnixTimestamp = SparkField(spark_type="timestamp")
    blocking_status: BlockingStatusEnum
    business_type_code: str | None = None
    business_type_description: str | None = None
    chamber_of_commerce_establishment: str | None = None
    chamber_of_commerce_number: str | None = None
    city: str | None = None
    # TODO
    # class_01
    # class_02
    # class_03
    # class_04
    # class_05
    company_size_code: str | None = None
    company_size_description: str | None = None
    country: str | None = None
    created: ExactUnixTimestamp = SparkField(spark_type="timestamp")
    creator: GUID
    creator_full_name: str | None = None
    currency: str | None = None
    current: bool | None = None
    customer: GUID
    customer_code: str | None = None
    customer_name: str | None = None
    datev_accountant_number: str | None = None
    datev_client_number: str | None = None
    description: str | None = None
    division_hr__link_unlink_date: ExactUnixTimestamp = SparkField(
        spark_type="timestamp"
    )
    division_move_date: ExactUnixTimestamp = SparkField(spark_type="timestamp")
    email: str | None = None
    fax: str | None = None
    hid: int | None = SparkField(spark_type="long", default=None)
    is_dossier_division: bool | None = None
    is_hr__division: bool | None = None
    is_main_division: bool | None = None
    is_practice_division: bool | None = None
    legislation: str | None = None
    modified: ExactUnixTimestamp = SparkField(spark_type="timestamp")
    modifier: GUID
    modifier_full_name: str | None = None
    ob__number: str | None = None
    phone: str | None = None
    postcode: str | None = None
    sbi_code: str | None = None
    sbi_description: str | None = None
    sector_code: str | None = None
    sector_description: str | None = None
    share_capital: float | None = None
    siret_number: str | None = None
    start_date: ExactUnixTimestamp = SparkField(spark_type="timestamp")
    state: str | None = None
    status: DivisionStatusEnum
    subsector_code: str | None = None
    subsector_description: str | None = None
    tax_office_number: str | None = None
    tax_reference_number: str | None = None
    template_code: str | None = None
    vat__number: str | None = None
    website: str | None = None
