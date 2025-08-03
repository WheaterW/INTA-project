ipv6 host
=========

ipv6 host

Function
--------



The **ipv6 host** command configures an IPv6 static DNS entry.

The **undo ipv6 host** command deletes an IPv6 static DNS entry.



By default, no IPv6 static DNS entry is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 host** *host-name* *ipv6-address* [ **vpn-instance** *vpn-instance-name* ]

**undo ipv6 host** *host-name* [ *ipv6-address* [ **vpn-instance** *vpn-instance-name* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *host-name* | Specifies the host name. | The value cannot contain any other character except followings: a-z A-Z 0-9 . - \_ , and must contain letters and is a string of 1 to 255 case-sensitive characters, spaces not supported. |
| *ipv6-address* | Specifies the IPv6 address mapping the host name. | The value is a 128-bit hexadecimal number, in the format of X:X:X:X:X:X:X:X, with each X representing four hexadecimal numbers. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance to which the IPv6 address corresponding to the host name belongs. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When requesting the IPv6 address mapping a domain name, the DNS client searches for the specified domain name in the static DNS table to obtain the corresponding IPv6 address. The **ipv6 host** command configures an IPv6 static DNS entry.

**Precautions**

1. You can run the **ipv6 host** command to configure a maximum of 50 static DNS entries. Each host name corresponds to only one IPv6 address. If a host name is configured for multiple times, the latest configured IP address takes effect.
2. A domain name at each level can contain a maximum of 63 characters.
3. The address specified by ipv6 host can be configured as long as it complies with the IPv6 address format, including some special addresses such as :: and ::1. Users can determine how to use these addresses.

Example
-------

# Configures an IPv6 static DNS entry mapping the host named www.huawei.com.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 host www.huawei.com 2001:db8::8

```

# Configure a static IPv6 DNS entry for host www.huawei.com in vpn1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] ipv6 host www.huawei.com 2001:db8::2 vpn-instance vpn1

```