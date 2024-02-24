#!/usr/bin/env python3
"""Auth module"""
from flask import request
from typing import List


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns path"""
        return path

    def authorization_header(self, request=None) -> str:
        """Returns request"""
        return request

    def current_user(self, request=None):
        """Returns request"""
        return request
