from pwdlib import PasswordHash

#create one PasswordHash object when the module loads
password_hash=PasswordHash.recommended()

def hash_password(password:str)->str:
    """
    convert plain text password into secure hash.
    called during user registration
    """

    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str)->bool:
    """
    verify the entered password aganaist the stored hash.
    called during login
    """
    return password_hash.verify(plain_password, hashed_password)
