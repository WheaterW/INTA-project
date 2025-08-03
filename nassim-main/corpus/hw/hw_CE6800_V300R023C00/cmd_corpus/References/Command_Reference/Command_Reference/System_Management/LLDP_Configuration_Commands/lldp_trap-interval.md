lldp trap-interval
==================

lldp trap-interval

Function
--------



The **lldp trap-interval** command sets the delay time for a device to send alarms about Link Layer Discovery Protocol (LLDP) neighbor information changes to a network management system (NMS).

The **undo lldp trap-interval** command restores the default delay time.



The default delay time is 5 seconds.


Format
------

**lldp trap-interval** *interval*

**undo lldp trap-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the delay time for a device to send alarms about LLDP neighbor information changes to an NMS. | The value is an integer ranging from 5 to 3600, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After the LLDP alarm function is enabled for a device, the device sends alarms to the NMS if LLDP neighbor information changes. If LLDP neighbor information changes frequently, the device frequently sends alarms to an NMS, causing network flapping.Setting a delay effectively prevents network flapping caused by alarms being frequently sent to the NMS. To set a delay for the device to send alarms about LLDP neighbor information changes to the NMS, run the lldp trap-interval command.



**Configuration Impact**

The delay time for sending alarms about LLDP neighbor information changes must be appropriate. You can flexibly adjust this parameter based on the network load:

* The longer the delay, the lower the frequency of network flapping. However, if the delay is too long, the NMS cannot dynamically trace neighbor status changes. As a result, the NMS cannot immediately refresh the network topology.
* The shorter the delay, the higher the frequency of sending local status information to neighbors. This helps the neighbors dynamically refresh the network topology. However, if the delay is too short, the device refreshes status information about neighbors frequently. This causes network topology flapping, increases the system load, and wastes resources.The default delay time is recommended.


Example
-------

# Set the delay time for a device to send alarms about LLDP neighbor information changes to 6 seconds.
```
<HUAWEI> system-view
[~HUAWEI] lldp enable
[*HUAWEI] lldp trap-interval 6

```