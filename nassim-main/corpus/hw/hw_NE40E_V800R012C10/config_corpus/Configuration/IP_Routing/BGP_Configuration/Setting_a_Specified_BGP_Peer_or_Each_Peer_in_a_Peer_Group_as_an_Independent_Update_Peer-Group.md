Setting a Specified BGP Peer or Each Peer in a Peer Group as an Independent Update Peer-Group
=============================================================================================

Setting a specified peer or each peer in a peer group as an independent update peer-group prevents routes learned from the peer from being sent back to the peer.

#### Usage Scenario

To improve the efficiency of route advertisement, BGP uses the dynamic update peer-group mechanism. The BGP peers with the same configurations are placed in an update peer-group. These routes are grouped once and then sent to all peers in the update peer-group, improving the grouping efficiency exponentially. However, the routes learned from a peer may be sent back to the peer, for example, the preferred route learned from an EBGP peer is sent back to the EBGP peer, or the preferred route that an RR learns from a client is reflected back to the client. In this case, messages are discarded, wasting network resources.

To address this problem, you can set a specified peer or each peer in a peer group as an independent update peer-group so that the routes learned from the peer are not sent back to the peer.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Setting a specified peer or each peer in a peer group as an independent update peer-group can be performed in multiple address families. This section uses the IPv4 unicast address family as an example. For details about the address families supported, see [**peer update-group-independent**](cmdqueryname=peer+update-group-independent).




#### Pre-configuration Tasks

Before configuring a specified peer or each peer in a peer group as an independent update peer-group, complete the following tasks:

* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Set a specified peer or each peer in a peer group as an independent update peer-group.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of a peer takes precedence over that of the peer group to which the peer belongs.
   
   * To set a specified peer as an independent update peer-group, run the [**peer**](cmdqueryname=peer+update-group-independent+enable) *ipv4-address* **update-group-independent** **enable** command.
   * To set each peer in a peer group as an independent update peer-group, run the [**peer**](cmdqueryname=peer+update-group-independent) *group-name* **update-group-independent** command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, you can run the [**display bgp update-peer-group**](cmdqueryname=display+bgp+update-peer-group) command to view information about update peer-groups.