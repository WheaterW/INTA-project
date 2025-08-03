Configuring an IBGP Peer Group
==============================

Configuring an IBGP Peer Group

#### Prerequisites

Before configuring an IBGP peer group, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

If multiple IBGP peers exist, adding them to an IBGP peer group can simplify the BGP4+ network configuration and management. When configuring an IBGP peer group, you do not need to specify an AS number. Instead, the local AS number is used for the peer group.


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
4. Enter the IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
5. Enable the peer group.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv6-address | ipv4-address } [enable](cmdqueryname=enable)
   ```
6. Add a peer to the peer group.
   
   
   ```
   [peer](cmdqueryname=peer+group) { ipv6-address | ipv4-address } group group-name
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * You can repeat Step 6 to add multiple peers to the peer group. If the IBGP peer does not exist, the system automatically creates it in the BGP view and enables it in the IPv6 address family view.
   * To add a peer in a BGP VPN instance to a peer group in this instance, you can also run the [**peer group enable**](cmdqueryname=peer+group+enable) command. Before running this command, you need to create the peer and peer group in the VPN instance view, and then enable the peer and peer group in the BGP VPN instance address family view.
   
   When creating an IBGP peer group, you do not need to specify an AS number for it.
   
   You can configure BGP4+ functions after configuring a peer group, and these will take effect for each peer in the group. By default, each peer in a peer group inherits the configurations of the peer group. However, if you configure a member peer separately, the configuration of this peer will override that inherited from the peer group.
7. (Optional) Configure a description for the peer group.
   
   
   ```
   [peer](cmdqueryname=peer) group-name [description](cmdqueryname=description) description-text
   ```
   
   This configuration simplifies network management.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```