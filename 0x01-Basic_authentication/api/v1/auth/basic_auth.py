#!/usr/bin/env python3
"""Basic Authentication"""
from api.v1.auth.auth import Auth
from base64 import decode, encode, b64decode
from typing import Tuple


class BasicAuth(Auth):
    """ Basic Authentication
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Return Base64 part of Authorization header"""
        if type(authorization_header) is not str:
            return None
        elif authorization_header.startswith('Basic '):
            return authorization_header[6:]
        else:
            return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Return decoded value of base64 string"""
        if type(base64_authorization_header) is not str:
            return None
        else:
            try:
                b64bytes = base64_authorization_header.encode('utf-8')
                string_bytes = b64decode(b64bytes)
                return string_bytes.decode('utf-8')
            except Exception:
                return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """Returns the user email and password
           from base64 decoded value
        """
        if (decoded_base64_authorization_header is not None and
                type(decoded_base64_authorization_header) is str and
                ':' in decoded_base64_authorization_header):
            try:
                return tuple(decoded_base64_authorization_header.split(":"))
            except Exception:
                return (None, None)
        else:
            return (None, None)
