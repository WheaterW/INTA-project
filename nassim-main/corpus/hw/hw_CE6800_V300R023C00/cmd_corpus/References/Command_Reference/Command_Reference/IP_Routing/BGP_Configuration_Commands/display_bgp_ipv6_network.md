display bgp ipv6 network
========================

display bgp ipv6 network

Function
--------



The **display bgp ipv6 network** command displays the IPv6 routes imported into the BGP routing table using the network command.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 network**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Displays the IPv6 routes advertised by BGP. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp ipv6 network** command displays the IPv6 routes imported into the BGP routing table using the **network** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display IPv6 routes advertised by BGP.
```
<HUAWEI> display bgp ipv6 network
BGP Local Router ID is 10.5.5.5
Local AS Number is 100(PublicV6)
Network          Prefix           Route-policy

2001:DB8:100::   64
2001:DB8:200::   64

```

**Table 1** Description of the **display bgp ipv6 network** command output
| Item | Description |
| --- | --- |
| BGP Local Router ID is | ID of the local BGP device. The ID is in the same format as an IPv4 address. |
| Local AS Number is | Local AS number. |