Configuring an Authentication Mode for VRRP Advertisement Packets
=================================================================

Configuring an Authentication Mode for VRRP Advertisement Packets

#### Context

When the master device in a VRRP group periodically sends VRRP Advertisement packets to inform downstream devices and backup devices that it is working properly, an attacker may simulate these packets for malicious purposes. To improve the security of networks, you can configure VRRP security policies as required.

Different authentication modes can be configured to meet different security requirements.

* Configure non-authentication (default setting) on a secure network. In this mode, the master device does not authenticate VRRP Advertisement packets before sending them, and backup devices consider the received VRRP Advertisement packets authentic and valid.
* Configure simple or HMAC-MD5 authentication to improve VRRP communication security. HMAC-MD5 authentication is more secure than simple authentication.

#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface where a VRRP group resides.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure an authentication mode for VRRP Advertisement packets.
   ```
   [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id authentication-mode { simple { [ plain ] key | cipher cipher-key } | md5 md5-key }
   ```
   
   By default, a VRRP group does not authenticate VRRP Advertisement packets.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * For security purposes, you are advised to specify the ciphertext mode and change the password periodically.
   * The same authentication key must be configured on the master and backup devices in a VRRP group.
   * It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] [ **verbose** ] command to check the VRRP group status.