from package.sec.Nomura import Nomura
from package.Crawler import Crawler

import json

if __name__ == '__main__':
    _nomura = Nomura()
    _nomura.setHeadless(True)
    print( _nomura.getData('00935') )
    