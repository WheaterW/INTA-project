peer graceful-restart timer restart (BGP-VPN instance IPv6 address family view) (IPv6)
======================================================================================

peer graceful-restart timer restart (BGP-VPN instance IPv6 address family view) (IPv6)

Function
--------



The **peer graceful-restart timer restart** command sets the maximum duration on a device for a specified peer to wait for its BGP peer relationship to be reestablished with the device. After the command is run, the device will advertise the maximum duration to the specified peer.

The **undo peer graceful-restart timer restart** command deletes the configured duration.



By default, a peer specified on a device waits for its BGP peer relationship to be reestablished for a maximum of 150 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **graceful-restart** **timer** **restart** *time-value*

**undo peer** *ipv6-address* **graceful-restart** **timer** **restart**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IP address of an IPv6 peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *time-value* | Specifies the maximum duration for a peer to wait for its BGP peer relationship to be reestablished. | The value is an integer ranging from 3 to 3600, in seconds. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


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
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-6-vpn1] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp-6-vpn1] peer 2001:DB8:1::1 graceful-restart timer restart 100

```