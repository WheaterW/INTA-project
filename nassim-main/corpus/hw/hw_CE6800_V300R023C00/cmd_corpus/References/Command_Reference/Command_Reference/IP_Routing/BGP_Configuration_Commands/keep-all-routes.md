keep-all-routes
===============

keep-all-routes

Function
--------



The **keep-all-routes** command saves all the routes carried in BGP Update messages advertised by BGP peers or peer groups after BGP connections are established.

The **undo keep-all-routes** command disables this function.



By default, the device saves only accepted routes (routes that match the import policy).


Format
------

**keep-all-routes**

**undo keep-all-routes**


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

After the import policy of BGP is changed, you can reset the BGP connection for the new import policy to take effect immediately on the BGP peer that does not support route-refresh. This, however, interrupts the BGP connection temporarily. To solve this problem, run the **keep-all-routes** command to retain all the original routes of the peer. In this manner, the routing table can be refreshed without resetting the BGP connection.

**Precautions**



If the device does not support the route-refresh capability, you need to run this command on both the local device and its peer. After the **keep-all-routes** command is run for the first time, the sessions between the local device and its peers are reestablished.If the device supports the route-refresh capability, running this command does not cause the sessions between the device and its peers to be reestablished. However, updating the routing table using the **refresh bgp** command does not take effect on the device.After the **keep-all-routes** command is run in the BGP view, the configuration of the **peer keep-all-routes** command is overwritten by the keep-all-routes configuration in the BGP view.After the **keep-all-routes** command is run in the BGP view, this function takes effect only in the BGP-IPv4 unicast address family, BGP-VPN instance IPv4 address family, BGP-IPv6 unicast address family, BGP-VPN instance IPv6 address family, BGP-IPv4 multicast address family, BGP-VPNv4 address family, and BGP-VPNv6 address family.




Example
-------

# Configure a device to save all BGP routing updates received from its peers.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] keep-all-routes

```