action-type encapsulate
=======================

action-type encapsulate

Function
--------



The **action-type encapsulate** command configures the device to encapsulate IOAM packets and specify the IOAM data encapsulation mode.

The **undo action-type encapsulate** command cancels the encapsulation action for IOAM packets.



By default, no IOAM encapsulation action is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**action-type encapsulate** [ **service-type** { **edge-to-edge** | **direct-export** } ]

**action-type encapsulate** [ **service-type** **trace** ]

**undo action-type encapsulate** [ **service-type** { **edge-to-edge** | **direct-export** } ]

**undo action-type encapsulate** [ **service-type** **trace** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **service-type** | IOAM data encapsulation mode. | - |
| **edge-to-edge** | IOAM edge-to-edge mode. | - |
| **direct-export** | IOAM direct-export mode. | - |
| **trace** | IOAM trace mode. | - |



Views
-----

IOAM-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To use a device as an IOAM network encapsulation node, run this command in the IOAM policy view to configure the device to encapsulate IOAM packets and specify the IOAM data encapsulation mode.


Example
-------

# Configure the device to encapsulate IOAM packets and specify the data encapsulation mode.
```
<HUAWEI> system-view
[~HUAWEI] ioam
[*HUAWEI-ioam] profile default
[*HUAWEI-ioam-profile-default] policy 1
[*HUAWEI-ioam-profile-default-policy-1] action-type encapsulate service-type trace

```