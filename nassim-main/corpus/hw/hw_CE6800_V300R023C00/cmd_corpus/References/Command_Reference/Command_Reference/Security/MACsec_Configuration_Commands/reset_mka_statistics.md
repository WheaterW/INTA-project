reset mka statistics
====================

reset mka statistics

Function
--------



The **reset mka statistics** command clears MKA packet statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset mka statistics interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | - |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | - |
| **interface** | Specifies an interface. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When locating a MACsec fault, you need to check whether the number of sent MKA protocol packets is the same as the number of received MKA protocol packets within a period of time. Before collecting statistics, run the **reset mka statistics** command to clear historical MKA protocol packet statistics on a specified interface. Then run the **display mka interface** command to check MKA protocol packet statistics on the interface.


Example
-------

# Clear MKA protocol packet statistics on 100GE 1/0/1.
```
<HUAWEI> reset mka statistics interface 100GE 1/0/1

```