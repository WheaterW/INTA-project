peer allow-as-loop (BGP-VPN instance IPv4 address family view) (group)
======================================================================

peer allow-as-loop (BGP-VPN instance IPv4 address family view) (group)

Function
--------



The **peer allow-as-loop** command sets the number of times that the local AS number can be repeated.

The **undo peer allow-as-loop** command disables this function.



By default, local AS number repetition is not allowed.


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

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP uses AS numbers to detect routing loops. The AS numbers in the AS\_Path of each received route are matched against the local AS number configured using the **bgp** command and the fake AS number configured using the **peer local-as** command.After the **peer allow-as-loop** command is executed to configure the number of local AS number repetitions, the BGP speaker can allow routes with repeated AS numbers in AS\_Path to pass to meet the requirements of special scenarios.

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
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] group test
[*HUAWEI-bgp-vpna] peer test allow-as-loop 2

```