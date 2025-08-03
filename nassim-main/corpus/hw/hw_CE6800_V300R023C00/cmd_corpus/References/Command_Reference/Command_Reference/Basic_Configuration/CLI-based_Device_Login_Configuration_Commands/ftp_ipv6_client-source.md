ftp ipv6 client-source
======================

ftp ipv6 client-source

Function
--------



The **ftp ipv6 client-source** command sets and source addresses of the FTP client to establish the connection with FTP server.

The **undo ftp ipv6 client-source** command cancels the source address of the FTP client.



By default, the source address contains all 0s.


Format
------

**ftp ipv6 client-source -a** *ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ]

**undo ftp ipv6 client-source** [ **-a** *ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *ipv6-address* | Specifies the IPv6 address of the local device. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **ipv6** | Specifies the FTP IPv6 server. | - |
| **-vpn-instance** *ipv6-vpn-instance-name* | Specifies the name of the VPN instance to which the FTP server belongs.  Before specifying vpn-instance <ipv6-vpn-instance-name>, ensure that a VPN instance has been configured. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* If you run the ftp command to log in to an FTP server without specifying a source IPv6 address, the source address that is specified through the ftp client-source command is adopted by default.
* If you run the ftp command and specify a source IPv6 address, the specified source IPv6 address is adopted.

**Precautions**



This command can be run successfully when source address does not exist, but the function does not take effect.




Example
-------

# Set the FTP source IPv6 address as 2001:db8:2::2.
```
<HUAWEI> system-view
[~HUAWEI] ftp ipv6 client-source -a 2001:db8:2::2

```