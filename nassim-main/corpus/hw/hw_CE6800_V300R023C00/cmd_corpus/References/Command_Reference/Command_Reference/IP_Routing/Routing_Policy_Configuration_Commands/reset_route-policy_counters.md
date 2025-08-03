reset route-policy counters
===========================

reset route-policy counters

Function
--------



The **reset route-policy counters** command resets route-policy statistics.




Format
------

**reset route-policy** *route-policy-name* **counters**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *route-policy-name* | Specifies the name of a routing policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The route-policy is used to filter routes and set the attributes of a route that matches a route-policy. When a route-policy filters routes, the system records the number of routes that match the route-policy nodes. You can run the display route-policy to view the numbers.The **reset route-policy counters** command clears the number of routes which match or do not match the route-policy.



**Configuration Impact**



The **reset route-policy counters** command clears the number of routes which match or do not match the route-policy. After the number is cleared, it cannot be restored.




Example
-------

# Reset the statistics of a route-policy named policy1.
```
<HUAWEI> reset route-policy policy1 counters

```