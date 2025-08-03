reset macsec statistics
=======================

reset macsec statistics

Function
--------



The **reset macsec statistics** command clears statistics about data packets protected by MACsec.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset macsec statistics interface** { *interface-name* | *interface-type* *interface-number* }


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

When locating a MACsec fault, you need to check whether the number of sent packets is the same as the number of received packets within a period of time. Before collecting statistics, run the **reset macsec statistics** command to clear historical statistics about data packets protected by MACsec on a specified interface. Then run the **display macsec statistics** command to check statistics about data packets protected by MACsec on the interface.


Example
-------

# Clear statistics about data packets protected by MACsec on 100GE 1/0/1.
```
<HUAWEI> reset macsec statistics interface 100GE 1/0/1

```