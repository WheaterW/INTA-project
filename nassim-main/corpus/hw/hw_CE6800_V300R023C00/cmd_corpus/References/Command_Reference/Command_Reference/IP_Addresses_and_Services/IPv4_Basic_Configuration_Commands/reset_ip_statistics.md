reset ip statistics
===================

reset ip statistics

Function
--------



The **reset ip statistics** command clears the statistics about IP traffic.




Format
------

**reset ip statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Clears the statistics about IP traffic of the specified interface. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



You need to clear the existing statistics about IP traffic before using the **display ip statistics** command to view the statistics about IP traffic in a specified period.



**Configuration Impact**



The **reset ip statistics** command clears the statistics about IP traffic on an interface board or on an interface. Therefore, confirm the action before running this command.




Example
-------

# Clear the statistics about IP traffic on all interfaces.
```
<HUAWEI> reset ip statistics

```