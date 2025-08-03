Configuring LDP Keychain Authentication for a TCP Connection
============================================================

LDP keychain authentication can be configured to improve the security of a TCP connection used to establish an LDP session. LDP authentication is configured on LSRs at both ends of an LDP session.

#### Pre-configuration Tasks

To help improve LDP session security, keychain authentication can be configured for a TCP connection over which an LDP session has been established.

During keychain authentication, a group of passwords are defined in the format of a password string, and each password is associated with a specified encryption and decryption algorithm, such as MD5 or secure hash algorithm-1 (SHA-1), and is assigned with a validity period. The system selects a valid password based on the user configuration before sending or receiving a packet. Based on the validity period of the password, the system uses the encryption algorithm matching the password to encrypt the packet before sending it, and uses the decryption algorithm matching the password to decrypt the packet before accepting it. In addition, the system automatically switches to a new valid password based on the password validity period, which minimizes password decryption risks if the password is not changed for a long time.

You can configure either LDP MD5 authentication or LDP keychain authentication as required:

* The MD5 algorithm is easy to configure and generates a single password, which can only be changed manually. MD5 authentication applies to networks requiring short-period encryption.
* Keychain authentication involves a set of passwords, which can be automatically switched based on the configuration. However, keychain authentication is complex to configure and applies to networks requiring high security.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

LDP authentication configurations are prioritized in descending order: for a single peer, for a specified peer group, and for all peers. Keychain authentication and MD5 authentication are mutually exclusive for configurations with the same priority. Keychain authentication and MD5 authentication can be configured simultaneously for LDP peers with different priorities, but only the configuration with a higher priority takes effect for a specified LDP peer. For example, if MD5 authentication is configured for Peer 1 and then keychain authentication is configured for all peers, MD5 authentication remains effective on Peer 1. Keychain authentication takes effect on other peers.

As MD5 is insecure, you are advised to use a more secure authentication mode.


Before configuring LDP keychain authentication for a TCP connection, complete the following task:

* [Configure a global keychain.](dc_vrp_keychain_cfg_0000.html)

#### Procedure

* Configure LDP keychain authentication for a single peer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**authentication key-chain**](cmdqueryname=authentication+key-chain+peer+name) **peer** *peer-id* **name** *keychain-name* LDP keychain authentication is enabled, and the referenced keychain name is specified.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     + Configuring LDP keychain authentication leads to reestablishment of an LDP session and deletes the LSP associated with the session.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure LDP keychain authentication for LDP peers in a specified peer group.
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
* Configure LDP keychain authentication for all LDP peers.
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