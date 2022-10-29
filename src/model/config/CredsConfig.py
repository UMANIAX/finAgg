from marshmallow_dataclass import dataclass

@dataclass
class CredsConfig:
    encrypted_file_path: str
    decrypted_file_path: str