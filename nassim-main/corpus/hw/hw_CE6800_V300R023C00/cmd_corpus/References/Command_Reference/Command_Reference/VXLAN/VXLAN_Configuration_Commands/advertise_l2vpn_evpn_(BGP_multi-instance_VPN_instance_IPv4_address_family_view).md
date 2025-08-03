advertise l2vpn evpn (BGP multi-instance VPN instance IPv4 address family view)
===============================================================================

advertise l2vpn evpn (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **advertise l2vpn evpn** command enables a device to advertise IP routes from a VPN instance to its EVPN instance.

The **undo advertise l2vpn evpn** command restores the default configuration..



By default, a device is disabled from advertising IP routes from a VPN instance to its EVPN instance.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**advertise l2vpn evpn** [ **import-route-multipath** ] [ **include-local-cross-route** ]

**undo advertise l2vpn evpn** [ **import-route-multipath** ] [ **include-local-cross-route** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **import-route-multipath** | Advertises all routes with the same destination address in a VPN instance to an EVPN instance. | - |
| **include-local-cross-route** | Advertises all routes of local cross in a VPN instance to an EVPN instance. | - |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After VTEPs establish VXLAN tunnels through IP prefix routes, run the **advertise l2vpn evpn** command to enable a VTEP to advertise host routes from a VPN instance to its EVPN instance. The VTEP then sends host routes to the remote VTEP through the BGP EVPN peer relationship.By default, the VPN instance local cross-route is not sent to the EVPN instance. To solve the problem of mutual access between different VRFs, you can enable the VPN instance to publish the local cross-connect function to the EVPN instance, and send the local cross-route collected by the VPN instance To the EVPN instance, and then send it to the remote device through the BGP EVPN peer relationship.In BGP VPN multi-instance scenarios, routes cannot be locally leaked between BGP VPN instances. For example, if VRF1 is a common BGP VPN instance and VRF2 is a BGP VPN multi-instance, routes imported or remotely leaked to VRF1 cannot be locally leaked to VRF2.


Example
-------

# Enable a device to advertise IP routes from VPN instance vpna to its EVPN instance.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100 instance evrf
[*HUAWEI-bgp-instance-evrf] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-evrf-vpna] advertise l2vpn evpn

```