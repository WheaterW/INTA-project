arp gratuitous-arp send enable (System view)
============================================

arp gratuitous-arp send enable (System view)

Function
--------



The **arp gratuitous-arp send enable** command enables a device to periodically send gratuitous Address Resolution Protocol (ARP) packets.

The **undo arp gratuitous-arp send enable** command disables a device from periodically sending ARP packets.



By default, a device is disabled from periodically sending ARP packets.


Format
------

**arp gratuitous-arp send enable**

**undo arp gratuitous-arp send enable**


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



If an attacker counterfeits a gateway and sends users a forged ARP packet, these user terminals will record incorrect ARP entries and cannot send data to the correct gateway. To prevent this problem, run the arp gratuitous-arp send enable command on the gateway to enable it to periodically send gratuitous ARP packets, thereby updating authorized users' ARP entries to be correct.



**Configuration Impact**



After the arp gratuitous-arp send enable command is run on a device, all interfaces on the device are enabled to periodically send gratuitous ARP packets. If the device has a lot of interfaces that are Up and have IP addresses configured, this configuration will cause the device to keep sending gratuitous ARP packets, consuming excessive CPU resources and affecting services.To disable an interface from periodically sending gratuitous ARP packets, run the **arp gratuitous-arp send disable** command in the interface view.



**Follow-up Procedure**



By default, after a device is enabled to send gratuitous ARP packets, the device sends them at an interval of 60s. To change the interval, you can run the **arp gratuitous-arp send interval** command.



**Precautions**



After the **undo arp gratuitous-arp send enable** command is run on a device, all interfaces on the device are disabled from periodically sending gratuitous ARP packets.




Example
-------

# Enable a device to periodically send gratuitous ARP packets.
```
<HUAWEI> system-view
[~HUAWEI] arp gratuitous-arp send enable

```