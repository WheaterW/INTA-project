reset ospf frr
==============

reset ospf frr

Function
--------



The **reset ospf frr** command resets OSPF IP FRR.




Format
------

**reset ospf** [ *process-id* ] **frr**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process. If this parameter is not specified, FRR is reset in all OSPF processes. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

This command is a maintenance command. It can be used to forcibly reset FRR without deleting the FRR configuration.

**Prerequisites**

FRR has been configured in an OSPF process.

**Configuration Impact**

OSPF IP FRR calculation does not affect the normal running of OSPF.


Example
-------

# Reset FRR in an OSPF process.
```
<HUAWEI> reset ospf frr

```