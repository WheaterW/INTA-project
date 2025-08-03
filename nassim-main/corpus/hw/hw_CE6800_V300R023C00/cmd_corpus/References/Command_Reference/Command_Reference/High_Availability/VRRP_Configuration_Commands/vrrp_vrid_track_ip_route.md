vrrp vrid track ip route
========================

vrrp vrid track ip route

Function
--------



The **vrrp vrid track ip route** command configures a VRRP group to track a specified route.

The **undo vrrp vrid track ip route** command disables a VRRP group from tracking a specified route.



By default, a VRRP group tracks no route.


Format
------

**vrrp vrid** *virtual-router-id* **track** **ip** **route** *ip-address* { *mask-address* | *mask-length* } **vpn-instance** *vpn-instance-name* [ { **reduce** *value-reduced* | **increase** *increased-value* } ]

**vrrp vrid** *virtual-router-id* **track** **ip** **route** *ip-address* { *mask-address* | *mask-length* } [ { **reduce** *value-reduced* | **increase** *increased-value* } ]

**undo vrrp vrid** *virtual-router-id* **track** **ip** **route** *ip-address* { *mask-address* | *mask-length* } **vpn-instance** *vpn-instance-name*

**undo vrrp vrid** *virtual-router-id* **track** **ip** **route** [ *ip-address* { *mask-address* | *mask-length* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |
| *ip-address* | Specifies the destination IP address of a route to be tracked. | The value is in dotted decimal notation. |
| *mask-address* | Specifies the destination IP address mask of a route to be tracked. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the length of the destination IP address mask of a route to be tracked. | The value is an integer ranging from 0 to 32. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **reduce** *value-reduced* | Indicates that the master device reduces its priority if the tracked route is withdrawn or becomes inactive. | The value is an integer ranging from 1 to 255. The default value is 10. |
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

To improve device reliability, two user gateways working in master/backup mode are connected to a network, and VRRP is enabled on these gateways to determine their master/backup status. If a VRRP group has been configured and an uplink route to a network becomes unreachable, access-side users still use the VRRP group to forward traffic along the uplink route, which causes user traffic loss.Association between a VRRP group and a route can prevent user traffic loss. A VRRP group can be configured to track the uplink route to a network. If the route is withdrawn or becomes inactive, the route management (RM) module notifies the VRRP group of the change. After receiving the notification, the VRRP group changes its master device's VRRP priority and performs a master/backup switchover.

**Prerequisites**

A VRRP group has been configured using the **vrrp vrid** command.

**Precautions**

When running the vrrp vrid track ip route command, note the following aspects:

* The route specified using the ip-address { mask-address | mask-length } parameter must be the same as a route in the routing table of a VRRP device. Otherwise, the VRRP group considers the route unreachable.
* The vrrp vrid virtual-router-id1 track admin-vrrp interface interface-type interface-number vrid virtual-router-id2 [ unflowdown ] command is run in an interface view to bind a VRRP group to an mVRRP group. Then, the VRRP group is a service VRRP group. Service VRRP groups do not support route monitoring.
* If a VRRP device is an IP address owner, the association between a VRRP group and a specified route does not take effect.

Example
-------

# Configure VRRP group 1 to track a route with an IP address of 10.2.1.0/24, and enable the master device's VRRP priority to decrease by 20 if the tracked route is withdrawn or becomes inactive.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.1
[*HUAWEI-100GE1/0/1] vrrp vrid 1 track ip route 10.2.1.0 24 reduce 20

```