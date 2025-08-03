Directing Multicast Traffic out of a P2MP TE Tunnel
===================================================

When a point-to-multipoint (P2MP) traffic engineering (TE) tunnel is used to carry multicast services, you must direct multicast traffic out of the P2MP TE tunnel on the tunnel egress so that the multicast traffic can be correctly forwarded after leaving the tunnel.

#### Context

When a P2MP TE tunnel is used to carry multicast services, you do not need to deploy the Protocol Independent Multicast (PIM) on the transit nodes of the tunnel. If an egress performs the Reverse Path Forwarding (RPF) check on a received multicast data packet, the RPF check fails. As a result, the multicast data packet cannot be forwarded to the next-hop device. To resolve this problem, disable each egress from performing the RPF check on received packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ]
   
   
   
   An advanced ACL is created, and the advanced ACL view is displayed.
3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ip** [ **destination** { *destination-ip-address* { *destination-wildcard* | **0** } | **any** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } ] \*
   
   
   
   Rules are configured for the advanced ACL.
   
   Run the [**rule**](cmdqueryname=rule) command, set the **source** parameter to a multicast source address, and set the **destination** parameter to a multicast group address.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The PIM view is displayed.
6. Run [**rpf disable**](cmdqueryname=rpf+disable) { **policy** { *advanced-acl-number* | **acl-name** *acl-name* } | **all** }
   
   
   
   The RPF check on multicast entries is disabled.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If a multicast entry matches an ACL rule and the action is **permit**, the device does not perform the RPF check on the entry.
   * If a multicast entry matches an ACL rule and the action is **deny**, the device performs the RPF check on the entry.
   * If a multicast entry does not match any ACL rule, the device performs the RPF check on the entry.
   * If a specified ACL does not exist or does not contain rules, the device performs the RPF check on all multicast entries.
7. Run [**traffic select p2mp-te**](cmdqueryname=traffic+select+p2mp-te) **root-ip** *ip-address* **tunnel-id** *tunnel-id*
   
   
   
   The multicast traffic from the specified P2MP TE tunnel is directed to the VPN.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.