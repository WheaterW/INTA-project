load-balancing med-ignore(BGP view)
===================================

load-balancing med-ignore(BGP view)

Function
--------

By default, a router compares the MED attributes of the routes to be used for load balancing.


Format
------

**load-balancing med-ignore**

**undo load-balancing med-ignore**


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

After the **load-balancing med-ignore** command is run, a device does not compare the MED attributes of the routes to be used for load balancing. Exercise caution when using the command because the execution of this command will change the conditions of load balancing.When routes are used for load balancing, the device processes the MED attribute as follows:

* Load balancing can be implemented only when the MEDs of routes are the same.
* Ignores the MED attribute if the **load-balancing med-ignore** command is run. After this command is run, the device does not compare MEDs. That is, load balancing can be performed among routes with different MED attributes.The **load-balancing med-ignore** command applies to BGP route load balancing scenarios. Exercise caution when running this command because it will change the conditions of load balancing.


Example
-------

# Disable a router from comparing the MED attributes of the routes to be used for load balancing.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] load-balancing med-ignore

```