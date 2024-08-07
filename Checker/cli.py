import argparse


def read_user_cli_args():
    """" The function to handle CLI arguments and options """

    parser = argparse.ArgumentParser(
        prog="Checker", description="check the availability of the websites"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Enter one or more websites for the check"
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="Enter filename for the check"
    )
    parser.add_argument(
        "-a",
        "--asynchronous",
        action="store_true",
        help="run the connectivity check asynchronously",
    )
    parser.add_argument(
        "-t",
        "--timer",
        action="store_true",
        help="display time for checks",
    )
    return parser.parse_args()


def display_check_result_wtime(result, url, time, error=""):
    """Display the result of the check"""
    print(f"The status of {url} is:", end=" ")
    if result:
        print(f'"Online!" 👍     Time taken: {time:.3f} sec')
    else:
        print(f'"Offline?" 👎 \n Error: "{error}"')


def display_check_result_notime(result, url, error=""):
    """Display the result of the check"""
    print(f"The status of {url} is:", end=" ")
    if result:
        print(f'"Online!" 👍')
    else:
        print(f'"Offline?" 👎 \n Error: "{error}"')