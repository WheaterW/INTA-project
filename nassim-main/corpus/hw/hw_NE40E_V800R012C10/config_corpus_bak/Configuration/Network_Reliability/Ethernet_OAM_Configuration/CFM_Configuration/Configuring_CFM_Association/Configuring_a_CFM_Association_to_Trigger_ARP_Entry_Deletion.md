Configuring a CFM Association to Trigger ARP Entry Deletion
===========================================================

If CFM detects a link fault, it notifies the OAM management module. Upon receipt of the notification, the OAM management module deletes ARP entries mapped to the link and triggers link switching.

#### Usage Scenario

[Figure 1](#EN-US_TASK_0172361959__fig_038CC0A1) illustrates the networking for a CFM association to trigger ARP entry deletion if link faults are detected.

1. CE2 is dual-homed to PE2a and PE2b. CFM is configured to monitor the link between CE2 and PE2a and that between CE2 and PE2b. A CFM association is configured on CE2 to trigger ARP entry deletion if CFM detects link faults.
2. VLL FRR is configured for the link between PE1 and PE2a and that between PE1 and PE2b. An association between CFM and VLL FRR is configured on PE2a and PE2b.

**Figure 1** CFM association that triggers ARP entry deletion  
![](images/fig_dc_vrp_cfm_cfg_00002801.png "Click to enlarge")

#### Pre-configuration Tasks

Before configuring a CFM association to trigger ARP entry deletion, complete the following tasks:

* [Configure basic CFM functions.](dc_vrp_cfm_cfg_000004.html)
* Configure VLL FRR.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**cfm**](cmdqueryname=cfm) **md** *md-name* **ma** *ma-name* **trigger clear-arp** [ **vlan** *vlan-id* ]
   
   
   
   A CFM association is configured to trigger ARP entry deletion.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.