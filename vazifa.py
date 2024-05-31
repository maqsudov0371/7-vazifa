import random
import string


from qr_code_scan import qr_code_make


def qr_random(num):
    for _ in range(num):
      
     object = []

    ascii_letters = string.ascii_lowercase + string.ascii_uppercase
    coder=random.sample(ascii_letters, 8)
    code=random.sample(ascii_letters, 4)
    numbers=''.join(code)
    data_search='https://'.join(coder)
    if coder not in object:
          
        qr_code_make(data_search, numbers)
        yield qr_code_make
for i in qr_random(5):
    print(i)