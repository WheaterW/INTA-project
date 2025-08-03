peer allow-as-loop (BGP-IPv4 unicast address family view)(IPv4)
===============================================================

peer allow-as-loop (BGP-IPv4 unicast address family view)(IPv4)

Function
--------



The **peer allow-as-loop** command sets the number of times that the local AS number can be repeated.

The **undo peer allow-as-loop** command disables this function.



By default, local AS number repetition is not allowed.


Format
------

**peer** *ipv4-address* **allow-as-loop** [ *number* ]

**undo peer** *ipv4-address* **allow-as-loop**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | It is in dotted decimal notation. |
| *number* | Specifies the maximum number of times the local AS number can be repeated in the AS\_Path of each received route. | The value is an integer in the range from 1 to 10. The default value is 1. |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP uses AS numbers to detect routing loops. The AS numbers in the AS\_Path of each received route are matched against the local AS number configured using the **bgp** command and the fake AS number configured using the **peer local-as** command.After the **peer allow-as-loop** command is executed to configure the number of local AS number repetitions, the BGP speaker can allow routes with repeated AS numbers in AS\_Path to pass to meet the requirements of special scenarios.

**Prerequisites**

Peer relationships have been established using the **peer as-number** command.

**Configuration Impact**

If this command is run for a peer multiple times, the latest configuration overrides the previous one.

**Precautions**

The **peer allow-as-loop** command does not take effect for IBGP peers or BGP peers in a sub-confederation. The device checks whether the routes received from EBGP peers or EBGP peers in the confederation contain the local AS number. The minimum number of repetitions is 2, and the value 1 is not displayed.Running the **peer allow-as-loop** command may cause routing loops. Therefore, exercise caution when running this command and specify the number of AS number repetitions as required.


Example
-------

# Set the number of local AS number repetitions to 2.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer 10.1.1.1 allow-as-loop 2

```