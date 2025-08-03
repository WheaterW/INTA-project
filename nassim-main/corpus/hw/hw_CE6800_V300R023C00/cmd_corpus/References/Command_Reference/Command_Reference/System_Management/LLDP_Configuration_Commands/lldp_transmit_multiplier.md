lldp transmit multiplier
========================

lldp transmit multiplier

Function
--------



The **lldp transmit multiplier** command sets the time multiplier of device information held on neighbors.

The **undo lldp transmit multiplier** command restores the default time multiplier.



The default time multiplier is 4.


Format
------

**lldp transmit multiplier** *hold-multiplier*

**undo lldp transmit multiplier**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *hold-multiplier* | Time multiplier. | The value is an integer that ranges from 2 to 10. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A time multiplier can be set for a device to calculate the valid time of LLDP packets being sent to neighbors. The time of device information held in neighbors can be adjusted by setting this parameter. The formula for calculating the TTL of device information held on neighbors is as follows:TTL = Min (65535, (interval x hold-multiplier)). The interval value is configured using the **lldp transmit interval** command.After receiving LLDP packets sent by a local device, neighbors update the aging time of local device information based on the TTL value. Even if the local device has LLDP disabled, neighbors still hold local device information until the TTL expires. This effectively prevents frequent network topology changes.



**Prerequisites**



LLDP has been enabled globally using the lldp enable command in the system view.



**Configuration Impact**

The hold-multiplier value must be appropriate. You can flexibly adjust this parameter based on the network load:

* The greater the value, the lower the frequency of network topology changes. However, if the value is too large, the local device cannot immediately notify neighbors of its status. As a result, the NMS cannot dynamically detect network topology changes.
* The smaller the value, the higher the frequency of sending local status information to neighbors. This helps the neighbors dynamically refresh the network topology. However, if the delay is too short, the neighbors refresh status information about the local device frequently. This increases the possibility of network flapping and system load and wastes resources.The default time multiplier is recommended.


Example
-------

# Set the time multiplier of device information held on neighbors to 5.
```
<HUAWEI> system-view
[~HUAWEI] lldp enable
[*HUAWEI] lldp transmit multiplier 5

```