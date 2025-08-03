reset ospf counters maxage-lsa
==============================

reset ospf counters maxage-lsa

Function
--------



The **reset ospf counters maxage-lsa** command deletes the statistics about router LSAs that have reached the aging time.




Format
------

**reset ospf** [ *process-id* ] **counters** **maxage-lsa**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After the statistics about router LSAs that have reached the aging time are deleted, OSPF services are not affected.Note:Statistics cannot be restored after being deleted. Therefore, exercise caution when running the command.


Example
-------

# Delete the statistics about router LSAs that have reached the aging time.
```
<HUAWEI> reset ospf counters maxage-lsa

```