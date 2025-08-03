reset arp all
=============

reset arp all

Function
--------



The **reset arp all** command clears all ARP entries.




Format
------

**reset arp all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Clears all ARP entries. | - |



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

# Clear dynamic ARP entries.
```
<HUAWEI> reset arp all

```