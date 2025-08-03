reset ipv6 nd miss anti-attack record
=====================================

reset ipv6 nd miss anti-attack record

Function
--------



The **reset ipv6 nd miss anti-attack record** command clears attack records in scenarios where ND entries are missing.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ipv6 nd miss anti-attack record** { **all** | { *interface-name* | *interface-type* *interface-num* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Clears all attack records in scenarios where ND entries are missing. | - |
| *interface-name* | Clears all attack records on a specified interface in scenarios where ND entries are missing. | - |
| *interface-type* *interface-num* | Clears all attack records on a specified interface in scenarios where ND entries are missing. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the number of attack records in scenarios where ND entries are missing exceeds the specification or a large number of redundant records exist, run the **reset ipv6 nd miss anti-attack record** command to clear the attack records.


Example
-------

# Clear all attack records in scenarios where ND entries are missing.
```
<HUAWEI> reset ipv6 nd miss anti-attack record all

```

# Clear all attack records on a specified interface in scenarios where ND entries are missing.
```
<HUAWEI> reset ipv6 nd miss anti-attack record 100GE 1/0/1

```