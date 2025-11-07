# Changelog

## Unreleased

### Fix

- **auth.py**: added log statement to expiration check for easier debugging
- **auth.py**: removed default time() value for now arg in is_token_refresh_needed to fix expiration check bug

## 0.0.18 (2025-11-06)

### Fix

- bugfixes for inline count
- **controllers/base.py**: added inline_count arg to all and all_paged methods with doc updates and return type updates
- **client.py**: added inline count arg to get method
- **controllers/base.py**: extra logic to deal with different api response structure in case top arg is set
- **controllers/base.py**: added top arg to all_paged method
- **controllers/base.py**: added top arg to all method
- **client.py**: added top arg to get method
- **controllers/base.py**: added integer cast to count method return value
- **client.py**: fixed wrong httpx return type hint
- **controllers/base.py**: added count method making use of the client's count method
- **client.py**: added count method to use  query arg

## 0.0.17 (2025-11-06)

### Fix

- **controllers/base.py**: implemented a new all_paged method that's a page level generator
- **utils**: added pydantic list validation func that allows skipping invalid inputs

## 0.0.16 (2025-11-04)

### Fix

- **client.py**: print contents only when request failed
- **client.py**: fix in client api method error prints

## 0.0.15 (2025-11-04)

### Fix

- **client.py**: bugfix in space separation empty filter operator

## 0.0.14 (2025-11-04)

### Fix

- **models**: made all enum types nullable
- **models**: added spark fields for all remaining model fields for all models
- **models**: added spark fields deductibility percentage model
- **models**: added spark fields aging paybles receivables list model
- **models**: added spark fields bank account model
- **models**: import bug fix account model
- **models**: added spark fields account model
- **models**: added spark fields aging overview model
- **models**: made exact_unix_transformer context aware, spark output is now timestamp insetad of str

## 0.0.13 (2025-10-31)

### Fix

- **models**: added specific coercions for division and gl_account models for long and double types in spark schema

## 0.0.12 (2025-10-31)

### Fix

- **models**: timestamp col string coercion for spark, now with right format

## 0.0.11 (2025-10-31)

### Fix

- **models**: timestamp col string coercion for spark

## 0.0.10 (2025-10-31)

### Fix

- **models/base.py**: base now deriving from sparkdantic.SparkModel for pyspark model schema functionality
- **controlles/base.py**: commented debug print
- **client.py**: removed debug print

## 0.0.9 (2025-10-30)

### Fix

- **controllers**: filters now based on pydantic field names with automatic conversion
- **controllers**: select now based on pydantic field names, and validation using dynamic partial models
- **client.py**: bugfix numeric filtering
- fixed some wrongly named properties in financial models
- \_pk now used as primary key for single object retrieval in show method
- **models/division**: date property fix
- **client**: added division controller reference
- **controllers**: implemented vision controller
- **models**: implemented division model
- **controllers/base.py**: fixed return type hint of query arg validation method
- **models**: implemented pydantic model validation for query args
- added all new financial controller classes and refactored how controller classes are registered to client
- **models**: implemented RevenueList model
- **models**: implemented Return model
- **models**: implemented ReportingBalanceModel model
- **models**: implemented ProfitLossOverviewModel
- **models**: implemented PayablesListByAccountAndAgeGroup model
- **models**: implemented OutstandingInvoicesOverview model
- **models**: implemented OfficialReturn model
- **models**: implemented JournalStatusByFinancialPeriod model
- **models**: implemented GLScheme model
- **models**: implemented ExchangeRate and FinancialPeriod models
- **models**: implemented AgingReceivablesList and AgingReceivablesListByAgeGroup models
- **models**: implemented AgingPayablesListByAgeGroup model
- **models**: implemented AgingPayables model
- **models**: implemented AgingOverview model
- **models**: implemented AgingOverviewByAccount model
- controllers and models are now namespaced by service
- **controllers**: lower case resource names
- **models/base.py**: enum value serializaton
- refactored model and controller imports
- added journal model and controller
- **types**: added journal type and payment service provider type enums
- **models/gl_account.py**: fixed property naming issue
- **controllers**: added default expand arg as controller property
- **validators**: added new validator to deal with expanded nested results
- **types**: fixed wrongly defined enums
- **client**: added endpoint properties for most new controllers
- **models**: added deductibility percentage model and added ref to glaccount model
- **controllers**: added GLAccount controller
- **models**: added GLAccount model properties
- **types**: added CostCenter and CostUnit enums
- **types**: added BalanceSide enum class
- **types**: added GLAccountType enum class
- **controllers**: added expand arg ref to show method
- **client**: added support for expand query arg in client
- **controllers**: added support for expand query arg in controllers
- **models**: added BankAccount model
- **models**: fixed ReportingBalanceByClassification controller
- **models**: added new GLAccountClassificationMappings model and controller
- **account.py**: small fixes in property types and names
- **types**: added new enum type for balance type
- **models**: added new ReportingBalanceByClassification model
- **controllers**: added support for mandatory query args in controller
- **types**: added explicit guid type
- **controllers**: added support for regular query args in controller's all()
- **client.py**: added support for regular query args in client get
- **controllers**: removed obsolete enum class
- **controllers**: removed pandas support
- **controllers**: added pandas output option
- **models**: fixed bug in pascal alias generation, added custom alias generator. Fixed unit tests
- **client.py**: implemented basics for rate limit handling
- added custom eo unix ts validator and serializer and fixed bug in controller paging functionality
- **models/account.py**: fixed some wrong attribute types in Account model
- **auth.py**: method name and argument name clean up
- first working auth and client setup
- **client.py**: method rename
- implemented paging
- api/controller setup basis finished; todo: add actual rest api methods
- **exactpy/auth**: first full auth setup

## 0.0.8 (2025-10-14)

### Fix

- **workflows**: added branch conditions

## 0.0.7 (2025-10-14)

### Fix

- **workflows**: using branch/tag conditions instead of [skip ci]

## 0.0.6 (2025-10-14)

### Fix

- **tag.yml**: no persist credentials

## 0.0.5 (2025-10-14)

### Fix

- **tag.yml**: removed redundant condition
- **tag.yml**: idem for changelog job
- **pyproject.toml**: removed [skip ci] from bump message
- **workflows**: hopefully fixed tag trigger using annotated tag

## 0.0.4 (2025-10-14)

### Fix

- **tag.yml**: fixed arg name for PAT token

## 0.0.3 (2025-10-10)

### Fix

- **tag.yml**: now using PAT for pushing
- **pyproject.toml**: fix in bump commit message

## 0.0.2 (2025-10-10)

### Fix

- **tag.yml**: fixed order of cz/git config commands
- **tag.yml**: fixed wrong commitizen path
