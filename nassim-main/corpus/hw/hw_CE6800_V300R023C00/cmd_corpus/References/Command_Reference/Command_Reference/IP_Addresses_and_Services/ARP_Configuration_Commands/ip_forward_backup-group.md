ip forward backup-group
=======================

ip forward backup-group

Function
--------



The **ip forward backup-group** command configures an interface backup group.

The **undo ip forward backup-group** command deletes the configuration of an interface backup group.



By default, no backup group is configured.


Format
------

**ip forward backup-group** *backup-group-name* **member** { *ifname1* | *iftype1* *ifnumber1* } { *ifname2* | *iftype2* *ifnumber2* }

**undo ip forward backup-group** *backup-group-name* **member** { *ifname1* | *iftype1* *ifnumber1* } { *ifname2* | *iftype2* *ifnumber2* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **member** | Indicates members. | - |
| *ifname1* | Specifies the name of interface 1 in the backup group. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| *iftype1* | Specifies the type of interface 1 in the backup group. | - |
| *ifnumber1* | Specifies the number of interface 1 in the backup group. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| *ifname2* | Specifies the name of interface 2 in the backup group. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| *iftype2* | Specifies the type of interface 2 in the backup group. | - |
| *ifnumber2* | Specifies the number of interface 2 in the backup group. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| **backup-group** *backup-group-name* | Specifies the name of the interface backup group. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In an M-LAG scenario, the active firewall or the ARP/ND connection between the active firewall and the device may be faulty. To ensure network stability, the ARP/ND connection needs to be switched from the active firewall to the standby firewall. In this case, you can run the **ip forward backup-group** command to configure the two interfaces on the active and standby firewalls to back up each other, implementing a fast and stable ARP/ND connection switchover.

**Prerequisites**

Interfaces have been created.

**Precautions**

* Currently, only Layer 2 Eth-Trunk interfaces are supported.
* Two identical interfaces cannot be configured in the same backup group.
* An interface that has been configured for another backup group cannot be configured.
* A configured interface in a backup group can be modified, but the interface cannot be changed to an existing interface in another backup group.
* After an Eth-Trunk interface is added to a backup group, the Eth-Trunk interface cannot be deleted. The interface can be deleted only after the backup group configuration is deleted.
* After an Eth-Trunk interface is added to a backup group, it cannot be configured as a Layer 3 interface. The interface can be configured as a Layer 3 interface only after the backup group configuration is deleted.

Example
-------

# Add Eth-Trunk 1 and Eth-Trunk 2 to the backup group bkN12.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[*HUAWEI-Eth-Trunk1] interface Eth-Trunk 2
[*HUAWEI-Eth-Trunk2] quit
[*HUAWEI] ip forward backup-group bkN12 member Eth-Trunk 1 Eth-Trunk 2

```