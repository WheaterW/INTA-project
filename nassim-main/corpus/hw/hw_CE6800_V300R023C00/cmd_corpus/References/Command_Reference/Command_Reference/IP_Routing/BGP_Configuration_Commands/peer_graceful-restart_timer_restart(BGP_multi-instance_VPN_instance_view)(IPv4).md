peer graceful-restart timer restart(BGP multi-instance VPN instance view)(IPv4)
===============================================================================

peer graceful-restart timer restart(BGP multi-instance VPN instance view)(IPv4)

Function
--------



The **peer graceful-restart timer restart** command sets the maximum time for a specified peer to wait for the local BGP peer relationship to be re-established and advertises the time to the specified peer.

The **undo peer graceful-restart timer restart** command deletes this configuration.



By default, a peer specified on a device waits for its BGP peer relationship to be reestablished with the device for a maximum of 150s.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**peer** *peerIpv4Addr* **graceful-restart** **timer** **restart** *time-value*

**undo peer** *peerIpv4Addr* **graceful-restart** **timer** **restart**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** *peerIpv6Addr* **graceful-restart** **timer** **restart** *time-value*

**undo peer** *peerIpv6Addr* **graceful-restart** **timer** **restart**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specify an IPv4 peer address. | The value is in dotted decimal notation. |
| *time-value* | Specifies the maximum duration on a device for a peer to wait for its BGP peer relationship to be reestablished with the device. | The value is an integer ranging from 3 to 3600, in seconds. |
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

If a device and a BGP peer specified on the device both support GR, you can run the peer graceful-restart timer restart command to set the maximum duration on the device for the peer to wait for its BGP peer relationship to be reestablished with the device. After this command is run, if the peer detects that the device is down, the BGP session on the peer enters the GR process. If the peer relationship fails to be reestablished within the specified duration, the BGP session exits from the GR process and the peer selects the optimal route from current reachable routes.

**Configuration Impact**

If this command is run, the BGP peer relationship is disconnected and re-established. Therefore, exercise caution when running this command.


Example
-------

# Set the maximum duration to 100s on a device for a specified peer to wait for its BGP peer relationship to be reestablished with the device.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] bgp 100 instance a
[*HUAWEI-bgp-instance-a] vpn-instance vpn1
[*HUAWEI-bgp-instance-a-instance-vpn1] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a-instance-vpn1] peer 10.1.1.1 graceful-restart timer restart 100

```