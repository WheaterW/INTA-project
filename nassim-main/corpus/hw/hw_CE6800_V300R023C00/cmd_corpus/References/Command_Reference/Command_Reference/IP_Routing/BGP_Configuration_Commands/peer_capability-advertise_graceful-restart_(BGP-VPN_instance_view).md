peer capability-advertise graceful-restart (BGP-VPN instance view)
==================================================================

peer capability-advertise graceful-restart (BGP-VPN instance view)

Function
--------



The **peer capability-advertise graceful-restart** command enables GR for a specified peer on a device. After this command is run, the device will advertise the GR capability to the specified peer.

The **peer capability-advertise graceful-restart disable** command disables GR for a specified peer on a device.

The **undo peer capability-advertise graceful-restart** command cancels GR enabling for a specified peer on a device.

The **undo peer capability-advertise graceful-restart disable** command cancels GR disabling for a specified peer on a device.



By default, GR is not enabled for a peer.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**peer** *ipv4-address* **capability-advertise** **graceful-restart**

**peer** *ipv4-address* **capability-advertise** **graceful-restart** **disable**

**undo peer** *ipv4-address* **capability-advertise** **graceful-restart**

**undo peer** *ipv4-address* **capability-advertise** **graceful-restart** **disable**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** *ipv6-address* **capability-advertise** **graceful-restart**

**peer** *ipv6-address* **capability-advertise** **graceful-restart** **disable**

**undo peer** *ipv6-address* **capability-advertise** **graceful-restart**

**undo peer** *ipv6-address* **capability-advertise** **graceful-restart** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | It is in dotted decimal notation. |
| *ipv6-address* | Specifies the IPv6 address of a peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X |



Views
-----

BGP-VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the **graceful-restart** command is run in the BGP view to enable GR globally on a device, all the device's peer relationships are disconnected, and the device has to renegotiate the GR capability with its peers. You are therefore advised to run the peer capability-advertise **graceful-restart** command instead to enable GR for a specified peer. If GR is not enabled globally, you can run this command to enable the GR capability and configure the device to notify the specified peer of the GR capability. In this manner, the routes and forwarding entries related to the specified peer are not deleted within the GR time, preventing traffic interruption.

**Configuration Impact**

Enabling or disabling GR for a specified peer on a device causes the BGP peer relationship to be disconnected and then reestablished.


Example
-------

# Enable GR for a specified peer on a device. The device will then advertise the GR capability to the specified peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-vpn1] peer 10.1.1.1 capability-advertise graceful-restart

```