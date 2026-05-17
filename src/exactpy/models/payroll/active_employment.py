from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    GUID,
    ContractTypeEnum,
    ExactUnixTimestamp,
)
from exactpy.utils.fields import GenericField


class ActiveEmploymentModel(ExactOnlineBaseModel):
    _pk = "id"
    id: GUID = GenericField(iceberg_type="string", spark_type="string")
    average_days_per_week: float | None = GenericField(
        iceberg_type="double", spark_type="double", default=None
    )
    average_hours_per_week: float | None = GenericField(
        iceberg_type="double", spark_type="double", default=None
    )
    contract: GUID = GenericField(iceberg_type="string", spark_type="string")
    contract_document: GUID = GenericField(iceberg_type="string", spark_type="string")
    contract_end_date: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    contract_probation_end_date: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    contract_probation_period: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    contract_start_date: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    contract_type: ContractTypeEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    contract_type_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    created: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    creator: GUID = GenericField(iceberg_type="string", spark_type="string")
    creator_full_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    department: GUID = GenericField(iceberg_type="string", spark_type="string")
    department_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    department_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    division: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    employee: GUID = GenericField(iceberg_type="string", spark_type="string")
    employee_full_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    employee__hid: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    employment_organization: GUID = GenericField(
        iceberg_type="string", spark_type="string"
    )
    end_date: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    HID: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    hourly_wage: float | None = GenericField(
        iceberg_type="double", spark_type="double", default=None
    )
    internal_rate: float | None = GenericField(
        iceberg_type="double", spark_type="double", default=None
    )
    jobtitle: GUID = GenericField(iceberg_type="string", spark_type="string")
    jobtitle_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    modified: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    modifier: GUID = GenericField(iceberg_type="string", spark_type="string")
    modifier_full_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    reason_end: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    reason_end_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    reason_end_flex: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    reason_end_flex_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    salary: GUID = GenericField(iceberg_type="string", spark_type="string")
    schedule: GUID = GenericField(iceberg_type="string", spark_type="string")
    schedule_average_hours: float | None = GenericField(
        iceberg_type="double", spark_type="double", default=None
    )
    schedule_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    schedule_days: float | None = GenericField(
        iceberg_type="double", spark_type="double", default=None
    )
    schedule_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    schedule_hours: float | None = GenericField(
        iceberg_type="double", spark_type="double", default=None
    )
    start_date: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    start_date_organization: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
