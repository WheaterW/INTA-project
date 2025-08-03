Configuring Interface Authentication
====================================

Interface authentication takes effect between neighboring devices' interfaces on which an authentication mode and password are configured. Interface authentication takes precedence over area authentication. Interfaces on the same network segment must have the same authentication mode and password. Interfaces on different network segments can have different authentication modes and passwords.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

You are advised to configure authentication to ensure system security.

For security purposes, you are advised not to use weak security algorithms in OSPF. If you need to use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function first.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The OSPF interface view is displayed.
3. Configure an interface authentication mode as required.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   
   
   
   * Run [**ospf authentication-mode**](cmdqueryname=ospf+authentication-mode) **simple** [ **plain** *plain-text* | [ **cipher** ] *cipher-text* ]
     
     Simple authentication is configured for the OSPF interface.
     
     + **simple** indicates simple authentication.
     + **plain** indicates the plaintext mode. In simple authentication mode, if this parameter is not specified, the **cipher** type is used by default.
     + **cipher** indicates the ciphertext mode. For MD5, HMAC-MD5, or HMAC-SHA256 authentication, **cipher** is used by default.
     
     When configuring an authentication password, you are advised to use the ciphertext mode. If you select the plaintext mode, the password is saved in configuration files in plaintext, which poses a high security risk. To ensure device security, change the password periodically.
   * Run [**ospf authentication-mode**](cmdqueryname=ospf+authentication-mode) { **md5** | **hmac-md5** | **hmac-sha256** } [ *key-id* { **plain** *plain-text* | [ **cipher** ] *cipher-text* } ]
     
     Ciphertext authentication is configured for the OSPF interface.
     
     + **md5** indicates the MD5 ciphertext authentication mode.
     + **hmac-md5** indicates the HMAC-MD5 ciphertext authentication mode.
     + **hmac-sha256** indicates the HMAC-SHA256 ciphertext authentication mode.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     For the sake of security, using the HMAC-SHA256 algorithm rather than the MD5 or HMAC-MD5 algorithm is recommended.
   * Run [**ospf authentication-mode**](cmdqueryname=ospf+authentication-mode) **keychain** *keychain-name*
     
     The Keychain authentication is configured for the OSPF interface.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Before using keychain authentication, run the [**keychain**](cmdqueryname=keychain) command to create a keychain. Then, run the [**key-id**](cmdqueryname=key-id), [**key-string**](cmdqueryname=key-string), and [**algorithm**](cmdqueryname=algorithm) commands to configure a key ID, a password, and an authentication algorithm, respectively, for this keychain. Otherwise, the OSPF authentication will fail.
   * Run [**ospf authentication-mode**](cmdqueryname=ospf+authentication-mode) **null**
     
     The OSPF interface does not perform authentication.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.