'''tzinfo timezone information for Asia/Thimphu.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Thimphu(DstTzInfo):
    '''Asia/Thimphu timezone definition. See datetime.tzinfo for details'''

    _zone = 'Asia/Thimphu'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1947,8,14,18,1,24),
d(1987,9,30,18,30,0),
        ]

    _transition_info = [
i(21540,0,'LMT'),
i(19800,0,'IST'),
i(21600,0,'BTT'),
        ]

Thimphu = Thimphu()

