reset arp vpn-instance
======================

reset arp vpn-instance

Function
--------



The **reset arp vpn-instance** command clears the ARP entries of a VPN instance.




Format
------

**reset arp vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Clears ARP entries learned in a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If an unauthorized user sends a large number of ARP messages to a device, the device learns a large number of ARP entries in a short period of time, causing a buffer overflow. As a result, users may fail to access the network. To resolve the problem, run the **reset arp** command to delete invalid ARP entries so that new ARP entries can be created to allow authorized user access.



**Prerequisites**



Before running the **reset arp** command, ensure that the corresponding ARP entries exist on the device.



**Configuration Impact**



After an ARP entry is cleared, the mapping between the IP and MAC addresses in the entry is cleared. As a result, users may fail to access the network, and services may be interrupted.




Example
-------

# Clears ARP entries learned in a specified VPN instance.
```
<HUAWEI> reset arp vpn-instance vpn

```