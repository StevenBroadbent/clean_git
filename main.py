import top_level
import top_level2
import top_level3
from top_level2.add_file import add

if __name__ == '__main__':
    print('This is an as yet untouched project')

    print(top_level.TL1)
    print(top_level2.TL2)
    print(top_level3.TL3)
    args = 1, 2, 3
    print(add(args))
