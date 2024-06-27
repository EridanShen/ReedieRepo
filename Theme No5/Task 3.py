import logging

logging.basicConfig(filename='task3.log', level=logging.INFO, format='%(asctime)s %(message)s')
#file = open('lorum.txt')

lst = []
for i in range(1000):
    lst.append(open('lorum.txt', 'w'))
