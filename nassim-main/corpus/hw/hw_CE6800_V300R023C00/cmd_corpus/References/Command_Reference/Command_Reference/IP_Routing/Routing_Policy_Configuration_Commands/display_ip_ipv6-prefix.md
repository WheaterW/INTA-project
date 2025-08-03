display ip ipv6-prefix
======================

display ip ipv6-prefix

Function
--------



The **display ip ipv6-prefix** command displays the IPv6 prefix list.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ip ipv6-prefix** [ *pf6name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pf6name* | Specifies the name of the IPv6 prefix list. If ipv6-prefix-name is not specified, all the configured IPv6 prefix lists are displayed. | The name is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view details of the IPv6 prefix list, the number of routes that match the route-policy, and the number of routes that do not match the route-policy, run the **display ip ipv6-prefix** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all the IPv6 prefix lists.
```
<HUAWEI> display ip ipv6-prefix
ipv6-prefix abc
Description prefixok
  total permitted: 0             denied: 0   
    index 10             permit ::/0
    index 20             permit ::/1  match-network ge 1   le 128

```

**Table 1** Description of the **display ip ipv6-prefix** command output
| Item | Description |
| --- | --- |
| ipv6-prefix abc | Name of an IPv6 prefix list. |
| Description | Description of an IPv6 prefix list. This field is displayed only after a description is configured using the ip ipv6-prefix ipv6-prefix-name description text command. |
| permit | Contents of the entry in the IPv6 prefix list. |
| ge | Greater than or equal to. |
| le | Less than or equal to. |
| total permitted | Number of routes that match the route-policy. |
| index | Index of the entry in the IPv6 prefix list. |
| denied | Number of routes that do not match the route-policy. |