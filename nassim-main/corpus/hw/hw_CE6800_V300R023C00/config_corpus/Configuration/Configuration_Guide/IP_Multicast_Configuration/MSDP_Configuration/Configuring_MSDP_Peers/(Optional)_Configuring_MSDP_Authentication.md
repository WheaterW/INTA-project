(Optional) Configuring MSDP Authentication
==========================================

(Optional) Configuring MSDP Authentication

#### Context

By default, MSDP MD5 authentication and MSDP keychain authentication are not configured. You are advised to configure an authentication mode to improve system security.

![](public_sys-resources/note_3.0-en-us.png) 

MD5 and keychain authentication modes are mutually exclusive.

The MD5 algorithm is insecure and poses security risks.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the MSDP view.
   
   
   ```
   [msdp](cmdqueryname=msdp) [ vpn-instance vpn-instance-name ]
   ```
3. Select an MSDP authentication mode as required.
   
   
   
   **Table 1** Configuring an MSDP authentication mode
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure MSDP MD5 authentication. | [**peer**](cmdqueryname=peer) *peer-address* [**password**](cmdqueryname=password) { **cipher** *cipher-password* | **simple** *simple-password* } | After this function is enabled, the transmit end peer sends an MD5-encrypted MSDP message, which is transferred to the receive end peer over a TCP connection. The receive end peer decrypts the MSDP message based on the uniform MD5 encryption rules and the key carried in the message. After decrypting the message successfully, the receive end peer sends the message to the MSDP module for processing.  MD5 authentication must be enabled on both peers, and the passwords configured for them must be the same.  NOTE:  If **simple** is specified, the password is saved in the configuration scripts in cleartext. However, as this introduces potential security risks, you are advised to specify **cipher** so that the password is instead saved in ciphertext.  The password must be at least eight characters long and contain at least two of the following: uppercase letters, lowercase letters, digits, and special characters (excluding question marks and spaces).  To ensure device security, change the password periodically. |
   | Configure MSDP keychain authentication. | [**peer**](cmdqueryname=peer) *peer-address* [**keychain**](cmdqueryname=keychain) *keychain-name* | MSDP supports keychains. Keychains and new TCP extension options can be used to configure a group of passwords for each TCP connection. Each password can be configured with different encryption algorithms and validity periods. Passwords can be changed at any time, significantly improving the security of encrypted packets. Only the packets that pass keychain authentication are processed. This effectively prevents attacks that use malicious packets.  Keychain authentication must be configured on both MSDP peers, and the keychains configured at both ends must use the same encryption algorithm and password so that a TCP connection can be set up and MSDP messages can be exchanged properly.  The keychain specified by *keychain-name* must already exist when you configure MSDP keychain authentication; otherwise, the TCP connection cannot be established. |
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```