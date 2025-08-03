peer capability-advertise graceful-restart (BGP-VPN instance IPv4 address family view) (group)
==============================================================================================

peer capability-advertise graceful-restart (BGP-VPN instance IPv4 address family view) (group)

Function
--------



The **peer capability-advertise graceful-restart** command enables GR for all peers in a specified group on a device. After this command is run, the device will advertise the GR capability to all the peers in the group.

The **undo peer capability-advertise graceful-restart** command cancels GR enabling for each peer in a specified group on a device.



By default, GR is not enabled for any peer in a specified group on a device.


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

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the **graceful-restart** command is run in the BGP view to enable GR globally on a device, all the device's peer relationships are disconnected, and the device has to renegotiate the GR capability with its peers. You are therefore advised to run the peer capability-advertise **graceful-restart** command instead to enable GR for peers in a specified group. After the command is run, the device advertises the GR capability to all the peers in the group. This ensures that the device does not delete the routes received from these peers and forwarding entries before the GR time elapses, thereby preventing traffic interruption.

**Configuration Impact**

Enabling or disabling GR for each peer in a specified group on a device causes the BGP peer relationships to be disconnected and then reestablished.


Example
-------

# Enable GR for each peer in a specified group on a device. The device will then advertise the GR capability to all the peers in the group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] group a
[*HUAWEI-bgp-vpn1] peer a capability-advertise graceful-restart

```