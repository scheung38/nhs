import os
import re

regex1 = re.compile('Care|Quality|Commission')  # 0,1,2,3,4,5,6 PASSED


# regex1 = re.compile('September|2004')  # 9 PASSED
# regex1 = re.compile('general|population|generally')  # 6,8 PASSED
# regex1 = re.compile('Care Quality Commission|admission')  # 1
# regex1 = re.compile('general population|Alzheimer')  # 6

# regex1 = re.compile('June|2013')  # [0, 1, 2, 3, 4, 5, 6, 7]


def my_query(regex, file_name):
    line_number = []
    with open(file_name, 'r') as inputFile:
        for line_i, line in enumerate(inputFile, 0):
            if regex.search(line):
                line_number.append(line_i)
        return line_number


def get_directory():
    base_dir = os.path.abspath(os.curdir)
    if ('src' or 'test') in base_dir:
        os.chdir('..')
        return os.path.join(os.path.abspath(os.curdir), 'hscicNews')
    else:
        return os.path.join(os.path.abspath(os.curdir), 'hscicNews')


if __name__ == '__main__':
    print my_query(regex1, get_directory())
