Enabling the ETH-BN Receiving Function for a VLAN
=================================================

When routing devices connect to microwave devices, enable the ETH-BN receiving function to implement association with the microwave bandwidth.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172362112__fig_dc_vrp_y1731_cfg_007801), the RTN links form a single chain and no intermediate services are on the chain.

**Figure 1** Enabling the ETH-BN receiving function for a VLAN![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/0.


  
![](images/fig_dc_vrp_y1731_cfg_0078_01.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

When planning ETH-BN, you must check that the service burst traffic is consistent with a device's buffer capability.




#### Procedure

1. Perform the following steps on CE1.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**cfm enable**](cmdqueryname=cfm+enable)
      
      CFM is enabled.
   3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
      
      The MD view is displayed.
   4. Run [**ma**](cmdqueryname=ma) *ma-name*
      
      The MA view is displayed.
   5. Run [**map**](cmdqueryname=map) **vlan** *vlan-id*
      
      The MA is bound to a VLAN.
   6. Run either of the following commands to configure an outward-facing MEP:
      
      * To configure an outward-facing MEP on a main interface, run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number* **outward** command.
      * To configure an outward-facing MEP on a sub-interface, run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number* [ **vlan** *vlan-id* | **pe-vid** *pe-vid-value* **ce-vid** *ce-vid-value* ] **outward** command.
   7. Run [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **eth-bn** **receive** **enable**
      
      The ETH-BN receiving function is enabled.
      
      After ETH-BN packets are received from microwave devices, association with the microwave bandwidth can be automatically implemented.
   8. (Optional) Set the ETH-BN flapping suppression time.
      1. Run the [**quit**](cmdqueryname=quit) command to return to the MD view.
      2. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
      3. Run the [**cfm suppress-flapping eth-bn notify hold-time**](cmdqueryname=cfm+suppress-flapping+eth-bn+notify+hold-time) *hold-time* command to set the ETH-BN flapping suppression time.
   9. (Optional) Add the channelized and common sub-interfaces to the microwave bandwidth sharing group.
      
      When channelized and common sub-interfaces are used to carry microwave channel services on a device, you can add the sub-interfaces to a microwave bandwidth sharing group so that the channelized sub-interface bandwidth is not affected by any change in the microwave channel bandwidth.
      
      1. Run the [**eth-bn**](cmdqueryname=eth-bn) **group** *group-name* command in the system view to create a microwave bandwidth sharing group and enter the ETH-BN group view.
      2. (Optional) Run the [**description**](cmdqueryname=description) *description-info* command to configure a description for the microwave bandwidth sharing group.
      3. Run the [**quit**](cmdqueryname=quit) command to exit the ETH-BN group view.
      4. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number.sub-num* command to enter the sub-interface view.![](../../../../public_sys-resources/note_3.0-en-us.png) 
         
         Only one common sub-interface can be added to a microwave bandwidth sharing group.
      5. Run the [**eth-bn-group**](cmdqueryname=eth-bn-group) *group-name* command to add the sub-interface to the microwave bandwidth sharing group.
      6. Run the [**quit**](cmdqueryname=quit) command to exit the sub-interface view.
   10. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.