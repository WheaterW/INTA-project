Configuring MSDP Peer Authentication
====================================

Configuring MSDP Peer Authentication

#### Context

MSDP peer authentication modes include MSDP Message-Digest Algorithm 5 (MD5) authentication, TCP-AO authentication, and keychain authentication.

By default, no authentication mode is configured for an MSDP peer. You are advised to configure an authentication mode to ensure system security.


#### Procedure

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
* Configure TCP-AO authentication.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The MSDP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *peer-address* [**tcp-ao**](cmdqueryname=tcp-ao) *tcpAoName*
     
     
     
     TCP-AO authentication is configured.
     
     
     
     The **tcp ao** command must be run to configure a TCP-AO name before you configure MSDP TCP-AO authentication; otherwise, no TCP connection can be set up. TCP-AO authentication must be configured at both ends of MSDP peers and the encryption algorithms and passwords configured for TCP-AO on both peers must be the same; otherwise, no TCP connection can be set up between the MSDP peers and MSDP messages cannot be exchanged.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     TCP-AO, MD5, and keychain authentication modes are mutually exclusive.