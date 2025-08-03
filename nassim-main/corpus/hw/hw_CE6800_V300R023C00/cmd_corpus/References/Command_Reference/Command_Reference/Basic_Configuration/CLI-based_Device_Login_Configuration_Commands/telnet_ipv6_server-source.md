telnet ipv6 server-source
=========================

telnet ipv6 server-source

Function
--------



The **telnet ipv6 server-source** command specifies an IPv6 address for a Telnet server.

The **undo telnet ipv6 server-source** command restores the default setting.



By default, the source IPv6 address of a Telnet server is not specified.


Format
------

**telnet ipv6 server-source -a** *ipv6-address* [ **-vpn-instance** *vpn-instance-name* ]

**telnet ipv6 server-source all-interface**

**undo telnet ipv6 server-source -a** *ipv6-address* [ **-vpn-instance** *vpn-instance-name* ]

**undo telnet ipv6 server-source all-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-vpn-instance** *vpn-instance-name* | Specifies the VPN. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-interface** | Indicates that any interface having an IP address configured can be used as the source interface of a Telnet server. | - |
| **-a** *ipv6-address* | Specifies the source IPv6 address of the Telnet server. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To improve system security, you can run this command to specify a source interface or source IPv6 address for a Telnet server. Only authorized users can log in to the Telnet server.

* If only the **telnet ipv6 server-source** **-a** command is run, the specified interface is used as the source interface.
* If only the **telnet ipv6 server-source** **all-interface** command is run, the source interface is any valid interface on the device, including the physical interface configured with an IP address and the created logical interface configured with an IP address.
* If both the **telnet ipv6 server-source** **-a** and **telnet ipv6 server-source** **all-interface** commands are run, the interface with the IPv6 address specified in the **telnet ipv6 server-source** **-a** command is preferentially used as the source interface of the Telnet server.
* If you do not run the **telnet server-source** command to specify a source interface when the system starts with factory configurations, users cannot access the system through Telnet.

**Prerequisites**

A VPN instance has been created before you specify it for a Telnet server using the **telnet ipv6 server-source** **-a** ipv6-address [ **-vpn-instance** vpn-instance-name ] command. Otherwise, the command cannot be executed.

**Configuration Impact**

After the source IPv6 address is specified, the system only allows Telnet users to log in to the Telnet server through this source ipv6 address, and Telnet users logging in through other interfaces are denied. Note that setting this parameter only affects Telnet users that attempt to log in to the Telnet server, and it does not affect Telnet users that have logged in to the server.

**Precautions**

* The Telnet protocol has security risks. You are advised to use the SSHv2 protocol.
* If a source interface or source IPv6 address is specified for a Telnet server, Telnet users must be able to communicate with the specified source interface or source IPv6 address at Layer 3 to ensure that authorized Telnet users can log in to the server.
* If the specified source interface is bound to a VPN instance, the Telnet server is also bound to the VPN instance.
* After the bound VPN instance is deleted, the VPN configuration in this command is not cleared, but the function does not take effect. In this case, the Telnet server uses the public network instance instead. After the VPN instance with the same name is reconfigured, the VPN function is restored.
* For an IPv6 Telnet server, you can run the telnet ipv6 server-source -a ipv6-address [ -vpn-instance <vpn-instance-name> ] command to configure users to log in to the server using a specified IPv6 source address.
* After the **telnet ipv6 server-source all-interface** command is run, no IPv6 source interface is specified for the Telnet server. Users can log in to the Telnet server through any valid interface, which increases system security risks. Therefore, running this command is not recommended.
* After the bound source interface is deleted, the interface configuration in this command is not deleted, but the function does not take effect. After the source interface with the same name is reconfigured, the function is restored.
* If both the **telnet ipv6 server-source -a** and **telnet ipv6 server-source all-interface** commands are run, the address specified in the **telnet ipv6 server-source -a** command is preferentially used as the source address of the Telnet server. If the specified source address cannot be used for login, another valid address is selected for login.
* The **telnet ipv6 server-source -a interface-type interface-number** and **telnet ipv6 server-source all-interface** commands take effect only for IPv6.


Example
-------

# Specify 2001:db8:1::1 as the ipv6 source address of the Telnet server.
```
<HUAWEI> system-view
[~HUAWEI] telnet ipv6 server-source -a 2001:db8:1::1

```

# Allow any IPv6 interface address on the Telnet server to be used as the source IPv6 address of the server.
```
<HUAWEI> system-view
[~HUAWEI] telnet ipv6 server-source all-interface

```