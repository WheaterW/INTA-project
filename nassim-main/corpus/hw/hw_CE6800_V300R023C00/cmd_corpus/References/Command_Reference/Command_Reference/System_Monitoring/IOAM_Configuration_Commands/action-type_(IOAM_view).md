action-type (IOAM view)
=======================

action-type (IOAM view)

Function
--------



The **action-type decapsulate** command configures the device to decapsulate IOAM packets.

The **action-type transit** command configures the action of encapsulating metadata for IOAM packets.



By default, the action-type is transit.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**action-type decapsulate**

**action-type transit**

**undo action-type decapsulate**

**undo action-type**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **transit** | Indicates the intermediate node. | - |
| **decapsulate** | Decapsulates IOAM packets. | - |



Views
-----

IOAM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To configure a device as the decapsulation node or transition node on an IOAM network, run this command in the IOAM view to configure the device to decapsulate IOAM packets or configure the action for IOAM packets to be metadata encapsulation.


Example
-------

# Configure the device to decapsulate IOAM packets.
```
<HUAWEI> system-view
[~HUAWEI] ioam
[*HUAWEI-ioam] action-type decapsulate

```