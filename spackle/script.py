import re
import sys

from subprocess import Popen, PIPE


FILENAME_RE = re.compile(r'^[\w//.-]+')
RANGE_RE = re.compile(r'\d+-\d+')


def main():
    process = Popen(['coverage', 'report', '-m'], stdin=PIPE, stdout=PIPE, stderr=PIPE)

    coverages = []
    for line in process.stdout:

        line = line.decode('utf8')

        # Write out original coverage report lines.
        sys.stdout.write(line)

        # Filename from coverage report Name column.
        filename = FILENAME_RE.match(line).group()

        # Any line ranges from coveage report Missing column.
        range_list = RANGE_RE.findall(line)

        if not range_list:
            continue

        for missing in range_list:
            line_numbers = list(map(int, missing.split('-')))
            coverages.append({
                'filename': filename,
                'missing': missing,
                'difference': line_numbers[1] - line_numbers[0]
            })

    # Was the report empty?
    if not coverages:
        return

    # Table formatting.
    max_filename = max([len(co['filename']) for co in coverages]) + 10
    max_missing = max([len(co['missing']) for co in coverages]) + 16
    header = 'Name%sMissing%sMiss' % (' ' * (max_filename - 4), ' ' * (max_missing - 8))

    sys.stdout.write('\nLargest gaps in coverage:\n\n')
    sys.stdout.write(header + '\n')
    sys.stdout.write('-' * len(header) + '\n')

    for c in sorted(coverages, key=lambda k: k['difference'], reverse=True):
        filename_output = c['filename'] + ' ' * (max_filename - len(c['filename']))
        missing_output = c['missing'] + ' ' * (max_missing - len(c['missing']))

        sys.stdout.write('%s%s%s\n' % (filename_output, missing_output, c['difference']))


if __name__ == '__main__':
    main()
