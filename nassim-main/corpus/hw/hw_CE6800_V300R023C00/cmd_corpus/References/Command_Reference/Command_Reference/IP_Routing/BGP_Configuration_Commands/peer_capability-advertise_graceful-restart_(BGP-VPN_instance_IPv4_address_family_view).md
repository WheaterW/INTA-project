peer capability-advertise graceful-restart (BGP-VPN instance IPv4 address family view)
======================================================================================

peer capability-advertise graceful-restart (BGP-VPN instance IPv4 address family view)

Function
--------



The **peer capability-advertise graceful-restart** command enables GR for a specified peer on a device. After this command is run, the device will advertise the GR capability to the specified peer.

The **peer capability-advertise graceful-restart disable** command disables GR for a specified peer on a device.

The **undo peer capability-advertise graceful-restart** command cancels GR enabling for a specified peer on a device.

The **undo peer capability-advertise graceful-restart disable** command cancels GR disabling for a specified peer on a device.



By default, GR is not enabled for a peer.


Format
------

**peer** *ipv4-address* **capability-advertise** **graceful-restart**

**peer** *ipv4-address* **capability-advertise** **graceful-restart** **disable**

**undo peer** *ipv4-address* **capability-advertise** **graceful-restart**

**undo peer** *ipv4-address* **capability-advertise** **graceful-restart** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |



Views
-----

BGP-VPN instance IPv4 address family view


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
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-vpn1] peer 10.1.1.1 capability-advertise graceful-restart

```