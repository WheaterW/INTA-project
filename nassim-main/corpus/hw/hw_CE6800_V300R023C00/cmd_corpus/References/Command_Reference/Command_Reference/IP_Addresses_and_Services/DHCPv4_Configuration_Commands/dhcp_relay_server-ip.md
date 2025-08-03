dhcp relay server-ip
====================

dhcp relay server-ip

Function
--------



The **dhcp relay server-ip** command configures a DHCP server address on an interface enabled with DHCP relay.

The **undo dhcp relay server-ip** command deletes a specified or all DHCP server addresses on an interface enabled with DHCP relay.



By default, no DHCP server address is configured on an interface.


Format
------

**dhcp relay server-ip** *ip-address*

**dhcp relay server-ip** *ip-address* { **vpn-instance** *vpn-instance-name* | **public-net** }

**undo dhcp relay server-ip** { *ip-address* | **all** }

**undo dhcp relay server-ip** *ip-address* { **vpn-instance** *vpn-instance-name* | **public-net** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of a DHCP server. | The value is in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance to which a DHCP server belongs. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **public-net** | Indicates that the DHCP server is the public network server. After the public-net parameter is specified, the DHCPv6 packets sent by interfaces do not carry VPN information. | - |
| **all** | Deletes all DHCP server addresses on a VLANIF interface. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a DHCP relay agent is used to forward a DHCP Request message from a DHCP client to a DHCP server on a different network segment, run the **dhcp relay server-ip** command on the DHCP relay agent to configure a DHCP server address.The vpn-instance vpn-instance-name parameter must be specified in this command if the DHCP clients and DHCP server are in different VPNs. When the DHCP clients and DHCP server are in the same VPN, do not specify the vpn-instance vpn-instance-name parameter. This is because the VPN to which the DHCP server belongs is by default the same as the VPN to which the DHCP relay interface belongs. In this case, you only need to bind the DHCP relay interface to the VPN and use the VPN information.

**Prerequisites**

DHCP relay has been enabled on the VLANIF interface using the **dhcp select relay** command.

**Precautions**

A DHCP relay interface can have a maximum of 20 source IP addresses configured. The DHCP relay agent sends DHCP request packets to all servers and DHCP reply packets to all clients.If the **dhcp relay server-ip** command has been run for multiple times, the latest configuration will not override the previous one.Multi-level DHCP relay is not supported in inter-VPN scenarios.


Example
-------

# Set the server IP 10.1.1.1 and 10.2.1.1 on the interface 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcp select relay
[*HUAWEI-100GE1/0/1] dhcp relay server-ip 10.1.1.1
[*HUAWEI-100GE1/0/1] dhcp relay server-ip 10.2.1.1

```