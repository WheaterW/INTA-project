telnet
======

telnet

Function
--------



The **telnet** command enables the system to log in to another device from the current device through Telnet.




Format
------

**telnet** [ **-i** { *interface-type* *interface-number* | *interface-name* } | [ **vpn-instance** *vpn-instance-name* ] [ **-a** *source-ip-address* ] ] *host-ip-address* [ *port-number* ]

**telnet ipv6** [ **-a** *source-ipv6-address* ] [ **public-net** | **vpn-instance** *ipv6-vpn-name* ] *ipv6-address* [ **-oi** { *interface-type* *interface-number* | *interface-name* } ] [ *port-number* ]

**telnet ipv6** [ **-a** *source-ipv6-address* ] *ipv6-address* [ **public-net** | **vpn-instance** *ipv6-vpn-name* ] [ **-oi** { *interface-type* *interface-number* | *interface-name* } ] [ *port-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-i** | Specifies the source interface. | - |
| *interface-type* | Specifies the source interface type. | - |
| *interface-number* | Specifies the source interface number. | - |
| *interface-name* | Specifies the source interface name. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance to which the device to be logged in using Telnet belongs. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **-a** *source-ip-address* | Specifying a source IP address, you can use this address to communicate with the server for passing security checks. If no source address is specified, the system will use the IP address of the outbound interface on the local device to initiate a Telnet connection. | The value is in the decimal format. |
| *host-ip-address* | Specifies the remote host IPv4 address or name. | The value is a string case-sensitive characters, spaces not supported. |
| *port-number* | Specifies the TCP port number used by the remote device that functions as the Telnet server. | Port number is an integer that ranges from 1 to 65535. By default, the port number is 23. |
| **public-net** | Connect in public network. | - |
| **ipv6** *ipv6-address* | Specifies the remote host IPv6 address or name. | The value is a string case-sensitive characters, spaces not supported. |
| *source-ipv6-address* | Specifying the source IPv6 address, you can use this address to communicate with the server for passing security checks. If no source address is specified, the system will use the IPv6 address of the outbound interface on the local device to initiate a Telnet connection. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *ipv6-vpn-name* | Specifies the name of the IPv6 VPN instance to which the device to be logged in using Telnet belongs. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **-oi** | Specifying a source interface. | - |



Views
-----

User view


Default Level
-------------

0: Visit level


Usage Guidelines
----------------

**Usage Scenario**

If one or more devices need to be configured and managed, you do not need to connect each of the devices to a terminal to maintain the devices locally. If you have obtained the IP address of a device, you can log in to the device from a terminal using Telnet to remotely configure the device. This allows you to maintain multiple devices on one terminal, greatly facilitating device management.

**Prerequisites**

The terminal communicates with the remote device at Layer 3 and the Telnet server function is enabled on the remote device.

**Implementation Procedure**

During a Telnet connection, you can enter CTRL+K to terminate the connection.

**Configuration Impact**

User logins through Telnet may bring security risks because Telnet does not provide any secure authentication mechanism and data is transmitted using TCP in plain text. Using STelnet is recommended for a network that has high security requirements.

**Precautions**



To ensure security, you are advised to use the STelnet service.This command can be used only after the weak protocol feature package (WEAKEA) is installed using the **install feature-software WEAKEA** command.




Example
-------

# Establish a telnet connection with a remote server.
```
<HUAWEI> telnet 10.0.1.6
Trying 10.0.1.6 ...
Press CTRL+K to abort
Connected to 10.0.1.6 ...

Username:john
Password:

```

# Establish a telnet connection with a remote server over IPv6.
```
<HUAWEI> telnet ipv6 2001:db8:1::1
Trying 2001:db8:1::1 ...
Press CTRL+K to abort
Connected to 2001:db8:1::1 ...

Username:john
Password:

```