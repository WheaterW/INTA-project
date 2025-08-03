ipv4-family unicast
===================

ipv4-family unicast

Function
--------



The **ipv4-family unicast** command displays the BGP-IPv4 unicast address family.



By default, the BGP-IPv4 unicast address family view is displayed.


Format
------

**ipv4-family unicast**


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

Before performing BGP configurations in an IPv4 address family, you need to run the **ipv4-family** command in the BGP view to enable the IPv4 address family and enter the address family view. By default, BGP uses the IPv4 unicast address family.

**Configuration Impact**



To disable the IPv4 unicast address family, run the **undo default ipv4-unicast** command.




Example
-------

# Enter the BGP-IPv4 unicast address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4]

```