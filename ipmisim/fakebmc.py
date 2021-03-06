# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ipmisim - Fake IPMI simulator for testing, forked from Conpot
# Maintainer - Rohit Yadav <bhaisaab@apache.org>
# Original Author: Peter Sooky <xsooky00@stud.fit.vubtr.cz>
# Brno University of Technology, Faculty of Information Technology

import logging

from pyghmi.ipmi.bmc import Bmc


logger = logging.getLogger('ipmisim')


class FakeBmc(Bmc):

    def __init__(self, authdata):
        self.authdata = authdata
        # Initialize fake BMC config
        self.deviceid = 0x24
        self.revision = 0x10
        self.firmwaremajor = 0x10
        self.firmwareminor = 0x1
        self.ipmiversion = 2
        self.additionaldevices = 0
        self.mfgid = 0xf
        self.prodid = 0xe

        self.powerstate = 'off'
        self.bootdevice = 'default'
        logger.info('IPMI BMC initialized.')

    def get_boot_device(self):
        logger.info('IPMI BMC Get_Boot_Device request.')
        return self.bootdevice

    def set_boot_device(self, bootdevice):
        logger.info('IPMI BMC Set_Boot_Device request.')
        self.bootdevice = bootdevice

    def cold_reset(self):
        logger.info('IPMI BMC Cold_Reset request.')
        self.powerstate = 'off'
        self.bootdevice = 'default'

    def get_power_state(self):
        logger.info('IPMI BMC Get_Power_State request.')
        return self.powerstate

    def power_off(self):
        logger.info('IPMI BMC Power_Off request.')
        self.powerstate = 'off'

    def power_on(self):
        logger.info('IPMI BMC Power_On request.')
        self.powerstate = 'on'

    def power_reset(self):
        logger.info('IPMI BMC Power_Reset request.')
        # warm boot
        self.powerstate = 'on'

    def power_cycle(self):
        logger.info('IPMI BMC Power_Cycle request.')
        # cold boot
        self.powerstate = 'off'
        self.powerstate = 'on'

    def power_shutdown(self):
        logger.info('IPMI BMC Power_Shutdown request.')
        self.powerstate = 'off'
