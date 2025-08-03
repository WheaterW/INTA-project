load-balance instance slave
===========================

load-balance instance slave

Function
--------



The **load-balance instance slave** command configures a load balancing instance for a Smart Link group.

The **undo load-balance instance slave** command deletes a load balancing instance from a Smart Link group.



By default, no load-balancing instance is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**load-balance instance** { *instance-id1* [ **to** *instance-id2* ] } &<1-10> **slave**

**undo load-balance instance** { **all** | { *instance-id1* [ **to** *instance-id2* ] } &<1-10> [ **slave** ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *instance-id1* | Specifies the first ID of a Smart Link load-balancing instance. | The value is an integer ranging from 0 to 48. |
| **to** | Specifies the range. | - |
| *instance-id2* | Specifies the last ID of a Smart Link load-balancing instance. | The value is an integer ranging from 0 to 48.  The value of <instance-id2> must be greater than the value of <instance-id1>. <instance-id2> and <instance-id1> specify a range of VLANs. If to <instance-id2> is not specified, only the load balancing instance specified by <instance-id1> is specified.  In one load-balance instance command, a maximum of 10 instance ranges can be specified using to. |
| **slave** | Specifies that packets from the Smart Link load-balancing instance are sent through the slave interface. | - |
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

* If Smart Link load balancing is not configured in a Smart Link group, the primary link forwards traffic, and the secondary link is idle in most cases.
* To improve link utilization, you can configure Smart Link load balancing. When the primary and secondary links in a Smart Link are both Up, traffic from the VLANs bound to a specified MSTI is forwarded only along the secondary link, and traffic from other VLANs is forwarded along the primary link. This configuration achieves load balancing between the primary and secondary links.
* Smart Link uses MSTIs. An MSTI is bound to multiple VLANs, but a VLAN can be bound to only one MSTI. MSTIs are bound to the secondary link in a Smart Link group to implement load balancing.

**Prerequisites**

A Smart Link group has been created using the **smart-link group** command, and mappings between VLANs and an MSTI have been configured using the **instance** command in the MST domain view or VLAN instance view.

**Configuration Impact**

If the load-balance **instance** command is run more than once, all configurations take effect.

**Follow-up Procedure**

Run the **display smart-link group** command to view the load balancing mode in the Smart Link group.

**Precautions**

A VLAN that is bound to a load-balancing instance cannot be configured as the control VLAN of sent Flush packets.


Example
-------

# Configure load balancing for Smart Link group 3 and bind MSTI 1 to the secondary link so that traffic from VLANs bound to MSTI 1 is forwarded along the secondary link.
```
<HUAWEI> system-view
[~HUAWEI] stp region-configuration
[*HUAWEI-mst-region] instance 1 vlan 10
[*HUAWEI-mst-region] quit
[*HUAWEI] smart-link group 3
[*HUAWEI-smlk-group3] load-balance instance 1 slave

```