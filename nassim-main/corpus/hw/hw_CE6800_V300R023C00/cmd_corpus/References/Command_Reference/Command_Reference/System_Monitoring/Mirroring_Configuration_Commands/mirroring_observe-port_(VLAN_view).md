mirroring observe-port (VLAN view)
==================================

mirroring observe-port (VLAN view)

Function
--------



The **mirroring observe-port** command configures VLAN mirroring.

The **undo mirroring** command deletes VLAN mirroring configuration.



By default, VLAN mirroring is not configured.


Format
------

**mirroring observe-port** { *observe-port-index* | **group** *group-id* } { **inbound** | **outbound** | **both** }

**undo mirroring** [ **observe-port** { *observe-port-index* | **group** *group-id* } ] { **inbound** | **outbound** | **both** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **group** *group-id* | Specifies the index of an observing port group. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 128.  For the CE6885-LL (low latency mode):The value is an integer that ranges from 1 to 8. |
| **inbound** | Indicates that mirroring is configured for the incoming traffic in the VLAN. | - |
| **outbound** | Indicates that mirroring is configured for the outgoing traffic in the VLAN. | - |
| **both** | Indicates that mirroring is configured for the incoming and outgoing traffic in the VLAN. | - |
| **observe-port** *observe-port-index* | Specifies the index of an observing port. | The value is an integer that ranges from 1 to 8. |



Views
-----

VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Users can use the **mirroring observe-port** command to mirror the traffic on all active ports in a specified VLAN to an observing port. Users can also run the **mirroring observe-port group** command to mirror the traffic to an observing port group so that the packets are copied to all the member ports of the observing port group.

**Prerequisites**

An observing port has been configured using the **observe-port** command or an observing port group has been configured using the **observe-port group** command.

**Implementation Procedure**

The traffic in the same direction of all active ports in a specified VLAN cannot be concurrently mirrored to an observing port and an observing port group.


Example
-------

# Mirror incoming packets on active ports in VLAN 10 to observing port 1.
```
<HUAWEI> system-view
[~HUAWEI] observe-port 1 interface 100GE 1/0/1
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] mirroring observe-port 1 inbound

```

# Mirror incoming packets on active ports in VLAN 10 to observing port group 1.
```
<HUAWEI> system-view
[~HUAWEI] observe-port group 1
[*HUAWEI-observe-port-group-1] vlan 10
[*HUAWEI-vlan10] mirroring observe-port group 1 inbound

```