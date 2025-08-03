stp transmit-limit
==================

stp transmit-limit

Function
--------



The **stp transmit-limit** command sets the maximum number of BPDUs that each interface sends every second.

The **undo stp transmit-limit** command restores the default value.



By default, interfaces send a maximum of six BPDUs every second.


Format
------

**stp transmit-limit** *packet-number*

**undo stp transmit-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *packet-number* | Specifies the maximum number of BPDUs that each interface sends every second. | The value is an integer ranging from 1 to 255. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* On a network running STP, a device sends BPDUs to other devices on the same spanning tree at an interval of the Hello time to maintain network stability. If the device sends too many BPDUs every second, the transmission occupies excessive system and bandwidth resources. To avoid this problem, run the **stp transmit-limit** command in the system view to configure the maximum number of BPDUs that each interface sends every second. This configuration limits the rate at which each interface sends BPDUs and prevents the spanning tree protocol from occupying excessive system and bandwidth resources.
* To set the maximum number of BPDUs that each interface on the device sends every second, run the **stp transmit-limit** command in the system view. To set the maximum number of BPDUs that a specified interface sends every second, run the stp transmit-limit (interface view) command.
* The Hello time is the value of the Hello timer and specifies the interval at which the device sends BPDUs. You can configure the Hello time using the **stp timer hello** command.

**Precautions**



If the same maximum number of BPDUs need to be sent by each interface on a device, run the stp transmit-limit (system view) command. The stp transmit-limit (interface view) command takes precedence over the stp transmit-limit (system view) command. If the stp transmit-limit (interface view) command is run on an interface, the stp transmit-limit (system view) command does not take effect on the interface.The maximum number of BPDUs that an interface can send in a process is set by using the **stp transmit-limit** command. If an interface joins multiple processes, the maximum number of BPDUs that an interface can send needs to be accumulated. For example, if the maximum number of BPDUs that an interface can send in a process is set to 5 by using the **stp transmit-limit** command, the interface joins three processes, in this case, the maximum number of BPDUs that the interface can send is 15.




Example
-------

# Set the maximum number of BPDUs that each interface of a device can send every second to 5.
```
<HUAWEI> system-view
[~HUAWEI] stp transmit-limit 5

```