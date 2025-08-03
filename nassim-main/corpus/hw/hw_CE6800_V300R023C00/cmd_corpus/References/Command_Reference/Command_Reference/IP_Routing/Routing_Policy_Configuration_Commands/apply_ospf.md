apply ospf
==========

apply ospf

Function
--------



The **apply isis** command sets the level of the routes imported to IS-IS.

The **undo apply isis** command cancels the configuration.

The **apply ospf** command imports routes into the specific OSPF area.

The **undo apply ospf** command cancels the configuration.



By default, the level of the routes imported to IS-IS is not set and no routes are imported to a specified OSPF area.


Format
------

**apply ospf** { **backbone** | **stub-area** }

**apply isis** { **level-1** | **level-2** | **level-1-2** }

**undo apply** { **isis** | **ospf** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **backbone** | Imports routes into the OSPF backbone area. | - |
| **stub-area** | Imports routes to the OSPF stub area. | - |
| **level-1** | Indicates IS-IS Level-1 routes. | - |
| **level-2** | Indicates IS-IS Level-2 routes. | - |
| **level-1-2** | Sets the level to Level-1 and Level-2. | - |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When importing routes to IS-IS, you can use the **apply isis** command to set the level of the routes imported to IS-IS.To import routes to the OSPF backbone area or an NSSA, run the **apply ospf** command, which prevents too many external routes from being imported into OSPF.



**Prerequisites**



A route-policy has been configured using the route-policy command.



**Configuration Impact**



After a route matches a route-policy, the level of the route imported to IS-IS is set.Routes matching the if-match clauses defined in the route-policy will be imported into the OSPF area specified in the command.




Example
-------

# Set the level of the routes imported to IS-IS.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] apply isis level-1

```

# Import routes into the OSPF backbone area.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] apply ospf backbone

```