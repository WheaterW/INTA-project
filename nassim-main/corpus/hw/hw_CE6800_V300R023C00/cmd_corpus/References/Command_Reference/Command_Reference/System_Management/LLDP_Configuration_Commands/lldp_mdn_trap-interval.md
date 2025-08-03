lldp mdn trap-interval
======================

lldp mdn trap-interval

Function
--------



The **lldp mdn trap-interval** command sets the delay time for a device to send alarms about MAC address discovery neighbor (MDN) information changes to an NMS.

The **undo lldp mdn trap-interval** command restores the default delay time.



The default delay time is 5 seconds.


Format
------

**lldp mdn trap-interval** *TRAP-INTERVAL*

**undo lldp mdn trap-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *TRAP-INTERVAL* | Trap notification interval. | The value is an integer ranging from 5 to 3600, the default is 5s. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After the LLDP alarm function is enabled for a device, the device sends alarms to the NMS when MDN neighbor information changes. If MDN neighbor information changes frequently, the device frequently sends alarms to an NMS, causing network flapping.You can run this command to set a delay for the device to send alarms about MDN neighbor information changes to the NMS. This command effectively prevents network flapping caused by alarms being frequently sent to the NMS.



**Prerequisites**



LLDP has been enabled globally using the lldp enable command in the system view.



**Configuration Impact**

The delay for sending alarms about MDN neighbor information changes must be appropriate. You can flexibly adjust this parameter based on the network load.

* The longer the delay, the lower the frequency of network flapping. However, if the delay time for sending alarms about MDN neighbor information changes is too long, the NMS cannot dynamically trace neighbor status changes. As a result, the NMS cannot immediately refresh the network topology.
* The shorter the delay, the higher the frequency of network flapping. This helps the NMS immediately refresh the network topology. However, if the delay is too short, the NMS refreshes information about the neighbor status frequently. This causes network flapping, increases the system burden, and wastes resources.The default delay time is recommended.


Example
-------

# Set the delay time for a device to send alarms about MDN neighbor information changes to 6 seconds.
```
<HUAWEI> system-view
[~HUAWEI] lldp mdn trap-interval 6

```