frr-policy route
================

frr-policy route

Function
--------



The **frr-policy route** command configures a filtering policy for OSPF/OSPFv3 IP FRR backup routes to control whether OSPF/OSPFv3 backup routes are added to the routing table.

The **undo frr-policy route** command disables the device from filtering backup routes for OSPF/OSPFv3 IP FRR.



By default, OSPF/OSPFv3 IP FRR-enabled backup routes are not filtered.


Format
------

**frr-policy route** { **route-policy** *route-policy-name* }

**undo frr-policy route**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-policy** *route-policy-name* | Specifies the name of an IP FRR filtering policy. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

OSPF FRR view,OSPFv3 FRR view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

OSPF/OSPFv3 IP FRR can rapidly switch traffic from a faulty link to a backup link, ensuring uninterrupted traffic transmission. OSPF/OSPFv3 IP FRR is a method to improve OSPF/OSPFv3 network reliability. After an OSPF or OSPFv3 filtering policy is configured using the **frr-policy route** command, only the backup OSPF or OSPFv3 routes that meet the filtering conditions can be added to the forwarding table. If the primary link fails, OSPF or OSPFv3 can quickly switch traffic to the backup route.

**Prerequisites**



The system has entered the OSPFv3 IP FRR view using the **frr** command, and OSPFv3 IP FRR has been enabled using the **loop-free-alternate** command.The system has entered the OSPF IP FRR view using the **frr** command, and OSPF IP FRR has been enabled using the **loop-free-alternate** command.



**Precautions**



If the command is run more than once, the last configuration overrides the previous one.




Example
-------

# Configure OSPFv3 IP FRR filtering policy abc.
```
<HUAWEI> system-view
[~HUAWEI] route-policy abc permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] frr
[*HUAWEI-ospfv3-1-frr] loop-free-alternate
[*HUAWEI-ospfv3-1-frr] frr-policy route route-policy abc

```

# Configure OSPF IP FRR filtering policy abc.
```
<HUAWEI> system-view
[~HUAWEI] route-policy abc permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] ospf 1
[*HUAWEI-ospf-1] frr
[*HUAWEI-ospf-1-frr] loop-free-alternate
[*HUAWEI-ospf-1-frr] frr-policy route route-policy abc

```