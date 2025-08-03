multicast longest-match
=======================

multicast longest-match

Function
--------



The **multicast longest-match** command selects the Reverse Path Forwarding (RPF) route based on the longest matching rule.

The **undo multicast longest-match** command restores the default configuration.



By default, the route with the highest preference is selected as the RPF route.


Format
------

**multicast longest-match**

**undo multicast longest-match**


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

When multiple optimal unicast routes exist, the RPF route is selected according to the following rules:

* By default, the route with the highest priority is selected as the RPF route.
* If the multicast longest-match command is used, the route with the longest mask is selected as the RPF route.
* If the multicast load-splitting command is used, multicast load splitting is performed among multiple optimal unicast routes.

Example
-------

# Select routes according to the longest match in the public network instance.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] multicast longest-match

```