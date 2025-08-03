Configuring a Pure EBGP Peer Group
==================================

Configuring a Pure EBGP Peer Group

#### Prerequisites

Before configuring a pure EBGP peer group, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

If multiple EBGP peers exist in an AS, adding them to an EBGP peer group can simplify the BGP4+ network configuration and management. In a pure EBGP peer group, all the peers must reside in the same AS.


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
   
   If peers already exist in a peer group, you can neither change the AS number of the peer group, nor delete the AS number of the peer group using the [**undo**](cmdqueryname=undo) command.
5. Enter the IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
6. Enable the peer group.
   
   
   ```
   [peer](cmdqueryname=peer) group-name [enable](cmdqueryname=enable)
   ```
7. Add a peer to the peer group.
   
   
   ```
   [peer](cmdqueryname=peer+group) { ipv6-address | ipv4-address } group group-name
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * You can repeat Step 7 to add multiple peers to the peer group. If the EBGP peer does not exist, the system automatically creates it in the BGP view and enables it in the IPv6 address family view.
   * To add a peer in a BGP VPN instance to a peer group in this instance, you can also run the [**peer group enable**](cmdqueryname=peer+group+enable) command. Before running this command, you need to create the peer and peer group in the VPN instance view, and then enable the peer and peer group in the BGP VPN instance address family view.
   
   When creating a pure EBGP peer group, you need to specify an AS number for it.
   
   If peers already exist in a peer group, the AS number of the peer group cannot be changed.
   
   After a peer group is created, you can configure BGP4+ functions for the peer group in batches. By default, each peer in a peer group inherits the configurations of the peer group. However, if you configure a member peer separately, the configuration of this peer will override that inherited from the peer group.
8. (Optional) Configure a description for the peer group.
   
   
   ```
   [peer](cmdqueryname=peer) group-name [description](cmdqueryname=description) description-text
   ```
   
   This configuration simplifies network management.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```