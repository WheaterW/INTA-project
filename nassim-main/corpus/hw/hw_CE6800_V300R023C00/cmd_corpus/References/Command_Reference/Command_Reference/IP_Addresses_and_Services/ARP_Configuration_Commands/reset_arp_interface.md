reset arp interface
===================

reset arp interface

Function
--------



The **reset arp interface** command clears ARP entries learned by a specified interface.




Format
------

**reset arp interface** { *interface-name* | *interface-type* *interface-number* } [ **ip** *ip-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** *ip-address* | Clears dynamic ARP entries containing a specified IP address. | The value is in dotted decimal notation. |
| **interface** *interface-name* | Clears dynamic ARP entries learned on a specified the name interface. | - |
| **interface** *interface-type* *interface-number* | Clears all dynamic ARP entries learned by a specified interface. | - |



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



ARP entries exist on a device.The interface specified by interface ifName exists if this parameter is configured.



**Configuration Impact**



After an ARP entry is cleared, the mapping between the IP and MAC addresses in the entry is cleared. As a result, users may fail to access the network, and services may be interrupted.




Example
-------

# Clear dynamic ARP entries containing the IP address 10.1.1.1 on the interface.
```
<HUAWEI> reset arp interface 100GE 1/0/1 ip 10.1.1.1

```

# Clear dynamic ARP entries on the interface.
```
<HUAWEI> reset arp interface 100GE 1/0/1

```