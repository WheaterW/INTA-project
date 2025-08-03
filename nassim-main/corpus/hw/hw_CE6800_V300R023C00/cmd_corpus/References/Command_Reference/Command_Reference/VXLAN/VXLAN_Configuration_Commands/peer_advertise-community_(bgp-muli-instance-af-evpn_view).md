peer advertise-community (bgp-muli-instance-af-evpn view)
=========================================================

peer advertise-community (bgp-muli-instance-af-evpn view)

Function
--------



The **peer advertise-community** command configures a device to advertise community attributes to a peer.

The **undo peer advertise-community** command cancels the configuration.



By default, a device advertises no community attribute to its peer

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **advertise-community**

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **advertise-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To determine whether to advertise the community attribute to a peer, run the **peer advertise-community** command.

**Prerequisites**

Enable the peer in current view using **peer enable** command.


Example
-------

# Configure a device to advertise a community attribute to its peer in the bgp-multi-instance-af-evpn view.
```
<HUAWEI> system-view
Enter system view, return user view with return command.
[~HUAWEI] evpn-overlay enable
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a] l2vpn-family evpn
[*HUAWEI-bgp-instance-a-af-evpn] peer 10.1.1.1 enable
[*HUAWEI-bgp-instance-a-af-evpn] peer 10.1.1.1 advertise-community

```