# Changelog

## Unreleased

### Fix

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
