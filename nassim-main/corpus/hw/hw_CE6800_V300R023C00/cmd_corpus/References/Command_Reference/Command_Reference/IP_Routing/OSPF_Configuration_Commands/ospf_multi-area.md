ospf multi-area
===============

ospf multi-area

Function
--------



The **ospf frr block multi-area** command blocks FRR on a specified OSPF multi-area adjacency interface.

The **undo ospf frr block multi-area** command restores the default configuration.



By default, FRR is not blocked on a multi-area adjacency interface.


Format
------

**ospf frr block multi-area** { *area-id* | *area-id-ipv4* }

**undo ospf frr block multi-area** { *area-id* | *area-id-ipv4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *area-id* | Specifies the ID of an OSPF area. The value is an integer. | The value is a decimal integer ranging from 0 to 4294967295. |
| *area-id-ipv4* | Specifies the ID of an OSPF area, in the format of an IP address. | The value is in the format X.X.X.X, where each X represents a value from 0 to 255 |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **ospf frr block multi-area** command on a device that transmits important services to prevent the device from becoming a node on the backup link. This prevents services from being affected after FRR calculation.

**Prerequisites**

The **ospf enable multi-area** command has been run.

**Precautions**

Before configuring OSPF IP FRR, run the ospf frr block command to block FRR on a specified interface. In this manner, the link where the interface resides is not calculated as a backup link during FRR calculation.


Example
-------

# Disable OSPF IP FRR on a multi-area adjacency interface.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] area 0
[*HUAWEI-ospf-1-area-0.0.0.0] quit
[*HUAWEI-ospf-1] area 1
[*HUAWEI-ospf-1-area-0.0.0.1] quit
[*HUAWEI-ospf-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf enable 1 area 0
[*HUAWEI-100GE1/0/1] ospf enable multi-area 1
[*HUAWEI-100GE1/0/1] ospf frr block multi-area 1

```