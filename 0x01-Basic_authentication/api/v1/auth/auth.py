#!/usr/bin/env python3
"""Auth module"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns path"""
        # Remove trailing slash
        for route in excluded_paths:
            if route != '/' and route[-1] == '/':
                route = route[:-1]

        if path != '/' and path[-1] == '/':
            path = path[:-1]

        if path in excluded_paths and excluded_paths is not None:
            return False
        elif path is None:
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        """Returns request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns request"""
        return None
