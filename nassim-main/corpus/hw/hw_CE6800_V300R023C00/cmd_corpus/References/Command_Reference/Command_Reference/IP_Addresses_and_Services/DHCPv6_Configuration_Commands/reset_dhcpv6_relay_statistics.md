reset dhcpv6 relay statistics
=============================

reset dhcpv6 relay statistics

Function
--------



The **reset dhcpv6 relay statistics** command clears packet statistics on a DHCPv6 relay agent.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset dhcpv6 relay statistics** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface.  If no interface is specified, all the DHCPv6 message statistics are cleared. If an interface is specified, DHCPv6 message statistics on the specified interface are cleared. | - |
| *interface-name* | Specifies the name of an interface.  If no interface is specified, DHCPv6 message statistics on all relay interfaces are cleared. If an interface is specified, DHCPv6 message statistics on the specified interface are cleared. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a device is enabled with the DHCPv6 relay function, the system takes the statistics about DHCPv6 messages passing through the DHCP relay agent. You can use the reset dhcpv6 relay statistics command to clear current message statistics on the DHCPv6 relay agent.


Example
-------

# Clear the DHCPv6 message statistics on100GE1/0/1.
```
<HUAWEI> reset dhcpv6 relay statistics interface 100GE1/0/1

```