lldp transmit interval
======================

lldp transmit interval

Function
--------



The **lldp transmit interval** command sets the global interval for a device to send LLDP packets.

The **undo lldp transmit interval** command restores the default global interval for sending LLDP packets.



By default, the global interval for a device to send LLDP packets is 30 seconds.


Format
------

**lldp transmit interval** *interval*

**undo lldp transmit interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies a global interval for a device to send LLDP packets. | The value is an integer ranging from 5 to 32768, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By periodically exchanging LLDP packets with neighbors, a device can notify neighbors of its own status to ensure the accuracy and timely discovery of network topology and communication stability.To configure a global interval for a device to send LLDP packets, run the lldp transmit interval command. This command helps adjust the frequency of network topology discovery.



**Prerequisites**



LLDP has been enabled globally using the lldp enable command in the system view.



**Configuration Impact**

The interval value must be appropriate. You can flexibly adjust this parameter based on the network load:

* The greater the value, the lower the frequency of LLDP packets being exchanged. This saves resources of the system. However, if the value is too large, the local device cannot immediately notify neighbors of its status. As a result, the NMS cannot dynamically detect network topology changes.
* The smaller the value, the higher the frequency of LLDP packets being exchanged. This ensures timely network topology discovery. However, if the delay is too short, LLDP packets are exchanged too frequently. This increases the system burden and wastes resources.The default interval is recommended.

**Precautions**

The interval value is closely related to the delay value specified using the **lldp transmit delay** command.

* If you increase the INTERVAL value, the target INTERVAL value is not restricted by the delay value, but and ensure that the target INTERVAL value is smaller than or equal to 32768.
* If you decrease the INTERVAL value, ensure that the target INTERVAL value is greater than or equal to four times the delay value.Note:
* If the target INTERVAL value is less than four times the delay value, you must adjust the delay value to be less than or equal to a quarter of the target interval value before setting the target interval value.
* If the delay value is greater than a quarter of the default INTERVAL value, you must adjust the delay value to be less than or equal to a quarter of the default INTERVAL value before running the **undo lldp transmit interval** command to restore the default interval value.


Example
-------

# Set the global interval for a device to send LLDP packets to 60 seconds.
```
<HUAWEI> system-view
[~HUAWEI] lldp transmit interval 60

```