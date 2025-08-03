prefix memory-limit (BGP view)
==============================

prefix memory-limit (BGP view)

Function
--------



The **prefix memory-limit** command configures BGP memory protection. With BGP memory protection, BGP will no longer receive BGP routes from peers and a log will be generated if the memory usage reaches the upper limit.

The **undo prefix memory-limit** command disables BGP memory protection.



By default, BGP memory protection is disabled.


Format
------

**prefix memory-limit**

**undo prefix memory-limit**


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

If BGP keeps receiving BGP routes from peers after the memory usage reaches the upper limit, the local device will restart and a master/slave main control board switchover will be performed, which affects system stability. To address this problem, run the **prefix memory-limit** command to enable BGP memory protection. With BGP memory protection, BGP will no longer receive BGP routes from peers and a log will be generated if the memory usage reaches the upper limit.


Example
-------

# Enable BGP memory protection.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] prefix memory-limit

```