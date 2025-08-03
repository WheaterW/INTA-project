Configuring Filtering Policies for SA Messages
==============================================

Configuring Filtering Policies for SA Messages

#### Context

ACL rules are often used to filter SA messages. When configuring SA message filtering policies in different scenarios, select the corresponding ACL configuration method.

**Table 1** ACL application scenarios
| Application Scenario | ACL Type |
| --- | --- |
| Configure a filtering policy to filter the outgoing locally generated SA messages of a specified VPN instance. | Basic or advanced ACLs |
| Configure a rule for an MSDP peer to filter SA Request messages that it receives. | Basic ACL |
| Configure a rule for an MSDP peer to filter SA messages that it receives. | Advanced ACL |
| Configure a rule for filtering the SA messages to be forwarded. |



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Run either of the following commands to configure an ACL:
   * Create a basic ACL.
     ```
     [acl](cmdqueryname=acl) { name basic-acl-name basic | [ number ] basic-acl-number }
     [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } source { source-ip-address { source-wildcard | 0 } | any }
     quit
     ```
   * Create an advanced ACL.
     ```
     [acl](cmdqueryname=acl) { name advance-acl-name advance | [ number ] advance-acl-number }
     [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } ip [ destination { destination-ip-address { destination-wildcard | 0 } | any } | source { source-ip-address { source-wildcard | 0 } | any } ] *
     quit
     ```
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If a basic ACL is used, run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to the source address of multicast data packets.
   
   If an advanced ACL is used, run the [**rule**](cmdqueryname=rule) command, set the **source** parameter to the source address of multicast data packets, and set the **destination** parameter to a multicast group address.
3. Enter the MSDP view.
   
   
   ```
   [msdp](cmdqueryname=msdp) [ vpn-instance vpn-instance-name ]
   ```
4. Use any of the following methods to configure an SA message filtering policy.
   * Configure a filtering policy to filter the outgoing locally generated SA messages of a specified VPN instance.
     ```
     [import-source](cmdqueryname=import-source) [ acl { acl-number | acl-name } ]
     ```
     
     If no ACL is specified, the device does not send any local SA messages. If an ACL is specified, the device sends only the local SA messages that match the filtering policy.
   * Configure a rule for filtering received SA messages.
     ```
     [peer](cmdqueryname=peer) peer-address [sa-policy import](cmdqueryname=sa-policy+import) { advanced-acl-number | acl-name acl-name }
     ```
     
     *peer-address*: specifies the IP address of a remote MSDP peer. *advanced-acl-number*: specifies a filtering policy.
     
     If no ACL is specified, the device does not accept any (S, G) information from the peer specified by *peer-address*. If an ACL is specified, the device accepts (S, G) information in the matching SA messages received from the peer specified by *peer-address*.
   * Configure a rule for filtering the SA messages to be forwarded.
     ```
     [peer](cmdqueryname=peer) peer-address [sa-policy export](cmdqueryname=sa-policy+export) { advanced-acl-number | acl-name acl-name }
     ```
     
     If no ACL is specified, the device does not forward any (S, G) information from the peer specified by *peer-address*. If an ACL is specified, the device accepts (S, G) information in the matching SA messages received from the peer specified by *peer-address*.
   * Configure a rule on the remote MSDP peer to filter SA Request messages to be received.
     ```
     [peer](cmdqueryname=peer) peer-address [sa-request-policy](cmdqueryname=sa-request-policy) [ { basic-acl-number | acl-name acl-name } ]
     ```
     
     *peer-address*: specifies the address of the MSDP peer that sends SA Request messages. *basic-acl-number* and **acl-name** *acl-name*: specify a filtering policy.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     If an SA Request message matches an ACL rule and the action is **permit**, the device permits the message. If the action is **deny**, the device rejects the message.
     
     If an SA Request message does not match any ACL rule, the device denies the message.
     
     If a specified ACL does not exist or does not contain rules, the device ignores all SA Request messages from this peer.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```