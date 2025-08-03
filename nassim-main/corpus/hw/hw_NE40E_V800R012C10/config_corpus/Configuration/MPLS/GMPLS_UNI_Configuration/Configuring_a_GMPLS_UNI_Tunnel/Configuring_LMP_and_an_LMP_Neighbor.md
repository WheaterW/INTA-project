Configuring LMP and an LMP Neighbor
===================================

LMP and an LMP neighbor are configured on an edge node on a transport network and an IP network to manage the data and control channels and detect link connectivity.

#### Context

GMPLS uses LMP to manage links of the control and data channels. LMP is classified into the following types:

* Static LMP: LMP neighbors, control channels, and data channels are manually configured, without exchanging LMP packets.
* Dynamic LMP: LMP neighbors, control channels, and data channels are all automatically discovered, which minimizes configurations and speeds up network deployment.

Currently, the NE40E supports only static LMP. Perform the following steps to configure LMP and a neighbor on an edge node:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**lmp**](cmdqueryname=lmp)
   
   
   
   The LMP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *name*
   
   
   
   An LMP neighbor is created, and its view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The neighbor of an IP network edge node is a transport network edge node that directly connects to the IP network edge node. This means that LMP neighbor relationships are created between the ingress EN and ingress CN, and between the egress EN and egress CN.
4. Run [**lmp static**](cmdqueryname=lmp+static)
   
   
   
   The working mode of an LMP neighbor is set to static LMP.
5. Run [**node-id**](cmdqueryname=node-id) *ip-address*
   
   
   
   An IP address is assigned to the LMP neighbor.
   
   The ingress EN's LMP neighbor is the ingress CN on an optical network, and the egress EN's LMP neighbor is the egress CN on the optical network. The *ip-address* parameter is set to the node ID of the ingress CN or egress CN.
6. Run [**te-link**](cmdqueryname=te-link) *te-link-id*
   
   
   
   A TE-link is configured between the neighbors, and the TE-link view is displayed.
   
   
   
   A TE-link is a bundle of data-links that directly connected LMP neighbors.
7. Run [**link-id**](cmdqueryname=link-id+local+ip) **local ip** *local-ip-value*
   
   
   
   A local TE-link ID is set.
8. Run [**link-id**](cmdqueryname=link-id+remote+ip) **remote ip** *remote-ip-value*
   
   
   
   A remote TE-link ID is set.
9. Run [**data-link**](cmdqueryname=data-link+interface+local+interface-id+remote+interface-id) **interface** { **interface-name** | *interface-type* *interface-number* } **local interface-id** **loccalIpAddr** ****remote**** ****interface-id**** **remoteIpAddr**
   
   
   
   A data-link is configured for the TE-link.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.