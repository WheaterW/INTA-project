open
====

open

Function
--------



The **open** command establishes the FTP connection with FTP server.




Format
------

**open** [ **-a** *source-ip4* | **-i** { *interface-type* *interface-number* | *interface-name* } ] *host-ip-address* [ *port-number* ] [ **vpn-instance** *vpn-instance-name* | **public-net** ]

**open ipv6** [ **-a** *source-ip6* ] *host-ipv6-address* [ *port-number* ] [ **vpn-instance** *vpn-instance-name* | **public-net** ]

**open ipv6** [ **-a** *source-ip6* ] *host-ipv6-address* **-oi** { *interface-type* *interface-number* | *interface-name* } [ *port-number* ] [ **vpn-instance** *vpn-instance-name* | **public-net** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *source-ip6* | Specifies the source IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **-a** *source-ip4* | Specifies the source IPv4 address. | The value is in dotted decimal notation. |
| **-i** *interface-name* | Specifies the source interface name. | - |
| *interface-type* | Specifies the source interface type. | - |
| *interface-number* | Specifies the source interface number. | - |
| *host-ip-address* | Specifies the IPv4 address or host name for the FTP server.  To view the mapping between the IPv4 address and host name, run the display dns dynamic-host or display ip host command. | The value is a string of 1 to 255 case-sensitive characters. It cannot contain spaces. |
| *port-number* | Specifies the FTP server port number. | The value is an integer ranging from 1 to 65535. The default value is 21. |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *vpn-instance-name* | Specifies the IPv6 VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **public-net** | Specifies the public network where the FTP server resides.  If you have run the set net-manager vpn-instance command to configure the default VPN instance used for an NMS to manage devices and want to use FTP to access a public network server, you must specify this parameter. | - |
| **ipv6** *host-ipv6-address* | Specifies the IPv6 address or host name for the FTP server.  To view the mapping between the IPv6 address and host name, run the display dns dynamic-host or display ip host command. | The value is a string of case-sensitive characters. It cannot contain spaces. |
| **-oi** | Specifies the source interface for the IPv6 FTP client, including the type and number of the interface. The IPv6 address configured in this interface view is the source IPv6 address of the packet. If no IPv6 address is configured for the source interface, the FTP connection cannot be set up.  Setting the loopback interface as the source IPv6 address is recommended. | - |



Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **ftp** command in the user view to connect the FTP client and server and enter the FTP client view. If FTP is disconnected, you can run this command to establish an FTP connection.

**Prerequisites**

The VPN instance to be specified in this command has been configured.

**Configuration Impact**

After establishing successful connection with the host, you can upload or download files.If server monitors the FTP connection through default port, you need not specify the port number. Otherwise you must specify the port number.


Example
-------

# Establish FTP connection with a remote server.
```
<HUAWEI> ftp
[ftp] open -a 10.1.1.1 10.1.1.2
Username:abcd
password:

```

# Establish FTP connection with a remote server with source interface loopback0.
```
<HUAWEI> ftp
[ftp] open -i loopBack0 10.1.1.2 1000
Username:abcd
password:

```

# Establish FTP connection with a remote server with through VPN.
```
<HUAWEI> ftp
[ftp] open 10.1.1.2 1000 vpn-instance vpn1
Username:abcd
password:

```

# Establish FTP connection with a remote server with IPv6 address.
```
<HUAWEI> ftp
[ftp] open ipv6 2001:db8:1::1 -oi 100GE 1/0/1
Trying 2001:db8:1::1
Press CTRL+K to abort
Connected to 2001:db8:1::1
220 FTP service ready.
User(ftp 2001:db8:1::1:(none)):huawei
331 Password required for huawei
Password:

```

# Set up a connection with FTP server 2001:db8:1::1.
```
<HUAWEI> ftp
[ftp] open ipv6 2001:db8:1::1
Trying 2001:db8:1::1 ...
Press CTRL+K to abort
Connected to 2001:db8:1::1
220 FTP service ready.
User(2001:db8:1::1:(none)):root
331 Password required for root
Enter Password:

```