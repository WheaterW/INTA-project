reset rip imported-routes
=========================

reset rip imported-routes

Function
--------



The **reset rip imported-routes** command deletes the routes imported from other RIP processes or protocols and re-imports the routes to RIP.




Format
------

**reset rip** { *process-id* | **all** } **imported-routes**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Indicates the ID of a RIP process. | The value is an integer ranging from 1 to 4294967295. |
| **all** | Specifies all RIP processes. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Importing a large number of routes within a short period of time affects device performance. Therefore, exercise caution when running this command.


Example
-------

# Re-import routes to RIP process 1.
```
<HUAWEI> reset rip 1 imported-routes

```