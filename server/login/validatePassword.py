import secrets


def validatePassword(username, passHash):
	if len(username) > 5:
		token = secrets.token_hex(32)
		return token
	return None
