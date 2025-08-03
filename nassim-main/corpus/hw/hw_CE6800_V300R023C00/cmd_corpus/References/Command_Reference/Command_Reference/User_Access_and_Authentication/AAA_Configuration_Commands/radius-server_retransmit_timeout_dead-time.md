radius-server retransmit timeout dead-time
==========================================

radius-server retransmit timeout dead-time

Function
--------

The **radius-server retransmit timeout dead-time** command sets the number of times RADIUS authentication request packets are retransmitted, the timeout period, and the interval for the server to revert to the active state.

The undo radius-server retransmit timeout dead-time command restores the default number of times that RADIUS authentication request packets are retransmitted, the default timeout period, and the default interval for the server to revert to the active state.

By default, the number of times RADIUS authentication request packets are retransmitted is 3, the timeout period is 5 seconds, and the interval for the server to revert to the active state is 5 minutes.



Format
------

**radius-server** { **retransmit** *retry-times* | **timeout** *time-value* | **dead-time** *dead-time* } \*

**undo radius-server** { **retransmit** [ *retry-times* ] | **timeout** [ *time-value* ] | **dead-time** [ *dead-time* ] } \*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **retransmit** *retry-times* | Specifies the number of retransmissions due to timeout. | The value is an integer that ranges from 1 to 5. The default value is 3. |
| **timeout** *time-value* | Specifies the timeout period. | The value is an integer that ranges from 1 to 100, in seconds. The default value is 5. |
| **dead-time** *dead-time* | Specifies the interval for the server to revert to the active state. | The value is an integer ranging from 1 to 65535, in minutes. The default value is 5. |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

The retransmission upon timeout mechanism is configured for a device to forward RADIUS authentication request packets sourced from users to the server. The overall retransmission time depends on the retransmission interval, number of retransmissions, RADIUS server status, and number of servers configured in the RADIUS server template.

You can configure the number of times that RADIUS authentication request packets are retransmitted and the timeout period using the radius-server retransmit retry-times and
**radius-server timeout time-value** commands, respectively. If a device sends an authentication request packet to the RADIUS server and does not receive any response packet from the server during the timeout period, the device sends an authentication request packet again.You can run the
**radius-server dead-time dead-time** command to configure the duration for which the RADIUS server remains Down. After the device sets the RADIUS server status to Down and the interval specified by dead-time expires, the device resets the server status to Force-up. If a new user needs to be authenticated using RADIUS and no RADIUS server is available, the device attempts to re-establish a connection with a RADIUS server in Force-up state. The Force-up state is defined to prevent servers in Down state from remaining idle.

**Prerequisites**

After automatic detection is enabled, the device immediately sends a detection packet to the RADIUS server in Force-up state. If a packet is received from the RADIUS server within the timeout period, the device sets the RADIUS server status to Up; otherwise, the device sets the RADIUS server status to Down. If automatic detection is disabled, the device can update the RADIUS server status only after receiving an authentication request packet from the user.

**Precautions**

If four authentication server IP addresses are configured in the RADIUS server template, you are advised to reduce the number of times RADIUS authentication request packets are retransmitted and the timeout period.



Example
-------

# Set the number of times RADIUS authentication request packets are retransmitted to 3, the timeout period to 2s, and the interval for the server to revert to the active state to 10 minutes.
```
<~HUAWEI> system-view
[~HUAWEI] radius-server template test1
[*HUAWEI-radius-test1] radius-server retransmit 3 timeout 2 dead-time 10

```