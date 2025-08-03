Configuring an ERP Instance and Activating the Mapping Between the ERP Instance and a VLAN
==========================================================================================

Configuring an ERP Instance and Activating the Mapping Between the ERP Instance and a VLAN

#### Context

On a Layer 2 device running ERPS, the VLANs in which R-APS PDUs and data packets are transmitted must be mapped to an ERP instance so that ERPS forwards or blocks the packets based on blocking rules. Otherwise, the preceding packets may cause broadcast storms on the ring network, causing the network to become unavailable.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the ERPS ring view.
   
   
   ```
   [erps ring](cmdqueryname=erps+ring) ring-id
   ```
3. Create an ERP instance for the ERPS ring.
   
   
   ```
   [protected-instance](cmdqueryname=protected-instance) { all | { instance-id1 [ to instance-id2 ] } &<1-10> }
   ```
   
   By default, no ERP instance is configured for an ERPS ring.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * If the [**stp mode**](cmdqueryname=stp+mode) command has been run in the system view to set the STP working mode to VBST, the ERP instance configured using the [**protected-instance**](cmdqueryname=protected-instance) command must be a created static instance.
   * If you run the [**protected-instance**](cmdqueryname=protected-instance) command multiple times in the same ERPS ring, multiple ERP instances are configured.
   * If ports have been added to the ERPS ring, the ERP instance cannot be changed. To delete a configured ERP instance, you must run the [**undo erps ring**](cmdqueryname=undo+erps+ring) command in the interface view or the [**undo port**](cmdqueryname=undo+port) command in the ERPS ring view to remove the ports from the ERPS ring, and then run the [**undo protected-instance**](cmdqueryname=undo+protected-instance) command to delete the ERP instance.
4. Exit the ERPS ring view to enter the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Configure the mapping between the ERP instance and a VLAN.
   1. Enter the MST region view.
      
      
      ```
      [stp region-configuration](cmdqueryname=stp+region-configuration)
      ```
   2. Configure the mapping between the ERP instance and a VLAN.
      
      
      ```
      [instance](cmdqueryname=instance) instance-id vlan { vlan-id1 [ to vlan-id2 ] } &<1-10>
      ```
      
      
      
      By default, all VLANs in an MST region are mapped to instance 0.
      
      The value of the *instance-id* parameter must be the same as the value of the *instance-id* parameter specified in the [**protected-instance**](cmdqueryname=protected-instance) command.
      
      
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      * A VLAN cannot be mapped to multiple instances. If you map a VLAN that has been mapped to an instance to another instance, the original mapping is deleted.
      * The [**vlan-mapping modulo**](cmdqueryname=vlan-mapping+modulo) *modulo* command configures mappings between MSTIs and VLANs based on a default algorithm. However, the mappings configured using this command cannot meet the actual requirements. Therefore, this command is not recommended.
      * To configure the mapping between an ERP instance and a MUX VLAN, you are advised to configure the principal VLAN, group VLANs, and separate VLANs of the MUX VLAN to map the same ERP instance. Otherwise, loops may occur.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```