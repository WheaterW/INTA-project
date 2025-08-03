vlan instance
=============

vlan instance

Function
--------



The **vlan instance** command displays a VLAN instance view in which mappings between MSTIs and VLANs are configured.

The **undo vlan instance** command restores the configured mappings between MSTIs and VLANs.



By default, all VLANs in an MST region are mapped to MSTI 0.


Format
------

**vlan instance**

**undo vlan instance**


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



Mappings between instances and VLANs need to be configured on a network running a Layer 2 ring protocol. Before configuring such mappings, run the **vlan instance** command to display the VLAN instance view. This command applies to all ring protocols, facilitating configurations.



**Prerequisites**



All mappings between MSTIs and VLANs configured in the MST region view have been deleted using the undo stp region-configuration command.



**Precautions**



The vlan instance and stp region-configuration commands are manually exclusive. The **vlan-instance** command takes effect only after the MSTI-VLAN mappings configured using the stp region-configuration command are deleted.




Example
-------

# Display the VLAN instance view.
```
<HUAWEI> system-view
[~HUAWEI] vlan instance

```