qos queue-alarm
===============

qos queue-alarm

Function
--------



The **qos queue-alarm** command is used to set the queue packet loss alarm threshold.

The **undo qos queue-alarm** command used to restore the default value of the queue packet loss alarm threshold.



By default, the alarm threshold for the packet loss rate of a port queue is 10.


Format
------

**qos queue-alarm** *queue-index* **drop-packet-rate** *drop-packet-rate-value*

**undo qos queue-alarm** *queue-index*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *queue-index* | Specifies the queue index. | The value is an integer ranging from 0 to 7. |
| **drop-packet-rate** *drop-packet-rate-value* | Specifies the alarm threshold for the packet loss rate of a port queue. | The value is an integer ranging from 0 to 4294967295. The default value is 10. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The interval for detecting queue packet loss alarms is 2 minutes, and the interval for calculating the queue packet loss rate is 1 minute. The data source is the queue rate statistics.


Example
-------

# Configure the queue of 1 index as 1pps.
```
<HUAWEI> system-view
[~HUAWEI] qos queue-alarm 1 drop-packet-rate 1

```