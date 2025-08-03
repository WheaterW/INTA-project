auto-defend action
==================

auto-defend action

Function
--------



The **auto-defend action** command enables the punishment function of attack source tracing and specify the punishment action.

The **undo auto-defend action** command disables the punishment function of attack source tracing.



By default, the attack source punish function is low-priority.


Format
------

**auto-defend action** { **deny** [ **timeout** *timeout-num* ] | **error-down** }

**undo auto-defend action** [ **deny** [ **timeout** *timeout-num* ] | **error-down** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **deny** | Discards packets sent from an attack source. | - |
| **timeout** *timeout-num* | Specifies the period during which packets sent from an identified attack source are discarded. | The value is an integer that ranges from 1 to 86400. The default value is 300,in second. |
| **error-down** | Sets an interface that receives attack packets to the error-down state. | - |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The attack source tracing process consists of four phases: packet parsing, traffic analysis, attack source identification, and taking attack source punish actions. The **auto-defend action** command is applied to taking attack source punish actions. The device discards the packets sent from the identified source or Error-Down the interface receiving attack packets.The device records the status of an interface as Error-Down when it detects that a fault occurs. The interface in Error-Down state cannot receive or send packets and the interface indicator is off.

**Prerequisites**

Attack source tracing has been enabled using the **auto-defend enable** command.

**Follow-up Procedure**

When an interface enters the Error-Down state, it is recommended that you identify the attack source and remove the attack first, and then recover the interface status.An interface in Error-Down state can be recovered using either of the following methods:

* Manual recovery (after an Error-Down event occurs): If a few interfaces need to be recovered, run the **shutdown** and **undo shutdown** commands in the interface view. Alternatively, run the **restart** command in the interface view to restart the interfaces.
* Automatic recovery (before an Error-Down event occurs): If a large number of interfaces need to be recovered, manual recovery is time consuming and some interfaces may be omitted. To avoid this problem, you can run the **error-down auto-recovery cause auto-defend interval** command in the system view to enable automatic interface recovery and set the recovery delay time. You can run the **display error-down recovery** command to view information about automatic interface recovery.

**Precautions**

If you run the **auto-defend action** command multiple times, only the latest configuration takes effect.After the auto-defend action is set to deny, the device discards packets when being attacked. The configuration result can be verified using the **display auto-defend attack-source** command.The device does not take punish actions on attack sources of whitelist users.


Example
-------

# Configure the device to discard packets from the identified source every 10 seconds.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-defend enable
[*HUAWEI-cpu-defend-policy-test] auto-defend action deny timeout 10

```