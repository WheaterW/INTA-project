peer allow-as-loop (BGP-IPv6 unicast address family view) (group)
=================================================================

peer allow-as-loop (BGP-IPv6 unicast address family view) (group)

Function
--------



The **peer allow-as-loop** command sets the number of times that the local AS number can be repeated.

The **undo peer allow-as-loop** command disables this function.



By default, local AS number repetition is not allowed.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **allow-as-loop** [ *number* ]

**undo peer** *group-name* **allow-as-loop**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *number* | Maximum number of times the local AS number can be included in the AS\_Path of each received route. | The value is an integer ranging from 1 to 10. The default value is 1. |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, BGP uses AS numbers to detect routing loops. The local AS number configured using the **bgp** command and the fake AS number configured using the **peer fake-as** command are compared with the AS\_Path carried in the received route. The number of loops is the largest. After the **peer allow-as-loop** command is run to set the number of times the local AS number is repeated, the BGP speaker allows the routes with repeated AS numbers in the AS\_Path attribute to pass, meeting the requirements of special scenarios.

**Prerequisites**

A peer group has been established using the **peer as-number** command.

**Configuration Impact**

If you run the command multiple times in the same peer group view, only the latest configuration takes effect.

**Precautions**

The **peer allow-as-loop** command does not take effect for IBGP peers or BGP peers in a sub-confederation. The device checks whether the routes received from EBGP peers or EBGP peers in the confederation contain the local AS number. The minimum number of repetitions is 2, and the value 1 is not displayed.Running the **peer allow-as-loop** command may cause routing loops. Therefore, exercise caution when running this command and specify the number of AS number repetitions as required.


Example
-------

# Set the number of local AS number repetitions to 2.
```
<HUAWEI> system-view
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test
[~HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer test enable
[*HUAWEI-bgp-af-ipv6] peer test allow-as-loop 2

```