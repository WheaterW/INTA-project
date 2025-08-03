ipv4-family
===========

ipv4-family

Function
--------



The **ipv4-family** command enables the IPv4 address family for a VPN instance and displays the VPN instance IPv4 address family view.

The **undo ipv4-family** command disables the IPv4 address family for a VPN instance.



By default, the IPv4 address family is not enabled for a VPN instance.


Format
------

**ipv4-family** [ **unicast** ]

**undo ipv4-family** [ **unicast** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **unicast** | Displays the unicast address family view. | - |



Views
-----

VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In L3VPN networking, after you run the **ip vpn-instance** command to create a VPN instance, you can run the ipv4-family command to enable the IPv4 address family for the VPN instance and perform VPN configurations in the address family view if you want to have IPv4 VPN routes advertised and IPv4 VPN data forwarded.



**Follow-up Procedure**



Run the **route-distinguisher** command to configure an RD for the IPv4 address family of the VPN instance. VPN configurations can be performed in the IPv4 address family view only after an RD is configured for the IPv4 address family of the VPN instance.



**Precautions**



Except the **description** command, the configurations of other commands in the VPN instance view are automatically synchronized to the VPN instance IPv4 address family view.After the IPv4 address family of a VPN instance is disabled using the undo ipv4-family [ unicast ] command, configurations related to the VPN instance in the address family view and BGP view will be deleted. Therefore, exercise caution when running this command.After the IPv4 address family of a VPN instance is disabled using the undo ipv4-family [ unicast ] command, the configurations, such as the IP address of the interface, on all the interfaces bound to the VPN instance are also deleted. Therefore, exercise caution when running this command.




Example
-------

# Enable the IPv4 address family for a VPN instance.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4]

```