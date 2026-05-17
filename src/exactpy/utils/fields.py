from typing import Type

from icedantic.model import IcebergField
from pydantic import Field
from sparkdantic.model import SparkField

_FIELD_MAPPING = {
    "iceberg": (IcebergField, "iceberg_type"),
    "spark": (SparkField, "spark_type"),
}


def GenericField(
    *args,
    iceberg_type: str,
    spark_type: str,
    **kwargs,
) -> Type[Field]:
    iceberg_field = IcebergField(*args, iceberg_type=iceberg_type, **kwargs)

    if spark_type is not None:
        kwargs["spark_type"] = spark_type

    kwargs["json_schema_extra"] = iceberg_field.json_schema_extra

    return Field(
        *args,
        **kwargs,
    )
