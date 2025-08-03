protocol
========

protocol

Function
--------



The **protocol** command configures local information (transmission mode + destination address + port + VPN + source address/source interface) about the PM server to which performance statistics files are uploaded.

The **undo protocol** command deletes local information about the PM server to which performance statistics files are uploaded.



By default, no server information is configured for uploading performance statistics files to a specified PM server.


Format
------

**protocol** { **ftp** | **sftp** } **ip-address** *ip-address* [ **port** *port-number* | { **net-manager-vpn** | **vpn-instance** *vpn-instance-name* } | { **client-source** **interface** { *interface-name* | *interface-type* *interface-number* } | **client-source** **ipv6** *IPV6ADDR* } ] \*

**undo protocol**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ftp** | Specifies the FTP protocol for uploading performance statistics files. | - |
| **sftp** | Specifies the SFTP protocol for uploading performance statistics files. | - |
| **ip-address** *ip-address* | Specifies the IP address of the PM server. | An IPv4 address is in dotted decimal notation. An IPv6 address is a 32-digit hexadecimal number in the format of X:X:X:X:X:X:X:X. |
| **port** *port-number* | Specifies the listening port number of the PM server.  If the port number is not specified, the default port number is used. | The value is an integer ranging from 1 to 65535. The default standard port number is 21 (using FTP) or 22 (using SFTP). |
| **net-manager-vpn** | Indicates the network management VPN. | - |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **client-source** | Specifies the source of a performance statistics file to be uploaded. | - |
| **interface** *interface-name* | Specifies the name of the source interface to which a performance statistics file is uploaded. | The value is a string of 1 to 63 case-sensitive characters. The interface name must exist and an IPv4 address must have been configured for the interface. |
| **interface** *interface-type* *interface-number* | Specifies the type and number of the source interface for uploading performance statistics files. | - |
| **ipv6** *IPV6ADDR* | Specifies the source IP address for uploading performance statistics files. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

PM server view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To upload performance statistics files to a specified PM server, run the pm server ip-address port-number command to specify the PM server with the IP address ip-address and port number port-number.If the IP address of the PM server is a private IP address, you can use the net-manager-vpn parameter to specify a network management VPN for uploading performance statistics files or use the vpn-instance vpn-instance-name parameter to specify a VPN instance name for uploading performance statistics files.

**Prerequisites**

You must run the **ip vpn-instance** command to create a VPN instance and run the **ipv4-family unicast** or **ipv6-family unicast** command to enable the corresponding family.The configured source interface must be a valid source interface, and an IPv4 address must have been configured for the source interface.

**Precautions**

FTP is not a secure protocol. You are advised to use SFTP.If no source IP address is configured using the **protocol** command, the source IP address configured using the **client-source** command is used to upload performance statistics files.The VPN matches the source address in use. If the VPN corresponding to the source address is not configured, the public VPN is used.

The priorities of the source address and VPN are as follows: Local source address + Local VPN (protocol configuration) > Global source address + Global VPN (client-source configuration) > Route selection + Local VPNThe priority sequence is based on the source address. If only the source address is configured but the corresponding VPN is not configured, the high-priority source address + public VPN is used.


Example
-------

# Configure the device to upload performance statistics files to a PM server with the IP address of 192.168.10.3 and the listening port number of 1025.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] pm-server a
[*HUAWEI-pm-server-a] protocol sftp ip-address 192.168.10.3 port 1025

```

# Configure the network management VPN for files to be uploaded to a PM server with the IP address of 192.168.10.2.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] pm-server a
[*HUAWEI-pm-server-a] protocol sftp ip-address 192.168.10.2 net-manager-vpn

```