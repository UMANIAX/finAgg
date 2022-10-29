import base64
import typing
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import json
from model.creds.Creds import Creds

class CredentialWorker:

    def __init__(self, key: str, encrypted_file_path: str, decrypted_file_path: str):
        self.encrypted_file_path = encrypted_file_path
        self.decrypted_file_path = decrypted_file_path
        self.key = self._get_fernet_key(key)

    def _get_fernet_key(self, key: str) -> typing.Union[bytes, str]:
        password = key.encode('utf-8')
        salt = b'some random salt'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000,
        )
        fernet_key = base64.urlsafe_b64encode(kdf.derive(password))
        return fernet_key

    def encrypt_file(self):
        with open(self.decrypted_file_path, 'rb') as file:
            original = file.read()
        fernet = Fernet(self.key)
        encrypted = fernet.encrypt(original)
        with open(self.encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def get_encrypted_file_content(self) -> Creds:
        with open(self.encrypted_file_path, 'rb') as enc_file:
            encrypted = enc_file.read()
        fernet = Fernet(self.key)
        decrypted = fernet.decrypt(encrypted)
        decrypted_json = decrypted.decode("utf-8")
        return Creds.Schema().loads(decrypted_json)

    def decrypt_file(self):
        creds = self.get_encrypted_file_content()
        creds_dict = Creds.Schema().dump(creds)
        content_bytes = json.dumps(creds_dict).encode('utf-8')
        with open(self.decrypted_file_path, 'wb') as dencrypted_file:
            dencrypted_file.write(content_bytes)