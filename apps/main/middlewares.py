from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'mysecretpassword'
iv = b'This is an IV456'

cipher = AES.new(key, AES.MODE_CBC, iv)


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith('/api/v1/'):
            response.content = cipher.encrypt(pad(response.content, AES.block_size))
        return response
