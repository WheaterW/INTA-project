Creating a Mixed EBGP Peer Group
================================

If multiple EBGP peers exist in different ASs, adding them to a mixed EBGP peer group can simplify the BGP network configuration and management. When creating a mixed EBGP peer group, specify an AS number for each peer.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**group**](cmdqueryname=group+external) *group-name* **external**
   
   
   
   An EBGP peer group is created.
4. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number*
   
   
   
   A peer is created, and an AS number is set for this peer.
5. Run [**peer**](cmdqueryname=peer+group) *ipv4-address* **group** *group-name*
   
   
   
   A peer is added to the peer group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * You can repeat Steps 4 and 5 to add multiple peers to the peer group.
   * To add a peer in a BGP VPN instance to a peer group in this instance, you can also run the [**peer group enable**](cmdqueryname=peer+group+enable) command. Before running this command, you need to create the peer and peer group in the VPN instance view, and then enable the peer and peer group in the BGP VPN instance address family view.
   
   You need to specify an AS number for each peer in a mixed EBGP peer group.
   
   After a peer group is created, you can configure BGP functions for the peer group in batches. By default, each peer in a peer group inherits the configurations of the peer group. If a peer is configured separately, its configurations override those inherited from the peer group.
6. (Optional) Run [**peer**](cmdqueryname=peer+description) *group-name* [**description**](cmdqueryname=description) *description-text*
   
   
   
   A description is configured for the peer group.
   
   You can simplify network management by configuring a description.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.