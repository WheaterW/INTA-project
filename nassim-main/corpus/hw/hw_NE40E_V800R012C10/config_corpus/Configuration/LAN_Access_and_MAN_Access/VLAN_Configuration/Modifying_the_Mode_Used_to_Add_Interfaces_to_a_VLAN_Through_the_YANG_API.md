Modifying the Mode Used to Add Interfaces to a VLAN Through the YANG API
========================================================================

Modify the mode used to add interfaces to a VLAN through the YANG API according to site requirements.

#### Usage Scenario

You can add trunk or hybrid interfaces to a VLAN through the YANG API using either of the following modes:

* VLAN range mode (used by default). It features good performance and is easy to use for VLAN query and configuration. However, this mode cannot be used for incremental configuration delivery when some third-party NMSs are involved.
* Leaf-list mode. It has poor performance, and its efficiency decreases as the number of VLANs increases. However, it supports incremental configuration delivery when some third-party NMSs are involved.

Determine whether to use this mode based on site requirements.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ethernet yang-mode trunk-vlan vlan-id-list**](cmdqueryname=ethernet+yang-mode+trunk-vlan+vlan-id-list)
   
   
   
   The default VLAN range mode is switched to the leaf-list mode.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check whether the mode is successfully switched.