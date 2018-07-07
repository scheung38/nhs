import re
import os

regex1 = re.compile('Care|Quality|Commission')  # 0,1,2,3,4,5,6 PASSED
# regex1 = re.compile('September|2004')  # 9 PASSED
# regex1 = re.compile('general|population|generally')  # 6,8 PASSED
# regex1 = re.compile('Care Quality Commission|admission')  # 1
# regex1 = re.compile('general population|Alzheimer')  # 6


def my_query(regex):
    output = []
    base_dir = os.getcwd()
    print(base_dir)
    filename = 'hscic-news'

    with open(os.path.join(base_dir, filename), 'r') as inputFile:
        for line_i, line in enumerate(inputFile, 0):
            if regex.search(line):
                output.append(line_i)
        return output


if __name__ == '__main__':
    print(my_query(regex1))
