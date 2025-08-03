reset ip ipv6-prefix
====================

reset ip ipv6-prefix

Function
--------



The **reset ip ipv6-prefix** command resets the statistics of the specified IPv6 prefix list. If ipv6-prefix-name is not specified, you can reset the statistics of all the IPv6 prefix lists.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ip ipv6-prefix** [ *pf6name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pf6name* | Specifies the name of the IPv6 prefix list. | The name is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To reset timers in permit and deny modes of an IPv6 prefix list, run the reset ip ipv6-prefix command.


Example
-------

# Reset the statistics of the specified IPv6 prefix list.
```
<HUAWEI> reset ip ipv6-prefix abc

```