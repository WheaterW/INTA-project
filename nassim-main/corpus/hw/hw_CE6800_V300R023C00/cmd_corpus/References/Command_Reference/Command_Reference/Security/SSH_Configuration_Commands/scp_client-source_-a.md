scp client-source -a
====================

scp client-source -a

Function
--------



The **scp client-source -a** command configures a source IPv4 address for the SCP client.

The **scp ipv6 client-source -a** command configures a source IPv6 address for the SCP client.

The **undo scp client-source** command restores the default source IPv4 address for the SCP client.

The **undo scp ipv6 client-source** command restores the default source IPv6 address for the SCP client.



By default, the source IPv4 address of the SCP client is 0.0.0.0 and the source IPv6 address is 0::0.


Format
------

**scp client-source -a** *source-ip-address*

**scp client-source -a** *source-ip-address* { **public-net** | **-vpn-instance** *vpn-instance-name* }

**scp ipv6 client-source -a** *source-ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ]

**undo scp client-source**

**undo scp ipv6 client-source**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *source-ip-address* | Specifies a source IPv4 address for the SCP client. | The value is in the decimal format. |
| **-a** *source-ipv6-address* | Specifies a source IPv6 address for the SCP client. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **public-net** | Specifies the public network where the SCP server resides. | - |
| **-vpn-instance** *ipv6-vpn-instance-name* | Specifies the name of a VPN instance to which the SCP server belongs.  Before specifying the parameter vpn-instance ipv6-vpn-instance-name, ensure that a VPN instance has been configured. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| **-vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance to which the SCP server belongs.  Before specifying the parameter vpn-instance vpn-instance-name, ensure that a VPN instance has been configured. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If you run the **scp** command to log in to the SCP server without specifying a source IP address or source interface, the source IP address or source interface specified using the **scp client-source** command is adopted by default. When the SCP connection on the server is viewed, the specified source IP address or the primary IP address of the specified source interface is displayed as the IP address of the user.

**Prerequisites**

VPN configuration must be successful, to configure the vpn instance using this command.

**Precautions**

* If the specified source interface has been bound to a VPN instance, the client is automatically bound to the same VPN instance.
* If the specified source interface has been bound to a VPN instance, for example, vpn1, but a different VPN instance, for example, vpn2, is specified in the **scp client-source -a source-ip-address -vpn-instance vpn-instance-name** command, the VPN configured by this command (vpn2) takes effect.
* After a bound VPN instance is deleted, the VPN configuration specified using the **scp client-source** command will not be cleared but does not take effect. In this case, the SCP server uses a public IP address. If you configure the VPN instance with the same name again, the VPN function restores.
* After a bound source interface is deleted, the interface configuration specified using the **scp client-source** command will not be cleared but does not take effect. If you configure the source interface with the same name again, the interface configuration specified using the **scp client-source** command is updated and the function restores.

Example
-------

# Set the source IPv6 address of the SCP client to 2001:db8:2::2.
```
<HUAWEI> system-view
[~HUAWEI] scp ipv6 client-source -a 2001:db8:2::2

```

# Set the source IPv4 address of the SCP client to 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] scp client-source -a 10.1.1.1

```