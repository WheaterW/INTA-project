apply dampening
===============

apply dampening

Function
--------



The **apply dampening** command sets BGP route dampening parameters.

The **undo apply dampening** command cancels the configuration.



By default, BGP route dampening parameters are not set.


Format
------

**apply dampening** *half-life-reach* *reuse* *suppress* *ceiling*

**undo apply dampening**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *half-life-reach* | Specifies the half-life of a reachable route. | The value is an integer ranging from 1 to 45, in minutes. |
| *reuse* | Specifies the threshold for routes to be released from the dampening state. When the penalty value falls below the threshold, routes are reused. | The value is an integer ranging from 1 to 19998. |
| *suppress* | Specifies the threshold for routes to enter the dampening state. When the penalty value exceeds the threshold, routes are suppressed. | The value is an integer ranging from 2 to 19999. The configured value of suppress must be greater than the value of reuse. |
| *ceiling* | Specifies the upper limit of the penalty value of routes. | The value is an integer ranging from 1001 to 20000. The configured value of ceiling must be greater than the value of suppress. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



This command is used to suppress the impact of frequent route flapping on all devices on the network. This command is mainly used in BGP.Different dampening parameters can be configured for different nodes in the same route-policy as required. When route flapping occurs, BGP uses different dampening parameters to dampen the routes that match the route-policy.



**Implementation Procedure**



If the apply dampening command is run more than once, the latest configuration overwrites the previous one.



**Configuration Impact**



If the apply dampening command is run, each time route flapping occurs, BGP adds a certain penalty value to this route.



**Precautions**



The parameters in this command do not have default values and must be configured explicitly. The values of reused, suppressed, and ceiling increase in ascending order. That is, the following condition must be met: reused <suppressed <ceiling. According to the formula MaxSuppressTime (second) = half-life-reach (minute) \*60\*(ln(ceiling/reused)/ln(2)), if the value of MaxSuppressTime is smaller than 1, dampening does not take effect. Therefore, to ensure that the value of MaxSuppressTime is greater than or equal to 1, the value of ceiling/reused must be large enough.




Example
-------

# Set dampening parameters for BGP routes.
```
<HUAWEI> system-view
[~HUAWEI] route-policy aa permit node 10
[*HUAWEI-route-policy] apply dampening 20 2000 10000 16000

```