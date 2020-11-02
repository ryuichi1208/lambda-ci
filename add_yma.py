# -*- coding: utf-8 -*-
from __future__ import print_function
import logging
import os
import tempfile
import zipfile
from shutil import copyfile, copytree
import boto3
import pip
import subprocess
import sys

log = logging.getLogger(__name__)


def read_file(path, loader=None, binary_file=False):
    open_mode = 'rb' if binary_file else 'r'
    with open(path, mode=open_mode) as fh:
        if not loader:
            return fh.read()
        return loader(fh.read())

def function_exists(cfg):
    """
    Check whether the given function in cfg exists or not
    """
    client = _client_from_cfg(cfg)
    try:
        client.get_function(FunctionName=cfg.get('function_name'))
    except:
        return False
    return True
