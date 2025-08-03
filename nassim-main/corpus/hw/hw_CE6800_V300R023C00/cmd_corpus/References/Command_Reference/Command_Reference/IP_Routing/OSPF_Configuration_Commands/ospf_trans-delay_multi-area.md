ospf trans-delay multi-area
===========================

ospf trans-delay multi-area

Function
--------



The **ospf trans-delay multi-area** command configures an LSA transmission delay on a multi-area adjacency interface.

The **undo ospf trans-delay multi-area** command restores the default LSA transmission delay.



By default, the LSA transmission delay on multi-area adjacency interfaces is 1s.


Format
------

**ospf trans-delay** *delayValue* **multi-area** { *area-id* | *area-id-ipv4* }

**undo ospf trans-delay multi-area** { *area-id* | *area-id-ipv4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delayValue* | Specifies an LSA transmission delay. | The value is an integer ranging from 1 to 500, in seconds. |
| *area-id* | Specifies the ID of an OSPF area. The value is an integer. | The value can be a decimal integer ranging from 0 to 4294967295 or in the format of an IP address. |
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

The aging time of each LSA in the LSDB increases by one every second, but LSAs do not age during transmission. To configure an LSA transmission delay on a multi-area adjacency interface so that an extension period (the configured delay) is added to the LSAs to be sent, run the ospf trans-delay multi-area command. This configuration is extremely important on low-speed networks.

**Prerequisites**

The **ospf enable multi-area** command has been run.

**Precautions**

The ospf trans-delay multi-area command does not apply to null interfaces.


Example
-------

# Set the LSA transmission delay on multi-area adjacency interface to 3s.
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
[*HUAWEI-100GE1/0/1] ospf trans-delay 3 multi-area 1

```