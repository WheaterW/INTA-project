Configuring OAM Mapping
=======================

This section describes how to configure OAM mapping. When an intermediary such as a switch exists between a PE and a CE, you can configure OAM mapping to associate the OAM status on an AC interface with the PW status.

#### Usage Scenario

When the AC interface bound to a VPLS changes, a PE sends an LDP MAC-Withdraw message to its peer. On the network shown in [Figure 1](#EN-US_TASK_0172370209__fig_dc_vrp_vpls_cfg_605501), an intermediate device exists between CE1 and PE1, and another intermediate device exists between CE1 and PE2. When CE1's interface goes down, PE1's AC interface that connects to CE1 does not go down immediately. As a result, PE1 does not immediately send an LDP MAC-Withdraw message to PE3, causing the downstream traffic from PE3 to PE1 to be lost. To prevent this problem, you can configure OAM mapping on CE1, PE1, and PE2 so that OAM monitors the links between the CE and PEs and the OAM status is associated with the PW status. When CE1's interface goes down, a primary/secondary PW switchover can be rapidly performed.

**Figure 1** Configuring OAM mapping for a VPLS network  
![](images/fig_dc_vrp_vpls_cfg_605501.png)  


#### Pre-configuration Tasks

Before configuring OAM mapping, complete the following tasks:

* Configure PWs between PE1, PE2, and PE3.
* Configure OAM on CE1, PE1, and PE2.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The AC interface view is displayed.
3. Run [**mpls l2vpn oam-mapping**](cmdqueryname=mpls+l2vpn+oam-mapping) **1ag** **md** *md-name* **ma** *ma-name*
   
   
   
   The OAM status on the AC interface is associated with the PW status.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If **1ag** is not configured, this command applies only to low-speed interfaces.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring OAM mapping, verify the configuration using the following commands:

* Run the [**display vsi**](cmdqueryname=display+vsi) **name** *vsi-name* **oam-mapping** command to check information about the AC interface with OAM mapping configured.
* Run the [**display vsi**](cmdqueryname=display+vsi) **name** *vsi-name* **statistics** command to check VSI statistics, such as the PWs and AC interfaces in different states.