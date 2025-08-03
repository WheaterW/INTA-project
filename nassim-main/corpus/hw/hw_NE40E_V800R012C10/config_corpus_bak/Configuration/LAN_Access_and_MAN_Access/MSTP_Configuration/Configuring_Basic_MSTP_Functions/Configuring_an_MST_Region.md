Configuring an MST Region
=========================

Multiple Spanning Tree Protocol (MSTP) divides a switching network into multiple MST regions. After an MST region name, VLAN-to-Multiple Spanning Tree Instance (MSTI) mapping, and MSTP revision level are configured, MST region configuration is complete.

#### Context

An MST region contains multiple devices and network segments between them. These devices are directly connected and have the same region name, same VLAN-to-MSTI mapping configuration, and same revision level configuration after MSTP is enabled. One switching network can have multiple MST regions and multiple devices can be grouped into one MST region by using MSTP configuration commands.

![](../../../../public_sys-resources/note_3.0-en-us.png) Two devices belong to the same MST region when they have the same:

* Name of the MST region
* Mapping between VLANs and MSTIs
* Revision level of the MST region

Do as follows on a device that needs to join an MST region:


#### Procedure

* Configure the name of the MST region.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**stp region-configuration**](cmdqueryname=stp+region-configuration)
     
     
     
     The MST region view is displayed.
  3. Run [**region-name**](cmdqueryname=region-name) *name*
     
     
     
     A name is configured for the MST region.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure mappings between MSTIs and VLANs.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  You can configure mappings between MSTIs and VLANs in the MST region view or in the VLAN instance view.
  
  Configure mappings between MSTIs and VLANs in the MST region view.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**stp region-configuration**](cmdqueryname=stp+region-configuration)
     
     
     
     The MST region view is displayed.
  3. Run [**instance**](cmdqueryname=instance) *instance-id* **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>
     
     
     
     Mappings between an MSTI and VLANs are configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A VLAN cannot be mapped to multiple MSTIs. If you map a VLAN that is already mapped to an MSTI, to another MSTI, the original mapping will be canceled.
     
     The [**vlan-mapping modulo**](cmdqueryname=vlan-mapping+modulo) **modulo** command configures mappings between MSTIs and VLANs based on a default algorithm. However, the mappings configured using this command cannot always meet the actual demand. Exercise caution when using this command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  
  
  Configure mappings between MSTIs and VLANs in the VLAN instance view.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vlan instance**](cmdqueryname=vlan+instance)
     
     
     
     The VLAN instance view is displayed.
  3. Run [**instance**](cmdqueryname=instance) *instance-id* **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>
     
     
     
     Mappings between an MSTI and VLANs are configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Do not run both the [**vlan instance**](cmdqueryname=vlan+instance) command and the [**stp region-configuration**](cmdqueryname=stp+region-configuration) command on the same device. If mappings between MSTIs and VLANs have been configured in the MST region view displayed by the [**stp region-configuration**](cmdqueryname=stp+region-configuration) command, you must delete the configured mappings before using the [**vlan instance**](cmdqueryname=vlan+instance) command.
  4. (Optional) Run [**check vlan instance mapping**](cmdqueryname=check+vlan+instance+mapping)
     
     
     
     The mappings between MSTIs and VLANs are checked.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure the revision level of the MST region.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**stp region-configuration**](cmdqueryname=stp+region-configuration)
     
     
     
     The MST region view is displayed.
  3. Run [**revision-level**](cmdqueryname=revision-level) *level*
     
     
     
     The MSTP revision level of the MST region is configured.
     
     
     
     To modify the MSTP revision level of the MST region to which the device belongs, run this command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.