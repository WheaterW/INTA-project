stp timer
=========

stp timer

Function
--------



The **stp timer** command sets a Forward Delay value, an interval (Hello time) at which BPDUs are sent, a Max Age value (BPDU aging time).

The **undo stp timer** command restores the default setting.



The default Forward Delay value is 1500 centiseconds, the interval at which BPDUs are sent is 200 centiseconds, the max age value is 2000 centiseconds.


Format
------

**stp timer** { **forward-delay** *forward-delay* | **hello** *hello-time* | **max-age** *max-age* }

**undo stp timer** { **forward-delay** | **hello** | **max-age** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **forward-delay** *forward-delay* | Specifies the value of the Forward Delay. | The value is an integer ranging from 400 to 3000, in centiseconds. The step is 100. |
| **hello** *hello-time* | Specifies the interval at which BPDUs are sent. | The value is an integer ranging from 100 to 1000 with a step of 100, in centiseconds.  To ensure proper working of a spanning tree, the Hello Time, Forward Delay, and Max Age must meet the following requirements. Otherwise, network flapping frequently occurs.   * 2 Ã (Forward Delay-1.0 second) >= Max Age * Max Age >= 2 Ã (Hello Time + 1.0 second)   Setting a network diameter using the stp bridge-diameter command is recommended. After the stp bridge-diameter command is run, the device sets optimal values for the Hello Time, Forward Delay, and Max Age. |
| **max-age** *max-age* | Specifies the BPDU aging time on a port. | The value is an integer ranging from 600 to 4000 with a step of 100, in centiseconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* On a network running STP, a device checks whether the BPDUs received from an upstream device time out based on the Max Age value. To set a Max Age value, run the stp timer max-age command. If the received BPDUs time out, the device ages the BPDUs and blocks the port that receives the BPDUs. Then, the device sends the BPDUs with itself as the root bridge. This aging mechanism effectively controls the radius of the spanning tree and timeout period of received BPDUs.
* On a network running STP, if the network topology is changed, it takes time for new configuration BPDUs to be advertised across the network. During this time, interfaces blocked may be unblocked before required interfaces are blocked. As a result, a temporary loop may occur. To prevent this problem, run the stp timer forward-delay command to set a Forward Delay value. During the delay time, all interfaces are blocked temporarily.
* On a network running STP, a device periodically sends BPDUs to other devices on the same spanning tree at the interval of the Hello Time to ensure that the spanning tree is stable. To set such an interval, run the stp timer hello command.
* If no BPDUs are received from the upstream device within the timeout period (Timeout period = Hello Time x 3 x Timer Factor), the spanning tree is calculated again.In a spanning tree where two devices are connected to each other, the device closer to the root bridge is the upstream device of another device.

**Configuration Impact**

* The Forward Delay value set on the root bridge is advertised to other devices of the same spanning tree using BPDUs. Then it becomes the Forward Delay value of all devices on the spanning tree.
* The Hello Time set on the root bridge is advertised to other devices of the same spanning tree using BPDUs. Then it becomes the Hello Time value of all devices on the spanning tree.
* The Max Age value set on the root bridge is advertised to other devices of the same spanning tree using BPDUs. Then it becomes the MaxAge value of all devices on the spanning tree.


Example
-------

# Set the Max Age to 1000 centiseconds.
```
<HUAWEI> system-view
[~HUAWEI] stp timer max-age 1000

```