#!/usr/bin/env python3
"""Auth module"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return true if path is require else 
           false
        """
        # Remove trailing slash in excluded paths
        if excluded_paths is not None and path:
            for i in range(len(excluded_paths)):
                if excluded_paths[i] != '/' and excluded_paths[i][-1] == '/':
                    excluded_paths[i] = excluded_paths[i][:-1]

        # Remove trailing slash in path
        if path is not None and path != '/' and path[-1] == '/' and excluded_paths:
            path = path[:-1]

        if not path or not excluded_paths:  # empty arguments or None
            return True
        elif path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """Returns request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns request"""
        return None
