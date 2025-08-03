stp vlan disable
================

stp vlan disable

Function
--------



The **stp vlan disable** command disables VBST in a VLAN on the device.

The **undo stp vlan disable** command restores the default VBST status in a VLAN on the device.



By default, VBST is enabled in all VLANs on the device.


Format
------

**stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **disable**

**undo stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **to** *vlan-id* | Specifies the VLAN which is enabled or disabled. vlan-id specifies the VLAN which is enabled or disabled.   * vlan-id to vlan-id indicates the range determined by two values of vlan-id. The value of vlan-id following to must be greater than or equal to the value of vlan-id before to. * If to vlan-id is not specified, the VLAN is only enabled or disabled specified by vlan-id.   In one stp vlan disable command, a maximum of 10 VLAN ranges can be specified by using to.  The VLAN can be specified only when VBST is deployed. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a complex Layer 2 network, to prevent or eliminate loops and allow traffic in different VLANs to be forwarded along spanning trees to implement load balancing, deploy VBST on the device.Spanning tree calculation occupies system resources. Therefore, run the **stp vlan disable** command to disable VBST in a VLAN where spanning tree calculation does not need to be performed.

**Prerequisites**

When VBST is enabled on a ring network, VBST immediately starts spanning tree calculation. Parameters such as the device priority, interface priority, and interface path cost in each VLAN affect spanning tree calculation, and the change of these parameters may cause network flapping. To ensure fast and stable spanning tree calculation, perform basic configurations on the device and interfaces before enabling VBST:

* Run the **stp mode vbst** command to configure the working mode of the device.
* Run the stp vlan vlan-id [ to vlan-id ] [ vlan-id [ to vlan-id ] ] & <1-9> priority priority-value command to configure the priority of the device in a VLAN.
* Run the stp vlan vlan-id [ to vlan-id ] [ vlan-id [ to vlan-id ] ] & <1-9> port priority priority-value command to configure the priority of the interface in a VLAN.
* Run the stp vlan vlan-id [ to vlan-id ] [ vlan-id [ to vlan-id ] ] & <1-9> root primary command to configure the device as the root bridge of the specified spanning tree.
* Run the stp vlan vlan-id [ to vlan-id ] [ vlan-id [ to vlan-id ] ] & <1-9> root secondary command to configure the device as the secondary root bridge of the specified spanning tree.
* Run the stp vlan vlan-id [ to vlan-id ] [ vlan-id [ to vlan-id ] ] & <1-9> cost cost command to configure the path cost of the interface.
* Run the **instance instance-id vlan vlan-id** command to configure 1:1 mapping between instances and VLANs.Perform the configurations as required.

**Precautions**

When VBST is enabled globally and in a VLAN, the interface that belongs to the VLAN participates in spanning tree calculation. Whether the interface is in forwarding state depends on the calculation result.When VBST is disabled in a VLAN, the interface that belongs to the VLAN does not participate in spanning tree calculation and is in forwarding state in the VLAN.


Example
-------

# Disable VBST in VLAN 5.
```
<HUAWEI> system-view
[~HUAWEI] stp vlan 5 disable

```