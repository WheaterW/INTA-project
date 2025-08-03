multicast mvpn route-import local-admin-id
==========================================

multicast mvpn route-import local-admin-id

Function
--------



The **multicast mvpn route-import local-admin-id** command configures a local VPN instance ID for a sender PE on an MVPN.

The **undo multicast mvpn route-import local-admin-id** command deletes a local VPN instance ID of a sender PE on an MVPN.



By default, no local VPN instance ID is configured for a sender PE on an MVPN.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast mvpn route-import local-admin-id** *local-admin-id*

**undo multicast mvpn route-import local-admin-id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *local-admin-id* | Specifies a local VPN instance ID. | The value is an integer ranging from 1 to 65535. |



Views
-----

VPN instance IPv4 address family view,VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

VRF Route Import is an extended MVPN community attribute used to advertise and receive C-multicast routes. In an IPv4 Layer 3 multicast over VXLAN scenario, this attribute is contained in a BGP EVPN route that a sender PE advertises to a receiver PE. Upon receipt of the BGP EVPN route, the receiver PE saves the attribute and carries this attribute in a C-multicast route when sending this route to the sender PE. When there are multiple sender PEs, each sender PE that receives a C-multicast route can determine, according to this attribute, whether the C-multicast route should be processed by itself and which VPN routing table that the C-multicast route should be installed into.The VRF Route Import extended community is in the format of Administrator field: Local Administrator field, where Administrator field represents the local device's MVPN ID (configured using the multicast mvpn command) and Local Administrator field represents a sender PE's local VPN instance ID. To configure a local VPN instance ID for a sender PE, run the **multicast mvpn route-import** command.

**Prerequisites**

Multicast routing has been enabled using the **multicast routing-enable** command in the VPN instance IPv4 address family view.


Example
-------

# Configure 2 as a local VPN instance ID of a sender PE on an MVPN.
```
<HUAWEI> system-view
[~HUAWEI] multicast mvpn 2.2.2.2
[*HUAWEI] ip vpn-instance mcast1
[*HUAWEI-vpn-instance-mcast1] ipv4-family
[*HUAWEI-vpn-instance-mcast1-af-ipv4] route-distinguisher 1:1
[*HUAWEI-vpn-instance-mcast1-af-ipv4] multicast routing-enable
[*HUAWEI-vpn-instance-mcast1-af-ipv4] multicast mvpn route-import local-admin-id 2

```