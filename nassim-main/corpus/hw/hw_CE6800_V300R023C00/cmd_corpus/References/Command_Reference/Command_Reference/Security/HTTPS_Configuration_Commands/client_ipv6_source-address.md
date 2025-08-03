client ipv6 source-address
==========================

client ipv6 source-address

Function
--------



The **client ipv6 source-address** command configures a source IPv6 address and a VPN for the device functioning as an HTTP client.

The **undo client ipv6 source-address** command cancels the source IPv6 address and VPN of the HTTP client.



By default, an HTTP client source is selected by the app or sock.


Format
------

**client ipv6 source-address** *ipv6-address* [ **vpn-instance** *ipv6-vpn-instance-name* ]

**undo client ipv6 source-address** *ipv6-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the source IPv6 address of an HTTP client. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **vpn-instance** *ipv6-vpn-instance-name* | Specifies the name of the VPN instance to which the HTTP client belongs. If ipv6-vpn-instance-name is specified, ensure that the VPN instance has been configured. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

HTTP view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* To improve system security, you can run this command to specify the source IPv6 address of an HTTP client. The login restriction function is added so that the configured IP address and VPN are used to establish a link.
* When **HTTP** commands are used to transfer files, if no source IPv6 address is specified in the download and upload commands, the source IPv6 address configured in this command is used by default.
* When **HTTP** commands are used to transfer files, if an IPv6 source address is specified in the download and upload commands, the specified IPv6 source address is used.

**Precautions**

After the bound VPN is deleted, the VPN configuration in this command is not cleared, but the public VPN is used. After the VPN with the same name is reconfigured, the VPN configured in this command takes effect.


Example
-------

# Set the source IPv6 address of an HTTP client to 2001:db8:1::1 and VPN name to abc.
```
<HUAWEI> system-view
[~HUAWEI] http
[*HUAWEI-http] client ipv6 source-address 2001:db8:1::1 vpn-instance abc

```