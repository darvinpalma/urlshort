from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(value):
	url_validator = URLValidator()
	added_value = value
	
	if "http://" in added_value:
		new_value = added_value
	elif "https://" in added_value:
		new_value = added_value
	else:
		new_value = "http://" + value

	try:
		url_validator(new_value)
	except:
		raise ValidationError("Invalid URL for the field")
	return new_value

def validate_dot_com(value):
	if not "com" in value:
		raise ValidationError("There is no .com")
	return value