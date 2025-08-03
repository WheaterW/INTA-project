stp loop-protection (Layer 2 interface view)
============================================

stp loop-protection (Layer 2 interface view)

Function
--------



The **stp loop-protection** command enables loop protection on a port.

The **undo stp loop-protection** command disables loop protection on a port.



By default, loop protection is disabled on ports.


Format
------

**stp loop-protection**

**undo stp loop-protection**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a network running STP, a device maintains the status of the root port and blocked port by continually receiving Bridge Protocol Data Units (BPDUs) from the upstream device. If ports cannot receive BPDUs from the upstream device due to link congestion or unidirectional link failures, the device will re-select a root port. Then, the previous root port becomes a designated port and the previous blocked port enters the Forwarding state. As a result, loops may occur on the network.To prevent network loops, run the stp loop-protection command to configure loop protection. If the root port or the Alternate port cannot receive BPDUs from the upstream device for a long period of time after the loop protection function is enabled, the root port or the Alternate port will send a notification message to the NMS. The root port will enter the Discarding state, and the Alternate port remains in the blocked state and no longer forwards packets. This prevents loops on the network. The root port or Alternate port restores the Forwarding state after receiving BPDUs.An Alternate port is the backup of the root port. When the root port can normally send and receive BPDUs, the Alternate port is in the blocked state.Between two interconnected devices on a spanning tree, the device closer to the root bridge is the upstream device of the other device.



**Prerequisites**



If loop protection needs to be configured on an interface in a non-zero process, the **stp binding process** command must have been run to bind this interface to the process.




Example
-------

# Enable loop protection on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp loop-protection

```