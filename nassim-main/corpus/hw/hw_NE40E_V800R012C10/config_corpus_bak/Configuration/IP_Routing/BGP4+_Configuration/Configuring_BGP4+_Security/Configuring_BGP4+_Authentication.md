Configuring BGP4+ Authentication
================================

BGP4+ authentication can be configured to enhance security of BGP networks.

#### Usage Scenario

BGP4+ authentication includes MD5, TCP-AO, and keychain authentication.

* MD5 authentication
  
  BGP uses TCP as the transport protocol and considers a packet valid if the source address, destination address, source port, destination port, and TCP sequence number of the packet are correct. However, most parameters in a packet are easily accessible to attackers. To protect BGP against attacks, configure MD5 authentication for TCP connections established between BGP peers.
  
  To prevent an MD5 password configured for a BGP peer from being cracked, change the password periodically.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.
  
  The MD5 algorithm is not recommended if high security is required.
* Keychain authentication
  
  A keychain consists of multiple authentication keys, each of which contains an ID and a password. Each key in a keychain has a lifecycle, and keys are dynamically selected based on the lifecycle of each key. After a keychain with the same rules is configured on the two ends of a BGP connection, the keychains can dynamically select authentication keys to enhance BGP attack defense.
* TCP-AO authentication
  
  The TCP authentication option (TCP-AO) is used to authenticate received and to-be sent packets during TCP session establishment and data exchange. It supports packet integrity check to prevent TCP replay attacks. TCP-AO authentication improves the security of the TCP connection between BGP peers and is applicable to the network that requires high security.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

BGP MD5 authentication and BGP keychain authentication are mutually exclusive.




#### Pre-configuration Tasks

Before configuring BGP4+ authentication, [configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).


#### Procedure

1. Configure MD5 authentication.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**peer**](cmdqueryname=peer) { *group-name* | *ipv6âaddress* } [**password**](cmdqueryname=password+cipher+simple) { **cipher** *cipher-password* | **simple** *simple-password* } command to configure an MD5 authentication password.
      
      
      
      In BGP4+ MD5 authentication, only the MD5 authentication password is set for the TCP connection, and the authentication is performed by TCP. If authentication fails, no TCP connection can be established.
      
      When setting a password, you can select either of the following input modes:
      
      * **cipher** *cipher-password*: indicates that a password is set using a ciphertext string.
      * **simple** *simple-password*: indicates that a password is set using a cleartext string.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        + It is recommended that the new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters, except the question mark (?) and space.
        + For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Configure keychain authentication.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**peer**](cmdqueryname=peer) { *group-name* | *ipv6âaddress* } [**keychain**](cmdqueryname=keychain) *keychain-name* command to configure keychain authentication.
      
      
      
      You must configure keychain authentication for TCP-based applications on both BGP peers. Note that encryption algorithms and passwords configured for keychain authentication on both peers must be the same; otherwise, a TCP connection cannot be set up between the BGP peers and BGP messages cannot be exchanged.
      
      The keychain specified by *keychain-name* must exist when you configure BGP4+ keychain authentication; otherwise, the TCP connection cannot be established. For keychain configuration details, see "Keychain Configuration" in *HUAWEI NE40E-M2 series Configuration Guide > Security*.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
3. Configure TCP-AO authentication.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**tcp ao**](cmdqueryname=tcp+ao)*tcpaoname* command to create a TCP-AO and enter the TCP-AO policy view.
   3. Run the [**binding keychain**](cmdqueryname=binding+keychain)*kcName* command to bind the TCP-AO to a keychain.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Before performing this step, complete [configuring basic keychain functions](dc_vrp_keychain_cfg_0005.html) in [Pre-configuration Tasks](dc_vrp_bgp_cfg_3062.html#EN-US_TASK_0172366284__context137663429214038) to create a keychain.
   4. Run the [**key-id**](cmdqueryname=key-id) *keyId* command to create a key ID for the TCP-AO and enter the TCP-AO key ID view.
   5. Run the [**send-id**](cmdqueryname=send-id+receive-id) *sndId* **receive-id***rcvId* command to configure send-id and receive-id for the Key ID.
   6. Run the [**quit**](cmdqueryname=quit) command to return to the upper-level view.
   7. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   8. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   9. Run the [**peer**](cmdqueryname=peer) *ipv6-address* [**as-number**](cmdqueryname=as-number) *as-number* command to specify the IP address of a peer and the number of the AS where the peer resides.
   10. Run the [**peer**](cmdqueryname=peer+tcp-ao+policy) *ipv6-address* **tcp-ao policy** *tcp-ao-name* command to configure TCP-AO authentication for the TCP connection to be set up between BGP peers. The value of the *tcp-ao-name* parameter must be set to the TCP-AO created in step 2.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       For the same peer, the authentication modes TCP-AO, MD5, and keychain are mutually exclusive.
   11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

# A peer relationship can be set between two peers that have the same authentication information. Run the [**display bgp ipv6 peer**](cmdqueryname=display+bgp+ipv6+peer) command to check the peer relationship status.