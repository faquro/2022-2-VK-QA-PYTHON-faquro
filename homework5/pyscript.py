import argparse
import json
import os.path
import re
from collections import Counter

HOST = r'^(?P<host>.*?)'
SPACE = r'\s'
IDENTITY = r'\S+'
USER = r'\S+'
TIME = r'(?P<time>\[.*?\])'
TYPE = r'\"(?P<type>\S+)'
REQUEST = r'(?P<request>\S+)'
HTTP = r'(?P<call>.*?)\"'
STATUS = r'(?P<status>\d{3})'
SIZE = r'(?P<size>\S+)'

DEFAULT_TYPES = ['GET', 'POST', 'HEAD', 'PUT']

REGEX = HOST + SPACE + IDENTITY + SPACE + USER + SPACE + TIME + SPACE + TYPE + SPACE + REQUEST + SPACE + HTTP + SPACE + STATUS + SPACE + SIZE + SPACE


def main():
    if get_arg().json:
        json_out()
    else:
        print_result()


def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', default='access,log')
    parser.add_argument('-j', '--json')
    return parser


def log_parser(log_line):
    match = re.search(REGEX, log_line)
    return match


def get_arg():
    parser = setup_args()
    args = parser.parse_args()
    return args


def get_filepath(file_path):
    repo_root = os.path.abspath(os.path.join(__file__, os.path.pardir))
    return os.path.join(repo_root, file_path)


def read_data():
    file_path = get_filepath(get_arg().file)
    with open(file_path) as file:
        requests = file.readlines()
    return requests


def count_total():
    result = sum(1 for _ in read_data())
    return result


def count_by_type():
    result = Counter([log_parser(line).group('type') for line in read_data()])
    return result


def top10_frequent():
    count_request = Counter([log_parser(line).group('request') for line in read_data()])
    result = sorted(count_request.items(), key=lambda item: item[1], reverse=True)[:10]
    return result


def top5_5xx():
    count_host = Counter([log_parser(line).group('host') for line in read_data() if re.match('5[0-9]{2}$', log_parser(line).group('status'))])
    result = sorted(count_host.items(), key=lambda item: item[1], reverse=True)[:5]
    return result


def print_result():
    print("Info from file:", get_filepath(get_arg().file), "\n")
    print("Total count:", count_total(), "\n")
    print("Total by type:")
    for type in DEFAULT_TYPES:
        print(type, "=", count_by_type()[type])
    print("\nTop 10 most frequent requests:")
    for i in top10_frequent():
        print(i[1], i[0])
    print("\nTop 5 users by number of requests with error 5XX:")
    for i in top5_5xx():
        print(i[1], i[0])


def json_out():
    info = {'Info from file': get_filepath(get_arg().file)}
    count_request = {'Total count': count_total()}
    top10 = {'Top 10 most frequent requests': {i[0]: i[1] for i in top10_frequent()}}
    top5 = {'Top 5 users by number of requests with error 5XX': {i[0]: i[1] for i in top5_5xx()}}
    total_by_type = {'Total by type': {type: count_by_type()[type] for type in DEFAULT_TYPES}}
    results = [total_by_type, top10, top5]
    for result in results:
        count_request.update(result)
    info.update(count_request)
    capitals_json4 = json.dumps(info, sort_keys=False, indent=4)
    with open(get_filepath(get_arg().json), "w") as my_file:
        my_file.write(capitals_json4)


if __name__ == '__main__':
    main()
