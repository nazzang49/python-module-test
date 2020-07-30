from module3 import get_module3_info
from test1.module1 import get_module1_info
import sys

# sys path list -> packages
print(sys.path)

# moduleNotFoundError occurred
get_module3_info()
get_module1_info()

# can access to function of module4
mod = __import__('%s' %('module4'), fromlist=['module4'])
mod_cls = getattr(mod, 'Module4')
mod_cls.get_module4_info(0)