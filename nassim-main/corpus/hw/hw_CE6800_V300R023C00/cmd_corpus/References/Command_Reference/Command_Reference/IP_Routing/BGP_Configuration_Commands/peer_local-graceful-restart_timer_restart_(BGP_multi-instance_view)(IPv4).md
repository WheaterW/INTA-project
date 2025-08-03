peer local-graceful-restart timer restart (BGP multi-instance view)(IPv4)
=========================================================================

peer local-graceful-restart timer restart (BGP multi-instance view)(IPv4)

Function
--------



The **peer local-graceful-restart timer restart** command sets the maximum duration for a device to wait for the BGP peer relationship with a specified peer to be reestablished. After this command is run, the device will not advertise the maximum duration to the specified peer.

The **undo peer local-graceful-restart timer restart** command deletes the configured duration.



By default, a device waits for the peer relationship with a peer to be reestablished for a maximum of 150 seconds.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **local-graceful-restart** **timer** **restart** *restart-time*

**undo peer** { *ipv4-address* | *ipv6-address* } **local-graceful-restart** **timer** **restart**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **local-graceful-restart** **timer** **restart** *restart-time*

**undo peer** *ipv4-address* **local-graceful-restart** **timer** **restart**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | It is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *restart-time* | Specifies the maximum time for the local end to wait for GR recovery of the peer. | The value is an integer ranging from 3 to 3600, in seconds. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the local device supports GR but the specified peer does not support GR, you can run this command to set the maximum waiting time for the local device to wait for the re-establishment of the BGP peer relationship.After the **peer local-graceful-restart timer restart** command is run, if the local end finds that the peer is Down, the BGP session enters the GR process. The local end must establish a connection with the peer within the configured maximum waiting time. Otherwise, the local end selects the optimal route from the existing routes.


Example
-------

# Set the maximum duration to 250 seconds for a device to wait for the peer relationship with a specified peer to be reestablished.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance vpn1
[*HUAWEI-bgp-instance-vpn1] peer 10.1.1.2 as-number 100
[*HUAWEI-bgp-instance-vpn1] peer 10.1.1.2 local-graceful-restart timer restart 250

```