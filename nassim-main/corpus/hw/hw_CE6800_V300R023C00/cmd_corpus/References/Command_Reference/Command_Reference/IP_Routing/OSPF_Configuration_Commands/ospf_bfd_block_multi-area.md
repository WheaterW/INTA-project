ospf bfd block multi-area
=========================

ospf bfd block multi-area

Function
--------



The **ospf bfd block multi-area** command disables BFD on a multi-area adjacency interface.

The **undo ospf bfd block multi-area** command enables BFD on a multi-area adjacency interface.



By default, BFD is enabled on multi-area adjacency interfaces.


Format
------

**ospf bfd block multi-area** { *area-id* | *area-id-ipv4* }

**undo ospf bfd block multi-area** { *area-id* | *area-id-ipv4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *area-id* | Specifies the ID of an OSPF area. The value is an integer. | The value is a decimal integer ranging from 0 to 4294967295. |
| *area-id-ipv4* | Specifies the ID of an OSPF area, in the format of an IP address. | The value is in the format X.X.X.X, where each X represents a value from 0 to 255 |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the **bfd all-interfaces enable** command is run in an OSPF process, all interfaces on which neighbor relationships are in Full state in the OSPF process create BFD sessions. To disable BFD on a multi-area adjacency interface, run the ospf bfd block multi-area command.

**Prerequisites**

* BFD has been enabled on the interface.
* the ospf enable multi-area command has been run.

Example
-------

# Disable BFD on a multi-area adjacency interface.
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
[*HUAWEI-100GE1/0/1] ospf bfd block multi-area 1

```