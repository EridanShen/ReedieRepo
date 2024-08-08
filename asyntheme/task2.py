import concurrent.futures
import os


def create_file(index):
    filename = f'file_{index}.txt'
    with open(filename, 'w') as file:
        file.write(str(index))


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(create_file, range(10))


if __name__ == '__main__':
    main()
