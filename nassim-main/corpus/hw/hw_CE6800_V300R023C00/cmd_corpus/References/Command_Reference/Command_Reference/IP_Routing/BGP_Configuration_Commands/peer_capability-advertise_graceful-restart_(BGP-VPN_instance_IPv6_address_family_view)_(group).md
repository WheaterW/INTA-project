peer capability-advertise graceful-restart (BGP-VPN instance IPv6 address family view) (group)
==============================================================================================

peer capability-advertise graceful-restart (BGP-VPN instance IPv6 address family view) (group)

Function
--------



The **peer capability-advertise graceful-restart** command enables GR for all peers in a specified group on a device. After this command is run, the device will advertise the GR capability to all the peers in the group.

The **undo peer capability-advertise graceful-restart** command cancels GR enabling for each peer in a specified group on a device.



By default, GR is not enabled for any peer in a specified group on a device.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **capability-advertise** **graceful-restart**

**undo peer** *group-name* **capability-advertise** **graceful-restart**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the **graceful-restart** command is run in the BGP view to enable GR globally on a device, all the device's peer relationships are disconnected, and the device has to renegotiate the GR capability with its peers. You are therefore advised to enable GR for peers in a specified group. Specifically, run this command when GR is not enabled globally, to enable the GR capability and notify the specified peer group of the GR capability. In this manner, the routes and forwarding entries related to the specified peers are not deleted within the GR time, preventing traffic interruption.

**Configuration Impact**

Enabling or disabling GR for each peer in a specified group on a device causes the BGP peer relationships to be disconnected and then reestablished.


Example
-------

# Enable GR for each peer in a specified group on a device. The device will then advertise the GR capability to all the peers in the group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-6-vpn1] group a
[*HUAWEI-bgp-6-vpn1] peer a capability-advertise graceful-restart

```