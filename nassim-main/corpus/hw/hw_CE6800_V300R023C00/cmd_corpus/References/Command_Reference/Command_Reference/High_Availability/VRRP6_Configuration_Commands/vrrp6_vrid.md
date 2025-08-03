vrrp6 vrid
==========

vrrp6 vrid

Function
--------



The **vrrp6 vrid** command creates a Virtual Router Redundancy Protocol for IPv6 (VRRP6) backup group and assigns a virtual IPv6 address to it.

The **undo vrrp6 vrid** command deletes a VRRP6 backup group or a virtual IPv6 address assigned to it.



By default, no VRRP6 backup group exists on a router.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vrrp6 vrid** *virtual-router-id* [ **virtual-ip** *virtual-address* [ **link-local** ] ]

**undo vrrp6 vrid** *virtual-router-id* [ **virtual-ip** *virtual-address* [ **link-local** ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id* | Specifies the ID of a VRRP6 backup group. | The value is an integer ranging from 1 to 255. |
| **virtual-ip** *virtual-address* | Specifies a virtual IPv6 address for a VRRP6 group.   * If link-local is configured, the <virtual-address> must be set to an IPv6 address prefixed with FE80. * If link-local is not specified, the <virtual-address> must be on the same network segment as the IPv6 address of the interface and cannot be an anycast address or a multicast address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **link-local** | Indicates that a virtual IPv6 address assigned to a VRRP6 group is a link-local address. A link-local address has a prefix of FE80 and is used for communication between adjacent nodes on the same link. The link-local address takes effect only on a local link. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, hosts use a default gateway to communicate with external networks. If the gateway fails, communication between the hosts and external networks is interrupted. VRRP is a fault-tolerant protocol that allows logical devices to work separately from physical devices and implements route selection among multiple egress gateways.

**Precautions**

Multiple virtual IPv6 addresses can be assigned to a VRRP6 group. A single virtual IPv6 address serves a separate user group, in which users have the same VRRP6 reliability requirements. This setting helps prevent the default gateway addresses from varying according to changes in VRRP6 configurations.When you configure a VRRP6 group on an interface, ensure that the first virtual IPv6 address configured for the group is a link-local address. That is, you must run the **vrrp6 vrid virtual-ip link-local** command before assigning other virtual IPv6 addresses to the VRRP6 group.If you assign a virtual IPv6 address when creating a VRRP6 group, the system automatically deletes the VRRP6 group when all virtual IPv6 addresses of the VRRP6 group are deleted. If you do not assign a virtual IPv6 address when creating a VRRP6 group, the system does not automatically delete the VRRP6 group even if all virtual IPv6 addresses of the VRRP6 group are deleted.VRRP6 cannot be configured together with MUX VLAN.


Example
-------

# Configure a VRRP6 group on 100GE1/0/7 and set the virtual IPv6 address of the VRRP6 group to FE80::7.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/7
[~HUAWEI-100GE1/0/7] undo portswitch
[*HUAWEI-100GE1/0/7] ipv6 enable
[*HUAWEI-100GE1/0/7] ipv6 address 2001:db8::1 64
[*HUAWEI-100GE1/0/7] vrrp6 vrid 1 virtual-ip FE80::7 link-local

```