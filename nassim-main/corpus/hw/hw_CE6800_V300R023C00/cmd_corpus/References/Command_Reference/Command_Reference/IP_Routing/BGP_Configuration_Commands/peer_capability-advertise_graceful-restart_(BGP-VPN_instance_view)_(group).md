peer capability-advertise graceful-restart (BGP-VPN instance view) (group)
==========================================================================

peer capability-advertise graceful-restart (BGP-VPN instance view) (group)

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
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the **graceful-restart** command is run in the BGP view to enable GR globally on a device, all the device's peer relationships are disconnected, and the device has to renegotiate the GR capability with its peers. You are therefore advised to enable GR for peers in a specified group. Specifically, run this command when GR is not enabled globally, to enable the GR capability and notify the specified peer group of the GR capability. In this manner, the routes and forwarding entries related to the specified peers are not deleted within the GR time, preventing traffic interruption.

**Configuration Impact**

Enabling or disabling GR for a specified peer on a device causes the BGP peer relationship to be disconnected and then reestablished.


Example
-------

# Enable GR for each peer in a specified group on a device. The device will then advertise the GR capability to all the peers in the group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group a
[*HUAWEI-bgp-instance-vpn1] peer a capability-advertise graceful-restart

```