tftp client source
==================

tftp client source

Function
--------



The **tftp client source** command sets the interface and IP addresses of the TFTP client to establish the connection with TFTP server.

The **undo tftp client source** command cancels the interface and IPv4 address of the TFTP client.

The **tftp ipv6 client source** command sets the IPv6 addresses and VPN of the TFTP client to establish the connection with TFTP server.

The **undo tftp ipv6 client source** command cancels the IPv6 address and VPN of the TFTP client.



By default, the source IPv4 address is set to 0.0.0.0, the source IPv6 address is set to 0::0.


Format
------

**tftp client source** { **-a** *ip-address* | **-i** { *interface-type* *interface-number* | *interface-name* } }

**tftp ipv6 client source -a** *ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ]

**undo tftp client source**

**undo tftp ipv6 client source**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *ip-address* | Specifies the source IPv4 address of the local machine. | The value is in the decimal format. |
| **-a** *ipv6-address* | Specifies the source IPv6 address of the local machine. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **-i** *interface-name* | Specifies the source interface type and source interface name. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. |
| *interface-type* | Specifies the source interface type and source interface type. | - |
| *interface-number* | Specifies the source interface type and source interface number. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. |
| **-vpn-instance** *ipv6-vpn-instance-name* | Specifies the name of a VPN instance to which the TFTP server belongs.  Before specifying the parameter vpn-instance ipv6-vpn-instance-name, ensure that a VPN instance has been configured. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



If you run the TFTP login command without specifying a source address or source interface, the source address or source interface specified through the command is adopted by default, that is, the source address or source interface specified through the tftp client source command. If you run the **tftp** command and specify the source address or source interface, the specified source address or source interface is used. When you check the current TFTP connection on the server, the displayed user IP address is the specified source IP address or the primary IP address of the specified interface.



**Prerequisites**

Ensure that the interface is configured before you use a specified source interface to configure a TFTP connection.


Example
-------

# Set the source IPv4 address of the TFTP client to 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] tftp client source -a 10.1.1.1

```

# Set the TFTP source as the loopback interface.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback 0
[*HUAWEI-LoopBack0] ip address 10.1.1.1 24
[*HUAWEI-LoopBack0] quit
[*HUAWEI] tftp client source -i loopback0

```

# Set the source IPv6 address of the TFTP client to 2001:db8:2::2.
```
<HUAWEI> system-view
[~HUAWEI] tftp ipv6 client source -a 2001:db8:2::2

```