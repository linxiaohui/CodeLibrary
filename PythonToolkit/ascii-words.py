# -*- coding: UTF-8 -*-

import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

init(strip=not sys.stdout.isatty())
# `pip install pyfiglet` 后可以使用 `pyfiglet -l`查看支持的字体名称
cprint(figlet_format("Hello World", font='banner'), 'yellow', 'on_red', attrs=['bold'])
