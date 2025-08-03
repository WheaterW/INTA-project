peer allow-as-loop (BGP view) (group)
=====================================

peer allow-as-loop (BGP view) (group)

Function
--------



The **peer allow-as-loop** command sets the number of local AS number repetitions.

The **undo peer allow-as-loop** command cancels the configuration.



By default, the local AS number cannot be repeated.


Format
------

**peer** *group-name* **allow-as-loop** [ *number* ]

**undo peer** *group-name* **allow-as-loop**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *number* | Specifies the maximum number of times the local AS number can be repeated in the AS\_Path of each received route. | The value is an integer in the range from 1 to 10. The default value is 1. |



Views
-----

BGP view


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
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] peer test allow-as-loop 2

```