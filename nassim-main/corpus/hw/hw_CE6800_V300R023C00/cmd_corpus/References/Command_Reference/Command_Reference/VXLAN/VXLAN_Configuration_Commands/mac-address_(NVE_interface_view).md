mac-address (NVE interface view)
================================

mac-address (NVE interface view)

Function
--------



The **mac-address** command configures a MAC address for an NVE interface.

The **undo mac-address** command restores the default MAC address of an NVE interface.



By default, MAC address of an NVE interface is a system MAC address.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-address** *macaddr*

**undo mac-address** [ *macaddr* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *macaddr* | Specifies the MAC address of an NVE interface. | The value is in the H-H-H format. H is a 4-bit hexadecimal number, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF. |



Views
-----

NVE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To use active-active VXLAN gateways in distributed VXLAN gateway (EVPN BGP) scenarios, configure the same VTEP MAC address on the two gateways.


Example
-------

# Set the MAC address of an NVE interface to 00e0-fc12-3456.
```
<HUAWEI> system-view
[~HUAWEI] interface nve 1
[*HUAWEI-Nve1] mac-address 00e0-fc12-3456

```