import urllib.parse
# декадировать из гет запроса имя арбитражного упровляюшего
def decode_from_(encoded_str):
    decoded_str = urllib.parse.unquote(encoded_str)
    print(decoded_str)


def decode_from_fio(encoded_str):
    decoded_str = urllib.parse.unquote_to_bytes()
    pass



encoded_str = "%D0%A1%D0%B0%D0%BF%D0%BE%D0%B6%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D0%B0%20%D0%AE%D0%BB%D0%B8%D1%8F%20%D0%94%D0%BC%D0%B8%D1%82%D1%80%D0%B8%D0%B5%D0%B2%D0%BD%D0%B0"
name = decode_from_(encoded_str)