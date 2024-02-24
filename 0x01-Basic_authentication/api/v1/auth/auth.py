#!/usr/bin/env python3
"""Auth module"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns path"""
        return False

    def authorization_header(self, request=None) -> str:
        """Returns request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns request"""
        return None
