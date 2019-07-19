import arrow
from pathlib import Path
import os

COLLECT_SUFFIX = ('.py')  # 统计的文件后缀
IGNORE_SUFFIX = ('.png', '.jpg', '.mp3','.mp4')
COMMENT_SYMBOL = ('#', '"""', '""', "'")  # 注释符号
IGNORE = ('venv', 'migrations', 'logs', '.git', 'coursepoints')  # 不需统计的文件夹


class CodeCount(object):

    def __init__(self):
        self.code_line = 0
        self.init_config()

    def init_config(self):
        self.collect_suffix = COLLECT_SUFFIX or ('*')
        self.ignore = IGNORE or ()
        self.comment_symbol = COMMENT_SYMBOL or ('#')
        self.ignore_suffix = IGNORE_SUFFIX or ()

    def recursion_folder(self, path):
        if os.path.isfile(path):
            self.check_file_ignore(path)
        else:
            self.check_ignore(path)

    def check_ignore(self, path):
        if str(path).endswith(self.ignore):
            print(path)
            return
        for path in Path(path).iterdir():
            self.recursion_folder(path)

    def check_file_ignore(self, path):
        if not '*' in self.collect_suffix:
            if Path(path).suffix not in self.collect_suffix: return
        else:
            if Path(path).suffix in self.ignore_suffix: return
        self.parser_file(path)

    def parser_file(self, path):
        print(path)
        f = open(path, 'r', encoding='utf8')
        lines = [line for line in f.readlines() if line]
        temp_count = 0
        for line in lines:
            if line.startswith(self.comment_symbol):continue
            temp_count+=1
        self.code_line += temp_count

    def write_data(self, folder):
        data_time = arrow.now().format('YYYY-MM-DD HH:mm:ss')
        f = open('out.txt', 'a+', encoding='utf8')
        line = '{}\t{}\t{}\n'.format(self.code_line, data_time, str(folder.rsplit('\\')[-1]))
        f.write(line)

    def start(self, folder):
        self.recursion_folder(folder)
        self.write_data(folder)


c = CodeCount()
# c.start(r'C:\Projects\coursepoint')
c.start(r'C:\Projects\learn\douyin')
