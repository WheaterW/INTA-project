Associating CFM with an Interface
=================================

This section describes how to associate connectivity fault management (CFM) with an interface.

#### Context

When a link fault, threshold-crossing event, or remote fault occurs, CFM can be associated with an interface to detect faults. As shown in [Figure 1](#EN-US_TASK_0172361951__fig_dc_vrp_cfm_cfg_00001501), CE1 is dual-homed to PE1 and PE2 over the primary and backup links. The dual-homing topology provides device redundancy and improves network robustness and service reliability. To check link continuity, deploy CFM on CE1 and PE1.

If CFM has been associated with Port1 and detects a fault in the link between CE1 and PE1, CFM instructs the Manager (MGR) module to intermittently disconnect Port1. In this manner, other modules can detect the fault. Traffic is then switched from the primary link to the backup link.

**Figure 1** CFM association with an interface  
![](images/fig_dc_vrp_cfm_cfg_00001501.png)

#### Pre-configuration Tasks

Before associating CFM with an interface, configure basic CFM functions.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface at one end of the link is displayed.
3. Associate CFM with an interface.
   * Run [**cfm**](cmdqueryname=cfm) **md** *md-name* **ma** *ma-name* **remote-mep** **mep-id** *mep-id* **trigger** **if-down**
     
     CFM is associated with the interface's flapping.
     
     If a MEP detects a connectivity fault between the MEP and a specified RMEP within the same MA, the OAM module blocks and later unblocks the interface on which the MEP resides so that other modules can also detect the fault.
   * Run [**cfm**](cmdqueryname=cfm) **md** *md-name* **ma** *ma-name* **remote-mep** **mep-id** *mep-id* **trigger** **if-link-down**
     
     CFM is associated with the interface's down status.
     
     The OAM module disables the interface's down status if the MEP in a specified MA detects a fault between itself and the RMEP.
     
     If CFM goes down, the associated member interface goes down and service traffic except CFM traffic is blocked. CFM detection continues. If the link is restored, the member interface goes up.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**cfm trigger if-link-down**](cmdqueryname=cfm+trigger+if-link-down) and [**cfm trigger if-down**](cmdqueryname=cfm+trigger+if-down) commands are mutually exclusive in the same interface view.
4. (Optional) Run [**port-link enable**](cmdqueryname=port-link+enable) **mep** **mep-id** *mep-id* [ **holdoff** *holdoff-time* ] [ **wtr** *wtr-time* ] [ **link-type** { **loc** | **interface-status-tlv** } \* ]
   
   
   
   Association between an interface and CFM is enabled on a specified MEP.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.