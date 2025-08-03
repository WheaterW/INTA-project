reset ospf redistribution
=========================

reset ospf redistribution

Function
--------



The **reset ospf redistribution** command re-imports OSPF routes.




Format
------

**reset ospf** [ *process-id* ] **redistribution**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process. If this parameter is not specified, OSPF routes are re-imported in all OSPF processes. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

To re-import OSPF routes, run the **reset ospf redistribution** command.


Example
-------

# Re-import OSPF routes in OSPF process 1.
```
<HUAWEI> reset ospf 1 redistribution

```