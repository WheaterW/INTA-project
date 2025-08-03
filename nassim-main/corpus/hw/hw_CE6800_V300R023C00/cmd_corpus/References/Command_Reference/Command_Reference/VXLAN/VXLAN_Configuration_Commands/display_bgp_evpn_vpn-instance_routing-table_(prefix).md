display bgp evpn vpn-instance routing-table (prefix)
====================================================

display bgp evpn vpn-instance routing-table (prefix)

Function
--------



The **display bgp evpn vpn-instance routing-table** command displays information about BGP-EVPN routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp evpn vpn-instance** *evpn-name-value* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* { **community-list** | **ext-community** | **large-community** | **cluster-list** }

**display bgp** [ **instance** *bgpName* ] **evpn** **vpn-instance** *evpn-name-value* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** } *prefix* { **community-list** | **ext-community** | **large-community** | **cluster-list** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ad-route** | Displays information about Ethernet A-D routes. | - |
| **es-route** | Displays information about Ethernet segment routes. | - |
| **inclusive-route** | Displays information about inclusive multicast routes. | - |
| **mac-route** | Displays information about MAC advertisement routes. | - |
| *prefix* | Specifies the prefix of an EVPN route. | An EVPN route prefix has the following formats:  Ethernet auto-discovery route. The value is in the format of xxxx.xxxx.xxxx.xxxx.xxxx:M, where:   * xxxx.xxxx.xxxx.xxxx.xxxx indicates the ESI configured for the device originating this route. * M is from 0 to 4294967295.   Ethernet segment route. The value is in the format of xxxx.xxxx.xxxx.xxxx.xxxx, xxxx.xxxx.xxxx.xxxx.xxxx:M:X.X.X.X.X, or xxxx.xxxx.xxxx.xxxx.xxxx:M:[X:X::X:X], where x is a hexadecimal integer ranging from 0 to F. The value equals the ESI configured for the device originating this route.   * M indicates the length of the OriginIp address corresponding to the ES route. The value ranges from 0 to 255. * X.X.X.X indicates the IPv4 OriginIP address in the ES route. * X:X::X:X:X indicates the IPv6 OriginIP address in the ES route.   Inclusive multicast route. The value is in the format of M:L:X.X.X.X, where:   * M is fixed at 0. * X.X.X.X indicates the source address configured for the device originating the route. * L indicates the mask length of the source address configured for the device originating the route.   MAC advertisement route. The value is in the format of E:M:H-H-H:L:X.X.X.X or E:M:H-H-H:L: [X:X::X:X], where:   * E indicates the ID of the VLAN to which the MAC address belongs. * M is fixed at 48, indicating the length of the MAC address. * H-H-H indicates the MAC address. The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H is 4 digits, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. * L is fixed at 0, indicating the mask length of the IP address corresponding to the MAC address. * X.X.X.X indicates the IP address corresponding to the MAC address. Currently, this part can only be displayed as 0.0.0.0. * X:X::X:X indicates the IPv6 address corresponding to the MAC address.   IP prefix route. The value is in the format of L:X.X.X.X:M or L:[X:X::X:X]:M, where:   * L is fixed at 0. * X.X.X.X indicates the host IP address. * M indicates the mask length of the host IP address. * X:X::X:X indicates the host IPv6 address. |
| **community-list** | Displays the community list of BGP EVPN routes. | - |
| **ext-community** | Displays the extended community list of BGP EVPN routes. | - |
| **large-community** | Displays the extended community attribute of BGP EVPN routes. | - |
| **cluster-list** | Displays the cluster list of EVN BGP routes. | - |
| **vpn-instance** *evpn-name-value* | Displays information about EVPN routes of a specified EVPN instance. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **instance** *bgpName* | Displays the routes of a specified BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about all active and inactive BGP-EVPN routes, run the display bgp mvpn routing-table command. You can specify different parameters to check specific routing information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BGP enhanced community attributes of routes.
```
<HUAWEI> display bgp evpn vpn-instance e1 routing-table mac-route 0:48:00e0-fc12-3456:0:0.0.0.0 ext-community

 Routes of evpn-instance e1:

 BGP routing table entry information of 0:48:00e0-fc12-3456:0:0.0.0.0:
 From: 2001:DB8:1::141
 Remote-Cross route
 Ext-Community: RT <1 : 1>, SoO <10.1.1.144 : 0>, Mac Mobility <flag:1 seq:0 res:0>

```

**Table 1** Description of the **display bgp evpn vpn-instance routing-table (prefix)** command output
| Item | Description |
| --- | --- |
| evpn-instance | EVPN instance name. |
| BGP routing table entry information of | Routing entry information. |
| Remote-Cross route | Route received from a peer and leaked into an EVPN instance. |
| SoO | SoO extended community attribute. |
| Mac Mobility | Extended community attribute for MAC address migration. |
| From | IP address of the device that sends the route. |
| Local-Cross route | Locally leaked routes. |
| Ext-Community | BGP EVPN extended community attribute. |