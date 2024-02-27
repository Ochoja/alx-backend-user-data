#!/usr/bin/env python3
"""Basic Authentication"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Authentication
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if type(authorization_header) is not str:
            return None
        elif authorization_header.startswith('Basic '):
            return authorization_header[6:]
        else:
            return None
