(Optional) Configuring IGMP
===========================

Configuring IGMP on the interfaces connecting a multicast device to a user network segment allows the device to manage multicast group members on that network segment.

#### Context

IGMP is a protocol in the TCP/IP protocol suite, and is used to establish and maintain IPv4 multicast group memberships between IP hosts and directly neighboring multicast routers.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
   
   
   
   The interface specified in *interface-type* *interface-number* must be the interface connected to a host.
3. Run the [**pim sm**](cmdqueryname=pim+sm) command to enable PIM-SM.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the current version, mLDP signaling can transmit only PIM-SM/PIM-SSM (S, G) Join messages.
4. Run the [**igmp enable**](cmdqueryname=igmp+enable) command to enable IGMP.
5. Run the [**igmp version**](cmdqueryname=igmp+version) *3* command to set the IGMP version to IGMPv3.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Follow-up Procedure

Configure static multicast groups or the range of multicast groups that interfaces are allowed to join. For configuration details, see IGMP Configuration.