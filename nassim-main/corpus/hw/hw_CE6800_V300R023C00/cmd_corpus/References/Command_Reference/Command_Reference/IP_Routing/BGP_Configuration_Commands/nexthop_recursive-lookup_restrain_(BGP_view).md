nexthop recursive-lookup restrain (BGP view)
============================================

nexthop recursive-lookup restrain (BGP view)

Function
--------



The **nexthop recursive-lookup restrain** command configures the intervals for increasing, retaining, and clearing the penalty value for BGP recursion suppression in case of next hop flapping.

The **undo nexthop recursive-lookup restrain** command restores the default configuration.



By default, the intervals for increasing, retaining, and clearing the penalty value for BGP recursion suppression in case of next hop flapping are 60s, 120s, and 600s, respectively.


Format
------

**nexthop recursive-lookup restrain suppress-interval** *add-count-time* **hold-interval** *hold-count-time* **clear-interval** *clear-count-time*

**undo nexthop recursive-lookup restrain suppress-interval hold-interval clear-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hold-interval** *hold-count-time* | Specifies the interval for retaining the penalty value for recursion suppression. | The value is an integer ranging from 1 to 65535, in seconds. The default values is recommended. |
| **clear-interval** *clear-count-time* | Specifies the interval for clearing the penalty value for recursion suppression. | The value is an integer ranging from 1 to 65535, in seconds. The default values is recommended. |
| **suppress-interval** *add-count-time* | Specifies the interval for increasing the penalty value for recursion suppression. | The value is an integer ranging from 1 to 65535, in seconds. The default value is recommended. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a large number of routes are recursed to the same next hop and the next hop flaps frequently, the system frequently processes the changes of the routes. As a result, a large number of resources are consumed and the CPU usage increases. To address this problem, recursion suppression in case of next hop flapping is enabled by default. This function slows down route processing, saves system resources, and reduces CPU usage.After recursion suppression in case of next hop flapping is enabled, BGP compares the interval between two next hop flappings with the configured threshold, and increases, maintains, or clears the suppression count based on the comparison result. When the suppression count reaches a certain value (greater than 10), the device suppresses recursion in case of next hop flapping. Assume that the intervals for increasing, retaining, and clearing the penalty value are T1, T2, and T3, respectively. The detailed processing is as follows:

* If the interval between two next hop flappings is less than T1, the penalty count increases by 1. Note that if the interval between two next hop flappings is too short, the penalty count does not increase even if the interval is less than T1.
* If the interval between two next hop flappings is greater than or equal to T1 and less than T2, the penalty count remains unchanged.
* If the interval between two next hop flappings is greater than or equal to T2 and less than T3, the penalty count decreases by 1.
* If the interval between two next hop flappings is greater than or equal to T3, the penalty count is cleared.

Example
-------

# Set the intervals for increasing, retaining, and clearing the penalty value for BGP recursion suppression in case of next hop flapping to 30s, 60s, and 120s, respectively.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] nexthop recursive-lookup restrain suppress-interval 30 hold-interval 60 clear-interval 120

```