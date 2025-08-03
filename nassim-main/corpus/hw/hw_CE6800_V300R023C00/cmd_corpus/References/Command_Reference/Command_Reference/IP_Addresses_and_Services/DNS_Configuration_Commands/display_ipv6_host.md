display ipv6 host
=================

display ipv6 host

Function
--------



The **display ipv6 host** command displays the static IPv6 DNS table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 host** [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After running the **ipv6 host** command to configure static IPv6 DNS entries, you can run the **display ipv6 host** command to check whether mappings between host names and IPv6 addresses are correct.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the static IPv6 DNS table.
```
<HUAWEI> display ipv6 host
Host                 Age        Flag    IPv6 Address
www.huawei.com        0        static   FC00:1::8
www.sohu.com          0        static   FC00:1::9
Total    :  2

```

# Display the static IPv6 DNS table of vpn1.
```
<HUAWEI> display ipv6 host vpn-instance vpn1
Host                 Age        Flag    IPv6 Address
www.huawei.com        0        static   FC00:1::8
www.sohu.com          0        static   FC00:1::9
Total    :  2

```

**Table 1** Description of the **display ipv6 host** command output
| Item | Description |
| --- | --- |
| Host | Host name. |
| Age | Aging time. The value 0 indicates that the entry is not aged out. |
| Flag | DNS table identifiers. The value static indicates a static domain name. |
| IPv6 Address | IPv6 address mapping the domain name. |
| Total | Number of dynamic DNS entries. |