reset bmp session
=================

reset bmp session

Function
--------



The **reset bmp session** command resets a specified BGP Monitoring Protocol (BMP) session.




Format
------

**reset bmp session** [ **vpn-instance** *vrf-name* ] { *ipv4Addr* | *ipv6Addr* | **all** }

**reset bmp session** [ **vpn-instance** *vrf-name* ] { *ipv4Addr* | *ipv6Addr* } **alias** *alias-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vrf-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *ipv4Addr* | Resets a BMP session with an IPv4 session address. | The value is in dotted decimal notation. |
| *ipv6Addr* | Resets a BMP session with an IPv6 session address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **all** | Resets all BMP sessions. | - |
| **alias** *alias-name* | Specifies a session alias. When the device needs to establish multiple TCP connections with the same monitoring server through different port numbers, specify session aliases for differentiation. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After configuring BMP session parameters, run the **reset bmp session** command to reset the BMP session for the new BMP session parameters to take effect.Run the following commands can change the BMP session configurations:

* The **bmp-session** command specifies an address of the monitoring server for the TCP connection between the router and the monitoring server.
* The **tcp** command configures parameters for the TCP connection between the router and the monitoring server.

**Configuration Impact**



Running the **reset bmp session** command will reset the TCP connection and BMP session between the router and the monitoring server. Therefore, exercise caution when running this command.




Example
-------

# Reset the BMP session with 10.1.1.1 as the session address.
```
<HUAWEI> reset bmp session 10.1.1.1

```

# Reset all BMP sessions.
```
<HUAWEI> reset bmp session all

```

# Reset the BMP session with 2001:DB8:1::1 as the session address.
```
<HUAWEI> reset bmp session 2001:DB8:1::1

```

# Reset the BMP session with the session address of 10.1.1.1 and alias of aa.
```
<HUAWEI> reset bmp session 10.1.1.1 alias aa

```