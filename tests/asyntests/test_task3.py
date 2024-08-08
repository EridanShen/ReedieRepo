import pytest
import aiohttp
import asyncio
from asyntheme import task3
import profile_tests


@pytest.mark.asyncio
async def test_fetch():
    async with aiohttp.ClientSession() as session:
        response_text = await task3.fetch(session, "https://google.com/")
        assert isinstance(response_text, str)
        assert len(response_text) > 0


@pytest.mark.asyncio
async def test_fetch_with_semaphore():
    sem = asyncio.Semaphore(10)
    async with aiohttp.ClientSession() as session:
        response_text = await task3.fetch_with_semaphore(sem, session, "https://google.com/")
        assert isinstance(response_text, str)
        assert len(response_text) > 0


@pytest.mark.asyncio
async def test_main():
    url = "https://google.com/"
    num_requests = 20
    max_requests_per_second = 10

    responses = await task3.main(url, num_requests, max_requests_per_second)

    assert len(responses) == num_requests
    assert all(isinstance(response, str) for response in responses)
    assert all(len(response) > 0 for response in responses)


profile_tests()
