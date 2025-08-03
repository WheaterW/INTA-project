load-balancing med-ignore(BGP-IPv4 unicast address family view/BGP-IPv6 unicast address family view)
====================================================================================================

load-balancing med-ignore(BGP-IPv4 unicast address family view/BGP-IPv6 unicast address family view)

Function
--------



The **load-balancing med-ignore** command configures a device not to compare the MEDs of routes when selecting routes for load balancing.

The **undo load-balancing med-ignore** command restores the default configuration.



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

BGP-IPv4 unicast address family view,BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the **load-balancing med-ignore** command is run, the device does not compare the MED attributes of the routes to be used for load balancing. Exercise caution when using the command because the execution of this command will change the conditions of load balancing.When routes are used for load balancing, the processes the MED attribute as follows:Load balancing can be implemented only when the MEDs of routes are the same.To configure the device to ignore the MED attribute, run the **load-balancing med-ignore** command. After this command is run, the device does not compare MEDs. That is, load balancing can be performed among routes with different MED attributes.The **load-balancing med-ignore** command applies to BGP route load balancing scenarios. Exercise caution when running this command because it will change the conditions of load balancing.


Example
-------

# Disable a router from comparing the MED attributes of the routes to be used for load balancing.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] load-balancing med-ignore

```