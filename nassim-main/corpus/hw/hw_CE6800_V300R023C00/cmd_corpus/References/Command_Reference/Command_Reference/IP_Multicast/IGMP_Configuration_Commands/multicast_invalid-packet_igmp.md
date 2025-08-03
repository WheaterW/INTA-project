multicast invalid-packet igmp
=============================

multicast invalid-packet igmp

Function
--------



The **multicast invalid-packet igmp** command sets the maximum number of invalid igmp packets that can be stored on a device.

The **undo multicast invalid-packet igmp** command deletes the set maximum number of invalid igmp packets that can be stored on a device.



By default, a device can save a maximum of 10 invalid packets for IGMP protocol.


Format
------

**multicast invalid-packet igmp max-count** *max-number*

**undo multicast invalid-packet igmp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **max-count** *max-number* | Sets the maximum number of invalid multicast protocol packets that can be stored on a device. max-number specifies the maximum number of invalid multicast protocol packets. | The value is an integer ranging from 1 to 100. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If multicast entries fail to be generated or peer relationships fail to be set up, you can enable a device to store invalid multicast protocol packets and run related commands to view statistics and details of the invalid multicast protocol packets. Based on the command output, you can locate and rectify faults.


Example
-------

# Set the maximum number of invalid IGMP messages that can be stored on a device to 20.
```
<HUAWEI> system-view
[~HUAWEI] multicast invalid-packet igmp max-count 20

```