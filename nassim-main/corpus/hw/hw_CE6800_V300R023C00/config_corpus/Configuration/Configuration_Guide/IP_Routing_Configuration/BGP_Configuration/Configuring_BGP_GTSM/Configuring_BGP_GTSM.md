Configuring BGP GTSM
====================

Configuring BGP GTSM

#### Prerequisites

Before configuring BGP GTSM, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

Perform the following steps at both ends of a BGP peer relationship:


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Configure BGP GTSM.
   
   
   ```
   [peer](cmdqueryname=peer+valid-ttl-hops) { group-name | ipv4-address } valid-ttl-hops [ hops ]
   ```
   
   
   
   The valid TTL range of detected messages is [255 â *hops* + 1, 255]. For example, the value of *hops* is 1 for an EBGP direct route, and the valid TTL value is 255. By default, the value of *hops* is 255, and the valid TTL range is [1, 255].
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * After GTSM is configured in the BGP view, the configuration also takes effect in the MP-BGP VPNv4 address family view because BGP and MP-BGP VPNv4 use the same TCP connection.
   * GTSM and EBGP-max-hop are mutually exclusive because they both affect the TTL values in sent BGP messages. Therefore, only one of them can be used for a peer or peer group.
   
   After a GTSM policy is configured for BGP, the device checks the TTL values of all BGP messages. As required by the actual networking, messages whose TTL values do not match the specified range in a GTSM policy are discarded directly. In scenarios where GTSM is not configured on a BGP device, the received BGP messages are forwarded if the BGP peer configuration exists. Otherwise, the received BGP messages are discarded. This prevents bogus BGP messages from consuming CPU resources.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display gtsm statistics**](cmdqueryname=display+gtsm+statistics) { *slot-id* | **all** } command to check GTSM statistics.