device-id
=========

device-id

Function
--------



The **device-id** command configures an IOAM device ID for the local device.

The **undo device-id** command restores the IOAM device ID to the default value (0).



By default, the device ID is 0.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**device-id** *device-id*

**undo device-id** [ *device-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **device-id** *device-id* | Specifies the IOAM device ID. | The value is an integer ranging from 0 to 16777215. The default value is 0. |



Views
-----

IOAM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In an IOAM network, a node needs to be identified. You can run this command to set the ID of the local device.


Example
-------

# Set the IOAM device ID to 1.
```
<HUAWEI> system-view
[~HUAWEI] ioam
[*HUAWEI-ioam] device-id 1

```