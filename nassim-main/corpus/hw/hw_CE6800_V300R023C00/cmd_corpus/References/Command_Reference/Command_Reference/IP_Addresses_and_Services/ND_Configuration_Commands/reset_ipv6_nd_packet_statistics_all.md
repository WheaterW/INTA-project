reset ipv6 nd packet statistics all
===================================

reset ipv6 nd packet statistics all

Function
--------



The **reset ipv6 nd packet statistics all** command clears all ND message statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ipv6 nd packet statistics all**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To clear all ND messages statistics for troubleshooting of ND-related issues, run the **reset ipv6 nd packet statistics all** command.


Example
-------

# Clear ND message statistics.
```
<HUAWEI> reset ipv6 nd packet statistics all

```