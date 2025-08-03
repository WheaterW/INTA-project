Configuring a Pure EBGP Peer Group
==================================

Configuring a Pure EBGP Peer Group

#### Prerequisites

Before configuring a pure EBGP peer group, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

If multiple EBGP peers exist in an AS, adding them to an EBGP peer group can simplify the BGP network configuration and management. In a pure EBGP peer group, all the peers must reside in the same AS.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Create an EBGP peer group.
   
   
   ```
   [group](cmdqueryname=group+external) group-name external
   ```
4. Specify an AS number for the peer group.
   
   
   ```
   [peer](cmdqueryname=peer+as-number) group-name as-number as-number
   ```
   
   If peers already exist in a peer group, the AS number of the peer group cannot be changed.
5. Add a peer to the peer group.
   
   
   ```
   [peer](cmdqueryname=peer+group)  { ipv4-address | ipv6-address } group group-name
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * You can repeat Step 5 to add multiple peers to the peer group. If the specified peer has not been created yet, the system automatically creates it in the BGP view and sets the AS number of the peer to that of the peer group.
   * To add a peer in a BGP VPN instance to a peer group in this instance, you can also run the [**peer group enable**](cmdqueryname=peer+group+enable) command. Before running this command, you need to create the peer and peer group in the VPN instance view, and then enable the peer and peer group in the BGP VPN instance address family view.
   
   After a peer group is created, you can configure BGP functions for the peer group in batches. By default, each peer in a peer group inherits the configurations of the peer group. However, if you configure a member peer separately, the configuration of this peer will override that inherited from the peer group.
6. (Optional) Configure a description for the peer group.
   
   
   ```
   [peer](cmdqueryname=peer) group-name [description](cmdqueryname=description) description-text
   ```
   
   This configuration simplifies network management.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```