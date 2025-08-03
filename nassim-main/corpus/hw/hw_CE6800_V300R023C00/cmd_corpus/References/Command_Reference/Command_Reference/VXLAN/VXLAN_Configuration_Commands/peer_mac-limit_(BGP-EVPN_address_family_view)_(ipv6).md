peer mac-limit (BGP-EVPN address family view) (ipv6)
====================================================

peer mac-limit (BGP-EVPN address family view) (ipv6)

Function
--------



The **peer mac-limit** command configures the maximum number of MAC advertisement routes allowed to be received from a peer.

The **undo peer mac-limit** command restores the default configuration.



By default, the number of MAC advertisement routes allowed to be received from a peer is not limited.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **mac-limit** *limit* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *times* ]

**undo peer** *peerIpv6Addr* **mac-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *limit* | Specifies the maximum number of MAC advertisement routes allowed to be received from a peer. | The value is an integer ranging from 1 to 4294967295. |
| *percentage* | Specifies a percentage of MAC advertisement routes for the device to generate an alarm. If the number of MAC advertisement routes received from a peer exceeds (number\*percentage)/100, the device generates an alarm. | The value is an integer ranging from 1 to 100. The default value is 75. |
| **alert-only** | Indicates that an alarm will be generated and additional routes will be denied if the maximum number of routes allowed have been received.  This parameter is recommended to prevent a peer disconnection when the number of routes received by the device exceeds the maximum limit. | - |
| **idle-forever** | Indicates that a connection that is interrupted after the maximum number of routes allowed have been received cannot be automatically re-established. | - |
| **idle-timeout** *times* | Specifies a timer for re-establishing a connection if the connection is interrupted after the maximum number of routes allowed have been received. Before the timer expires, the system does not re-establish a connection. | The value is an integer ranging from 1 to 1200, in minutes. |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If an EVPN instance may import many invalid MAC advertisement routes from peers and these routes occupy a large proportion of the total number of MAC advertisement routes, run the **peer mac-limit** command to configure the maximum number of MAC advertisement routes allowed to be received from each peer. If the number of received MAC advertisement routes exceeds the specified maximum number, the system displays an alarm, instructing users to check the validity of the MAC advertisement routes received in the EVPN instance.

**Precautions**

The peer mac-limit and **peer route-limit** commands are mutually exclusive.


Example
-------

# Configure a device only to generate an alarm when more than 1000 MAC advertisement routes are received.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:2::2 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 2001:DB8:2::2 enable
[*HUAWEI-bgp-af-evpn] peer 2001:DB8:2::2 mac-limit 1000 alert-only

```