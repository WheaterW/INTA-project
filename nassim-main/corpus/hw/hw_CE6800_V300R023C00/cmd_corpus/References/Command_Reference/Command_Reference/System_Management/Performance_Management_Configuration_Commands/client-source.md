client-source
=============

client-source

Function
--------



The **client-source interface** command configures a global IPv4 source interface for uploading performance statistics files to a specified PM server. (The IPv4 address of the source interface is used as the source address, and the VPN instance of the source interface is used as the VPN instance.).

The **undo client-source interface** command deletes the global source interface used to upload performance statistics files to a specified PM server.

The **client-source ipv6** command configures a global source IPv6 address and a VPN instance for uploading performance statistics files to a specified PM server.

The **undo client-source ipv6** command cancels the configuration.



By default, no global source IP address or global VPN information is configured for uploading performance statistics files to a specified PM server.


Format
------

**client-source interface** { *interface-name* | *interface-type* *interface-number* }

**client-source ipv6** *IPV6ADDR* [ **vpn-instance** *vpnInstanceName* ]

**undo client-source interface**

**undo client-source ipv6**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **client-source** | Specifies the source of a performance statistics file to be uploaded. | - |
| **ipv6** *IPV6ADDR* | Specifies the source IP address for uploading performance statistics files. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpnInstanceName* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| **interface** *interface-name* | Specifies the name of the source interface to which a performance statistics file is uploaded. | The value is a string of 1 to 63 case-sensitive characters. The interface name must exist and an IPv4 address must have been configured for the interface. |
| **interface** *interface-type* *interface-number* | Specifies the type and number of the source interface for uploading performance statistics files. | - |



Views
-----

Performance management view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To upload performance statistics files to an IPv4 PM server, run the **client-source interface** command to specify the IPv4 address and VPN of an interface as the global source address and VPN, respectively. Other upload parameters can be specified using the **protocol** command.To upload performance statistics files to an IPv6 PM server, run the **client-source ipv6** command to specify a global source address and a VPN instance. Other upload parameters can be specified using the **protocol** command. If the IPv6 PM server address is a private address, you can use the vpn-instance vpn-instance-name parameter to specify a VPN instance name for file upload.

**Prerequisites**

The VPN configured using the **client-source ipv6** command must exist, and the IPv6 address family must be enabled for the VPN.The source interface configured using the **client-source interface** command must be a valid source interface, and an IPv4 address must have been configured for the source interface.

**Precautions**

If no source IP address is configured using the **protocol** command, the source IP address configured using the **client-source** command is used to upload performance statistics files.The VPN matches the source address in use. If the VPN corresponding to the source address is not configured, the public VPN is used.

The priorities of the source address and VPN are as follows: Local source address + Local VPN (protocol configuration) > Global source address + Global VPN (client-source configuration) > Route selection + Local VPNThe priority sequence is based on the source address. If only the source address is configured but the corresponding VPN is not configured, the high-priority source address + public VPN is used.


Example
-------

# Set the source IPv6 address for uploading performance statistics files to 2001:db8:1::1.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] client-source ipv6 2001:db8:1::1

```