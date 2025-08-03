reset ospf process
==================

reset ospf process

Function
--------



The **reset ospf process** command restarts an OSPF process.




Format
------

**reset ospf** [ *process-id* ] **process**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an OSPF process ID.  If the parameter is not specified, all OSPF processes are restarted. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To restart an OSPF process, run the **reset ospf process** command.If OSPF connections are reset, OSPF neighbor relationships will be interrupted and the original information cannot be restored. Exercise caution when using the reset ospf command.

**Configuration Impact**

After the **reset ospf process** command is run, the following situations may occur:

* If the router ID is changed, a new router ID will take affect.
* The DR and BDR are reselected.
* OSPF configuration will not be lost before OSPF restarts.

Example
-------

# Restart all OSPF processes.
```
<HUAWEI> reset ospf process

```