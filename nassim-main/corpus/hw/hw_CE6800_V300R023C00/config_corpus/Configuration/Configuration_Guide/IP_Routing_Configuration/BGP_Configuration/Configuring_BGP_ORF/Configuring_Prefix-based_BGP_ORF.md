Configuring Prefix-based BGP ORF
================================

Configuring Prefix-based BGP ORF

#### Prerequisites

Before configuring prefix-based BGP outbound route filtering (ORF), you have completed the following tasks:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).
* [Configure an IPv4 prefix list](vrp_route-policy_cfg_0004.html).

#### Context

If a device expects to receive only required routes from a remote device, and the remote device cannot maintain a separate outbound routing policy for each connected peer, you can configure prefix-based ORF to implement on-demand route advertisement.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
4. Configure an import route-policy that is based on an IP prefix list to filter routes received from a specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer+ip-prefix+import) { group-name | ipv4-address | ipv6-address } ip-prefix ip-prefix-name import
   ```
5. Enable prefix-based ORF for the specified BGP peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer+capability-advertise+orf+non-standard-compatible+ip-prefix) { group-name | ipv4-address | ipv6-address } capability-advertise orf [ non-standard-compatible ] ip-prefix { both | receive | send }
   ```
   
   By default, prefix-based ORF is not enabled for any BGP peer or peer group.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After completing the configuration, perform the following operations to check the configurations:

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) [ *ipv4-address* | *ipv6-address* ] **verbose** command to check detailed BGP peer information.
* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) [ *ipv4-address* | *ipv6-address* ] [**orf ip-prefix**](cmdqueryname=orf+ip-prefix) command to check prefix-based ORF information learned from a specified peer.