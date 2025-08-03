graceful-restart timer restart (BGP multi-instance view)
========================================================

graceful-restart timer restart (BGP multi-instance view)

Function
--------



The **graceful-restart timer restart** command sets the maximum duration on a device for each peer to wait for its BGP peer relationship to be reestablished with the device.

The **undo graceful-restart timer restart** command deletes the configured duration.



By default, each peer specified on a device waits for its BGP peer relationship to be reestablished with the device for a maximum of 150s.


Format
------

**graceful-restart timer restart** *restart-time*

**undo graceful-restart timer restart**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *restart-time* | Specifies the maximum duration on a device for each peer to wait for its BGP peer relationship to be reestablished with the device. | The value is an integer ranging from 3 to 3600, in seconds. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To set the maximum duration on a device for each peer to wait for its BGP peer relationship to be reestablished with the device, run the **graceful-restart timer restart** command. After this command is run, if any peer detects that the device is down, the BGP session on the peer enters the GR process. If the peer relationship is not reestablished within the specified duration, the BGP session exits the GR process, and the peer selects the optimal route among existing routes.



**Configuration Impact**



If the **graceful-restart timer restart** command is run more than once, the latest configuration overrides the previous one.After the **graceful-restart timer restart** command is run on a device, all the device's BGP peer relationships will be disconnected and then reestablished.



**Precautions**



If there are a large number of routes, setting time to a large value is recommended.




Example
-------

# Set the maximum duration to 250s on a device for each peer to wait for its BGP peer relationship to be reestablished with the device.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] graceful-restart timer restart 250

```