import subprocess


def count_lines(website):
    return subprocess.check_output('curl %s | wc -l' % website, shell=True)
