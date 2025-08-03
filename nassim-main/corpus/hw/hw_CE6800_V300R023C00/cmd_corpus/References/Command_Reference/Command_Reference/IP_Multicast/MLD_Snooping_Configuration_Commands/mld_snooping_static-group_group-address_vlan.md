mld snooping static-group group-address vlan
============================================

mld snooping static-group group-address vlan

Function
--------



The **mld snooping static-group group-address vlan** command configures static member interfaces for a multicast group in a VLAN.

The **undo mld snooping static-group group-address vlan** command cancels the configuration.



By default, no static member interfaces are configured for a multicast group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping static-group** [ **source-address** *source-address* ] **group-address** *group-address* **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>

**undo mld snooping static-group** [ **source-address** *source-address* ] **group-address** { **all** | *group-address* } **vlan** { **all** | { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **source-address** *source-address* | Specifies a multicast source address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *group-address* | Specifies a multicast group address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. The value range is FF00::-FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF. Addresses starting with FFX1 and FFX2 are reserved group addresses and cannot be used. |
| *vlan-id1* | Specifies a VLAN ID. | The value is an integer ranging from 1 to 4094. |
| **to** *vlan-id2* | Specifies a VLAN ID. The value of vlan-id2 must be greater than that of vlan-id1. | The value is an integer ranging from 1 to 4094. |
| **all** | Indicates all of multicast group addresses. | - |
| **all** | Indicates all of VLANs. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If hosts need to regularly receive the data of a multicast group (including source-specific group) on an interface, run the mld snooping static-group command to configure the interface as a static member interface of the multicast group.

**Prerequisites**

MLD snooping has been enabled globally and in the VLAN view.


Example
-------

# Configure 100GE 1/0/1 in VLAN 2 as a static member interface of multicast group FF33::1.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] mld snooping static-group group-address ff33::1 vlan 2

```