Configuring OSPF Interface Authentication
=========================================

Configuring OSPF Interface Authentication

#### Prerequisites

Before configuring OSPF interface authentication, you have completed the following tasks:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).
* If keychain authentication is used, [Configuring a Keychain](../vrp_keychain_cfg_0009.html).

#### Context

To implement interface authentication, the authentication mode and password must be set between neighboring devices. Interface authentication takes precedence over area authentication. For OSPF interfaces on the same network segment, the same authentication mode and password must be set. By default, no authentication mode is configured for an OSPF interface. For security purposes, you are advised to configure an authentication mode.

![](../public_sys-resources/note_3.0-en-us.png) 

For security purposes, the weak security algorithm in OSPF is not recommended. If it is required, run the [**install feature-software WEAKEA**](cmdqueryname=install+feature-software+WEAKEA) command first to install the weak security algorithm/protocol feature package WEAKEA.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure one of the following authentication modes for the OSPF interface as required:
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   
   
   
   * Configure simple authentication.
     
     ```
     [ospf authentication-mode](cmdqueryname=ospf+authentication-mode) simple [ plain plain-text | [ cipher ] cipher-text ]
     ```
     **plain** indicates the cleartext password. **cipher** indicates the ciphertext password.![](../public_sys-resources/note_3.0-en-us.png) 
     
     When configuring an authentication password, you are advised to use the ciphertext mode. The password is saved in configuration scripts in cleartext if you select the cleartext mode, which poses a high security risk. To ensure device security, change the password periodically.
   * Configure ciphertext authentication.
     
     ```
     [ospf authentication-mode](cmdqueryname=ospf+authentication-mode) { md5 | hmac-md5 | hmac-sha256 } [ key-id { plain plain-text | [ cipher ] cipher-text } ]
     ```
     
     **plain** indicates the cleartext password. **cipher** indicates the ciphertext password. For MD5, HMAC-MD5, or HMAC-SHA256 authentication, ciphertext passwords are used by default.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     To ensure high security, you are advised to use the HMAC-SHA256 algorithm instead of the simple, MD5, and HMAC-MD5 algorithms.
   * Configure keychain authentication.
     
     ```
     [ospf authentication-mode](cmdqueryname=ospf+authentication-mode) keychain keychain-name
     ```
   * Configure non-authentication.
     ```
     [ospf authentication-mode](cmdqueryname=ospf+authentication-mode) null
     ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display this**](cmdqueryname=display+this) command in the view of the specified interface to check the authentication configuration on the interface.