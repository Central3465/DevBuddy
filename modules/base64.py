import base64

def encode(input):
    bytes = input.encode('utf-8')
    encoded = base64.b64encode(bytes)
    return encoded.decode('utf-8')

def decode(input):
    bytes = input.encode('utf-8')
    decoded = base64.b64decode(bytes)
    return decoded.decode('utf-8')