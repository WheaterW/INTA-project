Assigning an IP Address to a VLANIF Interface
=============================================

As a VLANIF interface is a Layer 3 logical interface, it can communicate with other interfaces at the network layer only after being assigned an IP address.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **vlanif** *vlan-id*
   
   
   
   The VLANIF interface view is displayed.
   
   
   
   The VLAN ID specified in this command must be the ID of an existing VLAN.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
   
   
   
   An IP address is assigned to the VLANIF interface for communication at the network layer.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If IP addresses assigned to VLANIF interfaces on a Layer 3 device belong to different network segments, a routing protocol must be configured on the Layer 3 switch to provide reachable routes. Otherwise, VLANIF interfaces cannot communicate with each other at the network layer. For configurations of routing protocols, see the *NE40E Configuration Guide - IP Routing*.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

To disable all users in a VLAN from communicating with users in other VLANs through a VLANIF interface, whereas communication is available between users within the VLAN, run the [**shutdown**](cmdqueryname=shutdown) command in the VLANIF interface view.

Both Layer 2 and Layer 3 traffic is transmitted over the VLANIF interface. Running the [**shutdown**](cmdqueryname=shutdown) command in the VLANIF interface view prohibits only Layer 3 traffic. After running the [**display interface**](cmdqueryname=display+interface) **vlanif** command, you can view that traffic statistics still increase on this VLANIF interface.

To prohibit all traffic on the VLANIF interface, run the [**shutdown vlan**](cmdqueryname=shutdown+vlan) command in the VLANIF interface view.