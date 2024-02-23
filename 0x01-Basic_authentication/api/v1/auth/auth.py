#!/usr/bin/env python3
"""Auth module"""
from flask import request
from models.user import User
from typing import List, TypeVar

T = TypeVar('User')


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> T:
        return None
