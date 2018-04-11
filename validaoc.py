import owncloud
import lerConfig
import logging
import os
import sys
import time
import logUtil


def geraOC(usuario):
    oc = owncloud.Client(lerConfig.get_server())
    oc.login(lerConfig.get_user(usuario), lerConfig.get_password(usuario))
    return oc

geraOC('usuario00')
