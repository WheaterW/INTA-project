check-first-as (BGP view)
=========================

check-first-as (BGP view)

Function
--------



The **check-first-as** command enables BGP to check the first AS number in the AS\_Path that is carried in Update messages sent by EBGP peers.

The **undo check-first-as** command disables the function.



By default, the function is enabled.


Format
------

**check-first-as**

**undo check-first-as**


Parameters
----------

None

Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, BGP checks the first AS number in the AS\_Path list that is carried in the Update message sent by the EBGP peer. If only the first AS number indicates the AS where the EBGP peer locates, the Update message is permitted. Otherwise, the update information is rejected.

**Follow-up Procedure**



Run the **refresh bgp** command if you want to check the received routes again.



**Precautions**



The check-first-as command is not listed in the configuration file.After the **undo check-first-as** command is configured, routing loops may occur. Therefore, exercise caution when running the command.




Example
-------

# Check the first AS number in the AS\_Path list that is carried in the Update messages sent by EBGP peers.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] check-first-as

```