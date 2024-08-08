import aiohttp
import asyncio
import time


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def fetch_with_semaphore(sem, session, url):
    async with sem:
        return await fetch(session, url)


async def main(url, num_requests, max_requests_per_second):
    sem = asyncio.Semaphore(max_requests_per_second)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_semaphore(sem, session, url) for _ in range(num_requests)]
        start_time = time.time()
        responses = await asyncio.gather(*tasks)
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        return responses


if __name__ == '__main__':
    url = "http://google.com"
    num_requests = 20
    max_requests_per_second = 10
    asyncio.run(main(url, num_requests, max_requests_per_second))
