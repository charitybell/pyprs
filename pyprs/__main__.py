import argparse
import subprocess
import sys
import tomllib
import typing as t


class DigException(Exception):
    pass


def main() -> t.NoReturn:
    parser = argparse.ArgumentParser(
        prog='pyprs',
        description='Run scripts defined in a pyproject.toml file',
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', action='store_true')
    group.add_argument('script_name', nargs='?')

    # exit_on_error doesn't actually stop exiting on error
    parse_failed = False
    try:
        args = parser.parse_args()
    except SystemExit as e:
        if e.code:
            parse_failed = True
        raise
    finally:
        if parse_failed:
            print(file=sys.stderr)
            parser.print_help(sys.stderr)

    with open('pyproject.toml', 'rb') as f:
        data = tomllib.load(f)

    scripts = data['tool']['pyprs']['scripts']

    if args.list:
        for script_name, script in scripts.items():
            print(f'{script_name}:\t{script}')
        sys.exit()

    try:
        subprocess.run(scripts[args.script_name], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)

    sys.exit()


main()
