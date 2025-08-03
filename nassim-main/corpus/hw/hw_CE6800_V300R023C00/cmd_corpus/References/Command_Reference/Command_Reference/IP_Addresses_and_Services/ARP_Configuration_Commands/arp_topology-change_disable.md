arp topology-change disable
===========================

arp topology-change disable

Function
--------



The **arp topology-change disable** command disables the device from responding to Topology Checksum (TC) packets.

The **undo arp topology-change disable** command enables the device to respond to TC packets.



By default, the device responds to TC packets.


Format
------

**arp topology-change disable**

**undo arp topology-change disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, after a loop-prevention protocol detects a network topology change, it will send a protocol packet to instruct the device to age or delete ARP entries. Then the device will re-learn ARP entries.However, if the network topology changes frequently or a device has a large number of ARP entries, re-learning of ARP entries causes ARP entry flooding, which consumes network resources and affects other services on the device. To resolve this problem, run the arp topology-change disable command to disable the device from responding to TC packets.



**Precautions**



After the arp topology-change disable command is run, the device will not age or delete ARP entries. Therefore, if an ARP entry does not contain the latest information about a peer device, services will be interrupted between the local and peer devices.




Example
-------

# Disable the device from responding to TC packets.
```
<HUAWEI> system-view
[~HUAWEI] arp topology-change disable

```