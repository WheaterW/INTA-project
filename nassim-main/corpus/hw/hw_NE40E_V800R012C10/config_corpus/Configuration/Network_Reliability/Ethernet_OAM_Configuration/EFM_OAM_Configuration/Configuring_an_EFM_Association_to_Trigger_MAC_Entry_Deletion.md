Configuring an EFM Association to Trigger MAC Entry Deletion
============================================================

An EFM association can be configured on a CE interface connected to a PE to trigger MAC entry deletion. This function allows the CE to use EFM to detect faults in VLL PW to a PE and to delete the MAC address entry for the PE to trigger PW switching.

#### Usage Scenario

[Figure 1](#EN-US_TASK_0172362031__fig_038CC0A1) illustrates the networking for an EFM association to trigger MAC entry deletion if link faults are detected.

1. CE2 is dual-homed to PE2a and PE2b. EFM is configured to monitor the link between CE2 and PE2a and that between CE2 and PE2b. An EFM association is configured on CE2 to trigger MAC entry deletion if EFM detects link faults.
2. VLL FRR is configured for the link between PE1 and PE2a and that between PE1 and PE2b. An association between EFM and VLL FRR is configured on PE2a and PE2b.

**Figure 1** EFM association that triggers MAC entry deletion  
![](images/fig_dc_vrp_efm_cfg_203501.png "Click to enlarge")

#### Pre-configuration Tasks

Before configuring an EFM association to trigger MAC entry deletion, complete the following tasks:

* [Configure basic EFM functions.](dc_vrp_efm_cfg_2003.html)
* Configure VLL FRR.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**efm trigger mac-renew**](cmdqueryname=efm+trigger+mac-renew)
   
   
   
   An EFM association is configured to trigger MAC entry deletion.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.