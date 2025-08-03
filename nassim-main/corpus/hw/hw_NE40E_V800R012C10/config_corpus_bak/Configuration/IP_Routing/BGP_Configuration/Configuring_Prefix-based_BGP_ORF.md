Configuring Prefix-based BGP ORF
================================

After prefix-based BGP outbound route filtering (ORF) is configured, the local device sends its prefix-based import policy to a peer so that the peer filters routes during route advertisement.

#### Usage Scenario

When a device expects to receive only required routes from the remote device and the remote end does not want to maintain a separate export policy for each connected peer, you can configure prefix-based ORF which supports on-demand route advertisement.


#### Pre-configuration Tasks

Before configuring prefix-based BGP ORF, complete the following tasks:

* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).
* [Configure an IPv4 prefix list](dc_vrp_route-policy_cfg_0004.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. (Optional) Run [**orf-limit**](cmdqueryname=orf-limit) *limit-value*
   
   
   
   The maximum number of ORF entries that can be accepted from a peer is set.
4. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
5. Run [**peer**](cmdqueryname=peer+ip-prefix+import) { *group-name* | *ipv4-address* } [**ip-prefix**](cmdqueryname=peer+ip-prefix+import) *ip-prefix-name* [**import**](cmdqueryname=peer+ip-prefix+import)
   
   
   
   An IP prefix list-based import policy is configured to filter routes received from the specified peer or peer group.
6. Run [**peer**](cmdqueryname=peer+capability-advertise+orf+ip-prefix) { *group-name* | *ipv4-address* } [**capability-advertise orf**](cmdqueryname=peer+capability-advertise+orf+ip-prefix) [ **non-standard-compatible** ] [**ip-prefix**](cmdqueryname=peer+capability-advertise+orf+ip-prefix) { **both** | **receive** | **send** }
   
   
   
   Prefix-based ORF is configured for a BGP peer or peer group.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) *ipv4-address* **verbose** command to check detailed information about BGP peers.
* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) *ipv4-address* [**orf ip-prefix**](cmdqueryname=orf+ip-prefix) command to check prefix-based ORF information received from a specified peer.