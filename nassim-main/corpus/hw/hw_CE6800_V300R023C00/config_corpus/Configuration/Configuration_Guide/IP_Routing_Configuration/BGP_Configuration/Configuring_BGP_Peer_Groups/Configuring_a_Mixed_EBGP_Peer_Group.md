Configuring a Mixed EBGP Peer Group
===================================

Configuring a Mixed EBGP Peer Group

#### Prerequisites

Before configuring a mixed EBGP peer group, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

If multiple EBGP peers exist in different ASs, adding them to a mixed EBGP peer group can simplify the BGP network configuration and management. When configuring a mixed EBGP peer group, you need to specify an AS number for each peer.


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
4. Specify the IP address of a peer and the number of the AS where the peer resides.
   
   
   ```
   [peer](cmdqueryname=peer+as-number) ipv4-address as-number as-number
   ```
5. Add the peer to the peer group.
   
   
   ```
   [peer](cmdqueryname=peer+group)  { ipv4-address | ipv6-address } group group-name
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * You can repeat Steps 4 and 5 to add multiple peers to the peer group.
   * To add a peer in a BGP VPN instance to a peer group in this instance, you can also run the [**peer group enable**](cmdqueryname=peer+group+enable) command. Before running this command, you need to create the peer and peer group in the VPN instance view, and then enable the peer and peer group in the BGP VPN instance address family view.
   
   You need to specify an AS number for each peer in a mixed EBGP peer group.
   
   You can configure BGP functions after configuring a peer group, and these will take effect for each peer in the group. By default, each peer in a peer group inherits the configurations of the peer group. However, if you configure a member peer separately, the configuration of this peer will override that inherited from the peer group.
6. (Optional) Configure a description for the peer group.
   
   
   ```
   [peer](cmdqueryname=peer) group-name [description](cmdqueryname=description) description-text
   ```
   
   This configuration simplifies network management.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```