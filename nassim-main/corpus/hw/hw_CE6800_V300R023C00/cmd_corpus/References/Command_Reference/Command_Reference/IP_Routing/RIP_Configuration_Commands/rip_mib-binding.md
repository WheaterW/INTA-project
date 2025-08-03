rip mib-binding
===============

rip mib-binding

Function
--------



The **rip mib-binding** command sets the binding between the Management Information Base (MIB) and RIP process ID and specifies the ID of the RIP process that receives SNMP requests.

The **undo rip mib-binding** command cancels the binding.



By default, no RIP process is associated with MIB.


Format
------

**rip mib-binding** *process-id*

**undo rip mib-binding**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Indicates the ID of a RIP process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **rip mib-binding** command sets the binding between the MIB and RIP process ID, and specifies the ID of the RIP process that receives SNMP requests.

**Precautions**

All Simple Network Management Protocol (SNMP) requests are sent to the bound RIP process.


Example
-------

# Associate MIB with RIP process 100.
```
<HUAWEI> system-view
[~HUAWEI] rip 100
[*HUAWEI-rip-100] quit
[*HUAWEI] rip mib-binding 100

```