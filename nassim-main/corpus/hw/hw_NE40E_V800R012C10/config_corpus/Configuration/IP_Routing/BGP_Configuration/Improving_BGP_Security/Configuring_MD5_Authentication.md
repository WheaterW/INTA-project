Configuring MD5 Authentication
==============================

In MD5 authentication, a Message Digest 5 (MD5) authentication password is set for a TCP connection, and the MD5 authentication is performed by TCP. If authentication fails, no TCP connection will be established.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.

The encryption algorithm used for MD5 authentication is insecure and poses security risks. As such, you are advised to use a more secure encryption algorithm.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**password**](cmdqueryname=password+cipher) { **cipher** *cipher-password* | **simple** *simple-password* }
   
   
   
   An MD5 authentication password is configured.
   
   
   
   The password can be set in either of the following modes:
   
   * **cipher** *cipher-password*: indicates that a password is set using a ciphertext string.
   * **simple** *simple-password*: indicates that a password is set using a cleartext string.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If MD5 authentication is configured in the BGP view, the configuration also takes effect in extended BGP address family views because they use the same TCP connection. BGP MD5 authentication and BGP keychain authentication are mutually exclusive.
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * It is recommended that the new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters, except the question mark (?) and space.
   * For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After completing the configuration, verify it.

Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) [ *ipv4-address* ] **verbose** command to view the authentication information about BGP peers.