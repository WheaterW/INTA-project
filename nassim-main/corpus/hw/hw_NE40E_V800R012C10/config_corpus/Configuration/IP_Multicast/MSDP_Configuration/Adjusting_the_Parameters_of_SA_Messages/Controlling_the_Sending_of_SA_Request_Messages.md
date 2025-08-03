Controlling the Sending of SA Request Messages
==============================================

If the Source Active (SA) cache capacity is large on a remote MSDP peer, to shorten the time taken by a receiver to obtain multicast source information, you can enable the local Rendezvous Point (RP) to send SA Request messages, and configure a policy on the peer to filter SA Request messages to be received from the local RP.

#### Context

If the local RP has a small SA cache capacity and needs to receive multicast data, the local RP cannot immediately obtain valid (S, G) information. Instead, it has to wait for the SA message sent by the remote MSDP peer in the next sending period.

If the SA cache function is enabled and the SA cache capacity is large on the remote MSDP peer, enable the local RP to send SA Request messages to shorten the time taken by a receiver to obtain multicast source information.

* When the local RP needs to receive (S, G) information, it actively sends an SA Request message to the specified remote MSDP peer rather than waits for the SA message sent in the next sending period.
* Upon receipt of the SA Request message, the remote MSDP peer responds with an SA Response message carrying the required (S, G) information.
  
  If the remote MSDP peer is configured to filter SA Request messages to be received, the remote peer responds to only the SA Request messages that matches the specified rule.

#### Procedure

* Enable the local RP to send SA Request messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The MSDP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *peer-address* **request-sa-enable**
     
     
     
     The local RP is enabled to send SA Request messages to a specified MSDP peer.
     
     *peer-address*: specifies the IP address of a remote MSDP peer. When the local RP receives a new Join message, it sends an SA Request message only to the peer specified by *peer-address*.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Before running this command on the local RP, disable the SA cache function on the local RP and ensure that the SA cache function is enabled on the MSDP peer specified by *peer-address*.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a policy on the remote MSDP peer to filter SA Request messages to be received.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic numbered ACL or a naming ACL as needed.
     
     
     + Configure a basic numbered ACL.
       
       1. Run the [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ] command to create a basic numbered ACL and enter the corresponding ACL view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } command to configure a rule for the basic numbered ACL.
       3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     + Configure a named ACL.
       
       1. Run the [**acl**](cmdqueryname=acl) **name** *acl-name* **basic** [ **match-order** { **auto** | **config** } ] command to create a named ACL and enter the corresponding ACL view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } command to configure a rule for the named ACL.
       3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     
     If a basic numbered ACL is used, run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to the multicast group address.
     
     If a named ACL is used, run the [**rule**](cmdqueryname=rule) command and set the **destination** parameter to a multicast group address.
  3. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The MSDP view is displayed.
  4. Run [**peer**](cmdqueryname=peer) *peer-address* **sa-request-policy** [ **acl** { *basic-acl-number* | *acl-name* } ]
     
     
     
     A policy is configured to filter SA Request messages to be received.
     
     
     
     + *peer-address*: specifies the address of the MSDP peer that sends SA Request messages.
     + **acl** *basic-acl-number* and *acl-name*: defines a filtering policy.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If an SA Request message matches an ACL rule and the action is **permit**, the device permits this message.
     + If an SA Request message matches an ACL rule and the action is **deny**, the device denies this message.
     + If an SA Request message does not match any ACL rule, the device denies this message.
     + If a specified ACL does not exist or does not contain rules, the device ignores all SA Request messages from this peer.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.