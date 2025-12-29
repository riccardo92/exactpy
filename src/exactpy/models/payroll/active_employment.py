from sparkdantic import SparkField

from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    GUID,
    ContractTypeEnum,
    ExactUnixTimestamp,
)


class ActiveEmploymentModel(ExactOnlineBaseModel):
    _pk = "id"
    id: GUID = SparkField(spark_type="string")
    average_days_per_week: float | None = SparkField(spark_type="double", default=None)
    average_hours_per_week: float | None = SparkField(spark_type="double", default=None)
    contract: GUID = SparkField(spark_type="string")
    contract_document: GUID = SparkField(spark_type="string")
    contract_end_date: ExactUnixTimestamp = SparkField(spark_type="timestamp")
    contract_probation_end_date: ExactUnixTimestamp = SparkField(spark_type="timestamp")
    contract_probation_period: int | None = SparkField(
        spark_type="integer", default=None
    )
    contract_start_date: ExactUnixTimestamp = SparkField(spark_type="timestamp")
    contract_type: ContractTypeEnum | None = SparkField(
        spark_type="integer", default=None
    )
    contract_type_description: str | None = SparkField(
        spark_type="string", default=None
    )
    created: ExactUnixTimestamp = SparkField(spark_type="timestamp")
    creator: GUID = SparkField(spark_type="string")
    creator_full_name: str | None = SparkField(spark_type="string", default=None)
    department: GUID = SparkField(spark_type="string")
    department_code: str | None = SparkField(spark_type="string", default=None)
    department_description: str | None = SparkField(spark_type="string", default=None)
    division: int | None = SparkField(spark_type="integer", default=None)
    employee: GUID = SparkField(spark_type="string")
    employee_full_name: str | None = SparkField(spark_type="string", default=None)
    employee__hid: int | None = SparkField(spark_type="integer", default=None)
    employment_organization: GUID = SparkField(spark_type="string")
    end_date: ExactUnixTimestamp = SparkField(spark_type="timestamp")
    HID: int | None = SparkField(spark_type="integer", default=None)
    hourly_wage: float | None = SparkField(spark_type="double", default=None)
    internal_rate: float | None = SparkField(spark_type="double", default=None)
    jobtitle: GUID = SparkField(spark_type="string")
    jobtitle_description: str | None = SparkField(spark_type="string", default=None)
    modified: ExactUnixTimestamp = SparkField(spark_type="timestamp")
    modifier: GUID = SparkField(spark_type="string")
    modifier_full_name: str | None = SparkField(spark_type="string", default=None)
    reason_end: int | None = SparkField(spark_type="integer", default=None)
    reason_end_description: str | None = SparkField(spark_type="string", default=None)
    reason_end_flex: int | None = SparkField(spark_type="integer", default=None)
    reason_end_flex_description: str | None = SparkField(
        spark_type="string", default=None
    )
    salary: GUID = SparkField(spark_type="string")
    schedule: GUID = SparkField(spark_type="string")
    schedule_average_hours: float | None = SparkField(spark_type="double", default=None)
    schedule_code: str | None = SparkField(spark_type="string", default=None)
    schedule_days: float | None = SparkField(spark_type="double", default=None)
    schedule_description: str | None = SparkField(spark_type="string", default=None)
    schedule_hours: float | None = SparkField(spark_type="double", default=None)
    start_date: ExactUnixTimestamp = SparkField(spark_type="timestamp")
    start_date_organization: ExactUnixTimestamp = SparkField(spark_type="timestamp")
