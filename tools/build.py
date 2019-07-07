import argparse
import os
import re
import sys
import tarfile
import typing
from datetime import date

_versionPat = re.compile(r'^SELF_VERSION\s*<-\s*(\d+);$')
_datePat = re.compile(r'^SELF_DATE\s*<-\s*"([\d\-]+)";$')
_namePat = re.compile(r'^SELF_NAME\s*<-\s*"([^"]+)";$')


def get_data(sourceDir: str, pattern: re.Pattern):
    versionPath = os.path.join(sourceDir, 'version.nut')
    with open(versionPath, 'r') as f:
        for line in f:
            m = pattern.match(line)
            if m:
                return m.group(1)
    return None


def get_version(sourceDir):
    version = get_data(sourceDir, _versionPat)
    return int(version) if version else -1


def get_name(sourceDir):
    return get_data(sourceDir, _namePat)


def refresh_date(sourceDir):
    today = date.today().strftime('%Y-%m-%d')
    versionPath = os.path.join(sourceDir, 'version.nut')
    lines = []
    with open(versionPath, 'r') as f:
        for line in f:
            m = _datePat.match(line)
            if m and m.group(1) != today:
                line = f'SELF_DATE <- "{today}";'
            lines.append(line)

    with open(versionPath, 'w') as f:
        f.writelines(lines)


def sanitize(name: str):
    return re.sub(r'[_\s\.]+', '_', name)


def make_tar(outputDir: str, sourceDir: str, licensePath: str):
    try:
        os.makedirs(outputDir)
    except OSError:
        pass
    rootName = f'{sanitize(get_name(sourceDir))}-{get_version(sourceDir)}'
    with tarfile.open(os.path.join(outputDir, rootName + '.tar'), 'w') as tar:
        tar.add(sourceDir, arcname=rootName)
        tar.add(licensePath, arcname=os.path.join(rootName, 'LICENSE'))


def main(argv: typing.List[str]):
    parser = argparse.ArgumentParser()
    scriptDir = os.path.dirname(argv[0])
    sourceDir = os.path.relpath(os.path.join(scriptDir, '..', 'src'))

    parser.add_argument('output', metavar='OUT_DIR',
                        help='path to output directory')
    parser.add_argument('--source', default=sourceDir, nargs='?',
                        metavar='DIR', help='path to the source directory')
    parser.add_argument('--license', default=os.path.join(scriptDir, '..', 'LICENSE'),
                        nargs='?', metavar='PATH', help='path to the license file')
    parser.add_argument('--date', action='store_true',
                        help='whether to refresh the date')
    args = parser.parse_args(argv[1:])
    if args.date:
        refresh_date(args.source)
    make_tar(args.output, args.source, args.license)


if __name__ == '__main__':
    main(sys.argv)
