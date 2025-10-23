from exactpy.models import ExactOnlineBaseModel


class Me(ExactOnlineBaseModel):
    user_id: str | None = None
    accounting_division: int | None = None
    current_division: int | None = None
    customer_code: str | None = None
    division_customer: str | None = None
    division_customer_code: str | None = None
    division_customer_name: str | None = None
    division_customer_siret_number: str | None = None
    division_customer_vat_number: str | None = None
    dossier_division: int | None = None
    email: str | None = None
    employee_id: str | None = None
    first_name: str | None = None
    full_name: str | None = None
    gender: str | None = None
    initials: str | None = None
    is_client_use: bool = False
    is_employee_self_service_user: bool = False
    is_my_firm_lite_user: bool = False
    is_my_firm_portal_user: bool = False
    is_oei_migration_mandatory: bool = False
    is_starter_user: bool = False
    language: str | None = None
    language_code: str | None = None
    last_name: str | None = None
    legislation: int | None = None
    middle_name: str | None = None
    mobile: str | None = None
    nationality: str | None = None
    package_code: str | None = None
    phone: str | None = None
    phone_extension: str | None = None
    picture_url: str | None = None
    server_time: str | None = None
    server_utc_offset: float | None = None
    thumbnail_picture: bytes | None = None
    thumbnail_picture_format: str | None = None
    title: str | None = None
    user_name: str | None = None


print(Me.model_config)
