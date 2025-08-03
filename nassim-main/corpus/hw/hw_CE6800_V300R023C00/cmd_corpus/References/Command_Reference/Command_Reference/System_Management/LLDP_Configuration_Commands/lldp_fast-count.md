lldp fast-count
===============

lldp fast-count

Function
--------



The **lldp fast-count** command sets the number of Link Layer Discovery Protocol (LLDP) packets to be quickly sent to neighbors.

The **undo lldp fast-count** command restores the default number of LLDP packets to be sent to neighbors.



A device by default quickly sends four LLDP packets to its neighbors.


Format
------

**lldp fast-count** *count*

**undo lldp fast-count**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *count* | Specifies the number of LLDP packets to be quickly sent to neighbors. | The value is an integer ranging from 1 to 8. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To help neighbors quickly obtain information about a local device, the local device sends a number of LLDP packets to neighbors when the local device discovers a new neighbor (that is, when the device receives an LLDP packet from a transmit device for which it has no information), or when LLDP is enabled for the device that previously had LLDP disabled, or the interface connected to a neighbor goes Up.You can run the lldp fast-count command to set the number of LLDP packets to be quickly sent to neighbors to help neighbors quickly obtain information about the local device, and help the NMS quickly detect network topology.



**Prerequisites**



LLDP has been enabled globally using the lldp enable command in the system view.



**Precautions**



The device fast sends LLDP packets to neighbors at an interval of 1s. This process is not restricted by the delay. After quickly sending a specified number of LLDP packets, the device sends LLDP packets to neighbors at an interval specified by lldp transmit interval.Description:The delay in sending LLDP packets is set using the **lldp transmit delay** command. This prevents the device from frequently sending LLDP packets to neighbors and suppresses network flapping.




Example
-------

# Configure a device to quickly send five LLDP packets to neighbors.
```
<HUAWEI> system-view
[~HUAWEI] lldp enable
[*HUAWEI] lldp fast-count 5

```