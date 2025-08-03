reset ipv6 pathmtu
==================

reset ipv6 pathmtu

Function
--------



The **reset ipv6 pathmtu** command clears dynamic PMTU entries.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ipv6 pathmtu** [ **vpn-instance** *vpn-instance-name* ] **dynamic**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Clears dynamic PMTU entries of a specified IPv6 VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **dynamic** | Clears all dynamic PMTU entries. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To clear dynamic PMTU entries, run the **reset ipv6 pathmtu** command. Either all dynamically learned PMTU entries or the PMTU entries of a specified VPN instance can be cleared.If you want to collect statistics about dynamic PMTU entries within a specified period, run the **reset ipv6 pathmtu** command beforehand to clear the existing statistics about dynamic PMTU entries. You can then run the **display ipv6 pathmtu** command to view dynamic PMTU entries.



**Configuration Impact**

Running the **reset ipv6 pathmtu** command clears all dynamic PMTU entries. Exercise caution when running this command.


Example
-------

# Clear all dynamic PMTU entries.
```
<HUAWEI> reset ipv6 pathmtu dynamic

```