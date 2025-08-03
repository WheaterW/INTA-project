ip vpn-instance(System view)
============================

ip vpn-instance(System view)

Function
--------



The **ip vpn-instance** command creates a VPN instance and displays the VPN instance view.

The **undo ip vpn-instance** command deletes a specified VPN instance.



By default, no VPN instance is created.


Format
------

**ip vpn-instance** *vpn-instance-name*

**undo ip vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string.  \_public\_ refers to a public network VPN instance. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If private network data needs to travel across a public network, you must configure VPN instances on public network PEs.VPN instances are required for all L3VPN configurations.



**Configuration Impact**



After the ip vpn-instance command is run on a PE, a virtual routing table is created on the PE and consumes resources on the PE.After the **undo ip vpn-instance** command is used to delete a VPN instance, all the configurations of this VPN instance are deleted.



**Follow-up Procedure**

After creating a VPN instance, perform the following configurations in the VPN instance view:

* Enable the IPv4 or IPv6 address family for the VPN instance. A VPN instance supports the IPv4 and IPv6 address families. You need to run the ipv4-family (VPN instance view) or ipv6 family (VPN instance view) command to enable the IPv4 or IPv6 address family based on the type of the protocol stack used to advertise VPN routes in the VPN instance.
* Configure a Route Distinguisher (RD) for the IPv4 or IPv6 address family of the VPN instance. You are allowed to perform VPN configurations in the address family view only after using the **route-distinguisher** command to configure an RD for the address family.
* Configure a VPN target for the IPv4 or IPv6 address family of the VPN instance using the **vpn-target** command. VPN targets control route learning between VPN instances.
* Bind the VPN instance to a VPN-connected interface on the PE using the **ip binding vpn-instance** command.

**Precautions**



After a VPN instance is deleted using the **undo ip vpn-instance** command, configurations in the VPN instance as well as the VPN instance-related configurations in the BGP view will be deleted. Exercise caution when you run this command.When the **undo ip vpn-instance** command is run to delete a VPN instance, if a large number of routes are imported between VPN and public network instances, the commit operation may time out, but the VPN instance data can be correctly deleted.




Example
-------

# Create a VPN instance named vrf1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1

```