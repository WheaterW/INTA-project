multicast layer-2 invalid-packet mld snooping
=============================================

multicast layer-2 invalid-packet mld snooping

Function
--------



The **multicast layer-2 invalid-packet mld snooping** command sets the maximum number of invalid Layer 2 multicast protocol messages that can be stored on the device.

The **undo multicast layer-2 invalid-packet mld snooping** command cancels the setting.



By default, a multicast device can store a maximum of 10 invalid Layer 2 multicast protocol messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast layer-2 invalid-packet mld snooping max-count** *max-number*

**undo multicast layer-2 invalid-packet mld snooping**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **max-count** *max-number* | Sets the maximum number of invalid Layer 2 multicast protocol messages that can be stored on the device. | The value is an integer ranging from 1 to 100. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If forwarding entries cannot be created on a multicast network, run the multicast layer-2 invalid-packet mld snooping command to set the maximum number of invalid Layer 2 multicast protocol messages that can be stored on the device.


Example
-------

# Specify 20 as the maximum number of invalid Layer 2 multicast protocol messages that can be stored on the device.
```
<HUAWEI> system-view
[~HUAWEI] multicast layer-2 invalid-packet mld snooping max-count 20

```