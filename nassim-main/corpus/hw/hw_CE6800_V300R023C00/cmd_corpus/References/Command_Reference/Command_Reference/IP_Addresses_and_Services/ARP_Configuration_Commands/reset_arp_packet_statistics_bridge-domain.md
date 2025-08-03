reset arp packet statistics bridge-domain
=========================================

reset arp packet statistics bridge-domain

Function
--------



The **reset arp packet statistics bridge-domain** command clears statistics about ARP packets in a bridge domain (BD).



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset arp packet statistics bridge-domain** *bd-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *bd-id* | Clears statistics about ARP packets in a BD with a specified ID.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The bd-id value is an integer ranging from 1 to 16777215. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To collect correct ARP packet statistics within a specified period in a BD, run the **reset arp packet statistics bridge-domain** command to delete existing ARP packet statistics.



**Precautions**



After the **reset arp packet statistics bridge-domain** command is run, statistics about the ARP packets sent and received in the BD will be cleared and cannot be restored. Exercise caution when running this command.




Example
-------

# Clear statistics about ARP packets in BD 10.
```
<HUAWEI> reset arp packet statistics bridge-domain 10

```