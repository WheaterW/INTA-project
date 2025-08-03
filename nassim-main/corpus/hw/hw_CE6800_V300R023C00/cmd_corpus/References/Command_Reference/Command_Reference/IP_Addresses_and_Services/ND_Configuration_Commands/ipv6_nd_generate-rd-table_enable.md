ipv6 nd generate-rd-table enable
================================

ipv6 nd generate-rd-table enable

Function
--------



The **ipv6 nd generate-rd-table enable** command enables a device to generate ND entries based on host information synchronized from EVPN routes.

The **undo ipv6 nd generate-rd-table enable** command restores the default configuration and deletes ND entries generated based on host information synchronized from EVPN routes.



By default, a device is disabled from generating ND entries based on host information synchronized from EVPN routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd generate-rd-table enable**

**undo ipv6 nd generate-rd-table enable**


Parameters
----------

None

Views
-----

VBDIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the NFVI distributed gateway scenario where BGP EVPN peer relationships are established between L2GWs/L3GWs and DC-GWs, L2GWs or L3GWs learn MAC address and ND information through the data plane and advertise the information to DC-GWs through EVPN routes. This allows ND entries to be generated for Layer 2 forwarding and ensures that user services run properly. To enable a device to generate ND entries based on host information synchronized from EVPN routes, run the **ipv6 nd generate-rd-table enable** command.

**Prerequisites**

IPv6 has been enabled using the **ipv6 enable** command in the VBDIF interface view.

**Configuration Impact**

After the **undo ipv6 nd generate-rd-table enable** command is run, the device deletes ND entries generated based on host information synchronized from EVPN routes and will not generate ND entries upon receipt of host information synchronized from EVPN routes advertised by the peer.


Example
-------

# Enable VBDIF 10 to generate ND entries based on host information synchronized from EVPN routes.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] commit
[~HUAWEI-bd10] quit
[~HUAWEI] interface vbdif 10
[*HUAWEI-Vbdif10] ipv6 enable
[*HUAWEI-Vbdif10] ipv6 nd generate-rd-table enable

```