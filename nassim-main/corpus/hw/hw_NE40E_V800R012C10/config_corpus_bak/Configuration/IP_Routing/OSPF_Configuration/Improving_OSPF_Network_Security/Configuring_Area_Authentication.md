Configuring Area Authentication
===============================

OSPF supports packet authentication. With the authentication, only the packets that are authenticated are accepted; if packets fail to be authenticated, a neighbor relationship cannot be established. If area authentication is used, the authentication mode and password configurations on all the interfaces in the area must be identical.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

You are advised to configure authentication to ensure system security.

For security purposes, you are advised not to use weak security algorithms in OSPF. If you need to use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function first.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**area**](cmdqueryname=area) *area-id*
   
   
   
   The OSPF area view is displayed.
4. Configure an authentication mode for the OSPF area as required.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   
   
   
   * Run [**authentication-mode simple**](cmdqueryname=authentication-mode+simple) [ **plain** *plain-text* | [ **cipher** ] *cipher-text* ]
     
     Simple authentication is configured for the OSPF area.
     
     + **plain** indicates the plaintext mode.
     + **cipher** indicates the ciphertext mode. For MD5, HMAC-MD5, or HMAC-SHA256 authentication, **cipher** is used by default.
     
     When configuring an authentication password, you are advised to use the ciphertext mode. If you select the plaintext mode, the password is saved in configuration files in plaintext, which poses a high security risk. To ensure device security, change the password periodically.
   * Run [**authentication-mode**](cmdqueryname=authentication-mode) { **md5** | **hmac-md5** | **hmac-sha256** } [ *key-id* { **plain** *plain-text* | [ **cipher** ] *cipher-text* } ]
     
     Ciphertext authentication is configured for the OSPF area.
     
     + **md5** indicates the MD5 ciphertext authentication mode.
     + **hmac-md5** indicates the HMAC-MD5 ciphertext authentication mode.
     + **hmac-sha256** indicates the HMAC-SHA256 ciphertext authentication mode.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     For the sake of security, using the HMAC-SHA256 algorithm rather than the MD5 or HMAC-MD5 algorithm is recommended.
   * Run [**authentication-mode**](cmdqueryname=authentication-mode) **keychain** *Keychain-Name*
     
     The Keychain authentication is configured for the OSPF area.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Before using the Keychain authentication, run the [**keychain**](cmdqueryname=keychain) command to create a keychain. Then, run the [**key-id**](cmdqueryname=key-id), [**key-string**](cmdqueryname=key-string), and [**algorithm**](cmdqueryname=algorithm) commands to configure a key ID, a password, and an authentication algorithm for this keychain. Otherwise, the OSPF authentication will fail.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.