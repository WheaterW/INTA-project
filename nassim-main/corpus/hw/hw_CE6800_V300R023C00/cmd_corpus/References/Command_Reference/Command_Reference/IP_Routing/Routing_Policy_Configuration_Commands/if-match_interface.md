if-match interface
==================

if-match interface

Function
--------



The **if-match interface** command sets a filtering rule that is based on the outbound interface.

The **undo if-match interface** command cancels the configuration.



By default, no filtering rule based on the outbound interface is set.


Format
------

**if-match interface** { { *interface-name* | *interface-type* *interface-number* } &<1-16> }

**undo if-match interface** [ [ *interface-name* | *interface-type* *interface-number* ] &<1-16> ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | - |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the interface number. | - |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To filter routes based on the outbound interface, run the **if-match interface** command.



**Prerequisites**



A route-policy has been configured using the route-policy command.



**Configuration Impact**



When you filter routes based on the outbound interfaces, the routes that match the filtering rule are permitted and the routes that do not match the filtering rule are denied.



**Follow-up Procedure**



Define apply clauses to set route attributes for the routes matching the rules.



**Precautions**



Multiple interface-based matching rules can be configured under a policy node. The relationship between them is OR. That is, if a route matches one of the interfaces, the route passes the filtering of the command.




Example
-------

# Define a rule to match the routes with the outbound interface 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] if-match interface 100GE 1/0/1

```