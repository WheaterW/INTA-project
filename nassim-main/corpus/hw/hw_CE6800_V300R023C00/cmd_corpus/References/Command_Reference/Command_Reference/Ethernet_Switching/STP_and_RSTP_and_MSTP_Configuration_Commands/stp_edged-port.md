stp edged-port
==============

stp edged-port

Function
--------



The **stp edged-port** command sets a port as an edge or a non-edge port.

The **undo stp edged-port** command restores the default setting.



By default, all ports are non-edge ports.


Format
------

**stp edged-port** { **enable** | **disable** }

**undo stp edged-port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enable** | Sets the current port as an edge port. | - |
| **disable** | Sets the current port as a non-edge port. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a Layer 2 network running STP, if a port connected to a terminal is configured as an edge port using the **stp edged-port enable** command, the port will not participate in spanning tree calculation. This speeds up network convergence and improves network stability.Running the **stp edged-port enable** command in the interface view configures only the current port as a bridge protocol data unit (BPDU)-filter port. If multiple BPDU-filter ports are required on a device, run the **stp edged-port default** command in the system view to configure all the ports as BPDU-filter ports, and then run the **stp edged-port disable** command in the view of the interfaces that need to participate in spanning tree calculation.If a port has been configured as a non-BPDU filter port using the **stp edged-port disable** command, it remains a non-BPDU filter port, even if the **stp edged-port default** command is run.



**Configuration Impact**



Automatic edge port detection starts by default after RSTP or MSTP is enabled on a port. If the port fails to receive BPDUs within (2 x Hello Timer intervals + 1) seconds, the port is set to an edge port. Otherwise, the port is set to a non-edge port. If the stp edged-port enable or **stp edged-port disable** command is run in the port view, or the **stp edged-port default** command is run in the system view, automatic edge port detection does not take effect on the port. After the **undo stp edged-port** command is run to restore the default edge port attribute, automatic detection of edge ports takes effect again.



**Precautions**



An edge port is automatically changed to a non-edge port after receiving a BPDU, and the spanning tree is recalculated.A non-edge port configured using the **undo stp edged-port** command will become an edge port if the **stp edged-port default** command is run in the system view. However, a non-edge port configured using the **stp edged-port disable** command remains a non-edge port, even if the **stp edged-port default** command is run in the system view.To prevent an edge port from becoming a non-edge port after the edge port receives bogus BPDUs, run the stp bpdu-protection command in the system view to configure BPDU protection. After BPDU protection is configured, if an edge port receives a BPDU, the device where the edge port resides shuts down the edge port but retains the edge port attribute. Meanwhile, the device notifies the NMS of the shutdown event.




Example
-------

# Set 100GE1/0/1 as an edge port.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp edged-port enable

```