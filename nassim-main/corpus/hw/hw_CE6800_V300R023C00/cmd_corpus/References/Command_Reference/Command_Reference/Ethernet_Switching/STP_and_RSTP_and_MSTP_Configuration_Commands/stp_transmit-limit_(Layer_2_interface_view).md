stp transmit-limit (Layer 2 interface view)
===========================================

stp transmit-limit (Layer 2 interface view)

Function
--------



The **stp transmit-limit** command sets the maximum number of Bridge Protocol Data Units (BPDUs) that an interface sends every second.

The **undo stp transmit-limit** command restores the default value.



By default, the maximum number of BPDUs that interfaces send every second is the value configured using the stp transmit-limit (system view) command. If the stp transmit-limit (system view) command is not configured, an interface sends a maximum of six BPDUs every second.


Format
------

**stp transmit-limit** *packet-number*

**undo stp transmit-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *packet-number* | Specifies the maximum number of BPDUs that an interface sends every second. | The value is an integer ranging from 1 to 255. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a network running STP, a device sends BPDUs to other devices on the same spanning tree at an interval of the Hello time. BPDUs are transmitted to help maintain network stability. If the device sends too many BPDUs within the Hello time, the transmission occupies excessive system and bandwidth resources.To avoid this problem, run the **stp transmit-limit** command in the interface view to configure the maximum number of BPDUs that an interface sends every second. This configuration limits the rate at which an interface sends BPDUs and prevents the spanning tree protocol from occupying excessive system and bandwidth resources.The Hello time is the value of the Hello timer and specifies the interval at which the device sends BPDUs. You can configure the Hello time using the **stp timer hello** command.



**Precautions**



If the same maximum number of BPDUs need to be sent by each interface on a device, run the stp transmit-limit (system view) command. The stp transmit-limit (interface view) command takes precedence over the stp transmit-limit (system view) command. If the stp transmit-limit (interface view) command is run on an interface, the stp transmit-limit (system view) command does not take effect on the interface.The **stp transmit-limit** command sets the maximum number of BPDUs that an interface sends every second in each process. If an interface is added to multiple processes, the maximum number of BPDUs multiplies. For example, If you run the **stp transmit-limit** command to configure an interface to send a maximum number of five BPDUs every second and the interface joins 3 processes, the interface can send a maximum of 15 (5 x 3) BPDUs every second.




Example
-------

# Set the maximum number of BPDUs that 100GE1/0/1 sends every second to 5.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] stp transmit-limit 5

```