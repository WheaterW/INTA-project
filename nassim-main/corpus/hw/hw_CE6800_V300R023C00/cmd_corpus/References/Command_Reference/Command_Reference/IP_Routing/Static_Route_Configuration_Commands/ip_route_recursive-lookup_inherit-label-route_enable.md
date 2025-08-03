ip route recursive-lookup inherit-label-route enable
====================================================

ip route recursive-lookup inherit-label-route enable

Function
--------



The **ip route recursive-lookup inherit-label-route enable** command allows routes to recurse to remotely leaked VPN routes.

The **undo ip route recursive-lookup inherit-label-route enable** command disables routes from recursing to remotely leaked VPN routes.



By default, non-static routes cannot recurse to remotely leaked VPN routes.


Format
------

**ip route recursive-lookup inherit-label-route enable**

**undo ip route recursive-lookup inherit-label-route enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The next hop of a route may not be directly reachable. Such a route cannot guide packet forwarding and needs to be recursed. During route recursion, you can run the **ip route recursive-lookup inherit-label-route enable** command to enable route recursion to remotely leaked VPN routes. If a route can be recursed to a remotely leaked VPN route, the route correctly inherits the label and tunnel ID of the remotely leaked VPN route to guide traffic forwarding.




Example
-------

# Allow routes to recurse to remotely leaked VPN routes.
```
<HUAWEI> system-view
[~HUAWEI] ip route recursive-lookup inherit-label-route enable

```