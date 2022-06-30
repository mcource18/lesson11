import os
from Victory.Victory_ver2 import date_to_str
from filemanager import filenames

def test_date_to_str_1():
    assert (date_to_str('01.01.2001') == 'первое января 2001 года')


def test_date_to_str_2():
    assert (date_to_str('03.06.2007') == 'третье июня 2007 года')


def test_filenames_1():
    assert(not os.path.isdir(filenames()[0]))


def test_filenames_2():
    assert (os.path.exists(filenames()[0]))
