reset dns ipv6 dynamic-host
===========================

reset dns ipv6 dynamic-host

Function
--------



The **reset dns ipv6 dynamic-host** command clears IPv6 dynamic DNS entries.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset dns ipv6 dynamic-host** [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After confirming the action of deleting IPv6 dynamic DNS entries, you can run the **reset dns ipv6 dynamic-host** command to delete them.

**Precautions**

IPv6 dynamic DNS entries cannot be restored after being deleted. Confirm the action before you run the command.


Example
-------

# Clear all IPv6 dynamic DNS entries.
```
<HUAWEI> reset dns ipv6 dynamic-host

```

# Clear dynamic IPv6 DNS entries in vpn1.
```
<HUAWEI> reset dns ipv6 dynamic-host vpn-instance vpn1

```