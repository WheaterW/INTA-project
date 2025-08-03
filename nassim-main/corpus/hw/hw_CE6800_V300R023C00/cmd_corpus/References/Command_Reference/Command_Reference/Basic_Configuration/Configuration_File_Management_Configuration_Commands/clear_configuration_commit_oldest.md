clear configuration commit oldest
=================================

clear configuration commit oldest

Function
--------



The **clear configuration commit oldest** command deletes the earliest generated list of configuration rollback points.




Format
------

**clear configuration commit oldest** *number-of-commits*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number-of-commits* | Specifies the number of configuration rollback points to be deleted in the earliest generated list. | The value is an integer ranging from 1 to 80. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* If the earliest configuration rollback points are no longer required, run the clear configuration commit oldest command to delete one or more of the earliest configuration rollback points. The configuration helps reclaim system resources.
* This command is not used to reduce the number of configuration rollback points in the earliest generated list under normal circumstances. If the number of configuration rollback points reaches the upper limit (80) in a list and subsequent configuration rollback points are generated, the earliest configuration rollback points are deleted automatically.
* When you run this command to delete a configuration rollback point with a label, only the commit point is deleted, but the label is not deleted. The configuration point can be managed only by label, and the commit point has been cleared. After this operation is complete, the configuration rollback points with labels become discontinuous configuration rollback points. When you run the **display configuration commit list** command to view the configuration rollback points, the commit IDs of the discontinuous configuration rollback points are marked with asterisks (\*).

**Follow-up Procedure**



Run the **display configuration commit list** command to check that the earliest configuration rollback points have been deleted.




Example
-------

# Delete three of the earliest configuration rollback points.
```
<HUAWEI> clear configuration commit oldest 3

```