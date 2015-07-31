#
# Copyright 2013-2015 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
#

"""
Easyconfig constants module that provides all constants that can
be used within an Easyconfig file.

@author: Stijn De Weirdt (Ghent University)
@author: Kenneth Hoste (Ghent University)
"""
import platform
from vsc.utils import fancylogger

from easybuild.tools.systemtools import get_shared_lib_ext, get_os_name, get_os_type, get_os_version
from easybuild.tools.utilities import mk_rst_table, FORMAT_TXT, FORMAT_RST

_log = fancylogger.getLogger('easyconfig.constants', fname=False)

EXTERNAL_MODULE_MARKER = 'EXTERNAL_MODULE'

# constants that can be used in easyconfig
EASYCONFIG_CONSTANTS = {
    'EXTERNAL_MODULE': (EXTERNAL_MODULE_MARKER, "External module marker"),
    'SYS_PYTHON_VERSION': (platform.python_version(), "System Python version (platform.python_version())"),
    'OS_TYPE': (get_os_type(), "System type (e.g. 'Linux' or 'Darwin')"),
    'OS_NAME': (get_os_name(), "System name (e.g. 'fedora' or 'RHEL')"),
    'OS_VERSION': (get_os_version(), "System version"),
}


def constant_documentation(output_format=FORMAT_TXT):
    """Generate the easyconfig constant documentation"""
    constant_documentation_functions = {
        FORMAT_TXT: constant_documentation_txt,
        FORMAT_RST: constant_documentation_rst,
    }

    return constant_documentation_functions[output_format]()

def constant_documentation_txt():
    """Generate easyconfig constant documentation in txt format"""
    indent_l0 = " " * 2
    indent_l1 = indent_l0 + " " * 2
    doc = []

    doc.append("Constants that can be used in easyconfigs")
    for cst, (val, descr) in EASYCONFIG_CONSTANTS.items():
        doc.append('%s%s: %s (%s)' % (indent_l1, cst, val, descr))

    return "\n".join(doc)

def constant_documentation_rst():
    """Generate easyconfig constant documentation in rst format"""
    title = "Constants that can be used in easyconfigs"
    doc = [title, "=" * len(title), '']

    table_titles = [
        "Constant name",
        "Constant value",
        "Description",
    ]

    table_values = [
        ["``%s``" % cst for cst in EASYCONFIG_CONSTANTS.keys()],
        ["``%s``" % cst[0] for cst in EASYCONFIG_CONSTANTS.values()],
        [cst[1] for cst in EASYCONFIG_CONSTANTS.values()],
    ]

    doc.extend(mk_rst_table(table_titles, table_values))

    return "\n".join(doc)
