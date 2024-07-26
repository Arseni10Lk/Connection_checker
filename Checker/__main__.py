import sys
import asyncio
import pathlib
import time

from Checker.cli import read_user_cli_args, display_check_result_wtime, display_check_result_notime
from Checker.checker import site_is_online, site_is_online_async


def main():
    """ Run the Checker """

    user_args = read_user_cli_args()
    urls = _get_websites_urls(user_args)
    if not urls:
        print("Error: no URLs to check", file=sys.stderr)
        sys.exit(1)

    if user_args.timer:

        start_time_overall = time.time()

        if user_args.asynchronous:
            asyncio.run(_asynchronous_check_wtime(urls))
        else:
            _synchronous_check_wtime(urls)

        end_time_overall = time.time()

        print(f"The check took {end_time_overall-start_time_overall:.3f} sec")

    else:

        if user_args.asynchronous:
            asyncio.run(_asynchronous_check_notime(urls))
        else:
            _synchronous_check_notime(urls)


def _get_websites_urls(user_args):
    urls = user_args.urls
    if user_args.input_file:
        urls += _read_urls_from_file(user_args.input_file)
    return urls


def _read_urls_from_file(file):
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            print(f"Error: empty input file, {file}", file=sys.stderr)
    else:
        print("Error: input file not found", file=sys.stderr)
    return []


async def _asynchronous_check_notime(urls):
    async def check_url(url):
        error = ""
        try:
            result = await site_is_online_async(url)
        except Exception as e:
            result = False
            error = e
        display_check_result_notime(result, url, error)

    await asyncio.gather(*(check_url(url) for url in urls))


async def _asynchronous_check_wtime(urls):
    async def check_url(url):
        error = ""
        time_specific = 0
        try:
            start_time = time.time()
            result = await site_is_online_async(url)
            end_time = time.time()
            time_specific = end_time - start_time
        except Exception as e:
            result = False
            error = e
        display_check_result_wtime(result, url, time_specific, error)

    await asyncio.gather(*(check_url(url) for url in urls))


def _synchronous_check_wtime(urls):
    for url in urls:
        error = ""
        time_specific = 0
        try:
            start_time = time.time()
            result = site_is_online(url)
            end_time = time.time()
            time_specific = end_time - start_time
        except Exception as e:
            result = False
            error = str(e)
        display_check_result_wtime(result, url, time_specific, error)


def _synchronous_check_notime(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result_notime(result, url, error)

if __name__ == "__main__":
    main()
