from pyignite import Client

if __name__ == '__main__':
    client = Client()
    client.connect('127.0.0.1', 10800)

    mycache = client.create_cache('mycache')
    mycache.put('key', 42)

    print(mycache.get('key'))
