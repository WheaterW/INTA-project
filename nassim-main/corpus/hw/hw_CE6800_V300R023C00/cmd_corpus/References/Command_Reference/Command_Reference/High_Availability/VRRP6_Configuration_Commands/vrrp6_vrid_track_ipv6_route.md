vrrp6 vrid track ipv6 route
===========================

vrrp6 vrid track ipv6 route

Function
--------



The **vrrp6 vrid track ipv6 route vpn-instance** command configures a VRRP6 group to track a specified route.

The **undo vrrp6 vrid track ipv6 route vpn-instance** command disables a VRRP6 group from tracking a specified route.



By default, a VRRP6 group is not configured to track a specified route.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vrrp6 vrid** *virtual-router-ID* **track** **ipv6** **route** *ip-address* *mask-length* **vpn-instance** *vpn-name* [ { **reduce** *reduced-value* | **increase** *increased-value* } ]

**vrrp6 vrid** *virtual-router-ID* **track** **ipv6** **route** *ip-address* *mask-length* [ { **reduce** *reduced-value* | **increase** *increased-value* } ]

**undo vrrp6 vrid** *virtual-router-ID* **track** **ipv6** **route** *ip-address* *mask-length* **vpn-instance** *vpn-name*

**undo vrrp6 vrid** *virtual-router-ID* **track** **ipv6** **route** [ *ip-address* *mask-length* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-ID* | Specifies the ID of a VRRP6 group. | The value is an integer ranging from 1 to 255. |
| *ip-address* | Specifies the IPv6 address of a route to be tracked. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the mask length of the IPv6 address of the route to be tracked. | It is an integer ranging from 0 to 128. |
| **vpn-instance** *vpn-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **reduce** *reduced-value* | Indicates that the master device reduces its priority if the tracked route is withdrawn or becomes inactive. | The value is an integer ranging from 1 to 255. |
| **increase** *increased-value* | Specifies the value by which the master device's priority increases if the tracked route is withdrawn or becomes inactive. | The value is an integer ranging from 1 to 255. The default value is 10. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To improve device reliability, user gateways are connected to a Layer 3 network in master/backup mode, and VRRP6 is deployed to determine the master/backup status of the gateways. However, after a VRRP6 group is configured, the uplink route may still change frequently due to a link fault, but users on the access side are unaware of the route change. As a result, service traffic is lost.A VRRP6 group can be configured to track an uplink route to resolve the preceding problem. If the uplink route is withdrawn or becomes inactive, the RM module instructs the VRRP6 group to reduce the master's priority to trigger a master/backup switchover.

**Prerequisites**

A VRRP6 group has been configured using the **vrrp6 vrid** command.

**Precautions**

When running the vrrp vrid track ip route command, note the following aspects:

* The route specified by ip-address mask-length must be the same as that in the routing table. Otherwise, the VRRP6 module considers the route unreachable.
* If a common VRRP6 group is bound to an mVRRP6 group using the vrrp6 vrid virtual-router-id1 track admin-vrrp6 interface interface-type interface-number vrid virtual-router-id2 [ unflowdown ] command in the interface view, the common VRRP6 group becomes a service VRRP6 group, which cannot track a route.
* If a VRRP6-enabled device is an IPv6 address owner, the function of using VRRP6 to track a route does not take effect.

Example
-------

# Configure VRRP6 group 1 to track a route to 2001:db8:1::2/64, and set the value by which the priority of the master router decreases to 20 if the route is withdrawn or becomes inactive.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 virtual-ip 2001:db8:1::1
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 track ipv6 route 2001:db8:1::2 64 reduce 20

```