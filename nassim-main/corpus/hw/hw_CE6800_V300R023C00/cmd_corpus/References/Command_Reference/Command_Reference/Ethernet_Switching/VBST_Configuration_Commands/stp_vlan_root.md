stp vlan root
=============

stp vlan root

Function
--------



The **stp vlan root** command configures the device as a root bridge or secondary root bridge of a spanning tree.

The **undo stp vlan root** command cancels the configuration.



By default, the device does not function as the root bridge or secondary root bridge of a spanning tree.


Format
------

**stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **root** { **primary** | **secondary** }

**undo stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **root** [ **primary** | **secondary** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **to** *vlan-id* | Configures the switching device functions as the root bridge or the secondary root bridge of a spanning tree in VLANs. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **primary** | Indicates that the switching device functions as the root bridge of a spanning tree. | - |
| **secondary** | Indicates that the switching device functions as the secondary root bridge of a spanning tree. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a spanning tree protocol network, each spanning tree has only one root bridge, which is responsible for sending BPDUs. Owning to the importance of the root bridge, the switch with high performance and network hierarchy is generally chosen as a root bridge. The priority of such a device, however, may be not that high. Therefore, setting a high priority for the switch is necessary so that the switch can function as a root bridge.To ensure nonstop traffic transmission, run the stp vlan root command to configure the switch as the secondary root bridge. When the root bridge is faulty or is powered off, the secondary root bridge becomes the root bridge during spanning tree calculation.NOTE:After the **stp root primary** command is run to set a device to be the primary root bridge, the priority value of the device is 0 in the spanning tree and the priority cannot be modified.The secondary root bridge specified using the **stp root secondary** command has the priority value of 4096 and the priority cannot be modified.

**Precautions**

On a network running STP, RSTP, MSTP, or VBST, specify the core switching device as the root bridge to ensure the stability of the STP Layer 2 network. Otherwise, new devices may trigger STP root switchover, causing temporary service interruption.A spanning tree can be configured with only one root bridge.If multiple secondary root bridges are configured in a spanning tree, the secondary root bridge with the smallest MAC address becomes the secondary root bridge of the spanning tree.When a Huawei device is connected to a non-Huawei device, you are advised to run the **stp vlan priority** command to set the device priority to ensure that the root bridge is selected correctly.


Example
-------

# Configure the device as the root bridge in VLAN 5.
```
<HUAWEI> system-view
[~HUAWEI] stp vlan 5 root primary

```

# Configure the device as the secondary root bridge in VLAN 5.
```
<HUAWEI> system-view
[~HUAWEI] stp vlan 5 root secondary

```