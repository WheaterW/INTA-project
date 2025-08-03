display dns ipv6 dynamic-host
=============================

display dns ipv6 dynamic-host

Function
--------



The **display dns ipv6 dynamic-host** command displays IPv6 dynamic DNS entries.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dns ipv6 dynamic-host** [ *domain-name* ] [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *domain-name* | Specifies the domain name. | The value is a string of 1 to 255 case-sensitive characters. If the string is enclosed in double quotation marks ("), spaces are allowed in the string. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the **display dns ipv6 dynamic-host** command to view IPv6 dynamic DNS entries and check whether domain names match the mapping entries.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display dynamic IPv6 DNS entries in the VPN named vpn1.
```
<HUAWEI> display dns ipv6 dynamic-host vpn-instance vpn1
Host                           TTL    Type   Address
excample.com                   119    IPv6   2001:db8:1::10

Total : 1

```

# Display IPv6 dynamic DNS entries.
```
<HUAWEI> display dns ipv6 dynamic-host
Host                                     TTL        Type   Address                                                                  
www.huawei.com                           86394      IPv6   2001:db8:1::101                                                 
                                                                                                                                    
Total  :  1

```

**Table 1** Description of the **display dns ipv6 dynamic-host** command output
| Item | Description |
| --- | --- |
| Host | Domain name. |
| TTL | Time left before dynamic DNS entries saved in the domain name cache will be aged out, in seconds. |
| Type | Dynamic DNS entry type. |
| Address | IPv6 address in a dynamic cache entry. |
| Total | Number of dynamic DNS entries. |