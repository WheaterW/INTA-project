(Optional) Configuring IGMP Message Replication
===============================================

By default, the IGMP message replication function is enabled. When a DHCP STB is dual-homed to master and backup routers, IGMP message replication can be disabled to reduce resource consumption.

#### Context

In a multicast hot backup scenario, if a DHCP STB connects to the master and backup routers over links in a smart link group, over an E-Trunk, or over VLL PWs, the access-side link status does not change with the network-side link status. If the network-side primary link fails and the secondary link becomes active, the access network cannot detect the network-side link status change. The DHCP STB continues to send IGMP messages to the master router, causing packet loss. To resolve this issue,
IGMP message replication can be enabled. This allows the master router to replicate IGMP messages for the backup router. The backup router can then create forwarding entries based on the received IGMP messages and rapidly implement on-demand data forwarding.

If a DHCP STB is dual-homed to the master and backup routers, both the routers can receive IGMP messages, without the need of IGMP message replication. In this situation, IGMP message replication can be disabled to reduce system resource consumption.

The IGMP messages sent by a PPPoE terminal can arrive only at a single router. The master and backup routers have to keep replicating IGMP messages. Neither the [**dhcp-stb igmp-copy**](cmdqueryname=dhcp-stb+igmp-copy) nor [**undo dhcp-stb igmp-copy**](cmdqueryname=undo+dhcp-stb+igmp-copy) command needs to be executed.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
   
   
   
   The RBP view is displayed.
3. Run [**undo dhcp-stb igmp-copy**](cmdqueryname=undo+dhcp-stb+igmp-copy)
   
   
   
   IGMP message replication is disabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the [**undo dhcp-stb igmp-copy**](cmdqueryname=undo+dhcp-stb+igmp-copy) command is run, the system stops replicating IGMP messages from a DHCP STB. However, the IGMP messages that have been replicated are not affected.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.