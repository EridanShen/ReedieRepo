import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return response.status


async def fetch_with_semaphore(sem, session, url):
    async with sem:
        return await fetch(session, url)


async def main(url, num_requests, max_requests_at_once, output_file):
    sem = asyncio.Semaphore(max_requests_at_once)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_semaphore(sem, session, url) for _ in range(num_requests)]
        statuses = await asyncio.gather(*tasks)

    with open(output_file, 'w') as f:
        for status in statuses:
            f.write(f"{status}\n")

    assert len(statuses) == num_requests, f"Expected {num_requests} requests, but got {len(statuses)}"


if __name__ == '__main__':
    url = "https://example.com/"
    num_requests = 50
    max_requests_at_once = 10
    output_file = "statuses.txt"

    asyncio.run(main(url, num_requests, max_requests_at_once, output_file))