ip binding vpn-instance
=======================

ip binding vpn-instance

Function
--------



The **ip binding vpn-instance** command associates an interface on a PE with a VPN instance.

The **undo ip binding vpn-instance** command disables the association between a VPN instance and an interface.



By default, an interface is a public network interface and is not associated with any VPN instance.


Format
------

**ip binding vpn-instance** *vpn-instance-name*

**undo ip binding vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of the VPN instance to be associated with the interface. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After creating a VPN instance, you must associate the PE interface connecting to the VPN with the VPN instance. Then, the interface is used as a private network interface on which a private network address and a private network routing protocol can be configured.

**Prerequisites**

A VPN instance has been configured using the **ip vpn-instance** command.

**Configuration Impact**

After an interface is associated with a VPN instance or an interface is disassociated from a VPN instance, the Layer 3 features on this interface, such as the IP address and routing protocol, are deleted. The Layer 3 features need to be reconfigured if required.

**Precautions**

Using the undo ipv4-family or undo ipv6 family command to disable the IPv4 or IPv6 address family also deletes the IPv4 or IPv6 configurations of the interfaces bound to the VPN instance.


Example
-------

# Associate 100GE 1/0/1 with a VPN instance named vrf1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv4-family
[*HUAWEI-vpn-instance-vrf1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vrf1-af-ipv4] quit
[*HUAWEI-vpn-instance-vrf1] quit
[*HUAWEI] commit
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[~HUAWEI-100GE1/0/1] ip binding vpn-instance vrf1

```