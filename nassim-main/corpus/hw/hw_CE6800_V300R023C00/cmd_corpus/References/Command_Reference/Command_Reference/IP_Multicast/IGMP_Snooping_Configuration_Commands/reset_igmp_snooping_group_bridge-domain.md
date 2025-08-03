reset igmp snooping group bridge-domain
=======================================

reset igmp snooping group bridge-domain

Function
--------



The **reset igmp snooping group bridge-domain** command clears the dynamic forwarding entries from a multicast forwarding table in BDs.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset igmp snooping group bridge-domain** { *BdId* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *BdId* | Clears the dynamic forwarding entries of a specified BD. | The value is an integer ranging from 1 to 16777215. |
| **all** | Clears the dynamic forwarding entries from the multicast forwarding tables in all BDs. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When the command is used to clear the dynamic forwarding entries in a certain BD, the multicast traffic received by hosts in the BD is interrupted until the hosts send IGMP Report messages again. After receiving the IGMP Report messages, the router regenerates the forwarding entries and the hosts start to receive the multicast traffic again.


Example
-------

# Clear all the dynamic forwarding entries in all BDs.
```
<HUAWEI> reset igmp snooping group bridge-domain all

```