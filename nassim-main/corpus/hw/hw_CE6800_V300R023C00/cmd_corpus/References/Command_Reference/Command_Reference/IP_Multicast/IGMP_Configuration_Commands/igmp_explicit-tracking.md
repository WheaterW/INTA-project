igmp explicit-tracking
======================

igmp explicit-tracking

Function
--------



The **igmp explicit-tracking** command enables host tracking on an interface.

The **undo igmp explicit-tracking** command restores the default configuration.



By default, host tracking is disabled on an interface.


Format
------

**igmp explicit-tracking**

**undo igmp explicit-tracking**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In Layer 3 multicast scenarios, after a multicast device receives a host's Leave message for a group, the device sends a group-specific Query message and considers that the host has left the group only if the device does not receive a response from the host within a specified wait period.To speed up the device's response to host leave requests, run the igmp explicit-tracking command to enable host tracking. After this function takes effect, the device records group join status of each multicast host and does not send a group-specific Query message any more after receiving a Leave message. The device considers that a host has left a group immediately after receiving a Leave message from the host. This function shortens the leave process and reduces network bandwidth consumption.

**Prerequisites**

IGMP has been enabled using the **igmp enable** command.

**Precautions**

The igmp explicit-tracking command applies only to IGMPv3-enabled interfaces that have IGMPv3 access users only.If a host has joined a multicast group before the igmp explicit-tracking command is run, the command configuration takes effect for the host only after the host's join status information is obtained, instead of taking effect immediately. To have the command configuration quickly take effect for such hosts, run the **reset igmp group** command to delete multicast group join information.Running the **reset igmp group** command interrupts ongoing multicast services for a short time. The services can be restored only after hosts join multicast groups again.


Example
-------

# Enable host tracking on an interface.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[~HUAWEI] vlan 10
[~HUAWEI] interface vlanif 10
[~HUAWEI-Vlanif10] igmp enable
[*HUAWEI-Vlanif10] igmp version 3
[*HUAWEI-Vlanif10] igmp explicit-tracking

```