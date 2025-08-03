arp smart-discover enable
=========================

arp smart-discover enable

Function
--------



The **arp smart-discover enable** command enables ARP active detection.

The **undo arp smart-discover enable** command disables ARP active detection.



By default, ARP active detection is disabled.


Format
------

**arp smart-discover enable**

**undo arp smart-discover enable**


Parameters
----------

None

Views
-----

VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In scenarios where hosts connected to a device do not send ARP messages proactively, to allow the device to proactively learn ARP entries of the hosts, enable ARP active detection on the device's interface. After this function is enabled, the device sends ARP probe messages to each host on the network segment where the device (gateway) address resides at the default or configured interval (1s by default). By default, a maximum of 128 ARP probe messages are sent in each interval. Alternatively, a configured number of ARP probe messages are sent in each interval. To configure an interval at which a device sends ARP probe messages and the number of ARP probe messages to be sent in each interval, run the **arp smart-discover interval** command. The IP addresses in the existing ARP entries, device IP addresses, and VRRP virtual IP addresses are not detected.

**Precautions**

1. If the gateway address is located on a small network segment, the hosts send a large number of ARP probe messages.
2. If a host does not communicate with a device properly, the device continuously sends ARP probe messages because it cannot learn the host's ARP entries.
3. If hosts can send ARP messages proactively, do not enable this function. Otherwise, ARP learning may be slowed down.

Example
-------

# Enable ARP active detection on a VLANIF interface.
```
<HUAWEI> system-view
[~HUAWEI] interface Vlanif 123
[*HUAWEI-Vlanif123] arp smart-discover enable

```