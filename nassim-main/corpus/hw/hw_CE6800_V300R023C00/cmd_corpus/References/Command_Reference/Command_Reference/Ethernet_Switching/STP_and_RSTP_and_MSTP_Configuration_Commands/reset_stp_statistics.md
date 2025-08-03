reset stp statistics
====================

reset stp statistics

Function
--------



The **reset stp statistics** command clears STP statistics.




Format
------

**reset stp** [ **interface** { *interface-name* | *interface-type* *interface-number* } ] **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies the interface type and number. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before collecting STP statistics on an interface within a certain period, run the **reset stp statistics** command to clear existing statistics.When you run the **reset stp statistics** command:

* If you specify an interface, STP statistics on this interface are cleared.
* If no interface is specified, STP statistics on all interfaces are cleared.


Example
-------

# Clear STP statistics on 100GE1/0/1.
```
<HUAWEI> reset stp interface 100GE1/0/1 statistics

```