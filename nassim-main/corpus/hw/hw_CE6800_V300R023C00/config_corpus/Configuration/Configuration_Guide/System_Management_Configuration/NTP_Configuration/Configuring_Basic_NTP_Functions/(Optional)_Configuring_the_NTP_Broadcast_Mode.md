(Optional) Configuring the NTP Broadcast Mode
=============================================

(Optional) Configuring the NTP Broadcast Mode

#### Context

When the broadcast mode is used, you need to perform the following configurations on both the broadcast server and client.


#### Procedure

* Configure an NTP broadcast server.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure an NTP authentication key.
     
     
     ```
     [ntp authentication-keyid](cmdqueryname=ntp+authentication-keyid) keyId authentication-mode { md5 | hmac-sha256 | aes-128-cmac | aes-256-cmac } { password | cipher password }
     ```
     
     
     
     MD5 is a weak security algorithm. It can be used only after the weak security algorithm or protocol feature package is installed after the **install feature-software WEAKEA** command is run. You are advised to use other security algorithms for NTP key authentication.
  3. Enter the view of the interface used for sending NTP broadcast packets.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  4. Configure the local device as the NTP broadcast server.
     
     
     ```
     [ntp broadcast-server](cmdqueryname=ntp+broadcast-server) [ authentication-keyid key-id | version version-number | port port-number ] *
     ```
     
     After the configuration is complete, the local device functions as the NTP broadcast server periodically sending clock synchronization packets to the broadcast address 255.255.255.255 from a specified interface.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure an NTP broadcast client.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of the interface used for receiving NTP broadcast packets.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Configure the local device as the NTP broadcast client.
     
     
     ```
     [ntp broadcast-client](cmdqueryname=ntp+broadcast-client)
     ```
     
     After the configuration is complete, the local device functions as the NTP broadcast client listening for the NTP broadcast packets sent from the server and synchronizing the local clock with the server.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```