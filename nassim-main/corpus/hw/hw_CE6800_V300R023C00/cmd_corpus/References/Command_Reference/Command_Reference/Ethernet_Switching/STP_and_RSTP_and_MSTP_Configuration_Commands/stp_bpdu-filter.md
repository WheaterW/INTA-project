stp bpdu-filter
===============

stp bpdu-filter

Function
--------



The **stp bpdu-filter enable** command specifies a port as a bridge protocol data unit (BPDU)-filter port.

The **stp bpdu-filter disable** command specifies a port as a non-BPDU-filter port.

The **undo stp bpdu-filter** command restores the default setting.



By default, ports are non-BPDU-filter ports.


Format
------

**stp bpdu-filter** { **enable** | **disable** }

**undo stp bpdu-filter**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enable** | Specifies a port as a bridge protocol data unit (BPDU)-filter port. | - |
| **disable** | Specifies a port as a non-BPDU-filter port. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a network running STP, if a port is configured as an edge port using the **stp edged-port enable** command, the port will not participate in the spanning tree calculation. This speeds up network convergence and improves network stability. However, this port may send BPDUs to other networks, causing network flapping.To prevent this problem, run the **stp bpdu-filter enable** command on the edge port. The port becomes a BPDU-filter port and will not process BPDUs.Running the **stp bpdu-filter enable** command in the interface view configures only the current port as a BPDU-filter port. If multiple BPDU-filter ports are required on a device, run the **stp bpdu-filter default** command in the system view to configure all the ports as BPDU-filter ports, and then run the **stp bpdu-filter disable** command in the view of the interfaces that need to participate in spanning tree calculation. If a port has been configured as a non-BPDU filter port using the **stp bpdu-filter disable** command, it remains a non-BPDU filter port, even if the **stp bpdu-filter default** command is run.



**Precautions**



After the **stp bpdu-filter disable** command is run on a port, the port becomes a non-BPDU-filter port. The port remains a non-BPDU-filter port even if the **stp bpdu-filter default enable** command is run in the system view. After the **undo stp bpdu-filter** command is run on the port, the port restores to the default setting.A BPDU-filter port cannot process and send BPDUs. Consequently, it cannot negotiate the STP status with the directly connected port on the remote device. Therefore, exercise caution when using the **stp bpdu-filter enable** command. Running the **stp bpdu-filter enable** command only on edge ports is recommended.




Example
-------

# Configure 100GE1/0/2 on a network edge device as a BPDU-filter port.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/2
[~HUAWEI-100GE1/0/2] portswitch
[~HUAWEI-100GE1/0/2] stp bpdu-filter enable

```

# Configure 100GE1/0/1 on a network edge device as a non-BPDU-filter port.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp bpdu-filter disable

```