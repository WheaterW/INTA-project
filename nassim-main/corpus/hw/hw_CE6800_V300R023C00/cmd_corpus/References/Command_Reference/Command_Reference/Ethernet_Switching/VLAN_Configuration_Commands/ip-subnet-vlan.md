ip-subnet-vlan
==============

ip-subnet-vlan

Function
--------



The **ip-subnet-vlan** command configures an IP subnet-based VLAN and 802.1p priority for this VLAN.

The **undo ip-subnet-vlan** command deletes the IP subnet-based VLAN configuration.



By default, no IP subnet-based VLAN is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip-subnet-vlan** [ *ip-subnet-index* ] **ip** *ip-address* { *mask* | *mask-length* } [ **priority** *priority* ]

**undo ip-subnet-vlan** { *ip-subnet-index* [ **to** *ip-subnet-end* ] | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-subnet-index* | Specifies the start subnet number. | The value is an integer that ranges from 1 to 12. |
| **ip** *ip-address* | Specifies a source IP address or network segment to be associated with a VLAN. | The value is in dotted decimal notation. |
| *mask* | Specifies a subnet mask. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the subnet mask length. | The value is an integer that ranges from 1 to 12. |
| **priority** *priority* | Specifies the 802.1p priority of a VLAN associated with the specified IP address or network segment. | The value is an integer that ranges from 0 to 7. The greater the value, the higher the priority. The default value is 0. |
| **to** *ip-subnet-end* | Specifies the end subnet number. | The value is an integer that ranges from 1 to 12. |
| **all** | Indicates all IP subnet-based VLANs. | - |



Views
-----

VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

IP subnet-based VLAN division is also called network layer-based VLAN division.Network layer-based VLAN division greatly reduces the workload of manual configurations and allows users to easily join a VLAN, move from one VLAN to another VLAN, or leave a VLAN.IP subnet-based VLAN division is applicable to networks that have traveling users and require simple management.

**Configuration Impact**

After a Layer 2 device receives untagged packets, it determines the VLANs to which the packets belong based on the packets' source IP addresses and then sends the packets to correct VLANs.

**Precautions**

1. The IP address must be a class A, B, or C address rather than a broadcast address.
2. A subnet segment can be associated with only one VLAN.
3. Different indexes cannot be associated with the same subnet segment.

Example
-------

# Associate VLAN 3 with network segment 10.10.10.1/24 to allow packets with the source IP addresses of this network segment to be transmitted in VLAN 3.
```
<HUAWEI> system-view
[~HUAWEI] vlan 3
[*HUAWEI-vlan3] ip-subnet-vlan ip 10.10.10.1 255.255.255.0

```