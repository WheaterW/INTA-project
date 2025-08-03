reset arp dynamic ip
====================

reset arp dynamic ip

Function
--------



The **reset arp dynamic ip** command clears dynamic ARP entries containing a specified IP address.




Format
------

**reset arp dynamic ip** *ipAddrValue*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipAddrValue* | Clears dynamic ARP entries containing a specified IP address learned on a specified interface.  This parameter can be configured if you only want to delete one of the several ARP entries learned on a specified interface. | The value is in dotted decimal notation. |



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



ARP entries exist on a device.



**Configuration Impact**



After an ARP entry is cleared, the mapping between the IP and MAC addresses in the entry is cleared. As a result, users may fail to access the network, and services may be interrupted.




Example
-------

# Clears the dynamic ARP entries containing a specified IP address 10.1.1.1 in an ARP table.
```
<HUAWEI> reset arp dynamic ip 10.1.1.1

```