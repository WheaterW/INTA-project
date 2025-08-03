stp vlan mcheck
===============

stp vlan mcheck

Function
--------



The **stp vlan mcheck** command configures a port to switch from the STP mode back to the VBST mode in the specified VLAN.




Format
------

**stp vlan** *vlan-id* **mcheck**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Specifies the VLAN for mode transition. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Interface group view,System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a port of a VBST-enabled device is directly connected to an STP-enabled device, the port automatically switches to the STP mode and then sends BPDUs. This ensures that the two devices properly communicate with each other. If the STP-enabled device is powered off or removed, the port on the VBST-enabled device cannot switch back to the VBST mode. As a result, the VBST-enabled device cannot communicate with other VBST-enabled devices.The **stp vlan mcheck** command can be used to address this problem. After this command is run on a port, the port will switch from the STP mode back to the VBST mode in the specified VLAN.

**Prerequisites**

Configure a port to switch from the STP mode back to the VBST mode in the specified VLAN has been set using the **stp mode vbst** command.

**Precautions**

Running the **stp vlan mcheck** command in the system view configures all ports on the device to switch back to the VBST mode in the specified VLAN.Running the **stp vlan mcheck** command in the interface view configures only the current port to switch back to the VBST mode in the specified VLAN.


Example
-------

# Perform stp vlan 4000 mcheck on the interface and switch it to the VBST mode in VLAN 4000.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp vlan 4000 mcheck

```