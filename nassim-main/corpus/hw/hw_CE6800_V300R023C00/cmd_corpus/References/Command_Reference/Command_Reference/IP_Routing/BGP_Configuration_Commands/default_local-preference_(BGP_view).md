default local-preference (BGP view)
===================================

default local-preference (BGP view)

Function
--------



The **default local-preference** command configures a Local\_Pref for BGP routes.

The **undo default local-preference** command restores the default value.



By default, the Local\_Pref of BGP routes is 100.


Format
------

**default local-preference** *local-preference*

**undo default local-preference**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *local-preference* | Specifies the local preference for BGP routes. The larger the value, the higher the priority. | The value is an integer ranging from 0 to 4294967295. The default value is 100. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The preference attribute is used to determine the optimal route when traffic leaves an AS. When a BGP device obtains multiple routes that have the same destination address but different next hops from IBGP peers, the route with the highest preference value is selected.The **default local-preference** command is used to configure the default local preference of BGP. If the default local preference of BGP is required, the configuration takes effect. For example, if a route carries the Local\_Pref attribute and does not require the default local preference of BGP, the route is not affected by the default local preference.

**Configuration Impact**

If the default Local\_Pref of BGP has been configured on the device, when you configure a new default Local\_Pref, the new default Local\_Pref replaces the original one.After this command is run, the default Local\_Pref is set for the BGP routes advertised to IBGP peers, and the reflected routes are not affected.If a route does not have a Local\_Pref, BGP uses the default Local\_Pref for the route during route selection.Running the **default local-preference** command causes routes to be resent. When there are a large number of routes, device performance may be affected.

**Precautions**

1. The **default local-preference** command sets the default Local\_Pref for all the routes (except reflected routes) advertised by the local device to all IBGP peers. The Local\_Pref is valid only between IBGP peers and is not advertised to other ASs.
2. In load balancing scenarios other than EIBGP load balancing, if routes do not carry the Local\_Pref attribute, the value 0 rather than the default Local\_Pref attribute configured on the local device is used during route selection for load balancing.

Example
-------

# Set the Local\_Pref for BGP routes to 200.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] default local-preference 200

```