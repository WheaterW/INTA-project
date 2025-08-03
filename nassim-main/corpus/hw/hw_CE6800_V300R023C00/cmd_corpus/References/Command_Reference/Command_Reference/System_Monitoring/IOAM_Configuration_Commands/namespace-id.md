namespace-id
============

namespace-id

Function
--------



The **namespace-id** command configures the IOAM namespace ID for the device.

The **undo namespace-id** command restores the IOAM namespace ID to 0 (default value).



By default, the IOAM namespace ID of a device is 0.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**namespace-id** *namespace-id*

**undo namespace-id** [ *namespace-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **namespace-id** *namespace-id* | Specifies the IOAM namespace ID for the device. | The value is an integer that ranges from 0 to 65535. The default value is 0. |



Views
-----

IOAM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On an IOAM network, the IOAM namespace ID needs to be configured for each hop. Only the IOAM packets with the same namespace ID as that of the device can be processed by the device based on the IOAM process.


Example
-------

# Set the IOAM namespace ID to 1 for the device.
```
<HUAWEI> system-view
[~HUAWEI] ioam
[*HUAWEI-ioam] namespace-id 1

```