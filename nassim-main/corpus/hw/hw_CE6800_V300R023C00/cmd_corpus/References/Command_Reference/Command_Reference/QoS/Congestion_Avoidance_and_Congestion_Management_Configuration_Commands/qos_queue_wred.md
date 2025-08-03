qos queue wred
==============

qos queue wred

Function
--------



The **qos queue wred** command applies a Weighted Random Early Detection (WRED) drop profile to an interface queue.

The **undo qos queue wred** command deletes a WRED drop profile from an interface queue.



By default, no WRED drop profile is applied to an interface queue.


Format
------

**qos queue** *queue-index* **wred** *drop-profile-name*

**undo qos queue** *queue-index* **wred**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *queue-index* | Specifies the index of a queue. | The value is an integer that ranges from 0 to 7. |
| *drop-profile-name* | Specifies the name of a WRED drop profile. | The value must be the name of an existing WRED drop profile on the device. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The traditional packet loss policy uses the tail drop method. This method processes all packets equally without classifying the packets into different types. When congestion occurs, packets at the end of a queue are discarded until the congestion problem is solved. This policy leads to global TCP synchronization. The RED technique randomly discards packets to prevent the transmission speed of multiple TCP connections from being reduced simultaneously.To prevent global TCP synchronization, use Random Early Detection (RED) and WRED.RED and WRED randomly discard packets to prevent global TCP synchronization. When packets of a TCP connection are discarded, packets of other TCP connections can still be sent at a high rate, ensuring bandwidth use efficiency.

**Prerequisites**

Before applying a WRED drop profile, run the **drop-profile** command to create a WRED drop profile.

**Precautions**

On the device, you can apply a WRED drop profile to an interface or a queue on an interface.If you apply a WRED drop profile to an interface and an interface queue simultaneously, the WRED drop profile that is applied to the interface queue first takes effect.To apply the same WRED drop profile to queues with the same index on multiple interfaces, perform the configuration on a port group to reduce the workload.


Example
-------

# Create a WRED drop profile named wred1 and apply it to queue 1 on the specified interface.
```
<HUAWEI> system-view
[~HUAWEI] drop-profile wred1
[*HUAWEI-drop-wred1] color green low-limit 80 high-limit 100 discard-percentage 10
[*HUAWEI-drop-wred1] color yellow low-limit 60 high-limit 80 discard-percentage 20
[*HUAWEI-drop-wred1] color red low-limit 40 high-limit 60 discard-percentage 40
[*HUAWEI-drop-wred1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] qos queue 1 wred wred1

```