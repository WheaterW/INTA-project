Configuring an IBGP Peer Group
==============================

Configuring an IBGP Peer Group

#### Prerequisites

Before configuring an IBGP peer group, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

If multiple IBGP peers exist, adding them to an IBGP peer group can simplify the BGP network configuration and management. When configuring an IBGP peer group, you do not need to specify an AS number. Instead, the local AS number is used for the peer group.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Create an IBGP peer group.
   
   
   ```
   [group](cmdqueryname=group+internal) group-name internal
   ```
4. Add a peer to the peer group.
   
   
   ```
   [peer](cmdqueryname=peer+group) { ipv4-address | ipv6-address } group group-name
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * You can repeat Step 4 to add multiple peers to the peer group. If the specified peer has not been created yet, the system automatically creates it in the BGP view and sets the AS number of the peer to that of the peer group.
   * To add a peer in a BGP VPN instance to a peer group in this instance, you can also run the **peer group enable** command. Before running this command, you need to create the peer and peer group in the VPN instance view, and then enable the peer and peer group in the BGP VPN instance address family view.
   
   When creating an IBGP peer group, you do not need to specify an AS number for it.
   
   You can configure BGP functions after configuring a peer group, and these will take effect for each peer in the group. By default, each peer in a peer group inherits the configurations of the peer group. However, if you configure a member peer separately, the configuration of this peer will override that inherited from the peer group.
5. (Optional) Configure a description for the peer group.
   
   
   ```
   [peer](cmdqueryname=peer) group-name [description](cmdqueryname=description) description-text
   ```
   
   This configuration simplifies network management.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```