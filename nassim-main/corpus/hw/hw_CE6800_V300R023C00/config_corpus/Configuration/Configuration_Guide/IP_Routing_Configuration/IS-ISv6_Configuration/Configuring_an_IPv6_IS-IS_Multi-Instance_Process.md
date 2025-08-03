Configuring an IPv6 IS-IS Multi-Instance Process
================================================

Configuring an IPv6 IS-IS Multi-Instance Process

#### Context

On an IPv6 IS-IS network, IPv6 IS-IS multi-instance processes need to be used to isolate different access rings. To close the access rings, the IPv6 IS-IS processes on all access rings need to be enabled. In this case, you need to enable one traditional IPv6 IS-IS process and multiple IPv6 IS-IS multi-instance processes on the same interface. This reduces the interface count and configuration workload of the access rings.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an IS-IS process and enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ] [ vpn-instance vpn-instance-name ]
   ```
   
   
   
   *process-id* specifies an IS-IS process ID. If the *process-id* parameter is not specified, the system creates process 1 by default. If a VPN instance is specified, the IS-IS process belongs to this VPN instance. If no VPN instance is specified, the process belongs to the public network instance.
3. Configure the IPv6 IS-IS process as an IS-IS multi-instance process.
   
   
   ```
   [multi-instance enable](cmdqueryname=multi-instance+enable) iid iid-value
   ```
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
6. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
7. Enable IS-IS on the interface.
   
   
   ```
   [isis ipv6 enable](cmdqueryname=isis+ipv6+enable) [ process-id ]
   ```
8. Set parameters for the IS-IS multi-instance process on the interface.
   
   
   * Configure the IS-IS interface to authenticate Hello packets using the specified authentication mode and password.
     + Configure simple authentication.
       ```
       [isis](cmdqueryname=isis) process-id process-id authentication-mode { simple { plain simple-plain |  [ cipher ] simple-cipher } | md5 { [ cipher ] md5-cipher | plain  md5-plain } } [ level-1 | level-2 ] [ ip | osi ] [ send-only ]
       ```
     + Configure HMAC-MD5 authentication.
       ```
       [isis](cmdqueryname=isis) process-id process-id authentication-mode { simple { plain simple-plain |  [ cipher ] simple-cipher } | md5 { [ cipher ] md5-cipher | plain  md5-plain } } [ level-1 | level-2 ] [ ip | osi ] [ send-only ]
       ```
     + Configure keychain authentication.
       ```
       [isis](cmdqueryname=isis) process-id process-id authentication-mode keychain keychain-name [ level-1 | level-2 ] [ send-only ]
       ```
     + Configure HMAC-SHA256 authentication.
       ```
       [isis](cmdqueryname=isis) process-id process-id authentication-mode hmac-sha256 key-id key-id { plain plain | [ cipher ] cipher } [ level-1 | level-2 ] [ send-only ]
       ```
       ![](public_sys-resources/note_3.0-en-us.png) 
       
       Simple or HMAC-MD5 authentication is not recommended if high security is required. To prevent routing information from being tampered with, you are advised to enable authentication and use keychain or HMAC-SHA256 authentication to improve security.
   * Configure a link cost for the IS-IS interface.
     ```
     [isis](cmdqueryname=isis) [ process-id process-id ] ipv6 cost cost [ level-1 | level-2]
     ```
   * Emulate the network type of an IS-IS broadcast interface as P2P.
     ```
     [isis](cmdqueryname=isis) [ process-id process-id ] circuit-type p2p [ strict-snpa-check ]
     ```
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```