Setting a Specified BGP4+ Peer or Each Peer in a Peer Group as an Independent Update Peer-Group
===============================================================================================

Setting a specified BGP4+ peer or each peer in a peer group as an independent update peer-group prevents routes learned from the peer from being sent back to the peer.

#### Prerequisites

Before configuring a specified BGP4+ peer or each peer in a peer group as an independent update peer-group, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

To improve the efficiency of route advertisement, BGP uses the update peer-group mechanism. The BGP peers with the same configurations are placed in an update peer-group. These routes are grouped once and then sent to all peers in the update peer-group, improving the grouping efficiency exponentially. However, the routes learned from a peer may be sent back to the peer, for example, the preferred route learned from an EBGP peer is sent back to the EBGP peer, or the preferred route that an RR learns from a client is reflected back to the client. In this case, messages are discarded, wasting network resources.

To address this problem, you can set a specified peer or each peer in a peer group as an independent update peer-group so that the routes learned from the peer are not sent back to the peer.

![](public_sys-resources/note_3.0-en-us.png) 

Setting a specified BGP peer or each peer in a peer group as an independent update peer-group can be performed in multiple address families. This section uses the IPv6 unicast address family as an example. For details about the address families supported, see [**peer update-group-independent**](cmdqueryname=peer+update-group-independent).



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
4. Set a specified BGP peer or each peer in a peer group as an independent update peer-group.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of a peer takes precedence over that of the peer group to which the peer belongs.
   
   1. Enable a specified peer as an independent update peer-group.
      ```
      [peer](cmdqueryname=peer+update-group-independent+enable) { ipv4-address | ipv6-address } update-group-independent enable
      ```
   2. Enable each peer in a peer group as an independent update peer-group.
      ```
      [peer](cmdqueryname=peer+update-group-independent) group-name update-group-independent
      ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After completing the configuration, verify it.

* Run the [**display bgp ipv6 update-peer-group**](cmdqueryname=display+bgp+ipv6+update-peer-group) command to check information about update peer-groups.