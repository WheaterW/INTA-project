stp revertive slow
==================

stp revertive slow

Function
--------



The **stp revertive slow** command enables the delay in revertive switching during VBST calculation on a port.

The **undo stp revertive slow** command disables the delay in revertive switching during VBST calculation on a port.



By default, the delay in revertive switching disabled during VBST calculation on a port.


Format
------

**stp revertive slow**

**undo stp revertive slow**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a VBST-enabled device interworks with a PVST-enabled third-party device that does not support P/A negotiation, negotiation is asynchronous. As a result, the network convergence time is long. If the remote device is the root bridge and the VBST-enabled device provides the alternate port in addition to the interconnected port, you can enable the delay in revertive switching on the interconnected interface. The delay is calculated as follows: 2 \* Forward Delay + 8s After the delay function is enabled, the remote interface first completes spanning tree calculation when the port status changes. Then the local interface performs spanning tree status switching. During status switching, services are not interrupted.

**Precautions**

After the delay in revertive switching is enabled on a port, this function takes effect for all VLANs that the port joins. If there is no alternate port in the VLAN where the interconnected port belongs, the port needs to wait for the delay for recovery (2 x Forward Delay + 8s). Exercise caution when you run this command in this situation.


Example
-------

# Enable the delay in revertive switching during VBST calculation on the interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp revertive slow

```