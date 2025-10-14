# Changelog

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
