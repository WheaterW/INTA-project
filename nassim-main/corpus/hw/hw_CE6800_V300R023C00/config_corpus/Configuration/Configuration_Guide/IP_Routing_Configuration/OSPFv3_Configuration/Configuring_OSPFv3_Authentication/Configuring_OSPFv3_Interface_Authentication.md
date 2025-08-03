Configuring OSPFv3 Interface Authentication
===========================================

Configuring OSPFv3 Interface Authentication

#### Prerequisites

Before configuring OSPFv3 interface authentication, you have completed the following tasks:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).
* If keychain authentication needs to be used, [configure a keychain](../vrp_keychain_cfg_0009.html).

#### Context

Interface authentication takes effect between neighboring devices' interfaces on which an authentication mode and password are configured. Interface authentication takes precedence over area authentication. For interfaces on the same subnet, the configured authentication mode and password must be identical. This requirement does not apply to the interfaces on different subnets. By default, no authentication mode is configured for an OSPFv3 interface. For security purposes, you are advised to configure an authentication mode.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure an authentication mode for the OSPFv3 interface as required.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   
   
   
   * Configure HMAC-SHA256 or HMAC-SM3 authentication.
     
     ```
     [ospfv3 authentication-mode](cmdqueryname=ospfv3+authentication-mode) { hmac-sha256 | hmac-sm3 } key-id KeyId { plain plainText | [ cipher ] cipherText } [ instance instanceId ]
     ```
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     When configuring an authentication password, select the ciphertext mode. For security purposes, you are advised to change the password periodically.
   * Configure keychain authentication.
     
     ```
     [ospfv3 authentication-mode](cmdqueryname=ospfv3+authentication-mode) { keychain Keychain-Name } [ instance instanceId ]
     ```
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   OSPFv3 authentication takes effect in descending order of priority as follows: interface authentication, area authentication, and process authentication.
   
   For security purposes, you are advised not to use the weak security algorithms in OSPFv3. If you need to use such an algorithm, run the [**install feature-software WEAKEA**](cmdqueryname=install+feature-software+WEAKEA) command first to install the weak security algorithm/protocol feature package WEAKEA.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```