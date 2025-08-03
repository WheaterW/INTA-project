Associating CFM with CFM
========================

If CFM is deployed at both sides, association between CFM and CFM can be configured. This allows CFM and CFM to notify each other of faults and ensures reliable service transmission.

#### Context

For details on the principles and usage scenarios of association between CFM and CFM, see [Overview of CFM](dc_vrp_cfm_cfg_000002.html).

Association between CFM and CFM is bidirectional. The details are as follows:

* When the user-side CFM detects a link fault, it will notify the network-side CFM of the fault.
* When the network-side CFM detects a link fault, it will notify the user-side CFM of the fault.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**oam-mgr**](cmdqueryname=oam-mgr)
   
   
   
   The OAM management view is displayed.
3. Perform either of the following configurations as required.
   
   
   
   **Table 1** Association between the CFM and CFM modules
   | Scenario | Configuration Solution 1 |
   | --- | --- |
   | Bidirectional fault information advertisement between the CFM modules | Run the following commands to allow CFM modules to notify each other of faults: * Run the [**oam-bind ingress cfm md**](cmdqueryname=oam-bind+ingress+cfm+md) *md-name1* **ma** *ma-name1* **egress** **cfm** **md** *md-name2* **ma** *ma-name2* command. **ingress** [**md**](cmdqueryname=md) *md-name1* specifies an MD name and **ma** *ma-name1* specifies an MA name on one end of the link. **egress** **md** *md-name2* specifies an MD name and **ma** *ma-name2* specifies an MA name on the other end of the link. * Run the [**oam-bind ingress cfm md**](cmdqueryname=oam-bind+ingress+cfm+md) *md-name1* **ma** *ma-name1* **egress** **cfm** **md** *md-name2* **ma** *ma-name2* command. **ingress** [**md**](cmdqueryname=md) *md-name1* specifies an MD name and **ma** *ma-name1* specifies an MA name, which are used on one end of the link. **egress** **md** *md-name2* specifies an MD name and **ma** *ma-name2* specifies an MA name on the other end of the link. |
   | Unidirectional fault information advertisement between the CFM modules | Run either of the following commands: * Run the [**oam-bind ingress cfm md**](cmdqueryname=oam-bind+ingress+cfm+md) *md-name1* **ma** *ma-name1* **egress** **cfm** **md** *md-name2* **ma** *ma-name2* command. **ingress** [**md**](cmdqueryname=md) *md-name1* **ma** *ma-name1* specifies the MD and MA names, which are used for the link on the left side of the device. **egress** **md** *md-name2* **ma** *ma-name2* specifies the MD and MA names, which are used for the link on the right side of the device. After CFM that monitors the link on the left side of the device detects a fault, it notifies CFM that monitors the link on the right side of the device. * Run the [**oam-bind ingress cfm md**](cmdqueryname=oam-bind+ingress+cfm+md) *md-name1* **ma** *ma-name1* **egress** **cfm** **md** *md-name2* **ma** *ma-name2* command. **ingress** [**md**](cmdqueryname=md) *md-name1* **ma** *ma-name1* specifies the MD and MA names, which are used for the link on the right side of the device. **egress** **md** *md-name2* **ma** *ma-name2* specifies the MD and MA names, which are used for the link on the left side of the device. After CFM that monitors the link on the right side of the device detects a fault, it notifies CFM that monitors the link on the left side of the device. |
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can also run both of the commands used for unidirectional association to configure bidirectional association.
   
   After CFM is associated with other functional modules, note the following:
   
   * If CFM is disabled on an interface, the association between CFM and other functional modules is deleted.
   * If an MA or MD is deleted, the association between CFM and other functional modules is deleted.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.