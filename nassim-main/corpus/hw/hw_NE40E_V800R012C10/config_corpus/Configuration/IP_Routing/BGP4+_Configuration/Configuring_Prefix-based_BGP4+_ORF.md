Configuring Prefix-based BGP4+ ORF
==================================

After prefix-based BGP4+ outbound route filtering (ORF) is configured, the local device sends its prefix-based import policy to a peer so that the peer filters routes during route advertisement.

#### Usage Scenario

If a device expects to receive only required routes from a remote device, and the remote device cannot maintain a separate export policy for each connected peer, you can configure prefix-based ORF to implement on-demand route advertisement.


#### Pre-configuration Tasks

Before configuring prefix-based BGP4+ ORF, complete the following tasks:

* [Configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).
* [Configure an IPv6 prefix list.](dc_vrp_route-policy_cfg_0004.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. (Optional) Run [**orf-limit**](cmdqueryname=orf-limit) *limit-value*
   
   
   
   The maximum number of ORF entries that can be accepted from a peer is set.
4. Run [**ipv6-family**](cmdqueryname=ipv6-family+unicast) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
5. Run [**peer**](cmdqueryname=peer+ipv6-prefix+import) { *group-name* | *ipv4-address* | *ipv6-address* } [**ipv6-prefix**](cmdqueryname=peer+ipv6-prefix+import) *ipv6-prefix-name* [**import**](cmdqueryname=peer+ipv6-prefix+import)
   
   
   
   An import route-policy that is based on an IPv6 prefix list is configured for a peer or peer group.
6. Run [**peer**](cmdqueryname=peer+capability-advertise+orf+ipv6-prefix) { *group-name* | *ipv4-address* | *ipv6-address* } [**capability-advertise orf**](cmdqueryname=peer+capability-advertise+orf+ipv6-prefix) [**ipv6-prefix**](cmdqueryname=peer+capability-advertise+orf+ipv6-prefix) { **both** | **receive** | **send** }
   
   
   
   Prefix-based ORF is configured for a BGP4+ peer or peer group.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp ipv6 peer**](cmdqueryname=display+bgp+ipv6+peer+verbose) [ *ipv4-address* | *ipv6-address* ] **verbose** command to check detailed information about BGP4+ peers.
* Run the [**display bgp ipv6 peer**](cmdqueryname=display+bgp+ipv6+peer) [ *ipv4-address* | *ipv6-address* ] [**orf ipv6-prefix**](cmdqueryname=orf+ipv6-prefix) command to check prefix-based ORF information received from a specified peer.