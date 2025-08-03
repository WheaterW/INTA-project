Configuring a CFM Association to Trigger MAC Entry Deletion
===========================================================

If CFM detects link faults, it notifies a node. Upon receipt of the notification, the node deletes MAC entries within the configured VLAN range and triggers link switching.

#### Usage Scenario

[Figure 1](#EN-US_TASK_0172361962__fig_038CC0A1) illustrates the networking for a CFM association to trigger MAC entry deletion if link faults are detected.

1. CE2 is dual-homed to PE2a and PE2b. CFM is configured to monitor the link between CE2 and PE2a and that between CE2 and PE2b. A CFM association is configured on CE2 to trigger MAC entry deletion if CFM detects link faults.
2. VLL FRR is configured for the link between PE1 and PE2a and that between PE1 and PE2b. An association between CFM and VLL FRR is configured on PE2a and PE2b.

**Figure 1** CFM association that triggers MAC entry deletion  
![](figure/en-us_image_0000001801062877.png "Click to enlarge")

#### Pre-configuration Tasks

Before configuring a CFM association to trigger MAC entry deletion, complete the following tasks:

* [Configure basic CFM functions.](dc_vrp_cfm_cfg_000004.html)
* Configure VLL FRR.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cfm trigger vlan**](cmdqueryname=cfm+trigger+vlan) { *vlanBng* [ **to** *vlanEnd* ] } &<1-10> **mac-renew**
   
   
   
   A CFM association is configured to trigger MAC entry deletion.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.