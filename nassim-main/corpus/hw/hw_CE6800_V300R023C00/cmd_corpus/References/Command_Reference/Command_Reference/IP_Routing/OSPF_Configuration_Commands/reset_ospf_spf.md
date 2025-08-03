reset ospf spf
==============

reset ospf spf

Function
--------



The **reset ospf spf** command enables a device to recalculate OSPF routes.




Format
------

**reset ospf** [ *process-id* ] **spf**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | process-id Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

To enable a device to recalculate OSPF routes, run the reset ospf spf command. This command improves maintainability and does not affect services.


Example
-------

# Reset OSPF route calculation.
```
<HUAWEI> reset ospf spf

```