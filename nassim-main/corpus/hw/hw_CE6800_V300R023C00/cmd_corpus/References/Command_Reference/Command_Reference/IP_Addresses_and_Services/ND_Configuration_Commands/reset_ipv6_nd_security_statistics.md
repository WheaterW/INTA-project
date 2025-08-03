reset ipv6 nd security statistics
=================================

reset ipv6 nd security statistics

Function
--------



The **reset ipv6 nd security statistics** command clears the statistics about SEND messages on an interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ipv6 nd security statistics** { *interface-name* | *interface-type* *interface-num* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Clears the statistics about SEND messages based on a specified interface name. | - |
| *interface-type* *interface-num* | Clears the statistics about SEND messages based on a specified interface type and number. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Running the **reset ipv6 nd security statistics** command will clear the statistics about SEND messages on a specified interface. Exercise caution when running this command.


Example
-------

# Clear the statistics about SEND messages on 100GE1/0/1
```
<HUAWEI> reset ipv6 nd security statistics 100GE 1/0/1

```