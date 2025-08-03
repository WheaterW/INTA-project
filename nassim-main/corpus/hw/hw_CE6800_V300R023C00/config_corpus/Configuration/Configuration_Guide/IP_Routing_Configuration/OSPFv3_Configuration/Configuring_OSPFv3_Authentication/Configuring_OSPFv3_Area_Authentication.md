Configuring OSPFv3 Area Authentication
======================================

Configuring OSPFv3 Area Authentication

#### Prerequisites

Before configuring OSPFv3 area authentication, you have completed the following tasks:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).
* If keychain authentication needs to be used, [configure a keychain](../vrp_keychain_cfg_0009.html).

#### Context

If OSPFv3 area authentication is used, the authentication mode and password configurations on all the interfaces in the area must be identical. By default, no authentication mode is configured for an OSPFv3 area. For security purposes, you are advised to configure an authentication mode.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Enter the OSPFv3 area view.
   
   
   ```
   [area](cmdqueryname=area) area-id
   ```
4. Configure an authentication mode for the OSPFv3 area as required.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   
   
   
   * Configure HMAC-SHA256 or HMAC-SM3 authentication.
     
     ```
     [authentication-mode](cmdqueryname=authentication-mode) { hmac-sha256 | hmac-sm3 } key-id KeyId  { plain PlainText | [ cipher ] CipherText }
     ```
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     When configuring an authentication password, select the ciphertext mode. For security purposes, you are advised to change the password periodically.
   * Configure keychain authentication.
     
     ```
     [authentication-mode](cmdqueryname=authentication-mode) { keychain Keychain-Name }
     ```
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   OSPFv3 authentication takes effect in descending order of priority as follows: interface authentication, area authentication, and process authentication.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```