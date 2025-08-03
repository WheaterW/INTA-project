description (VNI peer view)
===========================

description (VNI peer view)

Function
--------



The **description** command configures a description for a peer VXLAN tunnel.

The **undo description** command deletes the description configured for a peer VXLAN tunnel.



By default, no description is configured for a peer VXLAN tunnel.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**description** *desc*

**undo description** [ *desc* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *desc* | Specifies a description for a peer VXLAN tunnel. | The value is a string of 1 to 64 case-sensitive characters, spaces supported. |



Views
-----

VNI peer view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To use the DHCP Option 82 function in a BD for security reasons, run the **description** command to configure different descriptions for different VXLAN tunnels. The descriptions carried in the Option 82 fields of DHCP packets help you determine through which VXLAN tunnel each user goes online.


Example
-------

# Configure the description as VXLAN for a VXLAN tunnel with the VNI ID of 4096 and the peer IP address of 1.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] vni 4096
[*HUAWEI-vni4096] peer 1.1.1.1
[*HUAWEI-vni4096-peer1.1.1.1] description VXLAN

```