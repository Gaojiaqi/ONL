#!/usr/bin/python
############################################################
# <bsn.cl fy=2013 v=none>
#
#        Copyright 2013, 2014 BigSwitch Networks, Inc.
#
#
#
# </bsn.cl>
############################################################
#
# Platform driver for the Accton AS7712-32X
#
############################################################
import subprocess
import os
from onl.platform.base import *
from onl.vendor.accton import *

class OpenNetworkPlatformImplementation(OpenNetworkPlatformAccton):

    def model(self):
        return "AS7712-32X"

    def platform(self):
        return "x86-64-accton-as7712-32x-r0"

    def _plat_info_dict(self):
        return {
            platinfo.LAG_COMPONENT_MAX : 24,
            platinfo.PORT_COUNT : 32,
            platinfo.ENHANCED_HASHING : True,
            platinfo.SYMMETRIC_HASHING : True,
            }

    def sys_init(self):
        pass

    def sys_oid_platform(self):
        return ".7712.32"

    def baseconfig(self):
        return os.system(os.path.join(self.platform_basedir(), "boot", "x86-64-accton-as7712-32x-rx-devices.sh")) == 0

if __name__ == "__main__":
    print OpenNetworkPlatformImplementation()

