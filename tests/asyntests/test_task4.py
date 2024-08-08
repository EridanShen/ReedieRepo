import pytest
import asyncio
import aiohttp
from asyntheme import task4


@pytest.mark.asyncio
async def test_fetch():
    async with aiohttp.ClientSession() as session:
        status = await task4.fetch(session, "https://example.com/")
        assert status == 200


@pytest.mark.asyncio
async def test_fetch_with_semaphore():
    sem = asyncio.Semaphore(10)
    async with aiohttp.ClientSession() as session:
        status = await task4.fetch_with_semaphore(sem, session, "https://example.com/")
        assert status == 200


@pytest.mark.asyncio
async def test_task4():
    url = "https://example.com/"
    num_requests = 5
    max_requests_at_once = 2
    output_file = "test_statuses.txt"

    # Вызов функции main из task4
    await task4.main(url, num_requests, max_requests_at_once, output_file)

    with open(output_file, 'r') as f:
        statuses = f.readlines()

    assert len(statuses) == num_requests
    assert all(int(status) == 200 for status in statuses)
