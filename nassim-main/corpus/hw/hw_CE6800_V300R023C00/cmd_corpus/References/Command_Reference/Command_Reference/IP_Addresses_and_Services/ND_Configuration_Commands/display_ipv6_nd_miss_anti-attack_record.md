display ipv6 nd miss anti-attack record
=======================================

display ipv6 nd miss anti-attack record

Function
--------



The **display ipv6 nd miss anti-attack record** command displays attack records in scenarios where ND entries are missing.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 nd miss anti-attack record** { **all** | { *interface-name* | *interface-type* *interface-num* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays all attack records in scenarios where ND entries are missing. | - |
| *interface-name* | Displays all attack records on a specified interface in scenarios where ND entries are missing. | - |
| *interface-type* *interface-num* | Displays all attack records on a specified interface in scenarios where ND entries are missing. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the **display ipv6 nd miss anti-attack record** command to view attack records in scenarios where ND entries are missing, thereby obtaining information about the attack source. For example, you can configure a rate at which a device processes ND Miss messages so that the device processes only the specified number of ND Miss messages within a specified period and discards excess ND Miss messages. To view records about discarded ND Miss messages, run the **display ipv6 nd miss anti-attack record** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display attack records on a specified interface in scenarios where ND entries are missing.
```
<HUAWEI> display ipv6 nd miss anti-attack record 100ge 1/0/1
----------------------------------------------------------------------------------
Interface Name : 100GE1/0/1
Target IP      : 2001:db8:1::1
Source IP      : 2001:db8:1::2

----------------------------------------------------------------------------------
Total: 1

```

**Table 1** Description of the **display ipv6 nd miss anti-attack record** command output
| Item | Description |
| --- | --- |
| Interface Name | Interface name. |
| Target IP | Target IP address. |
| Source IP | The source IP address. |
| Total | Total number. |