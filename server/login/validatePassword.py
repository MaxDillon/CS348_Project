import secrets
import bcrypt
import sys

def validatePassword(username, passHash):
	if len(username) > 2:
		token = secrets.token_hex(32)
		passHashEncode = passHash.encode("utf-8")
		bcryptHash = bcrypt.hashpw(passHashEncode, bcrypt.gensalt())
		bcryptString = bcryptHash.decode()
		return {'token': token, 'hash': bcryptString}
	return None


def compare_passwords(passHashString, bcryptString):
	passHashBytes = passHashString.encode("utf-8")
	bcryptBytes = bcryptString.encode("utf-8")
	return bcrypt.checkpw(passHashBytes, bcryptBytes)