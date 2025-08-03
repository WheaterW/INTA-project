(Optional) Configuring a VLAN Range for Loop Detection Packets Sent by a VLAN Tag Termination Sub-interface
===========================================================================================================

Specifying the VLAN range for the loop detection packets sent by dot1q or QinQ VLAN tag termination sub-interfaces helps prevent PEs from sending detection packets with the VLAN IDs of all ranges, thereby avoiding unnecessary CPU consumption.

#### Context

Perform the following steps on PEs.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* *interface-number* command to enter the view of the Ethernet sub-interface or Eth-Trunk sub-interface used by the PE to connect to a CE.
3. (Optional) Create a user VLAN group.
   1. Run the [**vlan-group**](cmdqueryname=vlan-group) *group-id* command to create the user VLAN group.
   2. Run the [**group mode**](cmdqueryname=group+mode) { **single** | **multiple** } command to set the working mode of the VLAN group.
      
      
      * **single**: A VLAN group is considered as a user. This means that you cannot collect statistics about QinQ packets based on a VLAN or VLAN range.
      * **multiple**: Different VLANs or VLAN ranges in a VLAN group are considered as different users. This means that you can collect statistics about QinQ packets based on a VLAN or VLAN range for refined management.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the view of the Ethernet sub-interface used by the PE to connect to the user side.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Configuring a VLAN group allows you to achieve the following purposes:
   
   * Deploy QoS policies based on services or users so that higher-priority service traffic is preferentially forwarded, improving user experience.
   * View QinQ packet statistics collected based on VLAN groups to determine whether the device is working properly.
4. Configure a VLAN range for loop detection packets sent by a sub-interface.
   
   
   * Configure a VLAN range for loop detection packets sent by a dot1q VLAN tag termination sub-interface.
     1. Run the [**control-vid**](cmdqueryname=control-vid) *vid* **dot1q-termination** [ **rt-protocol** ] command to set the VLAN ID of the VLAN tag termination sub-interface and configure the sub-interface to terminate single-tagged user packets.
     2. Run the [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid) *low-pe-vid* [ **to** *high-pe-vid* ] [ **vlan-group** *group-id* ] command to configure the dot1q VLAN tag termination sub-interface to terminate packets.
     3. Run the [**loop-detect detection vid**](cmdqueryname=loop-detect+detection+vid) *low-vid* [ **to** *high-vid* ] command to configure a VLAN range for loop detection packets.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        It is recommended that the VLAN ranges of loop detection packets to be sent between the AC interfaces of two interconnected devices be equal or at least overlap.
   * Configure a VLAN range for loop detection packets sent by a QinQ VLAN tag termination sub-interface.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     1. Run the [**control-vid**](cmdqueryname=control-vid) *vid* **qinq-termination** [ **local-switch** | **rt-protocol** ] command to set the VLAN ID of the VLAN tag termination sub-interface and configure the sub-interface to terminate double-tagged user packets.
     2. Run the [**qinq termination**](cmdqueryname=qinq+termination) **pe-vid** *pe-vid* [ **to** *high-pe-vid* ] **ce-vid** *ce-vid* [ **to** *high-ce-vid* ] [ **vlan-group** *group-id* ] command to configure the sub-interface to terminate QinQ packets.
     3. Run the [**loop-detect detection pe-vid**](cmdqueryname=loop-detect+detection+pe-vid) *pe-vid* **ce-vid** *low-vid* [ **to** *high-vid* ] command to specify the range of VLANs to which the QinQ VLAN tag termination sub-interface sends loop detection packets.
        
        **pe-vid** and **ce-vid** respectively indicate the outer and inner VLAN IDs of the loop detection packets sent by the QinQ VLAN tag termination sub-interface. A QinQ VLAN tag termination sub-interface can be configured with only one outer VLAN ID.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        It is recommended that the VLAN ranges of loop detection packets to be sent between the AC interfaces of two interconnected devices be equal or at least overlap.
5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.