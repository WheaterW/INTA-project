Layer 3 Multicast
=================

Layer 3 Multicast

#### Security Policy Overview

* PIM neighbor filtering
  
  ACL rules can be configured on interfaces to filter received Hello packets. Neighbor relationships can be established only after the Hello packets pass the filtering.
  
  If a large number of malicious Hello packets exist, configure rules on interfaces so that the interfaces allow only specified Hello packets to pass through and discard malicious Hello packets.
* PIM Join message filtering
  
  ACL rules can be configured on interfaces to filter received Join messages. This can prevent attacks initiated using malicious Join messages.
  
  If a large number of malicious Join messages exist, configure rules on interfaces so that the interfaces allow only specified Join messages to pass through and discard malicious Join messages.
* IPv4/IPv6 PIM IPsec authentication
  
  IPsec authentication can be configured on interfaces to authenticate IPv4/IPv6 PIM messages. With IPv4/IPv6 PIM IPsec configured, the IPv4/IPv6 PIM messages that are not protected by IPsec or fail to be authenticated are discarded.
* MSDP whitelist
  
  MSDP is implemented based on the whitelist. MSDP establishes a stable link with the peer to construct the peer remote address, local interface address, remote port number, local port number, and IP protocol number (TCP). The call component interface instructs the underlayer to transmit the messages meeting these conditions first (the priority policy depends on the implementation at the underlayer). After the MSDP neighbor relationship is torn down, the call component interface instructs the underlayer to delete the policy of preferentially transmitting the messages meeting the conditions.
  
  The malicious messages that do not match the whitelist are discarded. This effectively prevents attacks that are conducted through malicious messages.
* MSDP MD5 authentication
  
  MD5 authentication can be configured on MSDP peers to provide security protection. To use MD5 authentication, enable it on both peers and set the same password for them. After this function is enabled, the transmit end peer sends an MD5-encrypted MSDP message, which is transferred to the receive end peer over a TCP connection. The receive end peer decrypts the MSDP message based on the uniform MD5 encryption rules and the key carried in the message. After decrypting the message successfully, the receive end peer sends the message to the MSDP module for processing. Only the MSDP messages that pass MD5 authentication are processed, which prevents attacks that are conducted using malicious messages.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  MD5 authentication is insecure. Keychain authentication is recommended.
* MSDP keychain authentication
  
  Multicast MSDP supports keychains. Keychains and new TCP extension options can be used to configure a group of passwords for each TCP connection. Each password can be configured with different encryption algorithms and validity periods. Passwords can be changed at any time, which greatly improves the security of encrypted messages. Only the messages that are authenticated using a keychain are processed. This effectively prevents attacks conducted using malicious messages.
* TCP-AO authentication
  
  Configuring TCP-AO authentication can enhance the security of the TCP connections between MSDP peers. Compared with MD5 authentication, MSDP TCP-AO authentication applies to networks that require high security.
* Source address-based IGMP/MLD message filtering
  
  ACL rules can be configured on interfaces to filter received IGMP/MLD messages. This can prevent attacks initiated using malicious IGMP/MLD messages.
  
  If a large number of malicious IGMP/MLD messages exist, configure rules on interfaces so that the interfaces allow only the IGMP/MLD messages with specified source IP addresses to pass through and discard malicious IGMP/MLD messages.
* IGMP/MLD IPsec authentication
  
  IPsec authentication can be configured on interfaces to authenticate IGMP//MLD messages. With IGMP/MLD IPsec configured, the IGMP/MLD messages that are not protected by IPsec or fail to be authenticated are discarded.
* Session-CAR
  
  The function of whitelist session-CAR for PIM sets an independent CAR channel for each PIM neighbor to ensure that the bandwidth of each PIM neighbor is not preempted by other traffic (including traffic of other neighbors of the same protocol and traffic of other protocols). When PIM messages form a traffic burst, bandwidth may be preempted among PIM sessions. To resolve this problem, you can configure whitelist session-CAR for PIM to isolate bandwidth resources by session to ensure that PIM messages can be sent to the CPU properly.
  
  The function of whitelist session-CAR for MSDP sets an independent CAR channel for each MSDP neighbor to ensure that the bandwidth of each MSDP neighbor is not preempted by other traffic (including traffic of other neighbors of the same protocol and traffic of other protocols). When MSDP messages form a traffic burst, bandwidth may be preempted among MSDP sessions. To resolve this problem, you can configure whitelist session-CAR for MSDP to isolate bandwidth resources by session to ensure that MSDP messages can be sent to the CPU properly.
* Micro-isolation CAR for IGMP/MLD
  
  The micro-isolation CAR function is enabled for IGMP/MLD by default to implement micro-isolation protection for IGMP/MLD connection establishment messages. If a device is attacked, messages of one IGMP/MLD session may preempt bandwidth of other sessions. Therefore, you are advised to keep this function enabled.

#### Attack Methods

Attacks can be initiated through malicious IGMP/MLD messages. To configure a device to discard such malicious messages, you can configure source address-based IGMP/MLD message filtering. The possible attack methods are as follows:

* Attackers send malicious Report messages of an earlier protocol version to join a multicast group to force the multicast group to work in the mode that is compatible with the earlier version. In this mode, when all hosts leave the multicast group, their Leave messages are not processed. As a result, traffic corresponding to the multicast group is still sent until the multicast group times out although it has no members.
* Attackers send Leave messages or IGMPv3 status change Report messages. In this case, routers and all multicast group members respond to source-specific or source/group-specific information query, but services of the multicast group or (S, G) are not interrupted.
* Attackers send IGMP Query messages with lower IP addresses. In this case, the querier becomes invalid and no longer responds to the prompt-leave of multicast group members. As a result, traffic of the multicast group is forwarded for one more period of the membership timer even if there is no member in the multicast group.
* By intercepting General Query messages, attackers learn multicast group members and send a large number of source-and-group-specific Query messages with a list of a large number of sources and a long query response delay. As a result, hosts process the query during the response delay, which consumes a large number of CPU and memory resources.

#### Procedure

* PIM neighbor filtering
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic numbered ACL or a named ACL as needed.
     
     
     + Configure a basic numbered ACL.
       
       1. Run the [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ] command to create a basic numbered ACL and enter the corresponding ACL view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } command to configure a rule for the basic numbered ACL.
     + Configure a named ACL.
       
       1. Run the [**acl**](cmdqueryname=acl) **name** *acl-name* **basic** [ **match-order** { **auto** | **config** } ] command to create a named ACL and enter the corresponding ACL view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } command to configure a rule for the named ACL.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The PIM interface view is displayed.
  5. Run [**pim neighbor-policy**](cmdqueryname=pim+neighbor-policy) { *basic-acl-number* | **acl-name** *acl-name* }
     
     
     
     A neighbor filtering policy is configured.
     
     The neighbor filtering policy defines the range of valid neighbor addresses. The Router discards Hello messages received from the Routers that are not in this address range.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If a peer matches an ACL and the action is **permit**, the local Router sets up a neighbor relationship with this peer.
     + If a peer matches an ACL and the action is **deny**, the local Router does not set up a neighbor relationship with this peer.
     + If a peer does not match any ACL rule, the local Router does not set up a neighbor relationship with this peer.
     + If a specified ACL does not exist or does not contain rules, the local Router does not set up neighbor relationships with any peers.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* PIM Join message filtering
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic or an advanced ACL as needed.
     
     
     + Configure a basic ACL.
       
       1. Run the [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ] command to create a basic ACL and enter the corresponding ACL view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } command to configure a rule for the basic ACL.
     + Configure an advanced ACL.
       
       1. Run the [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ] command to create an advanced ACL and enter the corresponding ACL view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ip** [ **destination** { *destination-ip-address* { *destination-wildcard* | **0** } | **any** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } ] \* command to configure a rule for the advanced ACL.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The PIM interface view is displayed.
  5. Run [**pim join-policy**](cmdqueryname=pim+join-policy) { { *advanced-acl-number* | **acl-name** *acl-name* } | **asm** { *basic-acl-number* | **acl-name** *acl-name* } | **ssm** { *advanced-acl-number* | **acl-name** *acl-name* } }
     
     
     
     A policy is created for filtering join information in Join/Prune messages.
     
     The Router filters join information in Join/Prune messages based on source addresses or both source and group addresses.
     
     If **asm** is specified, run the [**rule**](cmdqueryname=rule) command in the basic ACL view and set the **source** parameter to the multicast group address range of join information.
     
     If **ssm** is specified, run the [**rule**](cmdqueryname=rule) command in the advanced ACL view, set the **source** parameter to the multicast source address range of join information, and set the **destination** parameter to the multicast group address range of join information.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If a Join message's join information matches an ACL rule and the action is **permit**, the device permits this message.
     + If a Join message's join information matches an ACL rule and the action is **deny**, the device denies this message.
     + If a Join message's join information does not match any ACL rule, the device denies this message.
     + If a specified ACL does not exist or does not contain rules, the device denies all Join messages that contain join information.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure IPv4 PIM IPsec in the PIM view.
  + Configure IPsec authentication for IPv4 PIM messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The PIM view is displayed.
  3. Run [**ipsec**](cmdqueryname=ipsec) [ [**unicast-message**](cmdqueryname=unicast-message) ] **sa** *sa-name*
     
     
     
     IPv4 PIM IPsec is configured globally, enabling the device to authenticate the sent and received IPv4 PIM messages based on the specified SA.
     
     If you specify [**unicast-message**](cmdqueryname=unicast-message) in the command, the device authenticates IPv4 PIM unicast messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication for IPv4 PIM Hello messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The PIM view is displayed.
  3. Run [**hello ipsec**](cmdqueryname=hello+ipsec) [**sa**](cmdqueryname=sa) *sa-name*
     
     
     
     IPv4 PIM IPsec is configured globally, enabling the device to authenticate the sent and received IPv4 PIM Hello messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**ipsec sa**](cmdqueryname=ipsec+sa) and [**hello ipsec sa**](cmdqueryname=hello+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.
* Configure IPv4 PIM IPsec in the interface view.
  + Configure IPsec authentication for IPv4 PIM messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**pim ipsec sa**](cmdqueryname=pim+ipsec+sa) *sa-name*
     
     
     
     IPv4 PIM IPsec is configured on the interface, enabling the interface to authenticate the sent and received IPv4 PIM messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication for IPv4 PIM Hello messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**pim hello ipsec sa**](cmdqueryname=pim+hello+ipsec+sa) *sa-name*
     
     
     
     IPv4 PIM IPsec is configured on the interface, enabling the interface to authenticate the sent and received IPv4 PIM Hello messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**pim ipsec sa**](cmdqueryname=pim+ipsec+sa) and [**pim hello ipsec sa**](cmdqueryname=pim+hello+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.
* Configure global IPv6 PIM IPsec.
  + Configure IPsec authentication for IPv6 PIM messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
     
     
     
     The IPv6 PIM view is displayed.
  3. Run [**ipsec**](cmdqueryname=ipsec) [ **unicast-message** ] **sa** *sa-name*
     
     
     
     IPv6 PIM IPsec is configured globally, enabling the device to authenticate the sent and received IPv6 PIM messages based on the specified SA policy. If you specify [**unicast-message**](cmdqueryname=unicast-message) in the command, the device authenticates only the sent and received IPv6 PIM unicast messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication only for IPv6 PIM Hello messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
     
     
     
     The IPv6 PIM view is displayed.
  3. Run [**hello ipsec**](cmdqueryname=hello+ipsec) **sa** *sa-name*
     
     
     
     IPv6 PIM IPsec is configured globally, enabling the device to authenticate the sent and received IPv6 PIM Hello messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**ipsec sa**](cmdqueryname=ipsec+sa) and [**hello ipsec sa**](cmdqueryname=hello+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.
* Configure IPv6 PIM IPsec in the interface view.
  + Configure IPsec authentication for IPv6 PIM messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**pim ipv6 ipsec sa**](cmdqueryname=pim+ipv6+ipsec+sa) *sa-name*
     
     
     
     IPv6 PIM IPsec is configured on the interface, enabling the interface to authenticate the sent and received IPv6 PIM messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication for IPv6 PIM Hello messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**pim ipv6 hello ipsec sa**](cmdqueryname=pim+ipv6+hello+ipsec+sa) *sa-name*
     
     
     
     IPv6 PIM IPsec is configured on the interface, enabling the interface to authenticate the sent and received IPv6 PIM Hello messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**pim ipv6 ipsec sa**](cmdqueryname=pim+ipv6+ipsec+sa) and [**pim ipv6 hello ipsec sa**](cmdqueryname=pim+ipv6+hello+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.
* MSDP whitelist
  
  
  
  MSDP establishes a stable link with the peer.
* Configure MSDP MD5 authentication.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable)
     
     
     
     The weak algorithm plug-in is loaded.
  3. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The MSDP view is displayed.
  4. Run [**peer**](cmdqueryname=peer) *peer-address* **password** { **cipher** *cipher-password* | **simple** *simple-password* } MSDP
     
     
     
     MD5 authentication is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The password must be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters (excluding question marks and spaces).
     + For security purposes, you are advised to specify the ciphertext mode and change the password periodically.
     + For security purposes, MD5 is not recommended. If it is required, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.
     
     
     
     MD5 authentication can be configured on MSDP peers to provide security protection. To use MD5 authentication, enable it on both peers and set the same password for them. After this function is enabled, the transmit end peer sends an MD5-encrypted MSDP message, which is transferred to the receive end peer over a TCP connection. The receive end peer decrypts the MSDP message based on the uniform MD5 encryption rules and the key carried in the message. After decrypting the message successfully, the receive end peer sends the message to the MSDP module for processing. Only the MSDP messages that pass MD5 authentication are processed, which prevents attacks that are conducted using malicious messages.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure MSDP keychain authentication.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The MSDP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *peer-address* **keychain** *keychain-name*
     
     
     
     MSDP keychain authentication is configured.
     
     Keychain and new TCP extension options enable each TCP connection to be configured with a password. You can set different encryption algorithms and validity periods for passwords. In addition, passwords can be changed at any time. This significantly improves security of encrypted messages. Only the messages that are authenticated using a keychain are processed. This effectively prevents attacks conducted using malicious messages.
     
     Keychain authentication must be configured on both MSDP peers, and the keychains configured at both ends must use the same encryption algorithm and password so that a TCP connection can be set up and MSDP messages can be exchanged properly.
     
     Before configuring MSDP keychain authentication, configure the keychain corresponding to *keychain-name*; otherwise, the TCP connection cannot be set up.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     MSDP MD5 authentication and MSDP keychain authentication are mutually exclusive.
     
     The encryption algorithm used for MD5 authentication poses security risks. Therefore, you are advised to use an authentication mode based on a more secure encryption algorithm.
* TCP-AO authentication
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The MSDP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *peer-address* [**tcp-ao**](cmdqueryname=tcp-ao) *tcpAoName*
     
     
     
     TCP-AO authentication is configured.
     
     
     
     The **tcp ao** command must be run to configure a TCP-AO name before you configure MSDP TCP-AO authentication; otherwise, no TCP connection can be set up. TCP-AO authentication must be configured at both ends of MSDP peers and the encryption algorithms and passwords configured for TCP-AO on both peers must be the same; otherwise, no TCP connection can be set up between the MSDP peers and MSDP messages cannot be exchanged.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     TCP-AO, MD5, and keychain authentication modes are mutually exclusive.
* Configure source address-based IGMP Report or Leave message filtering
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic numbered ACL or a naming ACL as needed.
     
     
     + Configure a basic numbered ACL.
       
       1. Run [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ]
          
          A basic numbered ACL is created, and the basic numbered ACL view is displayed.
       2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
          
          Rules are configured for the basic numbered ACL.
     + Configure a naming ACL.
       
       1. Run [**acl**](cmdqueryname=acl) **name** *acl-name* **basic** [ **match-order** { **auto** | **config** } ]
          
          A naming ACL is created, and the naming ACL view is displayed.
       2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
          
          Rules are configured for the naming ACL.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  5. Run [**igmp ip-source-policy**](cmdqueryname=igmp+ip-source-policy) [ *basic-acl-number* | **acl-name** *acl-name* ]
     
     
     
     Source address-based IGMP Report or Leave message filtering is configured.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If an ACL is not configured in this command, the device permits an IGMP Report or Leave message if the message's source address is 0.0.0.0 or if the message's source address is on the same network segment as the address of the interface that receives the message, but discards the message if the message's source address is on a different network segment from the address of the interface that receives the message.
     + If an ACL is configured on an interface, the interface uses configured ACL rules to filter source addresses in IGMP Report or Leave messages.
       - If an IGMP Report or Leave message matches an ACL rule and the action is **permit**, the interface permits this message.
       - If an IGMP Report or Leave message matches an ACL rule and the action is **deny**, the interface denies this message.
       - If an IGMP Report or Leave message does not match any ACL rule, the interface denies this message.
       - If a specified ACL does not exist or does not contain rules, the interface denies all IGMP Report and Leave messages.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure source address-based IGMP Query message filtering
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic numbered ACL or a naming ACL as needed.
     
     
     + Configure a basic numbered ACL.
       
       1. Run [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ]
          
          A basic numbered ACL is created, and the basic numbered ACL view is displayed.
       2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
          
          Rules are configured for the basic numbered ACL.
     + Configure a naming ACL.
       
       1. Run [**acl**](cmdqueryname=acl) **name** *acl-name* **basic** [ **match-order** { **auto** | **config** } ]
          
          A naming ACL is created, and the naming ACL view is displayed.
       2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
          
          Rules are configured for the naming ACL.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  5. Run [**igmp query ip-source-policy**](cmdqueryname=igmp+query+ip-source-policy) { *basic-acl-number* | **acl-name** *acl-name* }
     
     
     
     Source address-based IGMP Query message filtering is configured to control querier election.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If an IGMP Query message matches an ACL rule and the action is **permit**, the interface permits this message.
     + If an IGMP Query message matches an ACL rule and the action is **deny**, the interface denies this message.
     + If an IGMP Query message does not match any ACL rule, the interface denies this message.
     + If a specified ACL does not exist or does not contain rules, the interface denies all IGMP Query messages.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure source address-based MLD Report or Done message filtering.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic numbered ACL6 or a named ACL6 as needed.
     
     
     + Configure a basic numbered ACL6.
       
       1. Run the [**acl ipv6**](cmdqueryname=acl+ipv6) [ **number** ] *basic-acl6-number* [ **match-order** { **auto** | **config** } ] command to create a basic numbered ACL6 and enter the ACL6 view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \* command to configure a rule for the basic numbered ACL6.
     + Configure a named ACL6.
       
       1. Run the [**acl ipv6**](cmdqueryname=acl+ipv6) **name** *acl6-name* **basic** [ **match-order** { **auto** | **config** } ] command to create a named ACL6 and enter its view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \* command to configure a rule for the named ACL6.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  5. Run [**mld ip-source-policy**](cmdqueryname=mld+ip-source-policy) { *basic-acl6-number* | **acl6-name** *acl6-name* }
     
     
     
     Source address-based MLD Report or Done message filtering is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If an MLD Report or Leave message matches an ACL rule and the action is **permit**, the interface permits this message.
     + If an MLD Report or Leave message matches an ACL rule and the action is **deny**, the interface denies this message.
     + If an MLD Report or Leave message does not match any ACL rule, the interface denies this message.
     + If a specified ACL does not exist or does not contain rules, the interface denies all MLD Report and Leave messages.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure source address-based MLD Query message filtering.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic numbered ACL6 or a named ACL6 as needed.
     
     
     + Configure a basic numbered ACL6.
       
       1. Run the [**acl ipv6**](cmdqueryname=acl+ipv6) [ **number** ] *basic-acl6-number* [ **match-order** { **auto** | **config** } ] command to create a basic numbered ACL6 and enter the ACL6 view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \* command to configure a rule for the basic numbered ACL6.
     + Configure a named ACL6.
       
       1. Run the [**acl ipv6**](cmdqueryname=acl+ipv6) **name** *acl6-name* **basic** [ **match-order** { **auto** | **config** } ] command to create a named ACL6 and enter its view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \* command to configure a rule for the named ACL6.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  5. Run [**mld query ip-source-policy**](cmdqueryname=mld+query+ip-source-policy) { *basic-acl6-number* | **acl6-name** *acl6-name* }
     
     
     
     Source address-based MLD Query message filtering is configured to control querier election.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If an MLD Query message matches an ACL rule and the action is **permit**, the interface permits this message.
     + If an MLD Query message matches an ACL rule and the action is **deny**, the interface denies this message.
     + If an MLD Query message does not match any ACL rule, the interface denies this message.
     + If a specified ACL does not exist or does not contain rules, the interface denies all MLD Query messages.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure global IGMP IPsec.
  + Configure IPsec authentication for IGMP messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**igmp**](cmdqueryname=igmp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The IGMP view is displayed.
  3. Run [**ipsec sa**](cmdqueryname=ipsec+sa) *sa-name*
     
     
     
     IGMP IPsec is configured globally, enabling the device to authenticate the sent and received IGMP messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication for IGMP Query messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**igmp**](cmdqueryname=igmp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The IGMP view is displayed.
  3. Run [**query ipsec sa**](cmdqueryname=query+ipsec+sa) *sa-name*
     
     
     
     IGMP IPsec is configured globally, enabling the device to authenticate the sent and received IGMP Query messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**ipsec sa**](cmdqueryname=ipsec+sa) and [**query ipsec sa**](cmdqueryname=query+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.
* Configure IGMP IPsec in the interface view.
  + Configure IPsec authentication for IGMP messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**igmp ipsec sa**](cmdqueryname=igmp+ipsec+sa) *sa-name*
     
     
     
     IGMP IPsec is configured on an interface, enabling the interface to authenticate the sent and received IGMP messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication for IGMP Query messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**igmp query ipsec sa**](cmdqueryname=igmp+query+ipsec+sa) *sa-name*
     
     
     
     IGMP IPsec is configured on an interface, enabling the interface to authenticate the sent and received IGMP Query messages based on the specified SA.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**igmp ipsec sa**](cmdqueryname=igmp+ipsec+sa) and [**igmp query ipsec sa**](cmdqueryname=igmp+query+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.
* Configure global MLD IPsec.
  + Configure IPsec authentication for MLD messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mld**](cmdqueryname=mld)
     
     
     
     The MLD view is displayed.
  3. Run [**ipsec sa**](cmdqueryname=ipsec+sa) *sa-name*
     
     
     
     MLD IPsec is configured globally, enabling the device to authenticate the sent and received MLD messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication for MLD Query messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mld**](cmdqueryname=mld)
     
     
     
     The MLD view is displayed.
  3. Run [**query ipsec sa**](cmdqueryname=query+ipsec+sa) *sa-name*
     
     
     
     MLD IPsec is configured globally, enabling the device to authenticate the sent and received MLD Query messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**ipsec sa**](cmdqueryname=ipsec+sa) and [**query ipsec sa**](cmdqueryname=query+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.
* Configure MLD IPsec in the interface view.
  + Configure IPsec authentication for MLD messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**mld ipsec sa**](cmdqueryname=mld+ipsec+sa) *sa-name*
     
     
     
     MLD IPsec is configured on an interface, enabling the interface to authenticate the sent and received MLD messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  + Configure IPsec authentication for MLD Query messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**mld query ipsec sa**](cmdqueryname=mld+query+ipsec+sa) *sa-name*
     
     
     
     MLD IPsec is configured on an interface, enabling the interface to authenticate the sent and received MLD Query messages based on the specified SA policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the [**mld ipsec sa**](cmdqueryname=mld+ipsec+sa) and [**mld query ipsec sa**](cmdqueryname=mld+query+ipsec+sa) commands are both configured, the command configured later overrides the command configured earlier.
* Configure whitelist session-CAR for PIM.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**whitelist session-car pim**](cmdqueryname=whitelist+session-car+pim) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
     
     
     
     Parameters of whitelist session-CAR for PIM are configured.
  3. (Optional) Run [**whitelist session-car pim disable**](cmdqueryname=whitelist+session-car+pim+disable)
     
     
     
     Whitelist session-CAR for PIM is disabled.
     
     
     
     If the function is abnormal or other services are affected, disable this function. In normal cases, you are advised to keep whitelist session-CAR for PIM enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure whitelist session-CAR for IPv6 PIM.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**whitelist session-car pim-ipv6**](cmdqueryname=whitelist+session-car+pim-ipv6) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
     
     
     
     Parameters of whitelist session-CAR for IPv6 PIM are configured.
  3. (Optional) Run [**whitelist session-car pim-ipv6 disable**](cmdqueryname=whitelist+session-car+pim-ipv6+disable)
     
     
     
     Whitelist session-CAR for IPv6 PIM is disabled.
     
     
     
     If the function is abnormal or other services are affected, disable this function. In normal cases, you are advised to keep whitelist session-CAR for IPv6 PIM enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure whitelist session-CAR for MSDP.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**whitelist session-car msdp**](cmdqueryname=whitelist+session-car+msdp) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
     
     
     
     Parameters of whitelist session-CAR for MSDP are set.
  3. (Optional) Run [**whitelist session-car msdp disable**](cmdqueryname=whitelist+session-car+msdp+disable)
     
     
     
     Whitelist session-CAR for MSDP is disabled.
     
     If this function is abnormal or affects other services, disable this function. In normal cases, you are advised to keep this function enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure micro-isolation CAR for IGMP.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run **micro-isolation protocol-car igmp** { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value*} \*
     
     
     
     Parameters of micro-isolation CAR for IGMP are set.
     
     
     
     In normal cases, you are advised to use the default values of these parameters. *pir-value* must be greater than or equal to *cir-value*, and *pbs-value* must be greater than or equal to *cbs-value*.
  3. (Optional) Run [**micro-isolation protocol-car igmp disable**](cmdqueryname=micro-isolation+protocol-car+igmp+disable)
     
     
     
     Micro-isolation CAR is disabled for IGMP.
     
     
     
     In normal cases, keeping micro-isolation CAR for IGMP enabled is recommended.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure micro-isolation CAR for MLD.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run **micro-isolation protocol-car mld** { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value*} \*
     
     
     
     Parameters of micro-isolation CAR for MLD are set.
     
     
     
     In normal cases, you are advised to use the default values of these parameters. *pir-value* must be greater than or equal to *cir-value*, and *pbs-value* must be greater than or equal to *cbs-value*.
  3. (Optional) Run [**micro-isolation protocol-car mld disable**](cmdqueryname=micro-isolation+protocol-car+mld+disable)
     
     
     
     Micro-isolation CAR is disabled for MLD.
     
     
     
     In normal cases, keeping micro-isolation CAR for MLD enabled is recommended.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Configuration and Maintenance Suggestions

None

#### Verifying the Security Hardening Result

* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **interface** [ *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ] command to check PIM interface information.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **neighbor** [ **interface** *interface-type* *interface-number* | *neighbor-address* | **verbose** ] \* command to check PIM neighbor information.
* Run the [**display mld interface**](cmdqueryname=display+mld+interface) [ *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ] command to check the interface configuration.
* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* ] **interface** [ *interface-type* *interface-number* | **up** | **down** ] **verbose** command to check the detailed configuration on an interface.
* Run the [**display cpu-defend whitelist-v6 session-car**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car) **pimv6** **statistics** **slot** **slot-id** command to check the configuration of whitelist session-CAR for IPv6 PIM on each board.
* Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **msdp** **resource** **slot** *slot-id* command to check statistics about whitelist session-CAR for MSDP on a specified interface board.