description (Route-policy view)
===============================

description (Route-policy view)

Function
--------



The **description** command configures a description for a route-policy.

The **undo description** command deletes the description of a route-policy.



By default, no description is configured for a route-policy.


Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | Specifies the description of a route-policy. | The value is a string of 1 to 80 case-sensitive characters, spaces supported. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To configure a description for a created route-policy, run the **description** command. If multiple route-policies have been configured, configuring descriptions for the policies will facilitate policy management.



**Prerequisites**



A route-policy has been configured using the **route-policy** command.




Example
-------

# Configure a description for the route-policy named temp.
```
<HUAWEI> system-view
[~HUAWEI] route-policy temp permit node 10
[*HUAWEI-route-policy] description This policy-name is temp

```