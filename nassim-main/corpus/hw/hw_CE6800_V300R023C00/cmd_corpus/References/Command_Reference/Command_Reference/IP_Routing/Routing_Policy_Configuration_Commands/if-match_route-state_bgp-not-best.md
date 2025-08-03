if-match route-state bgp-not-best
=================================

if-match route-state bgp-not-best

Function
--------



The **if-match route-state bgp-not-best** command sets a matching rule based on the non-optimal BGP route status.

The **undo if-match route-state** command deletes the matching rule.



By default, no matching rule based on the non-optimal BGP route status is configured.


Format
------

**if-match route-state bgp-not-best**

**undo if-match route-state** [ **bgp-not-best** ]


Parameters
----------

None

Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In a scenario where BGP Add-Path is deployed, you can run the **if-match route-state bgp-not-best** command to match non-optimal BGP routes.



**Prerequisites**



A route-policy must have been configured before you run the **if-match route-state bgp-not-best** command.



**Precautions**



This command applies only to BGP route export policy scenarios.




Example
-------

# Define a matching rule to match the non-optimal BGP routes.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] if-match route-state bgp-not-best

```