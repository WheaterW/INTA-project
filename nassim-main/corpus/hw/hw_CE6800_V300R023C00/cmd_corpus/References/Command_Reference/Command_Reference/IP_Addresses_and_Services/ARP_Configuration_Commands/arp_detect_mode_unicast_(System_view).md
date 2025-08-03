arp detect mode unicast (System view)
=====================================

arp detect mode unicast (System view)

Function
--------



The **arp detect mode unicast** command configures an interface to send ARP aging probe messages in unicast mode.

The **undo arp detect mode unicast** command restores the default configuration.



By default, an interface sends the last ARP aging probe message in broadcast mode and the rest ARP aging probe messages in unicast mode.


Format
------

**arp detect mode unicast**

**undo arp detect mode unicast**


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



Before aging ARP entries, an interface sends ARP aging probe messages at a specified aging probe interval. If responses are received, the device updates ARP entries on the interface. If no response is received for some ARP entries within a specified interval, the device ages these ARP entries. An aging probe message can be unicast or broadcast. To configure an interface to send aging probe messages in unicast mode, run the arp detect-mode unicast command.If a non-Huawei device receives an ARP aging probe message with the destination MAC address as the broadcast address from a Huawei device, but the IP-MAC mapping of the Huawei already exists in its ARP table, the non-Huawei device discards the ARP aging probe message. Because the Huawei device fails to receive a response to the ARP aging probe message, the Huawei device deletes the corresponding ARP entry. As a result, the traffic from the network side is interrupted. To resolve this problem, the Huawei device must be configured to send ARP aging probe messages in unicast mode, and non-Huawei devices must be able to respond to unicast ARP aging probe messages.



**Precautions**



If the IP address of the peer device remains the same but the MAC address changes frequently, configuring an interface to send ARP aging probe messages in broadcast mode is recommended.If the MAC address of the peer device remains the same, the network bandwidth is insufficient, and the aging time of ARP entries is set to a small value, configuring an interface to send ARP aging probe messages in unicast mode is recommended.




Example
-------

# Configure an interface to send ARP aging probe messages in unicast mode.
```
<HUAWEI> system-view
[~HUAWEI] arp detect mode unicast

```