storm control action
====================

storm control action

Function
--------



The **storm control action** command sets the storm control action to error-down or block.

The **undo storm control action** command cancels the configuration.



By default, no storm control action is configured.


Format
------

**storm control action** { **error-down** | **block** | **suppress** }

**undo storm control action**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **error-down** | Shuts down an interface. | - |
| **block** | Blocks packets. | - |
| **suppress** | Suppresses packets. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In a storm detection interval, when the average rate of broadcast, unknown multicast, or unknown unicast packets received on an interface is greater than the specified upper threshold, the interface shuts down, blocks the packets, or suppresses the packets based on the configured storm control action.A device sets the status of an interface to error-down when it detects a fault on the interface. An interface in error-down state cannot send or receive packets, and the interface indicator is off.Generally, when attack packets exist, the average rate at which an interface receives broadcast, unknown multicast, or unknown unicast packets is higher than the specified upper threshold. In this situation, identify the attack source, remove the attack, and recover the interface status.You can use either one of the following methods for interface recovery:

* Manual recovery (after an error-down event occurs): If a few interfaces need to be recovered, run the **shutdown** and **undo shutdown** commands in the interface view. Alternatively, run the **restart** command in the interface view to restart the interfaces.
* Automatic recovery (before an error-down event occurs): This function should be used if a large number of interfaces enter the error-down state, as manually recovering so many error-down interfaces is time-consuming and error-prone. You can run the **error-down auto-recovery cause storm-control interval** command in the system view to enable automatic interface recovery and set the automatic recovery delay. You can run the **display error-down recovery** command to check information about automatic interface recovery.

Example
-------

# Configure the interface to block packets.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] storm control action block

```