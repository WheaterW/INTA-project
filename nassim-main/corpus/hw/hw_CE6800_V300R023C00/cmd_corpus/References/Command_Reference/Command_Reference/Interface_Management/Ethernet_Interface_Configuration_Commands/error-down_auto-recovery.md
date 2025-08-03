error-down auto-recovery
========================

error-down auto-recovery

Function
--------



The **error-down auto-recovery** command configures the auto recovery function on a port to enable the port in the error-down state to automatically go Up, and sets the delay for the transition from Down to Up.

The **undo error-down auto-recovery** command disables the auto recovery function on the port.



By default, the auto recovery function is disabled on a port.


Format
------

**error-down auto-recovery cause** *error-down-type* **interval** *interval-value*

**undo error-down auto-recovery cause** *error-down-type*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interval** *interval-value* | Specifies the auto recovery delay. | The value is an integer ranging from 30 to 86400, in seconds. |
| **cause** *error-down-type* | Specifies the cause of the error-down event. | The value is a string. You can enter a question mark (?) and select a value from the displayed value range. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a network running the Spanning Tree Protocol (STP), after BPDU protection is configured on an edge port, if attackers send pseudo BPDUs to attack a switching device, the switching device automatically makes the edge port go Down immediately after the edge port receives BPDUs. As a result, all services on the edge port are interrupted.By default, the port in the Down state can communicate with other ports only after the administrator manually turns it Up. To enable the interface to go Up automatically, run this command to enable the interface to go Up automatically and set the delay time for the interface to go Up automatically.After a port goes Up, if it receives BPDUs again or the link is considered unavailable within a specific period, the port goes Down again.



**Configuration Impact**



After the **error-down auto-recovery** command is run, the port goes from Down to Up after the delay expires.



**Precautions**



There is no default value for the recovery time. Therefore, you must specify a delay when configuring this command.If you run the **error-down auto-recovery** command to modify the auto-recovery delay, the modification will not take effect on the interface that has been in the error-down state due to a specific cause. The modification only takes effect on the interface that has gone Up from the error-down state.A port enters the error-down state after being shut down due to an error.




Example
-------

# After the function is enabled, set the interval for an interface to automatically go Up to 50 seconds.
```
<HUAWEI> system-view
[~HUAWEI] error-down auto-recovery cause bpdu-protection interval 50

```