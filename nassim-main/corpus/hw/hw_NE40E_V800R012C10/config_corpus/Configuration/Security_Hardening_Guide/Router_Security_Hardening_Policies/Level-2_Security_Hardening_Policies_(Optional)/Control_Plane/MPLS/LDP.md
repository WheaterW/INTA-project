LDP
===

LDP

#### Security Policy

* LDP MD5 authentication
  
  Message-Digest Algorithm 5 (MD5) is a digest algorithm defined in relevant standards. MD5 is typically used to calculate a message digest to prevent message spoofing. The MD5 message digest is a unique result calculated using an irreversible character string conversion. If a message is modified during transmission, a different digest is calculated. In this way, after a message arrives at the receive end, the receive end determines that the message has been modified during transmission if the newly calculated digest is different from the carried digest.
  
  LDP MD5 authentication identifies LDP message modification by generating unique message digest for the same information segment. It is stricter than common TCP checksum-based authentication.
  
  LDP MD5 authentication is performed before LDP messages are sent over TCP. A unique message digest is added following the TCP header in a message. The message digest is calculated using the MD5 algorithm based on the TCP header, LDP message, and user-defined password.
  
  When receiving the message, the receive end obtains the TCP header, message digest, and LDP message. MD5 generates the message digest based on the TCP header, LDP message and the locally saved password. Then, it compares the calculated message digest with the message digest carried in the LDP message. If they are different, the receive end interprets the LDP message as having been tampered with.
  
  A password can be set either in non-ciphertext or ciphertext. These two modes differ in how passwords are recorded in the configuration file. In non-ciphertext mode, a user-defined password is directly recorded in the configuration file; however, in ciphertext mode, a password is encrypted using a special algorithm and then recorded in the configuration file.
  
  Characters set by users are used in digest calculation, regardless of whether a password is recorded in non-ciphertext or ciphertext mode. Although the conversion algorithms of the non-ciphertext and ciphertext are proprietary to different vendors, those proprietary algorithms become transparent to other vendors by this way.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  As MD5 is insecure, you are advised to use a more secure authentication mode.
* LDP keychain authentication
  
  Keychain is an enhanced encryption algorithm. Similar to MD5, it calculates a digest for a piece of information to prevent LDP packets from being tampered with.
  
  Keychain allows users to define a group of passwords to form a password string. Each password is assigned encryption and decryption algorithms, such as MD5 and secure hash algorithm-1 (SHA-1), and a validity period. The system selects a valid password before sending or receiving a packet. Within the validity period of the password, the system uses the encryption algorithm matching the password to encrypt the packet before sending it. The system also uses the decryption algorithm matching the password to decrypt the packet before accepting the packet. In addition, the system can automatically use a new password after the previous password expires, preventing the password from being decrypted.
  
  The password of keychain authentication, the encryption and decryption algorithms, and the expiration period of the password can be configured separately on a keychain configuration node. A keychain configuration node at least requires one password and has the encryption and decryption algorithms specified.
  
  To reference a keychain configuration node, specify a peer IP address and a node name in the MPLS-LDP view. The keychain configuration node is then used to encrypt an LDP session. Multiple peers can reference the same keychain configuration node.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  LDP authentication configurations are prioritized in descending order: for a single peer, for a specified peer group, for all peers. Keychain and MD5 configurations of the same priority are mutually exclusive. Keychain or MD5 authentication can be configured simultaneously for a specified LDP peer, for the peer group of this LDP peer, and for all LDP peers. The configuration with a higher priority takes effect. For example, if MD5 authentication is configured for Peer1 and then keychain authentication is configured for all LDP peers, MD5 authentication takes effect on Peer1. Keychain authentication takes effect on other peers.
  
  You can configure either LDP MD5 authentication or LDP keychain authentication in a specific scenario:
  + The MD5 algorithm is easy to configure and generates a single password which can only be changed manually. MD5 authentication applies to networks requiring short-period encryption.
  + Keychain authentication involves a set of passwords and uses a new password each time the previous one expires. Keychain authentication is complex to configure and applies to networks requiring high security.
* LDP GTSM
  
  LDP GTSM is the application of the GTSM in LDP.
  
  GTSM determines whether a packet is valid by checking its TTL. This protects devices from attacks. GTSM for LDP involves applying GTSM to LDP messages between adjacent devices or devices close to each other (based on the number of next hops). A TTL value range is then set. The LDP messages with TTLs not within the specified value range are interpreted as attack messages and discarded.
* LDP TCP-AO authentication
  
  The TCP Authentication Option (TCP-AO) is used to authenticate received and to-be sent packets during TCP session establishment and data exchange. It supports packet integrity check to prevent TCP replay attacks.

#### Attack Methods

None.



#### Procedure

* Configure LDP MD5 authentication for a single LDP peer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**md5-password**](cmdqueryname=md5-password+plain+cipher) { **plain** | **cipher** } *peer-lsr-id* *password*
     
     
     
     MD5 authentication is enabled, and an authentication password is set.
     
     
     
     For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters, except the question mark (?) and space.
     + For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password.
     
     A password can be set either in non-ciphertext or ciphertext. These two modes differ in how passwords are recorded in the configuration file. In non-ciphertext mode, a user-defined password is directly recorded in the configuration file; however, in ciphertext mode, a password is encrypted using a special algorithm and then recorded in the configuration file.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     + If you configure a password in non-ciphertext, the password will be saved in the same way in the configuration file. The non-ciphertext mode has high security risks, and therefore the ciphertext mode is recommended. In addition, change the password periodically.
     + Configuring LDP MD5 authentication causes an LDP session to be reestablished and deletes the LSP associated with the original LDP session.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure LDP MD5 authentication for LDP peers in a specified LDP peer group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**md5-password**](cmdqueryname=md5-password+plain+cipher+peer-group) { **plain** | **cipher** } **peer-group** *ip-prefix-name* *password*
     
     
     
     MD5 authentication is enabled for a specified peer group, and an authentication password is set.
     
     
     
     An IP prefix list can be specified using *ip-prefix-name* to define the range of peer IP addresses in a peer group. Ensure that the IP prefix list specified by *ip-prefix-name* has been configured before this step is performed.
     
     For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters, except the question mark (?) and space.
     + For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password.
  4. (Optional) Run [**authentication exclude**](cmdqueryname=authentication+exclude+peer) **peer** *peer-id*
     
     
     
     The device is disabled from authenticating a specified LDP peer.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure LDP MD5 authentication for all LDP peers.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**md5-password**](cmdqueryname=md5-password+plain+cipher+all) { **plain** | **cipher** } **all** *password*
     
     
     
     MD5 authentication is enabled for all peers, and an authentication password is set.
     
     
     
     For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters, except the question mark (?) and space.
     + For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password.
  4. (Optional) Run [**authentication exclude**](cmdqueryname=authentication+exclude+peer) **peer** *peer-id*
     
     
     
     The device is disabled from authenticating a specified LDP peer.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure LDP keychain authentication for a specified LDP peer based on the TCP connection.
  
  
  
  Before configuring LDP keychain authentication, configure keychain globally. For details, see *NE40E Configuration Guide - Security*.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**authentication key-chain**](cmdqueryname=authentication+key-chain+peer+name) **peer** *peer-id* **name** *keychain-name* LDP keychain authentication is enabled, and the referenced keychain name is specified.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     + Configuring LDP keychain authentication leads to reestablishment of an LDP session and deletes the LSP associated with the session.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure LDP keychain authentication for LDP peers in a specified LDP peer group based on the TCP connection.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**authentication key-chain peer-group**](cmdqueryname=authentication+key-chain+peer-group+name) *ip-prefix-name* **name** *keychain-name*
     
     
     
     LDP keychain authentication is enabled for a specified peer group, and the configured keychain name is referenced.
     
     
     
     The range of peer IP addresses in a peer group is defined by the IP prefix list *ip-prefix-name*. Therefore, you need to configure an IP prefix list named *ip-prefix-name* before you perform this step.
  4. (Optional) Run [**authentication exclude**](cmdqueryname=authentication+exclude+peer) **peer** *peer-id*
     
     
     
     The device is disabled from authenticating a specified LDP peer.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure LDP keychain authentication for all LDP peers based on the TCP connection.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**authentication key-chain all**](cmdqueryname=authentication+key-chain+all+name) **name** *keychain-name*
     
     
     
     LDP keychain authentication is enabled for all LDP peers, and the configured keychain name is referenced.
  4. (Optional) Run [**authentication exclude**](cmdqueryname=authentication+exclude+peer) **peer** *peer-id*
     
     
     
     The device is disabled from authenticating a specified LDP peer.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure LDP keychain authentication for a specified LDP peer based on the UDP connection.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**gtsm peer**](cmdqueryname=gtsm+peer) *ip-address* **valid-ttl-hops** *hops*
     
     
     
     LDP GTSM is configured.
     
     
     
     After the configuration is successful, the configured keychain authentication takes effect on the specified peer. If the authentication fails, the LDP session cannot be established.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     This command supports only the keychain authentication using a strong encryption algorithm (such as SHA-256, HMAC-SHA-256, HMAC-SHA-384, HMAC-SHA-512, or SM3) but not a weak encryption algorithm.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure LDP GTSM.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**gtsm peer**](cmdqueryname=gtsm+peer) *ip-address* **valid-ttl-hops** *hops*
     
     
     
     LDP GTSM is configured.
     
     
     
     If the value of hops is set to the maximum number of valid hops permitted by GTSM, when the TTL values carried in the packets sent by an LDP peer are within the range [255 â hops + 1, 255], the packets are accepted; otherwise, the packets are discarded.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure LDP TCP-AO authentication.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**tcp ao**](cmdqueryname=tcp+ao)*tcpaoname*
     
     
     
     A TCP-AO is created and its view is displayed.
  3. Run [**binding keychain**](cmdqueryname=binding+keychain)*kcName*
     
     
     
     A keychain is bound to the TCP-AO.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Before performing this step, complete "Configuring Keychain Authentication Globally" to create a keychain.
  4. Run [**key-id**](cmdqueryname=key-id) *keyId*
     
     
     
     A key ID for the TCP-AO is created and the TCP-AO key ID view is displayed.
  5. Run [**send-id**](cmdqueryname=send-id) *sndId* **receive-id***rcvId*
     
     
     
     The send-id and receive-id for the key ID are configured.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the upper-level view.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  8. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  9. Run [**authentication tcp-ao**](cmdqueryname=authentication+tcp-ao) **peer***peer-id* **name** *tcpaoname*
     
     
     
     The TCP-AO authentication for LDP is enabled.
     
     
     
     The value of *tcpaoname* must be the same as that of the TCP-AO created in Step 2.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     For the same peer, the authentication modes TCP-AO, MD5, and keychain are mutually exclusive.
     
     Configuring LDP TCP-AO authentication may cause the reestablishment of LDP sessions.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Security Hardening Result

* Run the [**display mpls ldp session**](cmdqueryname=display+mpls+ldp+session) **verbose** command to check LDP MD5 authentication, LDP keychain authentication, and LDP TCP-AO authentication configurations.
* Run the [**display gtsm statistics**](cmdqueryname=display+gtsm+statistics) { *slot-id* | **all** } command to check GTSM statistics.