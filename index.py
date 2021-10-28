from amstrong import main as amstr
from amstrong_series import main as amstr_ser
from auto_num import main as auto
from auto_series import main as auto_ser
from neon import main as nen
from neon_series import main as nen_ser
from pallen import main as pal
from pallen_series import main as pal_ser
from perfect_num import main as perf
from perfect_series import main as perf_ser
from prime import main as prm
from prime_series import main as prm_ser
from reverse import main as rev
from reverse_series import main as rev_ser
from strong import main as strn
from strong_series import main as strn_ser

def single(num: int):
    if num == 1:
        prm()
    elif num == 2:
        perf()
    elif num == 3:
        nen()
    elif num == 4:
        auto()
    elif num == 5:
        rev()
    elif num == 6:
        pal()
    elif num == 7:
        strn()
    elif num == 8:
        amstr()
    else:
        print('Invalid choice')


def series(num: int):
    if num == 1:
        prm_ser()
    elif num == 2:
        perf_ser()
    elif num == 3:
        nen_ser()
    elif num == 4:
        auto_ser()
    elif num == 5:
        rev_ser()
    elif num == 6:
        pal_ser()
    elif num == 7:
        strn_ser()
    elif num == 8:
        amstr_ser()
    else:
        print('Invalid choice')