Configuring IS-IS Interface Authentication
==========================================

Configuring IS-IS Interface Authentication

#### Context

Interface authentication ensures the validity and correctness of neighbor relationships by allowing interfaces to authenticate the IS-IS Hello packets they receive based on the authentication information carried in the packets. A neighbor relationship can be established between two ends only after the IS-IS Hello packets exchanged between them are authenticated by each other.

![](public_sys-resources/note_3.0-en-us.png) 

For security purposes, you are advised not to use the weak security algorithms in IS-IS. If you need to use such an algorithm, run the [**install feature-software WEAKEA**](cmdqueryname=install+feature-software+WEAKEA) command first to install the weak security algorithm/protocol feature package WEAKEA.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the working mode of the interface from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure an authentication mode as required.
   
   
   * Configure simple authentication.
     ```
     [isis authentication-mode](cmdqueryname=isis+authentication-mode) simple { plain simple-plain | [ cipher ] simple-cipher } [ level-1 | level-2 ] [ ip | osi ] [ send-only ]
     ```
   * Configure HMAC-MD5 authentication.
     ```
     [isis authentication-mode](cmdqueryname=isis+authentication-mode) md5 { [ cipher ] md5-cipher | plain md5-plain } [ level-1 | level-2 ] [ ip | osi ] [ send-only ]
     ```
   * Configure keychain authentication.
     ```
     [isis authentication-mode](cmdqueryname=isis+authentication-mode) keychain keychain-name [ level-1 | level-2 ] [ send-only ]
     ```
   * Configure HMAC-SHA256 authentication.
     ```
     [isis authentication-mode](cmdqueryname=isis+authentication-mode) hmac-sha256 key-id key-id { plain plain | [ cipher ] cipher } [ level-1 | level-2 ] [ send-only ]
     ```
   
   When you select parameters, note the following:
   * If **send-only** is specified, the interface encapsulates authentication information into the Hello packets to be sent, but does not authenticate received Hello packets. Neighbor relationships can be established only if authentication is not performed or IIHs are authenticated.
   * If **send-only** is not specified, ensure that all interfaces on the same network maintain the same password for IIHs of the same level.
   * The **level-1** and **level-2** parameters can be set only on Ethernet interfaces.
   * If the IS-IS interface is a Level-1-2 interface, and neither **level-1** nor **level-2** is specified, the authentication mode and password are configured for both Level-1 and Level-2 Hello packets.![](public_sys-resources/note_3.0-en-us.png) 
     
     Simple or HMAC-MD5 authentication is not recommended if high security is required. To prevent routing information from being tampered with, you are advised to enable authentication and use keychain or HMAC-SHA256 authentication to improve security.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```