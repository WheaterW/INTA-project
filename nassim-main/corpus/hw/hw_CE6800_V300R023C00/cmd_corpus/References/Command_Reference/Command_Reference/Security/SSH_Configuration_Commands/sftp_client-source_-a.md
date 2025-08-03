sftp client-source -a
=====================

sftp client-source -a

Function
--------



The **sftp client-source -a** command configures the specified address as the source IPv4 address of the device functioning as the SFTP client.

The **sftp ipv6 client-source -a** command configures the specified address as the source IPv6 address of the device functioning as the SFTP client.

The **undo sftp client-source** command restores the default SFTP client source IPv4 address.

The **undo sftp ipv6 client-source** command restores the default SFTP client source IPv6 address.



By default, the source IP address of the SFTP client is the IP address of the outbound interface for accessing the SFTP server.


Format
------

**sftp client-source -a** *source-ip-address*

**sftp client-source -a** *source-ip-address* { **public-net** | **-vpn-instance** *vpn-instance-name* }

**sftp ipv6 client-source -a** *source-ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ]

**undo sftp client-source**

**undo sftp ipv6 client-source** [ **-a** *source-ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *source-ip-address* | Specifies the IPv4 address of the local device. | The value is in dotted decimal notation. |
| **-a** *source-ipv6-address* | Specifies the IPv6 address of the local device. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **public-net** | Specifies the public network where the SFTP server resides. | - |
| **-vpn-instance** *ipv6-vpn-instance-name* | Specifies the name of a VPN instance to which the SFTP server belongs.  Before specifying the parameter vpn-instance ipv6-vpn-instance-name, ensure that a VPN instance has been configured. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| **-vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance to which the SFTP server belongs.  Before specifying the parameter vpn-instance vpn-instance-name, ensure that a VPN instance has been configured. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If you run the **sftp** command to log in to an SFTP server without specifying a source address or source interface, the source address or source interface specified through the **sftp client-source** command is adopted by default. If you run the **sftp** command and specify the source address or source interface, the specified source address or source interface is adopted. When viewing the current SFTP connection on the server, the specified source IP address or the primary IP address of the specified interface is displayed as the IP address of the user.

**Precautions**

* If the specified source interface has been bound to a VPN instance, the client is automatically bound to the same VPN instance.
* If the specified source interface has been bound to a VPN instance, for example, vpn1, but a different VPN instance, for example, vpn2, is specified in the **sftp client-source** command, The vpn configured by this command (vpn2) takes effect.
* After a bound VPN instance is deleted, the VPN configuration specified using the **sftp client-source** command will not be cleared but does not take effect. In this case, the SFTP server uses a public IP address. If you configure the VPN instance with the same name again, the VPN function restores.
* After a bound source interface is deleted, the interface configuration specified using the **sftp client-source** command will not be cleared but does not take effect. If you configure the source interface with the same name again, the interface configuration specified using the **sftp client-source** command is updated and the function restores.

Example
-------

# Set the source IP address of the SFTP client to 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] sftp client-source -a 10.1.1.1

```