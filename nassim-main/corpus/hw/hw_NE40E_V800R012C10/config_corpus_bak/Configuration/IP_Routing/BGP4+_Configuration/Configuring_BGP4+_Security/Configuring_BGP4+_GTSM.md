Configuring BGP4+ GTSM
======================

To apply BGP4+ GTSM, you need to configure GTSM on both ends of the corresponding BGP4+ peer relationship.

#### Usage Scenario

GTSM checks TTL values to defend against attacks. Attackers may simulate BGP4+ messages and continuously send them to a Router. After receiving these messages, an interface board on the Router sends them directly to the control plane for BGP4+ processing, without validating them, if they are destined for the device. Consequently, the Router becomes extremely busy, and CPU usage is high because the control plane needs to process these unverified messages.

GTSM protects the Router by checking whether the TTL value in the IP header is within a predefined range, thereby improving system security.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* GTSM supports only unicast addresses. Therefore, it needs to be configured on all the Routers running routing protocols.


#### Pre-configuration Tasks

Before configuring BGP4+ GTSM, complete the following task:

* [Configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).

Perform the following steps on both ends of the peer relationship for which GTSM is to be enabled:


#### Procedure

1. Configure basic BGP4+ GTSM functions.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**peer**](cmdqueryname=peer) { *group-name* | *ipv6-address* } **valid-ttl-hops** [ *hops* ] command to configure BGP4+ GTSM.
      
      
      
      The valid TTL range of checked messages is [255 â *hops* + 1, 255]. For example, the value of *hops* is 1 for an EBGP direct route, and the valid TTL value is 255.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * After GTSM is configured in the BGP view, the configuration also takes effect in the MP-BGP VPNv4 address family view because BGP and MP-BGP VPNv4 use the same TCP connection.
      * Because GTSM and EBGP-MAX-HOP both affect the TTL values in sent BGP4+ messages, only one of them can be configured for a peer or peer group.
      
      After a BGP4+ GTSM policy is enabled, the involved interface board checks the TTL values in all the BGP4+ messages and drops the messages whose TTL values are not within the range specified in the GTSM policy. This prevents bogus BGP4+ messages from consuming CPU resources.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Set a default action for the messages that do not match the specified GTSM policy.
   
   
   
   GTSM checks the TTL values of only the messages that match the specified GTSM policy. For messages that do not match the policy, you can set the default action taken on them as either pass or drop. When drop is configured as the default action, you must configure TTL values for all the messages from valid peers in the GTSM policy. Otherwise, the device drops the messages and cannot establish a connection to the peer.
   
   To facilitate fault locating, you can enable the device to log information about dropped messages.
   
   Perform the following steps on a GTSM-enabled Router:
   
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**gtsm default-action**](cmdqueryname=gtsm+default-action) { **drop** | **pass** } command to set a default action for the messages that do not match the GTSM policy.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If the default action is configured but no GTSM policy is configured, GTSM does not take effect.
      
      This command is supported only on the Admin-VS and cannot be configured in other VSs. This command takes effect on all VSs.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display gtsm statistics**](cmdqueryname=display+gtsm+statistics) { *slot-id* | **all** } command to check GTSM statistics.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In VS mode, this command is supported only by the admin VS.