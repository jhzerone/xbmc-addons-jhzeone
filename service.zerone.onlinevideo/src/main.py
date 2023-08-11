# -*- coding: utf-8 -*-

"""

    Copyright (C) 2019 Team Kodi

    This file is part of service.xbmc.versioncheck

    SPDX-License-Identifier: GPL-3.0-or-later
    See LICENSES/GPL-3.0-or-later.txt for more information.

"""

import sys

import xbmc  # pylint: disable=import-error
import xbmcaddon  # pylint: disable=import-error
import xbmcgui  # pylint: disable=import-error
import xbmcvfs  # pylint: disable=import-error

try:
    xbmc.translatePath = xbmcvfs.translatePath
except AttributeError:
    pass
KODI_VERSION_MAJOR = int(xbmc.getInfoLabel('System.BuildVersion')[0:2])
MONITOR = xbmc.Monitor()

def abort_requested():
    """ Kodi 13+ compatible xbmc.Monitor().abortRequested()

    :return: whether abort requested
    :rtype: bool
    """
    if KODI_VERSION_MAJOR > 13:
        return MONITOR.abortRequested()

    return xbmc.abortRequested


def wait_for_abort(seconds):
    """ Kodi 13+ compatible xbmc.Monitor().waitForAbort()

    :param seconds: seconds to wait for abort
    :type seconds: int / float
    :return: whether abort was requested
    :rtype: bool
    """
    if KODI_VERSION_MAJOR > 13:
        return MONITOR.waitForAbort(seconds)

    for _ in range(0, seconds * 1000 / 200):
        if xbmc.abortRequested:
            return True
        xbmc.sleep(200)

    return False

def loop(dt):
    xbmc.log("hello world")
    return dt

if __name__ == '__main__':
    dt = 2
    while not abort_requested():
        if wait_for_abort(dt):
            break
        dt = loop(dt)
