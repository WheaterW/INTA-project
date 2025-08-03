reset ipv6 nd multicast-suppress dynamic bridge-domain
======================================================

reset ipv6 nd multicast-suppress dynamic bridge-domain

Function
--------



The **reset ipv6 nd multicast-suppress dynamic bridge-domain** command clears dynamic proxy ND entries in a specified BD.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ipv6 nd multicast-suppress dynamic bridge-domain** [ *bd-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *bd-id* | Specifies the ID of the BD in which dynamic proxy ND entries are deleted.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The bd-id value is an integer ranging from 1 to 16777215. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When the number of dynamic proxy ND entries exceeds a specified threshold, run the **reset ipv6 nd multicast-suppress dynamic bridge-domain** command to clear dynamic proxy ND entries in a specified BD.




Example
-------

# Clear dynamic proxy ND entries in BD 10.
```
<HUAWEI> reset ipv6 nd multicast-suppress dynamic bridge-domain 10

```