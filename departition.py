

with open(f'cache.mp4', 'wb') as out:
    with open('video/vid/data', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')

    b = b''
    for i in range(4): #'''int(data[1])'''
        with open(f'{data[0]}/{1000 + i}', 'rb') as r:
            b += r.read()

    out.write(b)
