stp port priority (Layer 2 interface view)
==========================================

stp port priority (Layer 2 interface view)

Function
--------



The **stp port priority** command sets a priority for a port on a spanning tree.

The **undo stp port priority** command restores the default priority.



By default, the priority of a port on a spanning tree is 128.


Format
------

**stp** [ **process** *process-id* ] [ **instance** *instance-id* ] **port** **priority** *priority*

**undo stp** [ **process** *process-id* ] [ **instance** *instance-id* ] **port** **priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **process** *process-id* | Indicates the ID of a Multiple Spanning Tree Protocol (MSTP) process.  If this parameter is not specified, the priority of a port in process 0 is displayed. | The value is a decimal integer ranging from 1 to 256. |
| **instance** *instance-id* | Specifies the ID of a spanning tree instance.  If this parameter is not specified, statistics about the topology changes of a Common and Internal Spanning Tree (CIST) are displayed. | The value is an integer ranging from 0 to 4094, Value 0 indicates CIST. |
| *priority* | Specifies the priority of a port in spanning tree calculation. | The value is an integer that ranges from 0 to 240, with a step of 16. For example, the value can be 0, 16, or 32. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When ports participate in spanning tree calculation, the port IDs (PIDs) of these ports on devices may affect the designated port election result. During spanning tree calculation, the port with the smallest PID is elected as the designated port.A PID is the ID of a port and consists of a 4-bit priority and a 12-bit port number.To change the priority of a port, run the stp port priority command. This affects the PID of the port and determines whether the port can be elected as the designated port.



**Configuration Impact**



When the priority of a port changes, a spanning tree protocol recalculates the role of the port and performs status transition for the port.



**Precautions**



The port priority determines a port role in a specified spanning tree instance and process. You can set different priorities for a port in different spanning tree instances or processes so that user traffic can be forwarded along different links and traffic load balancing can be implemented.




Example
-------

# Set the priority of 100GE1/0/1 to 16 in spanning tree instance 2.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp instance 2 port priority 16

```