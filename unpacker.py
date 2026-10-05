import struct, zlib

def unpack_epf(path):
    with open(path, 'rb') as f:
        data = f.read()
    # пропускаем заголовок контейнера 1С
    offset = data.find(b'\xef\xbb\xbf')
    return zlib.decompress(data[offset+3:])
