reset dcb fail-record
=====================

reset dcb fail-record

Function
--------



The **reset dcb fail-record** command clears DCB negotiation failure records on an interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset dcb fail-record** [ **interface** { *interface-name* | *interface-type* *interface-num* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-num* | Specifies the type and number of an interface. | - |
| **interface** *interface-name* | Specifies an interface name. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To troubleshoot DCB faults, you may need to view DCB negotiation failure records within a certain period of time.Before recollecting DCB negotiation failure records on a specified interface or all interfaces, run the **reset dcb fail-record** command to clear existing DCB negotiation failure records. Then run the **display dcb fail-record** command to view DCB negotiation failure records.

**Precautions**

After the **reset dcb fail-record** command is executed, DCB negotiation failure records are cleared and cannot be restored. Confirm your action before you use this command.


Example
-------

# Clear DCB negotiation failure records on 100GE1/0/1.
```
<HUAWEI> reset dcb fail-record interface 100GE 1/0/1

```