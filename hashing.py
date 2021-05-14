from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def bcrypt(password):
        return pwd_context.hash(password)

    def verify(hashed_pwd, plain_password):
        return pwd_context.verify(plain_password, hashed_pwd)
