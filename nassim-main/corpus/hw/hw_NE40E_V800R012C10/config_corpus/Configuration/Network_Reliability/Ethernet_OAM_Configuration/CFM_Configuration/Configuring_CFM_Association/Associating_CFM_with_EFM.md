Associating CFM with EFM
========================

This section describes how to associate connectivity fault management (CFM) with Ethernet in the First Mile (EFM).

#### Context

CFM on the network side can be associated with EFM on the user side to detect faults, ensuring service reliability. With this association, when EFM or CFM detects a link fault, it instructs the Manager (MGR) module to notify the other mechanism of the fault. The association can be unidirectional or bidirectional. For details about this association, see [Overview of CFM](dc_vrp_cfm_cfg_000002.html).

Association between EFM and CFM is bidirectional.

* When EFM detects a link fault, it will notify CFM of the fault.
* When CFM detects a link fault, it will notify EFM of the fault.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**oam-mgr**](cmdqueryname=oam-mgr)
   
   
   
   The operation, administration and maintenance (OAM) management view is displayed.
3. Configure the association depending on the usage scenario:
   
   
   * Unidirectional association
     
     To enable EFM to instruct the MGR module to notify CFM of a fault, run the [**oam-bind ingress efm interface**](cmdqueryname=oam-bind+ingress+efm+interface) *interface-type* *interface-number* **egress** **cfm** **md** *md-name* **ma** *ma-name* command.
     
     To enable CFM to instruct the MGR module to notify EFM of a fault, run the [**oam-bind ingress cfm md**](cmdqueryname=oam-bind+ingress+cfm+md) *md-name* **ma** *ma-name* **egress** **efm** **interface** *interface-type* *interface-number* command.
   * Bidirectional association
     
     To enable both CFM and EFM to instruct the MGR module to notify each other of a fault, run the [**oam-bind cfm md**](cmdqueryname=oam-bind+cfm+md) *md-name* **ma** *ma-name* **efm** **interface** *interface-type* *interface-number* command.
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can also run both of the commands used for unidirectional association to configure bidirectional association.
   
   If the [**oam-bind cfm md**](cmdqueryname=oam-bind+cfm+md) *md-name* **ma** *ma-name* **efm** **interface** *interface-type* *interface-number* command is run, the [**oam-bind ingress efm interface**](cmdqueryname=oam-bind+ingress+efm+interface) *interface-type* *interface-number* **egress** **cfm** **md** *md-name* **ma** *ma-name* and [**oam-bind ingress cfm md**](cmdqueryname=oam-bind+ingress+cfm+md) *md-name* **ma** *ma-name* **egress** **efm** **interface** *interface-type* *interface-number* commands are displayed in the configuration file.
   
   After CFM is associated with EFM, note the following points:
   
   * If EFM is disabled on an interface, the association between CFM and EFM is deleted.
   * If a maintenance association (MA) or maintenance domain (MD) is deleted, the association between CFM and EFM is deleted.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.