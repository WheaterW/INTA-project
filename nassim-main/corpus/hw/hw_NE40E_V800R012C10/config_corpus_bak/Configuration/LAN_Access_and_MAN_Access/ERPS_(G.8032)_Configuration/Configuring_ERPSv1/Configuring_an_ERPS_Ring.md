Configuring an ERPS Ring
========================

A ring is the basic ERPS unit. After an ERPS ring is configured, ERPS runs to block redundant links and eliminate loops on Layer 2 networks.

#### Context

Perform the following operations to configure an ERPS ring:

1. Create an ERPS ring.
2. (Optional) Configure a description for the ERPS ring. The description can contain the ERPS ring ID.
3. Configure a control VLAN for the ERPS ring. A control VLAN is different from a data VLAN that transmits service packets. On ERPS rings, a control VLAN is used to transmit Ring Auto Protection Switching (R-APS) Protocol Data Units (PDUs), also called the ERPS protocol packets. A control VLAN does not transmit service packets, enhancing ERPS security.
   
   All devices on an ERPS ring must use the same control VLAN. Different ERPS rings cannot have the same control VLAN.
4. Configure an ERP instance and map the instance to a VLAN. Ports can be added to an ERPS ring only after an ERP instance is configured for the ring. VLANs can be mapped to protection instances for load balancing.
5. Add Layer 2 ports to the ERPS rings and specify Port Role.
   
   Before adding a port to an ERPS ring, ensure that:
   * No spanning tree protocol is enabled on the port. If a spanning tree protocol has been enabled for a port, run the [**stp disable**](cmdqueryname=stp+disable) command in the interface view to disable the spanning tree protocol.
   * The port is not a Layer 3 port. If the port is a Layer 3 port, run the [**portswitch**](cmdqueryname=portswitch) command to switch the port to the Layer 2 mode.
   * A control VLAN and an ERP instance have been configured for the ERPS ring to which the port will be added.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

A ring can either has STP or ERPS enabled. If you enable ERPS, the control VLAN and data VLAN must be mapped to an Ethernet Ring Protection (ERP) instance. Otherwise, a loop may occur because STP is disabled.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**erps ring**](cmdqueryname=erps+ring) *ring-id*
   
   
   
   An ERPS ring is created, and its view is displayed.
   
   
   
   An ERPS ring can be deleted only if it does not have any port. If you attempt to delete an ERPS ring that has a port, the system prompts a deletion failure. Before deleting an ERPS ring that has a port, run the [**undo erps ring**](cmdqueryname=undo+erps+ring) command in the interface view of the port or the [**undo port**](cmdqueryname=undo+port) command in the ERPS ring view to remove the port from the ERPS ring. Then run the [**undo erps ring**](cmdqueryname=undo+erps+ring) command to delete the ERPS ring.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If only one port is added to the ERPS ring, the port is set to the Discarding state.
3. (Optional) Run [**description**](cmdqueryname=description) *text*
   
   
   
   A description is configured for the ERPS ring.
4. Run [**control-vlan**](cmdqueryname=control-vlan) *vlan-id*
   
   
   
   A control VLAN is configured for the ERPS ring.
   
   The control VLAN specified by *vlan-id* must not be one that has been created or used in Smart Link protocol, VLAN mapping, VLAN stacking, [**port trunk allow-pass**](cmdqueryname=port+trunk+allow-pass), or [**port default vlan**](cmdqueryname=port+default+vlan) applications.
   
   * The control VLAN for an ERPS ring cannot be modified after a port is added to the ring. Before deleting the control VLAN for an ERPS ring that has a port, run the [**undo erps ring**](cmdqueryname=undo+erps+ring) command in the interface view of the port or the [**undo port**](cmdqueryname=undo+port) command in the ERPS ring view to remove the port from the ERPS ring. Then run the [**undo control-vlan**](cmdqueryname=undo+control-vlan) command to delete the control VLAN.
   * If an ERPS ring does not have any port, you can run the [**control-vlan**](cmdqueryname=control-vlan) command more than once, but only the latest configuration takes effect.
   * After a control VLAN is configured, the [**vlan batch**](cmdqueryname=vlan+batch) *vlan-id1* [ **to** *vlan-id2* ] &<1-10> command, instead of the [**control-vlan**](cmdqueryname=control-vlan) command, is saved in the configuration file.
     
     After a port is added to an ERPS ring that has a control VLAN configured, the port is automatically added to the control VLAN, and the **port trunk allow-pass vlan** *vlan-id* command configuration is automatically generated in the interface view of this port in the configuration file.
5. Run [**protected-instance**](cmdqueryname=protected-instance) { **all** | { *instance-id1* [ **to** *instance-id2* ] &<1-10> } }
   
   
   
   An ERP instance is configured for the ERPS ring.
   
   
   
   If you run the [**protected-instance**](cmdqueryname=protected-instance) command for an ERPS ring several times, all the configured ERP instances take effect.
   
   ERP instances for an ERPS ring cannot be modified after a port is added to the ring. Before deleting an ERP instance for an ERPS ring that has a port, run the [**undo erps ring**](cmdqueryname=undo+erps+ring) command in the interface view of the port or the [**undo port**](cmdqueryname=undo+port) command in the ERPS ring view to remove the port from the ERPS ring. Then run the [**undo protected-instance**](cmdqueryname=undo+protected-instance) command to delete the ERP instance.
6. Perform either of the following operations to configure the mapping between the ERP instance and VLANs and ensure that the control VLAN belongs to the configured ERP instance:
   
   
   * Configure the mapping between the instance and VLANs in the MST region view.
     
     1. Run the [**stp region-configuration**](cmdqueryname=stp+region-configuration) command to enter the MST region view.
     2. Run the [**instance**](cmdqueryname=instance) *instance-id* **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> command to map VLANs to an MSTI.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A VLAN cannot be mapped to multiple MSTIs. If you map a VLAN that has already been mapped to an MSTI to another MSTI, the original mapping will be canceled.
     
     The [**vlan-mapping modulo**](cmdqueryname=vlan-mapping+modulo) *modulo* command configures the mapping between MSTIs and VLANs based on a default algorithm. However, the mapping configured using this command cannot always meet the actual demand. Therefore, running this command is not recommended.
   * Configure the mapping between the instance and VLANs in the VLAN instance view.
     
     1. Run the [**vlan instance**](cmdqueryname=vlan+instance) command to enter the VLAN instance view.
     2. Run the [**instance**](cmdqueryname=instance) *instance-id* **vlan** { *vlan-id1* [ **to** *vlan-id2* ] }&<1-10> command to map VLANs to the VLAN instance.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The [**vlan instance**](cmdqueryname=vlan+instance) and [**stp region-configuration**](cmdqueryname=stp+region-configuration) commands are mutually exclusive. If the mapping between an MSTI and VLANs has been configured in the MST region view displayed by the [**stp region-configuration**](cmdqueryname=stp+region-configuration) command, you must delete the configured mapping before using the [**vlan instance**](cmdqueryname=vlan+instance) command.
     3. (Optional) Run the [**check vlan instance mapping**](cmdqueryname=check+vlan+instance+mapping) command to check the configured mapping.
7. Run either of the following commands to add a port to an ERPS ring and specify the port role.
   
   
   * Run the [**port**](cmdqueryname=port) *interface-type interface-number* [ **rpl owner** ] command in the ERPS ring view.
   * Run the [**erps ring**](cmdqueryname=erps+ring) *ring-id* [ **rpl owner** ] command in the interface view.
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   As MAC address updates cannot be separately sent currently, configuring the direct link between two upstream nodes as the RPL is not recommended.
   
   Before changing the port role, run the [**shutdown**](cmdqueryname=shutdown) command to shut down the port. Then change the port role and run the [**undo shutdown**](cmdqueryname=undo+shutdown) command to enable the port.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.