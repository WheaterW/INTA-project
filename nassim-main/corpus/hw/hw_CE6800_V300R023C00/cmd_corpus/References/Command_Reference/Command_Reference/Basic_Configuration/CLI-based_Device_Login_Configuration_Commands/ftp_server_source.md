ftp server source
=================

ftp server source

Function
--------



The **ftp server source** command sets the specific source IP address of the FTP server to establish the connection, including the source IP address and source interface.

The **undo ftp server source** command cancels the configuration of FTP server source configuration.



By default, the IPv4 source address of packets sent by the FTP server is 0.0.0.0 . The IPv6 source address of packets sent by the FTP server is ::.


Format
------

**ftp server source** { **-a** { *ip-address* } | **-i** { *interface-type* *interface-number* | *interface-name* } }

**ftp ipv6 server source -a** *ipv6-address* [ **-vpn-instance** *vpn-instance-name* ]

**ftp ipv6 server source all-interface**

**ftp server source all-interface**

**undo ftp server source** { **-a** { *ip-address* } | **-i** { *interface-type* *interface-number* | *interface-name* } }

**undo ftp ipv6 server source -a** *ipv6-address* [ **-vpn-instance** *vpn-instance-name* ]

**undo ftp ipv6 server source all-interface**

**undo ftp server source all-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *ip-address* | Specifies the source IP address. | The value is in dotted decimal notation. |
| **-a** *ipv6-address* | Specifies the source IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **-i** *interface-name* | Specifies the source interface name of an FTP server. | - |
| *interface-type* *interface-number* | Specifies the source interface type and interface number of an FTP server. | - |
| **ipv6** | Specifies the FTP IPv6 server. | - |
| **-vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **all-interface** | Indicates that any interface having an IP address configured can be used as the source interface of an FTP server. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



The FTP server receives login connection requests from all interfaces and addresses, which has low system security. To improve system security, run the ftp server-source command to specify the source interface of the FTP server.



**Prerequisites**



A VPN instance has been created before you specify it for an FTP server. Otherwise, the command cannot be executed.



**Configuration Impact**

If a source interface or source IPv6 address is specified for an FTP server, FTP users can log in only through the specified source interface or source IPv6 address.

**Precautions**

* The FTP protocol has security risks. You are advised to use the SFTP protocol.
* After the command is run, users can log in to the FTP server only through a specified interface or a specified IPv6 address.
* If the interface to which the specified source IPv6 address belongs is bound to a VPN instance, the -vpn-instance parameter must be specified when you specify an IPv6 address for the client.
* If the specified source interface is bound to a VPN instance (vpn1 for example) and another VPN instance (vpn2 for example) is specified in the **ftp ipv6 server source -a ipv6-address -vpn-instance** command, vpn1 is used for IPv4 users, and vpn2 is used for IPv6 users.
* If the VPN instance bound to the specified source interface is deleted, the VPN configuration specified in the command is not cleared but does not take effect. In this case, the FTP server uses the public network instance instead. If the VPN instance with the same name as the deleted one is reconfigured, the VPN function will be restored.
* If the specified source interface is deleted, the interface configuration in the command is not deleted but does not take effect. If the source interface with the same name as the deleted one is reconfigured, the function will be restored.
* For an IPv6 FTP server, you can run the ftp ipv6 server source -a ipv6-address [ -vpn-instance vpn-instance-name ] command to configure a user to log in to the server through a specified IPv6 source address.
* If the **ftp server source all-interface** command is run, users can log in to the FTP server through any valid IPv4 interface, which increases system security risks. Therefore, running this command is not recommended.
* If the **ftp ipv6 server source all-interface** command is run, users can log in to the FTP server through any valid IPv6 interface, which increases system security risks. Therefore, running this command is not recommended.
* If both the **ftp server source -i** and **ftp server source all-interface** commands are run, the interface whose IPv6 address is specified in the **ftp server-source -i** command is preferentially used as the source interface of the FTP server. If the specified source interface fails to be used for login, another valid interface address will be used for login.
* The **ftp server source -i interface-type interface-number** and **ftp server source all-interface** commands take effect only for IPv4.
* If both the **ftp ipv6 server source -a** and **ftp ipv6 server source all-interface** commands are run, the address specified in the **ftp ipv6 server-source -a** command is preferentially used as the source address of the FTP server. If the specified source address cannot be used for login, another valid address is selected for login.
* The **ftp ipv6 server source -a interface-type interface-number** and **ftp ipv6 server source all-interface** commands take effect only for IPv6.


Example
-------

# Set the source IPv4 address of the FTP server to 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] ftp server source -a 10.1.1.1

```

# Set the source interface of the FTP server to a loopback interface.
```
<HUAWEI> system-view
[~HUAWEI] interface LoopBack 0
[~HUAWEI-LoopBack0] ip address 10.1.1.1 16
[*HUAWEI-LoopBack0] quit
[*HUAWEI] ftp server source -i loopback 0

```

# Allow any IPv4 interface to be used as the source IPv4 interface of an FTP server.
```
<HUAWEI> system-view
[~HUAWEI] ftp server source all-interface

```

# Allow any IPv6 interface to be used as the source IPv6 interface of an FTP server.
```
<HUAWEI> system-view
[~HUAWEI] ftp ipv6 server source all-interface

```