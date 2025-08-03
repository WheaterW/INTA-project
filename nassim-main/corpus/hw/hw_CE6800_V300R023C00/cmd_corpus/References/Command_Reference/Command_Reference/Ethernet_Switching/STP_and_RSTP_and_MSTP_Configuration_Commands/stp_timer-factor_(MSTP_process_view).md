stp timer-factor (MSTP process view)
====================================

stp timer-factor (MSTP process view)

Function
--------



The **stp timer-factor** command sets a timer factor for the Hello time to determine the timeout period of the device.

The **undo stp timer-factor** command restores the default timer factor.



By default, the value is 3.

If a device does not receive BPDUs from an upstream device within the timeout period (Timeout period = Hello time x 3 x Timer factor), it performs spanning tree calculation again.




Format
------

**stp timer-factor** *factor*

**undo stp timer-factor**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *factor* | Specifies a timer factor. | The value is an integer ranging from 1 to 10. |



Views
-----

MSTP process view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a network running spanning tree protocol, if a device does not receive BPDUs from an upstream device within the timeout period, it considers that the upstream device becomes faulty and will recalculate the spanning tree.

The upstream device sometimes fails to send BPDUs within the timeout period because it is busy processing services. In this situation, the downstream device should not recalculate the spanning tree. You can run the stp timer-factor command to set a larger time factor to prolong the timeout period. This reduces network resource waste.



**Configuration Impact**



The smaller the factor value is, the shorted the timeout period. In this case, there is a higher probability that the device incorrectly considers the upstream device faulty.

The larger factor value is, the longer the timeout period. In this case, there is a higher probability that the traffic becomes interrupted because the upstream device has become faulty.



**Precautions**



In a spanning tree where two devices are connected to each other, the device closer to the root bridge is the upstream device of another device.




Example
-------

# Set the TimerFactor of the MSTP process 1 to 6.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] stp timer-factor 6

```