deny packet-type
================

deny packet-type

Function
--------



The **deny packet-type** command configures the device to discard packets sent to the CPU.

The **undo deny packet-type** command restores the default action taken for the packets sent to the CPU.



By default, the device does not discard packets sent to the CPU. Instead, the device limits the rate of packets sent to the CPU using the default rate. You can check the rate limit of each type of packets using the display cpu-defend configuration command.


Format
------

**deny packet-type** *packet-type*

**undo deny packet-type** *packet-type*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *packet-type* | Specifies the type of the packet to be discarded. | The packet type information displayed on the device prevails. You can run the display cpu-defend configuration command to check the supported packet types and rate limit. |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After an attack defense policy is created, if the device receives attack packets of a specified type or a large number of packets sent to the CPU, run the **deny** command to configure the device to discard packets of the specified type sent to the CPU.

**Precautions**

If you run the **deny** command, and then the car command, the car command takes effect; if you run the car command, and then the **deny** command, the **deny** command takes effect. After the **undo deny** command is executed, the default action for packets sent to the CPU is restored.


Example
-------

# Configure the drop action taken for arp-request packets to be sent to the CPU in the attack defense policy test.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] deny packet-type arp-request

```