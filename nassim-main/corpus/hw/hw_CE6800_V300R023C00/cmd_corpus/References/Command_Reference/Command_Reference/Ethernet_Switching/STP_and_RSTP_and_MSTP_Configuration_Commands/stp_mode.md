stp mode
========

stp mode

Function
--------



The **stp mode** command sets an operation mode for a spanning tree protocol.

The **undo stp mode** command restores the default operation mode of a spanning tree protocol.



By default, the operation mode of a spanning tree protocol is Multiple Spanning Tree Protocol (MSTP).


Format
------

**stp mode** { **mstp** | **rstp** | **stp** }

**undo stp mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **mstp** | Indicates the MSTP mode. | - |
| **rstp** | Indicates the rapid spanning tree protocol (RSTP) mode. | - |
| **stp** | Indicates the STP mode. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* On an STP/RSTP/MSTP network, devices running different spanning tree protocols cannot communicate with each other. As a result, spanning trees cannot be properly calculated.
* To resolve this problem, run the **stp mode** command to configure a proper operation mode for a local device so that the remote device can identify BPDUs sent by the local device. The operation mode can be MSTP, RSTP, or STP.
* By default, all ports on a device operate in MSTP mode. When a port is directly connected to an STP port, the operation mode of the port is automatically switched to STP.

**Configuration Impact**

* After the **stp mode mstp** command is run in an MSTP process, all MSTP process-binding ports except the port directly connected to an STP port operate in MSTP mode and send MST BPDUs. The port directly connected to an STP port operates in STP mode.
* After the **stp mode rstp** command is run in an MSTP process, all MSTP process-binding ports except the port directly connected to an STP port operate in RSTP mode and send RST BPDUs. The port directly connected to an STP port operates in STP mode.
* After the **stp mode stp** command is run in an MSTP process, all ports bound to the MSTP process operate in STP mode and send STP configuration BPDUs.

**Precautions**



A port operating in MSTP mode can communicate with a port operating in RSTP mode.The **stp mode rstp** command can be used to enable a device that does not support MSTP to communicate with an STP device.




Example
-------

# Set the device to work in STP mode.
```
<HUAWEI> system-view
[~HUAWEI] stp mode stp

```