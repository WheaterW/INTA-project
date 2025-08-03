Configuring BFD for BGP4+
=========================

BFD for BGP4+ provides BGP4+ with a fast fault detection mechanism, which speeds up network convergence.

#### Usage Scenario

BFD is dedicated to fast detection of forwarding faults to ensure QoS of voice, video, and other video-on-demand services on a network. It enables service providers to provide users with required VoIP and other real-time services of high availability and scalability.

BGP4+ periodically sends Keepalive messages to its peers to monitor peer relationships. This process takes more than one second. When the data transmission rate reaches the level of Gbit/s, such slow detection will cause a large amount of data to be lost. As a result, the requirement for high reliability of carrier-class networks cannot be met.

To address this problem, configure BFD for BGP4+, which can quickly detect faults on links between BGP4+ peers, speeding up network convergence.


#### Pre-configuration Tasks

Before configuring BFD for BGP4+, complete the following tasks:

* Configure link layer protocol parameters and IP addresses for interfaces and ensure that the link layer protocol on the interfaces is up.
* [Configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
5. Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv6-address* } [**bfd enable**](cmdqueryname=bfd+enable+single-hop-prefer) [ **single-hop-prefer** ] [ **compatible** ]
   
   
   
   BFD is configured for a peer or peer group, and default BFD parameters are used to establish a BFD session.
6. (Optional) Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv6-address* } [**bfd**](cmdqueryname=bfd+min-tx-interval+min-rx-interval+detect-multiplier) { **min-tx-interval** *min-tx-interval* | **min-rx-interval** *min-rx-interval* | **detect-multiplier** *multiplier* } \*
   
   
   
   Various parameters used for establishing BFD sessions are set.
   
   If BFD is configured on a peer group, the peers that are in the peer group but are not configured with the [**peer bfd block**](cmdqueryname=peer+bfd+block) command establish BFD sessions.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * A BFD session can be established only when the corresponding BGP session is in the Established state.
   * The configuration of a peer takes precedence over that of its peer group. If BFD is not configured on a peer while its peer group is enabled with BFD, the peer inherits the BFD configurations of its peer group.
7. (Optional) Run [**peer**](cmdqueryname=peer) *ipv6-address* [**bfd block**](cmdqueryname=bfd+block)
   
   
   
   A peer is prevented from inheriting the BFD configuration of its peer group.
   
   If BFD is enabled on a peer group, all its peers will inherit the BFD configuration of the peer group and create a BFD session. If you do not want a peer to inherit the BFD configuration of its peer group, you can run this command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**peer**](cmdqueryname=peer) *ipv6-address* [**bfd block**](cmdqueryname=bfd+block) command and the [**peer**](cmdqueryname=peer) *ipv6-address* [**bfd enable**](cmdqueryname=bfd+enable) command are mutually exclusive. After being configured with the [**peer bfd block**](cmdqueryname=peer+bfd+block) command, a device automatically deletes the BFD session established with a specified peer.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp ipv6 bfd session**](cmdqueryname=display+bgp+ipv6+bfd+session+vpnv6+vpn-instance) { [ **vpnv6** **vpn-instance** *vpn-instance-name* ] [**peer**](cmdqueryname=peer+all) *ipv6-address* | **all** } command to check BFD sessions established by BGP4+.
* Run the [**display bgp**](cmdqueryname=display+bgp+vpnv6+vpn-instance) [ **vpnv6** **vpn-instance** *vpn-instance-name* ] [**peer**](cmdqueryname=peer+verbose) [ *ipv6-address* ] [ **verbose** ] command to check BGP4+ peers.