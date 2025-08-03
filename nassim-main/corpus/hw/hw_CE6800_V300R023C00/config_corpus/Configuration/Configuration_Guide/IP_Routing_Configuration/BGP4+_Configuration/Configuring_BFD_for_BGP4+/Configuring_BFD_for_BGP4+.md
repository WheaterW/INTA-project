Configuring BFD for BGP4+
=========================

Configuring BFD for BGP4+

#### Prerequisites

Before configuring BFD for BGP4+, you have completed the following tasks:

* Configure link layer protocol parameters and IPv6 addresses for interfaces to ensure that the link layer protocol on the interfaces is up.
* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

BFD provides fast detection of forwarding faults to ensure QoS of voice, video, and other VOD services on a network. It also enables service providers to provide users with required VoIP and other real-time services with high availability and scalability.

BGP4+ periodically sends Keepalive messages to a peer to detect its status. This process takes more than one second. When traffic is transmitted at gigabit rates, fault detection adds up and eventually results in packet loss, meaning that the system is unable to satisfy the high reliability requirements of the carrier-class network.

To address this problem, configure BFD for BGP4+ to enable quick fault detection on links between BGP4+ peers, accelerating network convergence.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BFD globally on the local node.
   
   
   ```
   [bfd](cmdqueryname=bfd)
   ```
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
5. Configure BFD for a peer or peer group, and use default BFD parameters to establish a BFD session.
   
   
   ```
   [peer](cmdqueryname=peer) { group-name | ipv6-address } [bfd enable](cmdqueryname=bfd+enable+single-hop-prefer+compatible) [ [ single-hop-prefer ] [ compatible ] | [ per-link ] one-arm-echo ]
   ```
6. (Optional) Specify parameters for establishing a BFD session.
   
   
   ```
   [peer](cmdqueryname=peer) { group-name | ipv6-address } [bfd](cmdqueryname=bfd+min-tx-interval+min-rx-interval+detect-multiplier) { min-tx-interval min-tx-interval | min-rx-interval min-rx-interval | detect-multiplier multiplier } *
   ```
   
   After BFD is enabled for a peer group, BFD sessions will be created on the peers that belong to this peer group and that are not configured with the [**peer bfd block**](cmdqueryname=peer+bfd+block) command.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * A BFD session can be established only when the corresponding BGP4+ session is in the Established state.
   * The BFD configuration of a peer takes precedence over that of the peer group to which the peer belongs. If BFD is not configured on a peer but the peer group to which the peer belongs has BFD enabled, the peer inherits the BFD configurations from the peer group.
7. (Optional) Prevent a peer from inheriting the BFD function from a peer group.
   
   
   ```
   [peer](cmdqueryname=peer) ipv6-address [bfd block](cmdqueryname=bfd+block)
   ```
   
   If BFD is enabled on a peer group, all its peers will inherit the BFD configurations of the peer group and create a BFD session. If you do not want a peer to inherit the BFD configurations of its peer group, you can run this command.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The [**peer**](cmdqueryname=peer) *ipv6-address* [**bfd block**](cmdqueryname=bfd+block) and [**peer**](cmdqueryname=peer) *ipv6-address* [**bfd enable**](cmdqueryname=bfd+enable) commands are mutually exclusive. After the [**peer bfd block**](cmdqueryname=peer+bfd+block) command is run, the BFD session is automatically deleted.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp ipv6 bfd session**](cmdqueryname=display+bgp+ipv6+bfd+session) { [**peer**](cmdqueryname=peer) *ipv6-address* | **all** } command to check information about BFD sessions established by BGP4+.
* Run the [**display bgp**](cmdqueryname=display+bgp) **ipv6 peer** [ *ipv6-address* ] [ **verbose** ] command to check BGP4+ peer information.