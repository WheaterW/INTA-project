arp ip-conflict-detect enable
=============================

arp ip-conflict-detect enable

Function
--------



The **arp ip-conflict-detect enable** command enables remote IP address conflict detection.

The **undo arp ip-conflict-detect enable** command disables remote IP address conflict detection.



By default, remote IP address conflict detection is disabled.


Format
------

**arp ip-conflict-detect enable**

**undo arp ip-conflict-detect enable**


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

When receiving a non-gratuitous ARP (Address Resolution Protocol) packet, the device checks the address information carried in the ARP packet. The device considers that an IP address conflict occurs on the network in the following situations:

* Probe IP conflict: The interface receives a Probe ARP packet, and the destination IP address of the packet conflicts with the local interface address. This scenario is not controlled by this command.
* Remote IP conflict: The local device detects an IP address conflict between connected devices or users. That is, the source IP address in the ARP packet received by the local device is the same as the IP address in an existing ARP entry on the local device, but the source MAC address is different from the MAC address in the corresponding ARP entry.When an IP address conflict occurs between devices on a network, the CPU usage of the devices is high and routes on the devices flap frequently. This greatly affects user services and even interrupts user services. To help users better manage addresses of devices on the network and prevent address conflicts from affecting user services, run the command to enable remote IP address conflict detection.

**Precautions**



In scenarios where the arp ip-conflict-detect enable command is run in the system view to enable IP address conflict detection on the device, ARP fast reply does not take effect.




Example
-------

# Enable IP address conflict detection.
```
<HUAWEI> system-view
[~HUAWEI] arp ip-conflict-detect enable

```