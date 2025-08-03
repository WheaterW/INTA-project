isis prefix-attributes node-disable
===================================

isis prefix-attributes node-disable

Function
--------



The **isis prefix-attributes node-disable** command sets the N flag in the extended prefix attribute of a loopback interface in an IS-IS process to 0.

The **undo isis prefix-attributes node-disable** command restores the N flag of the extended prefix attribute of a loopback interface in an IS-IS process to 1.



By default, the N flag in the extended prefix attribute of a loopback interface in an IS-IS process is 1.


Format
------

**isis prefix-attributes node-disable**

**isis process-id** *process-id-value* **prefix-attributes** **node-disable**

**undo isis prefix-attributes node-disable**

**undo isis process-id** *process-id-value* **prefix-attributes** **node-disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **process-id** *process-id-value* | Specifies the ID of an IS-IS multi-instance process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

Loopback interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the 32-bit route of a loopback interface is a host route, you can run this command to determine whether to set the N flag in the extended prefix attribute of the loopback interface in an IS-IS process.


Example
-------

# Set the N flag of the extended prefix attribute of the loopback interface in an IS-IS process to 0.
```
<HUAWEI> system-view
[~HUAWEI] isis 100
[*HUAWEI-isis-100] quit
[*HUAWEI] interface LoopBack 0
[*HUAWEI-LoopBack0] isis enable 100
[*HUAWEI-LoopBack0] isis prefix-attributes node-disable

```