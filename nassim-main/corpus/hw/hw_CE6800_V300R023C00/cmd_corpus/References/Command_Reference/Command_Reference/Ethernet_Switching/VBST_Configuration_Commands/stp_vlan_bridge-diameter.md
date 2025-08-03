stp vlan bridge-diameter
========================

stp vlan bridge-diameter

Function
--------



The **stp vlan bridge-diameter** command configures the diameter of the spanning tree.

The **undo stp vlan bridge-diameter** command restores the default diameter.



By default, the diameter of the spanning tree is 7.


Format
------

**stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **bridge-diameter** *bridge-diameter*

**undo stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **bridge-diameter** [ *bridge-diameter* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Configures the diameter of a spanning tree in VLANs. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| *bridge-diameter* | Specifies the diameter. | The value is an integer that ranges from 2 to 7. The default value is 7. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a network running a spanning tree protocol, the network diameter is the maximum number of devices between two switching devices. If the network diameter is improperly set, network converge may slow down, affecting users' normal communication.The **stp vlan bridge-diameter** command can be used to set a proper network diameter based on the network scale. This helps to accelerate network convergence.The following time parameters are related to the network scale:

* Hello Time
* Forward Delay
* Max Age

**Precautions**

After the **stp vlan bridge-diameter** command is used on a switching device, the switching device will automatically set proper values for Hello Time, Forward Delay, and Max Age based on the configured network diameter.In VBST mode, the configuration of the bridge-diameter can only take effect on the root bridge.


Example
-------

# Set the diameter to 5 for VLAN 10 when VBST is running.
```
<HUAWEI> system-view
[~HUAWEI] stp vlan 10 bridge-diameter 5

```