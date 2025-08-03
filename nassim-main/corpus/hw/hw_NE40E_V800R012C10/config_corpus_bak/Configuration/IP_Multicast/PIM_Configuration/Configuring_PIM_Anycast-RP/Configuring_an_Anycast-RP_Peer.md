Configuring an Anycast-RP Peer
==============================

When sending a PIM Register message to all Anycast-Rendezvous Point (RP) peers, the local RP needs to use the peer addresses as the destination addresses of the Register message.

#### Context

The Routers functioning as Anycast-RPs can be identified by the same logical address so that the RP in the PIM-SM domain is unique. However, the Routers need to distinguish one another during the communication, so the Anycast-RP address cannot be used. To resolve this issue, configure Anycast-RP peers.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a basic or an advanced ACL as needed.
   
   
   * Configure a basic ACL.
     
     1. Run [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ]
        
        A basic ACL is created, and the basic ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
        
        Rules are configured for the basic ACL.
   * Configure an advanced ACL.
     
     1. Run [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ]
        
        An advanced ACL is created, and the advanced ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ip** [ **destination** { *destination-ip-address* { *destination-wildcard* | **0** } | **any** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } ] \*
        
        Rules are configured for the advanced ACL.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The PIM view is displayed.
5. Run [**anycast-rp**](cmdqueryname=anycast-rp) *rp-address*
   
   
   
   The Anycast-RP view is displayed.
6. Run [**peer**](cmdqueryname=peer) *peer-address* [ **fwd-msdp-sa** [ *acl-number* | **acl-name** *acl-name* ] ]
   
   
   
   An Anycast-RP peer is specified.
   
   
   
   * *peer-address*: specifies the local address of an Anycast-RP peer.
   * **fwd-msdp-sa**: enables a local RP to extract source and group information from received Multicast Source Discovery Protocol (MSDP) Source Active (SA) messages, encapsulate the information into Register messages, and send Register messages to Anycast-RP peers.
   * In a PIM-SM domain, all Anycast-RP-capable devices must be fully connected. Anycast-RP peer relationships must be configured between every two Anycast-RPs.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If no ACL is configured, the local RP extracts source/group information from received MSDP SA messages, encapsulates the information into a Register message, and sends the Register message to Anycast-RP peers.
   * If an ACL is configured, the local RP uses configured ACL rules to filter multicast group addresses in MSDP SA messages to be forwarded.
     + If an MSDP SA message matches an ACL rule and the action is **permit**, the local RP forwards this message.
     + If an MSDP SA message matches an ACL rule and the action is **deny**, the local RP does not forward this message.
     + If an MSDP SA message does not match any ACL rule, the local RP does not forward this message.
     + If a specified ACL does not exist or does not contain rules, the local RP does not forward MSDP SA messages.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.