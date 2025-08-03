qos queue ecn
=============

qos queue ecn

Function
--------



The **qos queue ecn** command enables the explicit congestion notification (ECN) function for a specified queue and sets the drop thresholds and maximum drop probability using the drop profile.

The **undo qos queue ecn** command disables ECN on a specified queue.



By default, ECN is disabled on a queue.


Format
------

**qos queue** *queue-index* **ecn**

**undo qos queue** *queue-index* **ecn**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *queue-index* | Specifies the index of a queue. | The value is an integer that ranges from 0 to 7 . |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the downstream and upstream devices support ECN, the downstream device identifies and marks the network congestion based on the ECN field in the packets. The downstream device notifies the upstream device of the detected network congestion. Upon receiving the notification, the upstream device lowers the rate of sending packets to avoid worsening congestion.

**Prerequisites**

Apply a WRED drop profile to a queue.

**Configuration Impact**

After ECN is enabled for a queue, the device does not drop packets according to the WRED drop profile upon queue congestion. Instead, the device changes the ECN field (value 01 or 10) to the CE field (value 11) in the packets.

**Precautions**

The ECN remarking low limit is configured in drop-profile.


Example
-------

# Enable ECN for queue 0 on the specified interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos queue 0 ecn

```