__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.main.modules import ModuleBase
import shpc.utils as utils
import os

class Client(ModuleBase):
    def __init__(self, **kwargs):
        """
        An Lmod client generates an lmod recipe for install
        """
        super(Client, self).__init__(**kwargs)
        self.module_extension = "lua"

    def _sys_module_default_version(self, version_file, tag):
        """
        default version (default version in sys_module or True).
        We generate a file with a non-existent version number.
        """
        template = self._load_template("default_version")
        utils.write_file(version_file, template.render())

     # LMOD False or null, don't generate a .version file
