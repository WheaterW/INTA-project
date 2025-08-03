adjust original-dscp
====================

adjust original-dscp

Function
--------



The **adjust original-dscp** command enables dragonfly deadlock prevention and adjusts the queue priority and DSCP value of matched packets.

The **undo adjust original-dscp** command disables dragonfly deadlock prevention and deletes the queue adjustment configuration for matched packets in a dragonfly profile.



By default, dragonfly deadlock prevention is disabled in a dragonfly profile.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**adjust original-dscp** *original-dscpvalue* **to** **priority** *prioritynumber* **dscp** *dscpvalue*

**undo adjust original-dscp** *original-dscpvalue* **to** **priority** *prioritynumber* **dscp** *dscpvalue*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **to** | Adjusts the information about the matched packets. | - |
| **priority** *prioritynumber* | Adjusts the queue priority of the matched packets so that the packets are forwarded from the specified queue. | The value is an integer that ranges from 0 to 5. |
| **dscp** *dscpvalue* | Adjusts the DSCP value of the matched packets to ensure that packets in a hook-shaped flow are still mapped to the specified queue on the downstream device. | The value is an integer that ranges from 0 to 63. |
| **original-dscp** *original-dscpvalue* | Specifies the DSCP value of packets to be adjusted. | The value is an integer that ranges from 0 to 63. |



Views
-----

Dragonfly-profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a direct topology, you can run this command in the dragonfly profile to switch the queue of service flows whose inbound and outbound interfaces are both local ports or whose inbound interface is a global port, proactively adjusting the queue priority and DSCP value of packets to prevent deadlock.

**Precautions**

* PFC deadlock prevention and dragonfly deadlock prevention cannot be both enabled.
* The **adjust original-dscp** command can be run twice at most, with different values configured for original-dscpvalue, prioritynumber, and dscpvalue the second time. To modify the configuration, run the **undo adjust original-dscp** command to delete the original configuration first.

For the CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM:

* Before running the **adjust original-dscp** command to enable dragonfly deadlock prevention, you must run the **abs-pfc priority enable** command to enable dragonfly antilocking PFC. In addition, the priority queue that original-dscp is mapped to and the priority queue specified by priority in the **adjust original-dscp** command must be within the range specified by priority in the **abs-pfc priority enable** command.
* If the priority queue that the original-dscp parameter is mapped to changes to a queue for which dragonfly antilocking PFC is not enabled due to the mapping change between DSCP values and priority queues, dragonfly deadlock prevention does not take effect for the priority queue that the original-dscp parameter is mapped to before and after the mapping change.
* To enable dragonfly deadlock prevention, enable dragonfly antilocking PFC for the corresponding lossless queue first.

For the CE8855 and CE8851-32CQ4BQ:

* If the adaptive routing role has been configured, you must enable PFC on the corresponding interface before running the **adjust original-dscp** command to enable dragonfly deadlock prevention. In addition, the priority queue that original-dscp is mapped to and the priority queue specified by priority in the **adjust original-dscp** command must be within the range of the PFC-enabled priority queues.
* When configuring the adaptive routing role on an interface, you must enable PFC for the priority queue that the original-dscp parameter is mapped to and the priority queue specified by the priority parameter in the **adjust original-dscp** command.
* If the priority queue that the original-dscp parameter is mapped to changes to a queue for which PFC is not enabled due to the mapping change between DSCP values and priority queues, dragonfly deadlock prevention does not take effect for the priority queue that the original-dscp parameter is mapped to before and after the mapping change.

Example
-------

# Adjust the queue priority and DSCP value of matched packets to 4 and 32, respectively. The original DSCP value is 10. (CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM)
```
<HUAWEI> system-view
[~HUAWEI] dragonfly profile default
[*HUAWEI-dragonfly-profile-default] abs-pfc priority 1 4 enable
[*HUAWEI-dragonfly-profile-default] adjust original-dscp 10 to priority 4 dscp 32

```

# Adjust the queue priority and DSCP value of matched packets to 4 and 32, respectively. The original DSCP value is 10. (CE8855 and CE8851-32CQ4BQ)
```
<HUAWEI> system-view
[~HUAWEI] qos buffer headroom-pool size 4 mbytes slot 1
[*HUAWEI] dcb pfc default
[*HUAWEI-dcb-pfc-default] priority 1 4
[*HUAWEI-dcb-pfc-default] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] dcb pfc enable
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] dragonfly profile default
[*HUAWEI-dragonfly-profile-default] adjust original-dscp 10 to priority 4 dscp 32

```