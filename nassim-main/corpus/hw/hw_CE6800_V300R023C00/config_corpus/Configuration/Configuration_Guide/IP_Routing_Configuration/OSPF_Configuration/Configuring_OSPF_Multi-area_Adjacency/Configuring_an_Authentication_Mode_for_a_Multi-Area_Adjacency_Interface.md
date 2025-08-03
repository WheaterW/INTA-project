Configuring an Authentication Mode for a Multi-Area Adjacency Interface
=======================================================================

Configuring an Authentication Mode for a Multi-Area Adjacency Interface

#### Prerequisites

Before configuring an authentication mode for a multi-area adjacency interface, you have completed the following tasks:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).
* Configure a keychain first if you want to use keychain authentication. For detailed configuration, see [Configuring a Keychain](../vrp_keychain_cfg_0009.html).

#### Context

Configuring an authentication mode for a multi-area adjacency interface improves OSPF network security.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Enable OSPF on the interface.
   
   
   ```
   [ospf enable](cmdqueryname=ospf+enable) [ process-id ] area area-id
   ```
4. Configure a multi-area adjacency interface and enable OSPF for it.
   
   
   ```
   [ospf enable multi-area](cmdqueryname=ospf+enable+multi-area) area-id
   ```
5. Configure one of the following authentication modes for the OSPF multi-area adjacency interface as needed:
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   
   
   
   * Configure simple authentication.
     
     ```
     [ospf authentication-mode](cmdqueryname=ospf+authentication-mode) simple [ plain plain-text | [ cipher ] cipher-text ] multi-area area-id
     ```
     **plain** indicates the cleartext password. **cipher** indicates the ciphertext password.![](../public_sys-resources/note_3.0-en-us.png) 
     
     When configuring an authentication password, you are advised to use the ciphertext mode. The password is saved in configuration scripts in cleartext if you select the cleartext mode, which poses a high security risk. To ensure device security, change the password periodically.
   * Configure ciphertext authentication.
     
     ```
     [ospf authentication-mode](cmdqueryname=ospf+authentication-mode) { md5 | hmac-md5 | hmac-sha256 } [ key-id { plain plain-text | [ cipher ] cipher-text } ] multi-area area-id
     ```
     
     **plain** indicates the cleartext password. **cipher** indicates the ciphertext password.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     To ensure high security, you are advised to use the HMAC-SHA256 algorithm instead of the simple, MD5, and HMAC-MD5 algorithms.
   * Configure keychain authentication.
     
     ```
     [ospf authentication-mode](cmdqueryname=ospf+authentication-mode) keychain keychain-name multi-area area-id
     ```
   * Configure null authentication for the OSPF multi-area adjacency interface. In this mode, OSPF authentication is not performed for this interface.
     ```
     [ospf authentication-mode](cmdqueryname=ospf+authentication-mode) null multi-area area-id
     ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```