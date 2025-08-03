arp anti-attack gateway-duplicate enable
========================================

arp anti-attack gateway-duplicate enable

Function
--------



The **arp anti-attack gateway-duplicate enable** command enables the ARP bogus gateway attack defense function.

The **undo arp anti-attack gateway-duplicate enable** command disables the ARP bogus gateway attack defense function.



By default, the ARP bogus gateway attack defense function is not enabled.


Format
------

**arp anti-attack gateway-duplicate enable**

**undo arp anti-attack gateway-duplicate enable**


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

If an attacker functions as a bogus gateway by sending ARP packets with the source IP address as the gateway IP address on a LAN, other devices on the LAN may record incorrect gateway address mappings in the ARP table. As a result, the traffic that is supposed to be sent to the gateway will be transmitted to the attacker. The attacker can then easily obtain the data content, and these devices will eventually fail to access the network.To defend against bogus gateways, you can run this command to enable the ARP bogus gateway attack defense function on the gateway directly connected to a user host. For the following conditions:

* A VLANIF interface is used to receive packets.
* The source IP address of received packets is the same as the IP address of the inbound interface.
* The source MAC address in the Ethernet header of received packets and the source MAC address in ARP packets are different from the interface MAC address.
* The source MAC address of received packets is not a virtual MAC address.If these conditions are all met, the device considers that the ARP packets have an address conflict with the gateway and generates ARP attack defense entries (such entries are not generated in virtual MAC scenarios). In addition, the device discards the packets received from the interface with the same VLAN ID or the same source MAC address in the same BD. In this manner, the ARP packets that have a gateway address conflict can be prevented from being broadcast in the VLAN or BD.

**Precautions**



Each device maintains a maximum of 1000 ARP gateway anti-collision entries at a time. If the number of ARP gateway anti-collision entries exceeds 1000, new gateway collision attacks cannot be prevented.

In scenarios where the arp anti-attack gateway-duplicate enable command is run in the system view to enable ARP gateway anti-collision on the device, ARP fast reply does not take effect.




Example
-------

# Enable the function of ARP bogus gateway attack defense.
```
<HUAWEI> system-view
[~HUAWEI] arp anti-attack gateway-duplicate enable

```