lldp transmit delay
===================

lldp transmit delay

Function
--------



The **lldp transmit delay** command sets the delay time for a device to send Link Layer Discovery Protocol (LLDP) packets.

The **undo lldp transmit delay** command restores the default delay time.



The default delay time is 2 seconds.


Format
------

**lldp transmit delay** *delay*

**undo lldp transmit delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay* | Specifies the delay time for initializing LLDP on interfaces. | The value is an integer ranging from 1 to 8192, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If the device status changes, a device sends LLDP packets to neighbors to notify the neighbors of its status change. If the device status changes frequently, the device will frequently send LLDP packets to its neighbors, causing network flapping.To prevent network flapping caused by LLDP packets frequently sent to neighbors, set a delay time. To set the delay time for sending LLDP packets on a device, run the lldp message-transmission delay command.



**Prerequisites**



LLDP has been enabled globally using the lldp enable command in the system view.



**Configuration Impact**

The delay time for sending LLDP packets must be properly set. You can flexibly adjust this parameter based on the network load.

* The longer the delay, the lower the frequency of network flapping. However, if the delay is too long, the neighbors cannot dynamically trace local device status changes. As a result, the neighbors cannot immediately refresh the network topology.
* The shorter the delay, the higher the frequency of sending local status information to neighbors. This helps the neighbors dynamically refresh the network topology. However, if the delay is too short, the neighbors refresh status information about the local device frequently. This increases the possibility of network flapping and system load and wastes resources.The default delay time for sending LLDP packets is recommended.

**Precautions**

The delay for sending LLDP packets is closely related to the interval for sending LLDP packets specified by the **lldp transmit interval** command.

* If you reduce the delay value, the target delay value is not restricted by the interval value, but the target delay value must be greater than or equal to 1.
* When increasing the value of delay, ensure that the target value of delay is less than or equal to a quarter of the value of interval.Description:
* If the target value of delay is greater than a quarter of the value of interval, you need to adjust the value of interval to be greater than or equal to four times the target value of delay, and then set delay to the target value.
* If the value of interval is smaller than four times the default value of delay, you cannot run the **undo lldp transmit delay** command to restore the default value of delay. Instead, you need to change the value of interval to be greater than or equal to four times the default value of delay, and then run the **undo lldp transmit delay** command.


Example
-------

# Set the delay time for sending LLDP packets to 3 seconds.
```
<HUAWEI> system-view
[~HUAWEI] lldp enable
[*HUAWEI] lldp transmit delay 3

```