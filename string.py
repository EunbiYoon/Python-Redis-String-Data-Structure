import redis
from time import sleep

client=redis.Redis(host='127.0.0.1', port=6379)

# demo the strings
client.set('language','Python')
print(client.get('language'))

# set expiration method 1 -> px
client.set('language','Python',px=10000) #expire after 10 seconds
print(client.get('language'))
print(client.ttl('language'))
sleep(3) #3seconds
print(client.ttl('language'))

# set expiration method 2 -> expire
client.set('language','Python')
print(client.expire('language',10)) #expire after 10 seconds
print(client.ttl('language'))
sleep(3)
print(client.ttl('language'))


