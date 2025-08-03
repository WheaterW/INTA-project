stp v-stp port-id-extension enable
==================================

stp v-stp port-id-extension enable

Function
--------



The **stp v-stp port-id-extension enable** command enables extension of the port ID carried in BPDUs sent by M-LAG interfaces in V-STP mode. This ID is calculated by subtracting the M-LAG ID from 4096.



By default, BPDUs sent by an M-LAG interface in V-STP mode carry the port ID 1.


Format
------

**stp v-stp port-id-extension enable**

**undo stp v-stp port-id-extension enable**


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



Virtual Spanning Tree Protocol (V-STP) is a Layer 2 topology management feature in the M-LAG solution. The core idea of V-STP is to virtualize STP of two devices into STP of one device and present the two devices as one device for STP calculation. The default port ID carried in BPDUs sent by an M-LAG interface is 1. When a device is connected to a downstream network or transparently transmits BPDUs, the BPDUs sent by the M-LAG interface are looped back to the two V-STP devices. As a result, as the system MAC address and port number are the same, the system incorrectly considers that a self-loop occurs on the M-LAG interface and blocks the M-LAG interface. To solve this problem, the port ID extension function is introduced for BPDUs sent by M-LAG interfaces.After this function is configured, because different M-LAG interfaces send different port IDs, the M-LAG interface with a larger V-STP port ID is blocked after transparent transmission loopback is performed on the peer end. You can run the **display stp v-stp** command to view the port ID.



**Precautions**



If the V-STP mode is configured on the device but the peer device of the M-LAG interface is not configured to transparently transmit STP packets, you are not advised to run this command.In V-STP mode, the configuration of the STP port ID extension function must be the same on the two devices. Otherwise, STP flapping may occur.




Example
-------

# Enable the port ID extension function for M-LAG interfaces.
```
<HUAWEI> system-view
[~HUAWEI] stp v-stp enable
[~HUAWEI] stp v-stp port-id-extension enable

```