port-mirroring observe-port group
=================================

port-mirroring observe-port group

Function
--------



The **port-mirroring observe-port group** command enables the device to mirror packets to an observing port group.

The **undo port-mirroring** command disables the device from mirroring packets to an observing port group.



By default, port mirroring is not configured on a port.


Format
------

**port-mirroring observe-port group** *group-id* { **inbound** | **outbound** | **both** }

**undo port-mirroring** [ **observe-port** **group** *group-id* ] { **inbound** | **outbound** | **both** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-id* | Specifies the ID of an observing port group. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 128.  For the CE6885-LL (low latency mode):The value is an integer that ranges from 1 to 8. |
| **inbound** | Assign mirror to the inbound of an interface. | - |
| **outbound** | Assign mirror to the outbound of an interface. | - |
| **both** | Assign mirror to both inbound and outbound of an interface. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To mirror packets to multiple observing port, configure an observing port group. The mirrored packets are then copied to all the member ports of the observing port group.


Example
-------

# Mirror incoming traffic on 100GE1/0/3 to observing group 1.
```
<HUAWEI> system-view
[~HUAWEI] observe-port group 1
[*HUAWEI-observe-port-group-1] group-member 100GE 1/0/1 to 100GE 1/0/2
[*HUAWEI-observe-port-group-1] quit
[*HUAWEI] commit
[~HUAWEI] interface 100GE 1/0/3
[~HUAWEI-100GE1/0/3] port-mirroring observe-port group 1 inbound

```