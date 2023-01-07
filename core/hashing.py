from passlib.context import CryptContext
from passlib.hash import pbkdf2_sha256 as pbk

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        # print(pwd_context.hash(password))
        return pwd_context.hash(password)


class HasherPbk:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pbk.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        # print(pwd_context.hash(password))
        return pbk.hash(password)

