ntp source-interface
====================

ntp source-interface

Function
--------



The **ntp source-interface** command enables an IPv4 interface to send NTP messages.

The **undo ntp source-interface** command disables an IPv4 interface from sending NTP messages.



By default, no interface is specified for sending NTP messages.


Format
------

**ntp** [ **ipv6** ] **source-interface** { *interface-name* | *interface\_type* *interface\_num* } [ **vpn-instance** *vpnName* ]

**undo ntp** [ **ipv6** ] **source-interface** [ **vpn-instance** *vpnName* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Indicates the NTP IPv6 service. | - |
| *interface-name* | Specifies the interface for sending NTP messages. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| *interface\_type* | Specifies the type and number of a local interface that sends NTP packets. | - |
| *interface\_num* | Specifies the type and number of a local interface that sends NTP packets. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| **vpn-instance** *vpnName* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the unicast mode, if you want only one IP address to send the NTP request or response packets, specify the interface of which an IP address is used as a source interface.

**Precautions**

* In the broadcast and multicast modes, the NTP service is enabled on the specified interface that actually is the source interface. Therefore, the **ntp source-interface** command is invalid for the broadcast and multicast modes.
* If you have specified a VPN instance when configuring a source IP address using this command, the source IP address can be used only by the NTP client mapping the specified VPN instance instead of other VPN instances or NTP clients that do not have the specified VPN instance.
* If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP server function. To enable the NTP service, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when you delete this command.
* If a VPN instance is specified, the instance must have been created using the **ip vpn-instance vpn-instance-name** command, and the corresponding address family must have been enabled using the ipv4-family (VPN instance view) or ipv6-family (VPN instance view) command based on the IPv4 or IPv6 service configured for the NTP peer. Otherwise, this command fails to be executed.
* When the **ntp source-interface** command is run on the server, the destination IP address sent by the client rather than the IP address of the interface is specified as the source IP address in the packet. If the **ntp source-interface** command is run on the client, the IP address of the interface is specified as the client IP address in the packet.
* If the VPN instance or source interface specified in the command is deleted, the source interface configuration of the corresponding NTP server is also deleted.


Example
-------

# Specify the IPv6 address of Vlanif 100 as the source IPv6 address for sending all NTP packets.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] ipv6 enable
[~HUAWEI-Vlanif100] quit
[~HUAWEI] ntp ipv6 source-interface Vlanif 100

```

# Specify the IPv4 address of Vlanif 100 as the source IPv4 address for sending NTP packets.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] ntp source-interface Vlanif 100

```