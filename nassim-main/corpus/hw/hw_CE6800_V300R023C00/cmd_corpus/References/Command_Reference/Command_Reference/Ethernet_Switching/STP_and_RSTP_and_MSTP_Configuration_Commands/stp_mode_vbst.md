stp mode vbst
=============

stp mode vbst

Function
--------



The **stp mode vbst** command sets an operation mode vbst for a spanning tree protocol.

The **undo stp mode** command restores the default operation mode of a spanning tree protocol.



By default, the operation mode of a spanning tree protocol is MSTP.


Format
------

**stp mode vbst**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On the network running a spanning tree protocol, devices running different spanning tree protocols cannot communicate with each other. As a result, spanning trees cannot be properly calculated. A switch has four operation modes: VBST, MSTP, RSTP, and STP.The **stp mode** command can be used to set a proper operation mode for a spanning tree protocol on a device and enables the device to identify BPDUs sent by a device that runs a different spanning tree protocol during communication.



**Configuration Impact**



After the **stp mode vbst** command is run on a device, all ports running VBST on the device, excluding the ports directly connected to STP switches, operate in VBST mode and can send VBST BPDUs. The ports directly connected to STP switches operate in STP mode.



**Precautions**

* A port operating in MSTP mode can communicate with a port operating in RSTP mode.
* VBST BPDUs and RST BPDUs can be used at the same time.
* The stp mode rstp command can be used to enable a switch that does not support MSTP to communicate with an STP device.
* In VBST mode, the destination MAC address of the BPDUs is 0100-0CCC-CCCD. In STP/RSTP/MSTP mode, the destination MAC address of the BPDUs is 0180-C200-0000.


Example
-------

# Set the device to work in VBST mode.
```
<HUAWEI> system-view
[~HUAWEI] stp mode vbst

```