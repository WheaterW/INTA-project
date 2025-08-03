multicast layer-2 invalid-packet igmp snooping
==============================================

multicast layer-2 invalid-packet igmp snooping

Function
--------



The **multicast layer-2 invalid-packet igmp snooping** command sets the maximum number of invalid Layer 2 multicast protocol packets allowed on a device.

The **undo multicast layer-2 invalid-packet igmp snooping** command deletes the set maximum number of invalid Layer 2 multicast protocol packets allowed on a device.



By default, a multicast device can store a maximum of 10 invalid Layer 2 multicast protocol packets.


Format
------

**multicast layer-2 invalid-packet igmp snooping max-count** *max-Num*

**undo multicast layer-2 invalid-packet igmp snooping**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **max-count** *max-Num* | Specifies the maximum number of invalid packets allowed on a device. | The value is an integer ranging from 1 to 100. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If forwarding entries cannot be created on a multicast network, set the maximum number of invalid Layer 2 multicast protocol packets allowed on a device. Then, you can run the **display igmp snooping invalid-packet** command to locate and rectify the fault based on statistics and detailed information about invalid Layer 2 multicast protocol packets.


Example
-------

# Set the maximum number of invalid IGMP Snooping protocol packets allowed on a device to 20.
```
<HUAWEI> system-view
[~HUAWEI] multicast layer-2 invalid-packet igmp snooping max-count 20

```