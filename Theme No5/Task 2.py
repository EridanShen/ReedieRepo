import logging

logging.basicConfig(filename='lorumtypes.log', level=logging.INFO, format='%(asctime)s %(message)s')

file = open('lorum.txt', 'a+')
print(file.read())