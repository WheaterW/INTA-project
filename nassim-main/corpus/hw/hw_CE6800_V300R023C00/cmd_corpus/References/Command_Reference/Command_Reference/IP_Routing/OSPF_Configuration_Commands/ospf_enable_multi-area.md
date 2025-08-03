ospf enable multi-area
======================

ospf enable multi-area

Function
--------



The **ospf enable multi-area** command enables OSPF on a multi-area adjacency interface.

The **undo ospf enable multi-area** command disables OSPF on a multi-area adjacency interface.



By default, OSPF is disabled on a multi-area adjacency interface.


Format
------

**ospf enable multi-area** { *area-id* | *area-id-ipv4* }

**undo ospf enable multi-area** { *area-id* | *area-id-ipv4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *area-id* | Specifies the ID of an OSPF area. | The value is an integer ranging from 0 to 4294967295. |
| *area-id-ipv4* | Specifies the ID of an OSPF area. | The value is in dotted decimal notation. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In OSPF, intra-area links take precedence over inter-area links. Therefore, even if a high-speed link exists between two areas, a low-speed intra-network link rather than the high-speed link is used to transmit inter-area traffic. To address this problem, run the **ospf enable multi-area** command to enable OSPF on a multi-area adjacency interface so that a link can be shared by multiple areas.

**Prerequisites**

OSPF has been enabled on the interface using the ospf enable [ process-id ] area area-id command.


Example
-------

# Enable OSPF on multi-area adjacency interface.
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

```