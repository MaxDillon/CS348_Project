import secrets
import bcrypt
import sys

def validatePassword(username, passHash, database):
	if len(username) > 2:
		token = secrets.token_hex(32)
		database[token] = username
		passHashEncode = passHash.encode("utf-8")
		bcryptHash = bcrypt.hashpw(passHashEncode, bcrypt.gensalt())
		bcryptString = bcryptHash.decode()
		return token
	return None


def validateToken(token, database):
	username = database.get(token)
	if username is None:
		return None

	return {'username': username}
	

def compare_passwords(passHashString, bcryptString):
	passHashBytes = passHashString.encode("utf-8")
	bcryptBytes = bcryptString.encode("utf-8")
	return bcrypt.checkpw(passHashBytes, bcryptBytes)