m-lag up-delay
==============

m-lag up-delay

Function
--------



The **m-lag up-delay** command sets the delay for the M-LAG member interface to report the Up event.

The **undo m-lag up-delay** command restores the default configuration.



By default, the delay for the M-LAG member interface to report the Up event is 240 seconds, and the automatic recovery interval is 0 seconds.


Format
------

**m-lag up-delay** *updelay* [ **auto-recovery** **interval** *intervaltime* ]

**undo m-lag up-delay** *updelay* [ **auto-recovery** **interval** *intervaltime* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *updelay* | Specifies the delay for the M-LAG member interface to report the Up event. | The value is an integer that ranges from 0 to 3600 and the default value is 240, in seconds. |
| **auto-recovery** | Specifies the automatic recovery delay. | - |
| **interval** *intervaltime* | Specifies the automatic recovery interval between M-LAG member interfaces based on the delay in reporting the Up event. | The value is an integer that ranges from 0 to 180 and the default value is 0, in seconds. |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the physical status of an interface changes, the device notifies the upper-layer protocol modules (such as routing and forwarding modules) of the change to guide packet sending and receiving. However, after the device restarts or a card resets, the physical status of the interface changes to Up. In this case, the status of the upper-layer protocol modules does not meet forwarding requirements. If the interface receives a packet and sends it to the upper-layer protocol modules, the upper-layer protocol modules cannot correctly process the packet. As a result, the upper-layer protocol negotiation mechanism does not take effect, causing packet loss. Generally, you can run the **set up-delay** command to set the delay for an interface to go Up. In an M-LAG scenario, you can also run the **m-lag up-delay** command to configure a delay after which an M-LAG member interface goes Up.However, in a device restart or subcard reset fault recovery scenario, if the delays for all interfaces to go Up are the same, M-LAG member interfaces go Up at the same time and service entries are delivered at the same time. As a result, services are interrupted for a long time. You can use auto-recovery interval interval-time to specify the automatic recovery delay between M-LAG member interfaces. M-LAG member interfaces automatically recover one by one based on M-LAG IDs in ascending order. In this manner, interfaces go Up at different time, and entries of each service do not affect each other.

**Precautions**

If you need to change the default configuration, you are advised to set the delay for an M-LAG member interface to report the Up state to 30 seconds or longer.After this command is configured, the delay in reporting the Up state of an M-LAG member interface takes effect only when the device restarts, a subcard resets, or a peer-link fault is rectified.If the **set up-delay** command is also configured on a physical member interface of the M-LAG member interface, the delay configured using the **m-lag up-delay** command takes effect.When M-LAG member interfaces go Up after a delay, they are automatically restored in ascending order of M-LAG IDs. It is recommended that the M-LAG ID of the interface on which services need to be restored preferentially be smaller.If you run the command to change the delay for an M-LAG member interface to go Up within the delay, the current interface recovery time is not affected immediately. When an M-LAG member interface configured with a delay to go Up is restarted, the interface status is restored to the original status immediately. The modified delay takes effect when the device restarts, a subcard resets, or the peer-link fault is rectified next time. Modify the configuration when the interface works properly.


Example
-------

# Set the delay for the M-LAG interface to report the Up event to 90s.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] m-lag up-delay 90

```