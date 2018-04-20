#coding:utf-8
import time,datetime


def datetime_to_string(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def string_to_datetime(string):
    return datetime.date.strftime(string, "%%Y-%m-%d %H:%M:%S")


def timestamp_to_string(stamp):
    return time.strftime("%Y-%m-%d-%H", time.localtime(stamp))


def datetime_to_timestamp(dateTim):
    return time.mktime(dateTim.timetuple())