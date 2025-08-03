Configuring BGP4+ GTSM
======================

Configuring BGP4+ GTSM

#### Prerequisites

Before configuring BGP4+ Generalized TTL Security Mechanism (GTSM), you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

Attackers may simulate BGP4+ messages and continuously send them to a BGP4+ device. The device then sends these messages directly to the control plane for processing, without validating them, if they are destined for the device. This causes high CPU usage due to the increased workload in processing the messages on the control plane.

GTSM protects a BGP4+ device by checking whether the time to live (TTL) value in each IP packet header is within a pre-defined range to enhance system security.

![](public_sys-resources/note_3.0-en-us.png) 

GTSM supports only unicast addresses. Therefore, GTSM must be configured on all the devices that run routing protocols.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Configure BGP4+ GTSM.
   
   
   ```
   [peer](cmdqueryname=peer+valid-ttl-hops) { group-name | ipv6-address } valid-ttl-hops [ hops ]
   ```
   
   The valid TTL range of detected messages is [255 â *hops* + 1, 255]. For example, the value of *hops* is 1 for an EBGP direct route, and the valid TTL value is 255. By default, the value of *hops* is 255, and the valid TTL range is [1, 255].
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * After GTSM is configured in the BGP view, the configuration also takes effect in the MP-BGP address family view because BGP and MP-BGP use the same TCP connection.
   * GTSM and EBGP-max-hop are mutually exclusive because they both affect the TTL values in sent BGP4+ messages. Therefore, only one of them can be used for a peer or peer group.
   
   A BGP4+ device that is enabled with GTSM checks the TTL values in all BGP4+ messages and discards the messages whose TTL values are not within the specified range. In scenarios where GTSM is not configured on a BGP4+ device, the received BGP4+ messages are forwarded if the BGP4+ peer configuration exists. Otherwise, the received BGP4+ messages are discarded. This prevents bogus BGP4+ messages from consuming CPU resources.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display gtsm statistics**](cmdqueryname=display+gtsm+statistics) { *slot-id* | **all** } command to check GTSM statistics.