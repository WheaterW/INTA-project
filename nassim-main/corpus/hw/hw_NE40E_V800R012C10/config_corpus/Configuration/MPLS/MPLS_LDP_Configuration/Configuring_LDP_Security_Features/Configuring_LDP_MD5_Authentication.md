Configuring LDP MD5 Authentication
==================================

LDP authentication can be configured to improve the security of a connection over which an LDP session is established. LDP authentication is configured on LSRs at both ends of an LDP session.

#### Context

MD5 authentication can be configured for a TCP connection over which an LDP session is established to improve security. Two peers of an LDP session can be configured with different authentication modes but must be configured with the same passwords

LDP MD5 authentication generates a unique digest for an information segment to prevent LDP packets from being modified. LDP MD5 authentication is stricter than TCP checksum verification.

You can configure either LDP MD5 authentication or LDP keychain authentication to match your scenario:

* The MD5 algorithm is easy to configure and generates a single password, which can only be changed manually. MD5 authentication applies to networks requiring short-period encryption.
* Keychain authentication involves a set of passwords, which can be automatically switched based on the configuration. However, keychain authentication is complex to configure and applies to networks requiring high security.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

LDP authentication configurations are prioritized in descending order: for a single peer, for a specified peer group, and for all peers. Both keychain and MD5 authentication can be configured. However, configurations with a higher priority override those with a lower priority, and those with the same priority are mutually exclusive. For example, if MD5 authentication is configured for Peer1 and keychain authentication is configured for all LDP peers, MD5 authentication takes effect on Peer1 and keychain authentication takes effect on other peers.

As MD5 is insecure, you are advised to use a more secure authentication mode.




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