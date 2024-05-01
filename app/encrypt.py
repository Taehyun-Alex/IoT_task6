# Import cryptography library
from cryptography.fernet import Fernet
from app.key_utils import key32, key64


class Encryptor:
    def __init__(self, key):
        key32_ = key32(key)
        self.key64_ = key64(key32_)

    def _encrypt(self, data: bytes) -> bytes:
        """
        This method performs the actual encryption on {data}..

        :param data: Data to be encrypteda
        :return: Encrypted data
        """
        fernet = Fernet(self.key64_)
        encrypted_data = fernet.encrypt(data)
        return encrypted_data

    def encrypt(self, data) -> bytes:
        """
        This method takes data and encrypts it using the key that
        was passed in through the initialiser. The parameter {data}
        can either be a string, which will be encrypted as such
        (after converting it to bytes), or an object that has the
        method {read_data}, which takes no arguments but *must*
        return a bytes object.

        :param data: Data to encrypt
        :return: Encrypted data as a bytes object
        """
        if isinstance(data, str):
            data = data.encode() # if the input is string
        elif hasattr(data, 'read_data'):
            data = data.read_data() # if the input is a TestAdapter object
        else:
            raise TypeError('Invalid input type')

        return self._encrypt(data)
