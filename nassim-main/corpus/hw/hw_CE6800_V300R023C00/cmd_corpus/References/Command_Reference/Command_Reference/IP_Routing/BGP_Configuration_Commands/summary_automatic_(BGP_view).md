summary automatic (BGP view)
============================

summary automatic (BGP view)

Function
--------



The **summary automatic** command enables automatic aggregation for the locally-imported routes.

The **undo summary automatic** command disables automatic aggregation for the locally-imported routes.



By default, the locally-imported routes are not aggregated automatically.


Format
------

**summary automatic**

**undo summary automatic**


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

Using the **summary automatic** command, you can summarize the routes imported by BGP. The routes can be direct routes, static routes, RIP routes, OSPF routes, or IS-IS routes. After this command is run, BGP summarizes routes based on the natural network segment (for example, 10.1.1.1/32 and 10.2.1.1/32 are summarized to 10.0.0.0/8, a Class A address), and sends only the summary route to peers. This reduces the amount of routing information.

**Configuration Impact**



BGP route aggregation is classified into manual aggregation and automatic aggregation. The command is used to implement automatic aggregation. Manual aggregation takes precedence over automatic aggregation.



**Precautions**



The **summary automatic** command is invalid for the routes imported by using the **network** command.When some summary routes are withdrawn, black holes may occur on the summary routes, causing traffic loss.




Example
-------

# Enable automatic aggregation for imported routes.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] summary automatic

```