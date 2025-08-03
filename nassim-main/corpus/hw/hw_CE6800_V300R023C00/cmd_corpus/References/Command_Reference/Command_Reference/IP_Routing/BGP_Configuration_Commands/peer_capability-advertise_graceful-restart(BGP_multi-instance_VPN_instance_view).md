peer capability-advertise graceful-restart(BGP multi-instance VPN instance view)
================================================================================

peer capability-advertise graceful-restart(BGP multi-instance VPN instance view)

Function
--------



The **peer capability-advertise graceful-restart** command enables the GR capability and configures the device to advertise the capability to a specified peer.

The **peer capability-advertise graceful-restart disable** command disables the GR capability of a peer.

The **undo peer capability-advertise graceful-restart** command cancels the configuration of enabling the GR capability of a peer.

The **undo peer capability-advertise graceful-restart disable** command cancels the configuration of disabling the GR capability of a peer.



By default, GR is not enabled for a peer.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**peer** *peerIpv4Addr* **capability-advertise** **graceful-restart**

**peer** *peerIpv4Addr* **capability-advertise** **graceful-restart** **disable**

**undo peer** *peerIpv4Addr* **capability-advertise** **graceful-restart**

**undo peer** *peerIpv4Addr* **capability-advertise** **graceful-restart** **disable**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** *peerIpv6Addr* **capability-advertise** **graceful-restart**

**peer** *peerIpv6Addr* **capability-advertise** **graceful-restart** **disable**

**undo peer** *peerIpv6Addr* **capability-advertise** **graceful-restart**

**undo peer** *peerIpv6Addr* **capability-advertise** **graceful-restart** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the **graceful-restart** command is run in the BGP view to enable GR globally on a device, all the device's peer relationships are disconnected, and the device has to renegotiate the GR capability with its peers. You are therefore advised to run the peer capability-advertise **graceful-restart** command instead to enable GR for a specified peer. If GR is not enabled globally, you can run this command to enable the GR capability and configure the device to notify the specified peer of the GR capability. In this manner, the routes and forwarding entries related to the specified peer are not deleted within the GR time, preventing traffic interruption.

**Configuration Impact**

Enabling or disabling GR for a peer causes the BGP peer relationships to be disconnected and then reestablished.


Example
-------

# Enable GR for a specified peer on a device. The device will then advertise the GR capability to the specified peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] vpn-instance vpn1
[*HUAWEI-bgp-instance-a-instance-vpn1] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a-instance-vpn1] peer 10.1.1.1 capability-advertise graceful-restart

```