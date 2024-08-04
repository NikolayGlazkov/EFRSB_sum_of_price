import urllib.parse

# декадировать из гет запроса имя арбитражного упровляюшего
def decode_from_str(encoded_str):
    decoded_str = urllib.parse.unquote(encoded_str)
    return decoded_str

# подготовка фио для гет запроса
def decode_from_fio(encoded_str):
    decoded_str = urllib.parse.quote(encoded_str)
    return decoded_str


