m-lag unpaired-port reserved
============================

m-lag unpaired-port reserved

Function
--------



The **m-lag unpaired-port reserved** command configures an interface not to enter the error-down state when the peer-link fails but the DAD status is normal.

The **undo m-lag unpaired-port reserved** command restores the default configuration of an interface when the peer-link fails but the DAD status is normal.



By default, this command is not configured on any interface.


Format
------

**m-lag unpaired-port reserved**

**undo m-lag unpaired-port reserved**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When M-LAG is used for dual-homing access on a common Ethernet, VXLAN, or IP network, if the peer-link fails but the DAD status is normal, interfaces excluding the management interface and peer-link interface on one M-LAG device are triggered to enter the error-down state. When the peer-link recovers, the M-LAG member interface in the error-down state automatically restores to the up state after 4 minutes by default, and the other interfaces in the error-down state automatically restore to the up state immediately.In actual networking, however, uplink interfaces running a routing protocol or interfaces at both ends of the DAD link should not enter the error-down state. You can configure this function on such interfaces based on actual requirements.

**Precautions**

It is recommended that you configure this command on interfaces of both the M-LAG master and backup devices to ensure that the interfaces in the error-down state on the two devices are consistent after a master/backup switchover.This command cannot be configured on peer-link interfaces or M-LAG member interfaces.This command cannot be configured on a physical interface that has been added to an Eth-Trunk interface.This command and the **m-lag unpaired-port suspend** command cannot be configured on the same interface of a device.A maximum of 1024 interfaces can be configured with this command.


Example
-------

# Configure Eth-Trunk 2 on the device not to enter the error-down state.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 2
[*HUAWEI-Eth-Trunk2] m-lag unpaired-port reserved

```