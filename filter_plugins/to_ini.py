# Copyright (c) 2024, Luke Stigdon <contact@lukestigdon.com>
# SPDX-License-Identifier: MIT

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from collections.abc import Mapping
from configparser import ConfigParser
from io import StringIO

from ansible.errors import AnsibleFilterError


# the builtin configparse doesn't support values outside of 
# predefined secitions this writes any, e.g.:
#
# ; These cause errors!
# RUN_USER: git
# RUN_MODE: prod
# APP_NAME: Gitea
#
# ; This is okay 
# [section]
# FOO = bar
# ; ...
#
# This implimentation of to_ini supports the ini that gitea uses

def to_ini(obj : Mapping):
    """ Read the given dict and return an INI formatted string """

    if not isinstance(obj, Mapping):
        raise AnsibleFilterError(f'to_ini requires a dict, got {type(obj)}')

    if obj is {}:
        raise AnsibleFilterError('to_ini recieved an empty dictionary')

    # initialize a buffer to write data
    output = StringIO()

    # convert the dict to an ini
    ini = ConfigParser()
    for (key, value) in obj.items():
        if isinstance(value, Mapping):
            ini.add_section(key)
            ini.set()
            for (k, v) in value.items():
                ini[key][k] = v
        else:
            # write out top level keys without a section
            output.write(f"{key} = {value}\n")

    # add a little space
    output.write("\n")

    # write the rest of the config
    ini.write(output)

    return output.getvalue()


class FilterModule(object):
    """ Query filter """

    def filters(self):
        return { "to_ini": to_ini }