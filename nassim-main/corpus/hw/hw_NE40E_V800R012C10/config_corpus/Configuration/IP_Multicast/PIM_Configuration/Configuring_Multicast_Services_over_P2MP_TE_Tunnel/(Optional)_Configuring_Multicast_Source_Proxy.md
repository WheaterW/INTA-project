(Optional) Configuring Multicast Source Proxy
=============================================

If a point-to-multipoint (P2MP) traffic engineering (TE) tunnel is used to carry multicast services and a rendezvous point (RP) is deployed on the egress side, configure multicast source proxy. Multicast source proxy enables a multicast source to register with the RP.

#### Context

If a multicast data packet for a multicast group transmitted over a P2MP TE tunnel is directed into the egress and the egress does not function as the RP to which the multicast group corresponds, the multicast data packet stops being forwarded because the egress is not directly connected to the multicast source. To enable downstream hosts to receive the multicast data packet, deploy multicast source proxy to enable the egress to send a Register message to the RP in the PIM domain so that the multicast data packet is forwarded along the shared tree.


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
6. Run [**source-proxy enable**](cmdqueryname=source-proxy+enable) [ **policy** { *advanced-acl-number* | **acl-name** *acl-name* } ]
   
   
   
   Multicast source proxy is configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If no ACL is configured, the device enables the multicast source proxy function for all multicast entries.
   * If an ACL is configured, the device determines whether to enable the multicast source proxy function for a multicast entry based on the matching result with the ACL.
     + If a multicast entry matches an ACL rule and the action is **permit**, the device enables the multicast source proxy function for the entry.
     + If a multicast entry matches an ACL rule and the action is **deny**, the device disables the multicast source proxy function for the entry.
     + If a multicast entry does not match any ACL rule, the device disables the multicast source proxy function for the entry.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.