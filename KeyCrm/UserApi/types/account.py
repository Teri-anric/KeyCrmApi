from pydantic import BaseModel


class Settings(BaseModel):
    class Config:
        extra = "allow"

    notifications: dict
    locale: str


class Permission(BaseModel):
    id: int
    name: str
    guard_name: str
    group_name: str
    position: int
    related: str
    created_at: str
    updated_at: str


class Role(BaseModel):
    id: int
    name: str
    alias: str
    color: str
    is_reserved: bool
    statuses_all: bool
    accepted_all: bool
    created_at: str
    updated_at: str
    deleted_at: str
    permissions: list[Permission]


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    username: str
    phone: str
    is_owner: bool
    role_id: int
    avatar_id: str
    status: str
    account_verified_at: str
    is_hidden: int
    settings: Settings
    locale: str
    last_logged_at: str
    created_at: str
    updated_at: str
    deleted_at: str
    carrot_hash: str
    tenant_id: int
    tenant_public_key: str
    account_code: str
    full_name: str
    is_bot: bool
    role: Role
    avatar: str
    call_route_mappings: list
