reset ipv6 nd source-mac statistics
===================================

reset ipv6 nd source-mac statistics

Function
--------



The **reset ipv6 nd source-mac statistics** command clears statistics about dropped ND attack messages with fixed source MAC addresses.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ipv6 nd source-mac statistics** { **interface** { *interface-name* | *interface-type* *interface-num* } | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specify value of User interface. | - |
| **interface** *interface-type* *interface-num* | Specifies the type and number of an interface. | - |
| **all** | Clears statistics about dropped ND attack messages with fixed source MAC addresses on all interfaces. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To clear statistics about dropped ND attack messages with fixed source MAC addresses, run the reset ipv6 nd source-mac statistics command.

**Precautions**

Exercise caution when using this command.


Example
-------

# Clear statistics about dropped ND attack messages with fixed source MAC addresses on all interfaces.
```
<HUAWEI> reset ipv6 nd source-mac statistics all

```