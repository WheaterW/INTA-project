Configuring Filtering Policies for SA Messages
==============================================

By default, an MSDP peer permits all Source Active (SA) messages that pass the Reverse Path Forwarding (RPF) check, and forwards the SA messages to other MSDP peers. To control the transmission of SA messages among MSDP peers, configure filtering policies to filter SA messages to be created, received, or forwarded.

#### Procedure

* Configure a filtering policy to filter the outgoing locally generated SA messages of a specified VPN instance.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic or an advanced ACL as needed.
     
     Configure a basic ACL.
     1. Run the [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ] command to create a basic ACL and enter the corresponding ACL view.
     2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } command to configure a rule for the basic ACL.
     Configure an advanced ACL.
     1. Run the [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ] command to create an advanced ACL and enter the corresponding ACL view.
     2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ip** [ **destination** { *destination-ip-address* { *destination-wildcard* | **0** } | **any** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } ] \* command to configure a rule for the advanced ACL.
     
     If a basic ACL is used, run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to the source address of multicast packets.
     
     If an advanced ACL is used, run the [**rule**](cmdqueryname=rule) command, set the **source** parameter to the source address of multicast packets, and set the **destination** parameter to a multicast group address.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The MSDP view is displayed.
  5. Run [**import-source**](cmdqueryname=import-source) **acl** { *acl-number* | *acl-name* }
     
     
     
     The device is configured to filter the outgoing locally generated SA messages of a specified VPN instance.
     
     
     
     + If no ACL is specified, the device does not send any locally generated SA messages.
     + If an ACL is specified, the device sends only the locally generated SA messages that match the filtering policy.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a filtering policy to filter the locally generated SA messages to be sent to a specified peer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ]
     
     
     
     An advanced ACL is created, and the corresponding ACL view is displayed.
  3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ip** [ **destination** { *destination-ip-address* { *destination-wildcard* | **0** } | **any** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } ] \*
     
     
     
     A rule is configured for the advanced ACL.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The MSDP view is displayed.
  6. Run [**peer**](cmdqueryname=peer) *peer-address* **sa-policy local-export acl** { *advanced-acl-number* | *acl-name* }
     
     
     
     The device is configured to filter the locally generated SA messages to be sent to the specified peer.
     
     
     
     If no ACL is specified, the device does not send any locally generated SA message to the specified peer. If an ACL is specified, the device sends only the locally generated SA messages that match the filtering policy to the specified peer.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Both the [**import-source**](cmdqueryname=import-source) and [**peer**](cmdqueryname=peer) **sa-policy local-export** commands can be used to configure a filtering policy for locally generated SA messages. If the [**import-source**](cmdqueryname=import-source) command is run in the MSDP view and the [**peer**](cmdqueryname=peer) **sa-policy local-export** command is also run on the MSDP peer, the rule specified in the [**peer**](cmdqueryname=peer) **sa-policy local-export** command preferentially takes effect.
* Configure a filtering policy to filter the SA messages to be received from a specified remote MSDP peer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ]
     
     
     
     An advanced ACL is created, and the corresponding ACL view is displayed.
  3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ip** [ **destination** { *destination-ip-address* { *destination-wildcard* | **0** } | **any** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } ] \*
     
     
     
     A rule is configured for the advanced ACL.
     
     
     
     In the [**rule**](cmdqueryname=rule) command, set the **source** parameter to the source address of SA messages, and set the **destination** parameter to a multicast group address.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The MSDP view is displayed.
  6. Run [**peer**](cmdqueryname=peer) *peer-address* **sa-policy** **import** [ **acl** { *advanced-acl-number* | *acl-name* } ]
     
     
     
     The device is configured to filter the SA messages to be received from a specified remote MSDP peer.
     
     
     
     *peer-address*: specifies the IP address of a remote MSDP peer.
     
     **acl** *advanced-acl-number*: specifies the name of an advanced ACL to be used as the filtering policy. The device uses the ACL to determine whether to accept the SA messages to be received from the specified remote MSDP peer.
     
     + If no ACL is specified, the device does not accept any (S, G) information from the peer specified by *peer-address*.
     + If an ACL is specified, the device accepts the matching SA messages received from the peer specified by *peer-address*.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a filtering policy to filter the SA messages to be forwarded to a specified remote MSDP peer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ]
     
     
     
     An advanced ACL is created, and the corresponding ACL view is displayed.
  3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ip** [ **destination** { *destination-ip-address* { *destination-wildcard* | **0** } | **any** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } ] \*
     
     
     
     A rule is configured for the advanced ACL.
     
     
     
     In the [**rule**](cmdqueryname=rule) command, the **source** parameter is used to specify a multicast source address of SA messages, and the **destination** parameter is used to specify a multicast group address.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The MSDP view is displayed.
  6. Run [**peer**](cmdqueryname=peer) *peer-address* **sa-policy** **export** [ **acl** { *advanced-acl-number* | *acl-name* } ]
     
     
     
     The device is configured to filter the SA messages to be forwarded to the specified remote MSDP peer.
     
     
     
     *peer-address*: specifies the IP address of a remote MSDP peer.
     
     **acl** *advanced-acl-number*: specifies the name of an advanced ACL to be used as the filtering policy. The device uses the ACL to determine whether to forward SA messages to the specified remote MSDP peer.
     
     + If no ACL is specified, the device does not forward any SA messages to the specified remote MSDP peer.
     + If an ACL is specified, the device forwards only the matching SA messages to the remote MSDP peer specified by *peer-address*.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.