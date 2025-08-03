Configuring RIP-2 Message Authentication
========================================

RIP-2 provides the following message authentication modes to enhance network security: cleartext authentication, MD5 authentication, HMAC-SHA256 authentication, and SM3 authentication. Configuring authentication to ensure system security is recommended. By default, authentication is not configured for RIP.

![](public_sys-resources/note_3.0-en-us.png) 

The HMAC-SHA256 algorithm is recommended because it provides higher security than the MD5 algorithm.

It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.

For security purpose,you are not advised to use the weak security algorithm or weak security protocols provided by this feature. If you need to use the weak security algorithm or protocols, run the **install feature-software WEAKEA** command to install the weak security algorithm or protocol feature package WEAKEA. By default, the device provides the weak security algorithm or protocol feature package WEAKEA. For details about how to install or uninstall the feature package, see "Upgrade Maintenance Configuration" in Configuration Guide > System Management Configuration.

The following commands can be used only after the weak security algorithm/protocol feature package is installed.

| Command | Parameters Available Only After Feature Package Installation |
| --- | --- |
| [**rip authentication-mode md5**](cmdqueryname=rip+authentication-mode+md5) **nonstandard** { [ **cipher** ] *password-key* | **plain** *plain-text* } *key-id* | **md5** |
| [**rip authentication-mode**](cmdqueryname=rip+authentication-mode) **md5** **usual** { [ **cipher** ] *password-key* | **plain** *plain-text* } | **md5** |
| [**rip authentication-mode md5**](cmdqueryname=rip+authentication-mode+md5) **nonstandard** **keychain** *keychain-name* | **md5** |



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
   
   Determine whether to perform this step based on the current interface mode.
4. Perform operations as required to configure authentication.
   
   
   
   **Table 1** Configuring authentication
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure cleartext authentication for RIP-2 messages. | [**rip authentication-mode**](cmdqueryname=rip+authentication-mode) **simple** { **plain** *plain-text* | [ **cipher** ] *password-key* } | In cleartext authentication mode, a cleartext password is transmitted with an authentication message. As such, cleartext authentication is not recommended on networks with high security requirements. |
   | Configure MD5 authentication for RIP-2 messages. | [**rip authentication-mode**](cmdqueryname=rip+authentication-mode) **md5** { **nonstandard** { { **plain** *plain-text* | [ **cipher** ] *password-key* } *key-id* | [**keychain**](cmdqueryname=keychain) *keychain-name* } | **usual** { **plain** *plain-text* | [ **cipher** ] *password-key* } } | In MD5 authentication mode, an MD5 password is used for message encapsulation and decapsulation. MD5 authentication is more secure than cleartext authentication. |
   | Configure HMAC-SHA256 authentication. | [**rip authentication-mode**](cmdqueryname=rip+authentication-mode) **hmac-sha256** { **plain** *plain-text* | [ **cipher** ] *password-key* } *key-id* | - |
   | Configure SM3 authentication. | [**rip authentication-mode**](cmdqueryname=rip+authentication-mode) **sm3** { **plain** *plain-text* | [ **cipher** ] *password-key* } *key-id* | - |
   
   
   ![](public_sys-resources/notice_3.0-en-us.png) 
   
   When configuring an authentication password, select the ciphertext mode because the password is saved in the configuration script as a plaintext if you select the plaintext mode, which has a high risk. You are also recommended to change the password periodically to ensure device security.
   
   For security purposes, the weak security algorithm in RIP is not recommended. If it is required, run the [**install feature-software WEAKEA**](cmdqueryname=install+feature-software+WEAKEA) command first to install the weak security algorithm/protocol feature package WEAKEA.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```