Configuring a Mixed EBGP Peer Group
===================================

Configuring a Mixed EBGP Peer Group

#### Prerequisites

Before configuring a mixed EBGP peer group, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

If multiple EBGP peers exist in different ASs, adding them to a mixed EBGP peer group can simplify the BGP4+ network configuration and management. When configuring a mixed EBGP peer group, you need to specify an AS number for each peer.


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
4. Specify a peer and the number of the AS where the peer resides.
   
   
   ```
   [peer](cmdqueryname=peer+as-number) ipv6-address as-number as-number
   ```
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
   * You can repeat Steps 4 and 7 to add multiple peers to the peer group. After an EBGP peer is added to a peer group, the system automatically enables the EBGP peer in the IPv6 address family view.
   * To add a peer in a BGP VPN instance to a peer group in this instance, you can also run the [**peer group enable**](cmdqueryname=peer+group+enable) command. Before running this command, you need to create the peer and peer group in the VPN instance view, and then enable the peer and peer group in the BGP VPN instance address family view.
   
   When creating a mixed EBGP peer group, you need to create peers separately, and can configure different AS numbers for them. However, you cannot configure an AS number for the peer group.
   
   You can configure BGP4+ functions after configuring a peer group, and these will take effect for each peer in the group. By default, each peer in a peer group inherits the configurations of the peer group. However, if you configure a member peer separately, the configuration of this peer will override that inherited from the peer group.
8. (Optional) Configure a description for the peer group.
   
   
   ```
   [peer](cmdqueryname=peer) group-name [description](cmdqueryname=description) description-text
   ```
   
   This configuration simplifies network management.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```