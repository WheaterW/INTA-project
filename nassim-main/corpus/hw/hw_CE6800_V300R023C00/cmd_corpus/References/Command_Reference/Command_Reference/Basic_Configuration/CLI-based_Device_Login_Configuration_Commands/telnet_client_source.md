telnet client source
====================

telnet client source

Function
--------



The **telnet client source** command configures a source for the Telnet client to establish a connection to the Telnet server.

The **undo telnet client source** command deletes the configured source.



By default, the IPv4 source address of the Telnet client is 0.0.0.0, the IPv6 source address of the Telnet client is::.


Format
------

**telnet client source** { { **-a** *source-ip-address* } | { **-i** { *interface-type* *interface-number* | *interface-name* } } }

**telnet ipv6 client source -a** *source-ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ]

**undo telnet client source**

**undo telnet ipv6 client source** [ **-a** *source-ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *source-ipv6-address* | Specifies the source IPv6 address of the Telnet client. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **-a** *source-ip-address* | Specifies the source IP address of the Telnet client. | The value is in the decimal format. |
| **-i** *interface-name* | Specifies the source interface name for the Telnet client to establish a connection to the server. | - |
| *interface-type* | Specifies the type of the source interface for the Telnet client to establish a connection to the server. | - |
| *interface-number* | Specifies the number of the source interface for the Telnet client to establish a connection to the server. | - |
| **ipv6** | Specifies the IPv6 protocol. | - |
| **-vpn-instance** *ipv6-vpn-instance-name* | Specifies the name of a VPN instance to which the Telnet server belongs.  Before specifying the parameter vpn-instance ipv6-vpn-instance-name, ensure that a VPN instance has been configured. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



When you run the **telnet** command to log in to a Telnet server without specifying a source address or interface, the source address or interface configured using the **telnet client source** command is adopted by default. If you run the **telnet** command and specify a source address or interface, you can log in to the Telnet server using the specified source address or interface.After a bound source interface is deleted, the interface configuration specified using the **telnet client source** command will not be cleared but does not take effect. If you configure the source interface with the same name again, the interface configuration specified using the **telnet client source** command is updated and the function restores.



**Precautions**

If the specified source interface has been bound to a VPN instance, the client is automatically bound to the same VPN instance.


Example
-------

# Set the source IP address of the Telnet client to 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] telnet client source -a 10.1.1.1

```

# Set the source interface of the Telnet client to Loopback 0.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback 0
[*HUAWEI-LoopBack0] ip address 10.1.1.1 24
[*HUAWEI-LoopBack0] quit
[*HUAWEI] telnet client source -i loopback0

```