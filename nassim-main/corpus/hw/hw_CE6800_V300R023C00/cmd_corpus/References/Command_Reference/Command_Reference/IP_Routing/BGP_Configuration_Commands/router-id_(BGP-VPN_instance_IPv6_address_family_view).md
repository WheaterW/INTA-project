router-id (BGP-VPN instance IPv6 address family view)
=====================================================

router-id (BGP-VPN instance IPv6 address family view)

Function
--------



The **router-id** command configures a router ID for the BGP-VPN instance IPv6 address family.

The **undo router-id** command deletes the router ID configured for the BGP-VPN instance IPv6 address family.



By default, if no router ID is configured for the BGP VPN instance IPv4/IPv6 address family, the BGP router ID (if any) is used. If no BGP router ID exists, an interface IP address in the VPN instance is used.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**router-id** { *router-id-value* | **auto-select** }

**undo router-id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *router-id-value* | Specifies a router ID in the IPv4 address format. The router ID 0.0.0.0 is not supported. | The value is in dotted decimal notation. |
| **auto-select** | Configures automatic route ID selection for the current BGP VPN instance IPv4/IPv6 address family. | - |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a router ID is configured for the BGP-VPN instance IPv6 address family, the router ID of the BGP-VPN instance IPv6 address family can be distinguished from the router ID of BGP, meeting the requirements of specific scenarios.For example, two VPN instances vrf1 and vrf2 are configured on a BGP device. To establish a BGP session between vrf1 and vrf2 through the bound interfaces, you can configure different router IDs for the BGP-VPN instance IPv4 address family. If the router ID is not configured, the BGP peer relationship cannot be established because the router IDs in the BGP-VPN instance IPv4 address family are the same as the BGP router ID.The rules for selecting a router ID for a BGP-VPN instance are as follows:

* If loopback interfaces configured with IP addresses are bound to the VPN instance, the largest IP address among the IP addresses of the loopback interfaces is selected as the router ID.
* If no loopback interface configured with an IP address is bound to the VPN instance, the largest IP address among the other interfaces bound to the VPN instance is selected as the router ID, regardless of whether the interface is Up or Down.

**Configuration Impact**



If the router ID of a BGP-VPN instance IPv6 address family is changed or the configured router ID is deleted, BGP sessions established in the BGP-VPN instance IPv6 address family will be reset. Exercise caution when running this command.



**Precautions**

If a BGP VPN peer exists and none of the BGP VPN instance router ID, BGP VPN instance address family router ID, BGP router ID, and RM router ID is configured, the system may display a message indicating that the router ID will change to 0.0.0.0 when you delete the IP address of the last VPN interface.If two devices have different router IDs, an IBGP or EBGP connection can be established between them. If the router IDs are the same and the **router-id allow-same enable** command is run in the BGP view, an EBGP connection can be established.


Example
-------

# Configure a router ID.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv6-family
[*HUAWEI-vpn-instance-vrf1-af-ipv6] quit
[*HUAWEI-vpn-instance-vrf1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vrf1
[*HUAWEI-bgp6-vrf1] router-id 10.1.1.1

```