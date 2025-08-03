reset slot
==========

reset slot

Function
--------



The **reset slot** command resets the board or subcard in a specified slot.




Format
------

**reset slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies a slot ID. | - |



Views
-----

User view,Management view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



If a board or subcard on a device is faulty, run this command to reset the board or subcard.



**Precautions**



This command can be used only when the board is in position. Before resetting the board, back up important data.




Example
-------

# Reset the board in a specified slot.
```
<HUAWEI> reset slot 1
Warning: The slot 1 will reset. Continue? [Y/N]:

```