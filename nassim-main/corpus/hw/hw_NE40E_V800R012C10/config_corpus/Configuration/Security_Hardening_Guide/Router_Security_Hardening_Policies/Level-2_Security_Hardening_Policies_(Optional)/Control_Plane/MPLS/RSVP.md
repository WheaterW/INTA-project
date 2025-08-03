RSVP
====

RSVP

#### Security Policy

RSVP transmits packets using raw IP, which does not ensure security. In raw IP, packets are easily tampered with, and devices can be easily attacked. Digests of RSVP messages are verified to protect them from being tampered with and forgery attacks, enhancing network reliability and security.

* Basic principles
  
  The same key must be configured on both nodes involved in authentication. When sending a packet, a node generates a digest using the HMAC-MD5 algorithm based on a configured key. The digest is carried in the packet as an integrity object to the peer node. The peer node generates a digest using the same algorithm based on the configured key and compares the two digests. If the two digests are the same, it accepts the packet; otherwise, it discards the packet. RSVP authentication, however, cannot prevent replay attacks or handle neighbor relationship termination problems resulting from out-of-sequence RSVP messages. To resolve these issues, RSVP authentication extensions are used. RSVP authentication extensions include the authentication lifetime, authentication handshake mechanism, and sliding window mechanism, in addition to the original authentication mechanism. They can improve RSVP security and enhance user authentication in adverse network environments, such as congested networks.
* RSVP key management modes
  
  RSVP supports two key management modes:![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  HMAC-MD5 authentication provides low security. To ensure high security, you are advised to use keychain authentication and a high-security algorithm, such as HMAC-SHA-256.
  
  
  + HMAC-MD5
    
    Users can enter non-ciphertext or ciphertext keys on RSVP interfaces and neighbors. The key algorithm is HMAC-MD5. The features of this mode are as follows:
    
    1. A key cannot be shared. Each protocol is configured with a separate key.
    2. Only one key can be assigned to each interface and neighbor. To change the key, you have to reconfigure one.
  + Keychain
    
    Keychain is an enhanced encryption algorithm. It allows users to define a group of passwords as a password string. An encryption/decryption algorithm and a validity period are defined for each password. The system selects a valid password, encrypts packets before sending them, and decrypts packets when receiving them using the encryption/decryption algorithm matching the selected password. In addition, the system can automatically use a new password after the previous password expires, preventing the password from being decrypted.
    
    The features of this mode are as follows:
    
    1. The password of keychain authentication, the encryption and decryption algorithms, and the expiration period of the password can be configured separately on a keychain configuration node. A keychain configuration node at least requires one password and has the encryption and decryption algorithms specified.
    2. Keychain settings can be shared by protocols and managed uniformly.
       
       In RSVP, a keychain can be referenced on interfaces or neighbors.
* RSVP authentication modes
  
  RSVP supports two authentication modes:
  
  + Neighbor-oriented authentication
    
    In this mode, you can configure authentication information, such as authentication keys based on different neighbor addresses. RSVP then authenticates each neighbor.
    
    Neighbor-oriented authentication can be configured in either of the following ways:
    
    1. The IP address of an interface on an RSVP neighboring node is used as an RSVP neighbor address.
    2. The LSR ID of an RSVP neighboring node is used as an RSVP neighbor address.
  + Interface-oriented authentication
    
    If interface-oriented authentication is configured, RSVP authenticates packets based on their inbound interfaces.
  
  Neighbor-oriented authentication takes precedence over interface-oriented authentication. Packets that do not pass authentication are discarded. If neighbor-oriented authentication is not enabled, interface-oriented authentication takes effect.

#### Attack Methods

The most common attacks and prevention methods are as follows:

* Replay attacks
  
  When processing packets, RSVP checks various information, including parameters, formats, and types. The information can be easily obtained by attackers. Therefore, attackers can intercept RSVP packets and repeatedly send packets to the device to increase the load of the device. Object verification is added to RSVP messages to protect the messages from being tampered with and forgery attacks, enhancing network reliability and security.
* Error packet attacks
  
  Attackers construct various types of error packets, such as super long packets, packets with incorrect headers, packets of incorrect lengths, and packets with invalid next hops, to initiate attacks. RSVP uses strict rules for outgoing packets. It discards error packets without ending neighbor relationships, ensuring service continuity. It does not accept or advertise packets with serious errors, such as extremely long packets or invalid packet types.


#### Procedure

* Configure RSVP key authentication in neighbor address-based mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which the MPLS TE tunnel is established is displayed.
  3. Run [**mpls rsvp-te authentication**](cmdqueryname=mpls+rsvp-te+authentication) { { **cipher** | **plain** } *auth-key* | **keychain** *keychain-name* }
     
     
     
     The key for RSVP authentication is configured.
     
     HMAC-MD5 or keychain authentication can be configured based on the selected parameter:
     
     + **cipher**: HMAC-MD5 authentication is used, and a key is displayed in ciphertext.
     + **plain**: HMAC-MD5 authentication is used, and a key is displayed in simple text.
     + **keychain**: Keychain authentication is used, and a globally configured keychain is referenced.![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     If you select the **plain** mode in authentication key configuration, the password is saved in the configuration file in plaintext. Because this mode has high security risks, you are advised to select the **cipher** mode. To improve the device security, periodically change the password.
     
     It is recommended that the password contain uppercase letters, lowercase letters, digits, and special characters.
     
     HMAC-MD5 authentication provides low security. To ensure high security, you are advised to use keychain authentication and a high-security algorithm, such as HMAC-SHA-256.
     
     The configuration must be completed on the two directly connected interfaces within three update periods. If the configuration is not completed after three update periods elapse, the session goes down.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure RSVP key authentication in neighbor-based mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. (Optional) Run [**mpls rsvp-te challenge-lost**](cmdqueryname=mpls+rsvp-te+challenge-lost) *max-miss-times*
     
     
     
     The maximum number of Challenge messages allowed to be dropped when being sent from the authenticated end to the authenticator end during RSVP-TE authentication is configured.
  4. (Optional) Run [**mpls rsvp-te retrans-timer challenge**](cmdqueryname=mpls+rsvp-te+retrans-timer+challenge) *retransmission-interval*
     
     
     
     The interval at which challenge messages are retransmitted is set.
  5. Run [**mpls rsvp-te peer**](cmdqueryname=mpls+rsvp-te+peer) *peer-address*
     
     
     
     The RSVP neighbor view is displayed.
  6. Run [**mpls rsvp-te authentication**](cmdqueryname=mpls+rsvp-te+authentication) { { **cipher** | **plain** } *auth-key* | **keychain** *keychain-name* }
     
     
     
     The key for RSVP authentication is configured.
     
     HMAC-MD5 or keychain authentication can be configured based on the selected parameter:
     
     + **cipher**: HMAC-MD5 authentication is used, and a key is displayed in ciphertext.
     + **plain**: HMAC-MD5 authentication is used, and a key is displayed in simple text.
     + **keychain**: Keychain authentication is used, and a globally configured keychain is referenced.![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     If you select the **plain** mode in authentication key configuration, the password is saved in the configuration file in plaintext. Because this mode has high security risks, you are advised to select the **cipher** mode. To improve the device security, periodically change the password.
     
     HMAC-MD5 authentication provides low security. To ensure high security, you are advised to use keychain authentication and a high-security algorithm, such as HMAC-SHA-256.
     
     It is recommended that the password contain uppercase letters, lowercase letters, digits, and special characters.
     
     The configuration must be completed on the two neighboring nodes within three update periods. If the configuration is not completed after three update periods elapse, the session goes down.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure the lifetime of the key authentication between directly connected interfaces of RSVP neighbors.
  
  
  
  When no CR-LSP is reachable between RSVP neighbors, they can keep the neighbor relationship until the configured TTL of RSVP authentication elapses. The configured TTL of RSVP authentication does not affect existing CR-LSPs.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The view of an RSVP-enabled interface is displayed.
  3. Run [**mpls rsvp-te authentication lifetime**](cmdqueryname=mpls+rsvp-te+authentication+lifetime) *lifetime*
     
     
     
     The RSVP authentication lifetime is set.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure RSVP authentication lifetime in the MPLS RSVP-TE peer view
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls rsvp-te peer**](cmdqueryname=mpls+rsvp-te+peer) *peer-addr*
     
     
     
     The MPLS RSVP-TE peer view is displayed.
     
     If *peer-addr* is an interface IP address of the neighbor, not the neighbor LSR ID, key authentication will only take effect on that neighbor interface. Key authentication then provides high security and has the highest priority.
     
     If *peer-addr* is a neighbor LSR ID, key authentication will take effect on all interfaces on the neighbor. Authentication configured using this method has a lower priority than that configured based on the neighbor's interface IP address but has a higher priority than that configured in the interface view.
  4. Run [**mpls rsvp-te authentication lifetime**](cmdqueryname=mpls+rsvp-te+authentication+lifetime) *lifetime*
     
     
     
     The RSVP authentication lifetime is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure the handshake function in the interface view
  
  
  
  The handshake function helps RSVP key authentication prevent replay attacks.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     Return to the system view.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The view of the interface on which the MPLS TE tunnel is established is displayed.
  3. Run [**mpls rsvp-te authentication handshake**](cmdqueryname=mpls+rsvp-te+authentication+handshake)
     
     
     
     The handshake function is enabled.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The task of "Configuring an RSVP Authentication Mode" must be complete before the RSVP handshake function is configured.
     
     The handshake function helps a device to establish an RSVP neighbor relationship with its neighbor. If a device receives RSVP messages from a neighbor, with which the device has not established an RSVP authentication relationship, the device will send Challenge messages carrying local identifier to this neighbor. After receiving the Challenge messages, the neighbor returns Response messages carrying the identifier the same as that in the Challenge messages. After receiving the Response messages, the local end checks identifier carried in the Response messages. If identifier in the Response messages is the same as the local one, the device determines to establish an RSVP authentication relationship with its neighbor.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure the handshake function in the MPLS RSVP-TE peer view
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls rsvp-te peer**](cmdqueryname=mpls+rsvp-te+peer) *peer-addr*
     
     
     
     The MPLS RSVP-TE neighbor view is displayed.
     
     
     
     + If *ip-address* is set to an interface IP address of a neighbor, not the neighbor LSR ID, the handshake function will only take effect on that neighbor interface.
     + If *ip-address* is set to a neighbor LSR ID, the handshake function will take effect on all interfaces of the neighbor.
  4. Run [**mpls rsvp-te authentication handshake**](cmdqueryname=mpls+rsvp-te+authentication+handshake)
     
     
     
     The handshake function is enabled.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The task of "Configuring an RSVP Authentication Mode" must be complete before the RSVP handshake function is configured. The handshake can only take effect after it is configured on both ends of an RSVP authentication relationship.
     
     The handshake function helps a device to establish an RSVP neighbor relationship with its neighbor. If a device receives RSVP messages from a neighbor, with which the device has not established an RSVP authentication relationship, the device will send Challenge messages carrying local identifier to this neighbor. After receiving the Challenge messages, the neighbor returns Response messages carrying the identifier the same as that in the Challenge messages. After receiving the Response messages, the local end checks identifier carried in the Response messages. If identifier in the Response messages is the same as the local one, the device determines to establish an RSVP authentication relationship with its neighbor.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the handshake function is configured between neighbors and the lifetime is configured, the lifetime must be greater than the interval at which RSVP update messages are sent. If the lifetime is smaller than the interval at which RSVP update messages are sent, authentication relationships may be deleted because no RSVP update message is received within the lifetime. As a result, the handshake mechanism is used again when a new update message is received. An RSVP-TE tunnel may be deleted or fail to be established.
* (Optional) Configure the message window function in the interface view
  
  
  
  The message window function prevents RSVP message mis-sequence.
  
  The default window size is 1. This allows a local device to store only the largest sequence number of the latest RSVP message sent by a neighbor node.
  
  If the window size is greater than 1, the local device stores several latest valid sequence numbers.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which the MPLS TE tunnel is established is displayed.
  3. Run [**mpls rsvp-te authentication handshake**](cmdqueryname=mpls+rsvp-te+authentication+handshake)
     
     
     
     The handshake function is enabled.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The task of "Configuring an RSVP Authentication Mode" must be complete before the RSVP handshake function is configured. The handshake can only take effect after it is configured on both ends of an RSVP authentication relationship.
  4. Run [**mpls rsvp-te authentication window-size**](cmdqueryname=mpls+rsvp-te+authentication+window-size) *window-size*
     
     
     
     The message window function is configured.
     
     
     
     The value is the number of valid sequence numbers of received RSVP messages that can be stored.
     
     If RSVP is enabled on a trunk interface, only one neighbor relationship is established on the trunk interface between RSVP neighbors. This means any trunk member interface receives RSVP messages in a random order, which results in message mis-sequence. An RSVP message sliding window is configured to address this problem. If the sliding window is too small, received out-of-order RSVP messages outside the window size are discarded, which terminates the RSVP neighbor relationship.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure the message window function in the MPLS RSVP-TE peer view
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls rsvp-te peer**](cmdqueryname=mpls+rsvp-te+peer) *peer-addr*
     
     
     
     The MPLS RSVP-TE peer view is displayed.
     
     
     
     + If *peer-addr* is set to an interface IP address of a neighbor, not the neighbor LSR ID, the message window will only take effect on that interface of the neighbor.
     + If *peer-addr* is set to a neighbor LSR ID, the message window will take effect on all interfaces of the neighbor.
  4. Run [**mpls rsvp-te authentication handshake**](cmdqueryname=mpls+rsvp-te+authentication+handshake)
     
     
     
     The handshake function is enabled.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The task of "Configuring an RSVP Authentication Mode" must be complete before the RSVP handshake function is configured. The handshake can only take effect after it is configured on both ends of an RSVP authentication relationship.
  5. Run [**mpls rsvp-te authentication window-size**](cmdqueryname=mpls+rsvp-te+authentication+window-size) *window-size*
     
     
     
     The message window function is configured. The value is the number of valid sequence numbers of received RSVP messages that can be stored.
     
     If RSVP is enabled on a trunk interface, only one neighbor relationship is established on the trunk interface between RSVP neighbors. This means any trunk member interface receives RSVP messages in a random order, which results in message mis-sequence. An RSVP message sliding window is configured to address this problem. If the sliding window is too small, received out-of-order RSVP messages outside the window size are discarded, which terminates the RSVP neighbor relationship.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

* Run the [**display mpls rsvp-te**](cmdqueryname=display+mpls+rsvp-te) command to check RSVP-TE configurations on a specific interface.
* Run the [**display mpls rsvp-te peer**](cmdqueryname=display+mpls+rsvp-te+peer) [ **interface** *interface-type interface-number* | *peer-address* ] command to check RSVP-TE neighbor information on an RSVP-TE-enabled interface.