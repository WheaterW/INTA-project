Configuring iNOF Authentication
===============================

Configuring iNOF Authentication

#### Context

In an iNOF system, the authentication mode and password must be configured to ensure the security of iNOF packet transmission. You can configure the device to encapsulate authentication information into iNOF packets and send them to the peer device, which then accepts only authenticated iNOF packets. This improves the security and reliability of the iNOF system.

The authentication mode for transmitting iNOF packets is HMAC-SHA256. The receiver uses the HMAC-SHA256 algorithm to encrypt the locally configured password and generate digest information. After receiving iNOF packets, the receiver compares the authentication key and authentication type in the packets with the digest information and the locally configured authentication type. If they are different, the receiver discards the packets.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the AI service and enter the AI service view.
   
   
   ```
   [ai-service](cmdqueryname=ai-service)
   ```
   
   By default, the AI service is disabled.
3. Enable iNOF and enter the iNOF view.
   
   
   ```
   [inof](cmdqueryname=inof)
   ```
   
   By default, iNOF is disabled.
4. Configure the authentication mode and password for transmitting iNOF packets.
   
   
   ```
   [authentication-mode hmac-sha256 password](cmdqueryname=authentication-mode+hmac-sha256+password) passwd
   ```
   
   By default, no authentication mode or password is configured for transmitting iNOF packets.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * iNOF packets can be transmitted only after they pass authentication. Therefore, after configuring the authentication mode and password for transmitting iNOF packets on a device, ensure that the same authentication mode and password are configured on the peer device; otherwise, the packets cannot pass authentication.
   * If a password change is required, change the passwords on both the local and peer devices. Changing passwords interrupts services for a short period of time. After the passwords on the two devices are changed to be the same, the two devices automatically re-establish the connection.
5. Exit the iNOF view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```