'''tzinfo timezone information for Europe/Bucharest.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Bucharest(DstTzInfo):
    '''Europe/Bucharest timezone definition. See datetime.tzinfo for details'''

    _zone = 'Europe/Bucharest'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1931,7,23,22,15,36),
d(1932,5,20,22,0,0),
d(1932,10,1,22,0,0),
d(1933,4,1,22,0,0),
d(1933,9,30,22,0,0),
d(1934,4,7,22,0,0),
d(1934,10,6,22,0,0),
d(1935,4,6,22,0,0),
d(1935,10,5,22,0,0),
d(1936,4,4,22,0,0),
d(1936,10,3,22,0,0),
d(1937,4,3,22,0,0),
d(1937,10,2,22,0,0),
d(1938,4,2,22,0,0),
d(1938,10,1,22,0,0),
d(1939,4,1,22,0,0),
d(1939,9,30,22,0,0),
d(1979,5,26,22,0,0),
d(1979,9,29,21,0,0),
d(1980,4,5,21,0,0),
d(1980,9,27,22,0,0),
d(1981,3,29,0,0,0),
d(1981,9,27,0,0,0),
d(1982,3,28,0,0,0),
d(1982,9,26,0,0,0),
d(1983,3,27,0,0,0),
d(1983,9,25,0,0,0),
d(1984,3,25,0,0,0),
d(1984,9,30,0,0,0),
d(1985,3,31,0,0,0),
d(1985,9,29,0,0,0),
d(1986,3,30,0,0,0),
d(1986,9,28,0,0,0),
d(1987,3,29,0,0,0),
d(1987,9,27,0,0,0),
d(1988,3,27,0,0,0),
d(1988,9,25,0,0,0),
d(1989,3,26,0,0,0),
d(1989,9,24,0,0,0),
d(1990,3,25,0,0,0),
d(1990,9,30,0,0,0),
d(1990,12,31,22,0,0),
d(1991,3,30,22,0,0),
d(1991,9,28,22,0,0),
d(1992,3,28,22,0,0),
d(1992,9,26,22,0,0),
d(1993,3,27,22,0,0),
d(1993,9,25,22,0,0),
d(1993,12,31,22,0,0),
d(1994,3,26,22,0,0),
d(1994,9,24,21,0,0),
d(1995,3,25,22,0,0),
d(1995,9,23,21,0,0),
d(1996,3,30,22,0,0),
d(1996,10,26,21,0,0),
d(1997,3,30,1,0,0),
d(1997,10,26,1,0,0),
d(1998,3,29,1,0,0),
d(1998,10,25,1,0,0),
d(1999,3,28,1,0,0),
d(1999,10,31,1,0,0),
d(2000,3,26,1,0,0),
d(2000,10,29,1,0,0),
d(2001,3,25,1,0,0),
d(2001,10,28,1,0,0),
d(2002,3,31,1,0,0),
d(2002,10,27,1,0,0),
d(2003,3,30,1,0,0),
d(2003,10,26,1,0,0),
d(2004,3,28,1,0,0),
d(2004,10,31,1,0,0),
d(2005,3,27,1,0,0),
d(2005,10,30,1,0,0),
d(2006,3,26,1,0,0),
d(2006,10,29,1,0,0),
d(2007,3,25,1,0,0),
d(2007,10,28,1,0,0),
d(2008,3,30,1,0,0),
d(2008,10,26,1,0,0),
d(2009,3,29,1,0,0),
d(2009,10,25,1,0,0),
d(2010,3,28,1,0,0),
d(2010,10,31,1,0,0),
d(2011,3,27,1,0,0),
d(2011,10,30,1,0,0),
d(2012,3,25,1,0,0),
d(2012,10,28,1,0,0),
d(2013,3,31,1,0,0),
d(2013,10,27,1,0,0),
d(2014,3,30,1,0,0),
d(2014,10,26,1,0,0),
d(2015,3,29,1,0,0),
d(2015,10,25,1,0,0),
d(2016,3,27,1,0,0),
d(2016,10,30,1,0,0),
d(2017,3,26,1,0,0),
d(2017,10,29,1,0,0),
d(2018,3,25,1,0,0),
d(2018,10,28,1,0,0),
d(2019,3,31,1,0,0),
d(2019,10,27,1,0,0),
d(2020,3,29,1,0,0),
d(2020,10,25,1,0,0),
d(2021,3,28,1,0,0),
d(2021,10,31,1,0,0),
d(2022,3,27,1,0,0),
d(2022,10,30,1,0,0),
d(2023,3,26,1,0,0),
d(2023,10,29,1,0,0),
d(2024,3,31,1,0,0),
d(2024,10,27,1,0,0),
d(2025,3,30,1,0,0),
d(2025,10,26,1,0,0),
d(2026,3,29,1,0,0),
d(2026,10,25,1,0,0),
d(2027,3,28,1,0,0),
d(2027,10,31,1,0,0),
d(2028,3,26,1,0,0),
d(2028,10,29,1,0,0),
d(2029,3,25,1,0,0),
d(2029,10,28,1,0,0),
d(2030,3,31,1,0,0),
d(2030,10,27,1,0,0),
d(2031,3,30,1,0,0),
d(2031,10,26,1,0,0),
d(2032,3,28,1,0,0),
d(2032,10,31,1,0,0),
d(2033,3,27,1,0,0),
d(2033,10,30,1,0,0),
d(2034,3,26,1,0,0),
d(2034,10,29,1,0,0),
d(2035,3,25,1,0,0),
d(2035,10,28,1,0,0),
d(2036,3,30,1,0,0),
d(2036,10,26,1,0,0),
d(2037,3,29,1,0,0),
d(2037,10,25,1,0,0),
        ]

    _transition_info = [
i(6240,0,'BMT'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
        ]

Bucharest = Bucharest()

