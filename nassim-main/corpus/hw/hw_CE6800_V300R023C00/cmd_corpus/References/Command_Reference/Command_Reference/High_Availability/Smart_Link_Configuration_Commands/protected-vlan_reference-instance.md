protected-vlan reference-instance
=================================

protected-vlan reference-instance

Function
--------



The **protected-vlan reference-instance** command configures a Smart Link protection instance.

The **undo protected-vlan reference-instance** command deletes a Smart Link protection instance.



By default, all instances are Smart Link protection instances.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**protected-vlan reference-instance** { *instance-id1* [ **to** *instance-id2* ] } &<1-10>

**undo protected-vlan reference-instance** { **all** | { *instance-id1* [ **to** *instance-id2* ] } &<1-10> }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *instance-id1* | Specifies the first ID of a Smart Link load-balancing instance. | The value is an integer ranging from 0 to 48. |
| **to** | Specifies the range. | - |
| *instance-id2* | Specifies the last ID of a Smart Link load-balancing instance. | The value is an integer ranging from 0 to 48.  <endInst> must be greater than <beginInst>. <beginInst> and instance-id1 specify an instance ID range. If you do not specify to <endInst>, only one load-balancing instance with the ID <beginInst> is specified.  In one load-balance instance command, a maximum of 10 instance ID ranges can be specified using to. |
| **all** | Deletes all Smart Link load-balancing instance IDs. | - |



Views
-----

Smart Link group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a protection instance is bound to a Smart Link group, Smart Link takes effect only on packets from VLANs mapped to the protection instance. If you want packets from some VLANs to be forwarded without being influenced by Smart Link, run the protected-vlan reference-**instance** command to configure protection instances to which only the other VLANs are mapped.

**Prerequisites**

A Smart Link group has been created using the **smart-link group** command, and mappings between VLANs and an MSTI have been configured using the **instance** command in the MST domain view or VLAN instance view.

**Configuration Impact**

If the protected-vlan reference-**instance** command is run more than once, all configurations take effect.

**Precautions**

When configuring protection instances for a Smart Link group, ensure that the VLAN ranges mapped to the protection instances contain all service VLANs and the VLANs mapped to load-balancing instances. Smart Link does not take effect on packets from VLANs that are not mapped to the protection instances.After protection instances are configured, packets from VLANs that are not mapped to the protection instances may cause broadcast storms on the network.


Example
-------

# Configure protection instance 10 for the Smart Link group.
```
<HUAWEI> system-view
[~HUAWEI] stp region-configuration
[*HUAWEI-mst-region] instance 10 vlan 100
[*HUAWEI-mst-region] quit
[*HUAWEI] smart-link group 1
[*HUAWEI-smlk-group1] protected-vlan reference-instance 10

```