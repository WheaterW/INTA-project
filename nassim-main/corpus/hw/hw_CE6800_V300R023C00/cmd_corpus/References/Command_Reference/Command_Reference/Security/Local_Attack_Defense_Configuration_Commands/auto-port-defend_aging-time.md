auto-port-defend aging-time
===========================

auto-port-defend aging-time

Function
--------



The **auto-port-defend aging-time** command configures the aging time for port attack defense.

The **undo auto-port-defend aging-time** command restores the default aging time for port attack defense.



By default, the aging time for port attack defense is 300 seconds.


Format
------

**auto-port-defend aging-time** *aging-time*

**undo auto-port-defend aging-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *aging-time* | Specifies the aging time for port attack defense. | The value is an integer that ranges from 30 to 86400. The default value is 300, in seconds. |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a device with port attack defense function enabled detects an attack on a port, the device traces the source and limits the rate of the attack packets on the port within the aging time (T seconds). When the aging time expires, the device calculates the protocol packet rate on the port again. If the rate is still above the protocol rate threshold, the device keeps tracing the source and limits the rate of the attack packets; otherwise, the device stops the operations.If the aging time is too short, the device frequently starts packet rate detection on ports, which consumes CPU resources. If the aging time is too long, protocol packets cannot be promptly processed by the CPU, which affects services. Therefore, you need to run the **auto-port-defend aging-time** command to set an appropriate aging time according to the CPU usage and service status.

**Precautions**

If you run the **auto-port-defend aging-time** command multiple times in the same attack defense policy view, only the latest configuration takes effect.


Example
-------

# Set the aging time in the attack defense policy test view to 350 seconds.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-port-defend aging-time 350

```