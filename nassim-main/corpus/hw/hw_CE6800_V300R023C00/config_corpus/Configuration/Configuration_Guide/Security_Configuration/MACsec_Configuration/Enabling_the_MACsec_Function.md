Enabling the MACsec Function
============================

Enabling the MACsec Function

#### Context

To enable the MACsec function on a device, you need to create and configure a MACsec profile, apply the profile to an interface, and configure a CAK.

After the MACsec function is enabled on interfaces of two connected devices, they elect a key server based on their priorities, which can be configured in a MACsec profile. A smaller priority value indicates a higher priority. The device with a higher priority is elected as the key server. If the two devices have the same priority, their Secure Channel Identifiers (SCIs) are compared. An SCI consists of the MAC address of an interface and the last two bytes of the interface index. The device with a smaller SCI value is elected as the key server.

To ensure secure transmission of service data on the network, MACsec provides the data encryption and integrity check functions. You can specify an encryption mode to selectively enable data encryption and integrity check. Three encryption modes are available:

* None: Neither data encryption nor integrity check is performed.
* Normal: Both data encryption and integrity check are performed.
* Integrity-only: Integrity check is performed, and data encryption is not performed.

![](public_sys-resources/note_3.0-en-us.png) 

After a MACsec connection is established, the server can switch the encryption algorithm, and the client also switches the encryption algorithm accordingly. However, when a Huawei device functions as a server and a non-Huawei device that does not support encryption algorithm switching functions as a client, encryption algorithm switching will cause the interruption of MACsec negotiation.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create and configure a MACsec profile.
   1. Create a MACsec profile and enter the MACsec profile view.
      
      
      ```
      [mac-security-profile name](cmdqueryname=mac-security-profile+name) profile-name
      ```
   2. (Optional) Configure the MKA key server priority.
      
      
      ```
      [mka keyserver priority](cmdqueryname=mka+keyserver+priority) priority
      ```
      
      By default, the MKA key server priority is 16.
   3. (Optional) Configure the MACsec encryption mode.
      
      
      ```
      [macsec mode](cmdqueryname=macsec+mode) { none | normal | integrity-only }
      ```
      
      By default, the MACsec encryption mode is normal.
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      When configuring MACsec on a network where data traffic is being transmitted, you can set the encryption mode on both ends to none. After MKA session negotiation is successful, change the encryption mode on both ends to normal. This shortens the traffic interruption time.
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Enter the view of the interface to which the MACsec profile is to be applied.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
5. Configure the CKN and CAK.
   
   
   ```
   [mka cak-mode static](cmdqueryname=mka+cak-mode+static) ckn string-name cak string-key
   ```
   
   By default, no CKN or CAK is configured.
   
   A CKN is the name of a CAK. To ensure that an MKA session can be successfully established between two devices, configure the same CKN and CAK on their connected interfaces.
6. Apply the MACsec profile to the interface.
   
   
   ```
   [mac-security-profile](cmdqueryname=mac-security-profile) profile-name
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The MACsec function takes effect only after the MACsec profile is applied to an interface. For details about interfaces that support MACsec, see Configuration Precautions for MACsec.
7. (Optional) Enable the MACsec module of the device to convert the byte order of XPN salt values.
   
   
   ```
   [macsec xpn-salt reverse](cmdqueryname=macsec+xpn-salt+reverse)
   ```
   
   When network devices of other brands implement the MACsec function, the salt values delivered in XPN mode use the network sequence or host sequence. You can configure this command to implement compatibility among different implementation modes.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```