Configuring OSPF Area Authentication
====================================

Configuring OSPF Area Authentication

#### Prerequisites

Before configuring OSPF area authentication, you have completed the following tasks:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).
* To use keychain authentication, complete the [Configuring a Keychain](../vrp_keychain_cfg_0009.html) task first.

#### Context

If OSPF area authentication is used, the authentication mode and password configurations on all the interfaces in the area must be identical. By default, no authentication mode is configured for an OSPF area. For security purposes, you are advised to configure an authentication mode.

![](../public_sys-resources/note_3.0-en-us.png) 

For security purposes, the weak security algorithm in OSPF is not recommended. If it is required, run the [**install feature-software WEAKEA**](cmdqueryname=install+feature-software+WEAKEA) command first to install the weak security algorithm/protocol feature package WEAKEA.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
   
   The *process-id* parameter specifies the ID of a process, and the default value is 1.
3. Enter the OSPF area view.
   
   
   ```
   [area](cmdqueryname=area) area-id
   ```
4. Configure one of the following authentication modes for the OSPF area as required:
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   
   
   
   * Configure simple authentication.
     
     ```
     [authentication-mode simple](cmdqueryname=authentication-mode+simple) [ plain SPlainText | [ cipher ] SCipherText ]
     ```
     **plain** indicates the cleartext password. **cipher** indicates the ciphertext password.![](../public_sys-resources/note_3.0-en-us.png) 
     
     When configuring an authentication password, you are advised to use the ciphertext mode. The password is saved in configuration scripts in cleartext if you select the cleartext mode, which poses a high security risk. To ensure device security, change the password periodically.
   * Configure ciphertext authentication.
     
     ```
     [authentication-mode](cmdqueryname=authentication-mode) { md5 | hmac-md5 | hmac-sha256 } [ KeyID { plain MPlainText | [ cipher ] MCipherText } ]
     ```
     
     **plain** indicates the cleartext password. **cipher** indicates the ciphertext password. By default, the authentication is in ciphertext mode.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     To ensure high security, you are advised to use the HMAC-SHA256 algorithm instead of the simple, MD5, and HMAC-MD5 algorithms.
   * Configure keychain authentication.
     
     ```
     [authentication-mode](cmdqueryname=authentication-mode) keychain Keychain-Name
     ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf+brief) [ *process-id* ] **brief** command to check brief OSPF information. The **Authtype** field in the command output indicates the authentication mode.