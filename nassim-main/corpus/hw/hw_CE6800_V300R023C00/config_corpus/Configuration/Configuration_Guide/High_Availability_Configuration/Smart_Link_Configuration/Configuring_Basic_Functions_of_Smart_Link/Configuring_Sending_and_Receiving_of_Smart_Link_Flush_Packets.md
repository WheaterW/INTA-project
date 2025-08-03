Configuring Sending and Receiving of Smart Link Flush Packets
=============================================================

Configuring Sending and Receiving of Smart Link Flush Packets

#### Context

Flush packets enable devices to update entries before they are aged out and allow link switching within milliseconds, minimizing traffic loss. When Flush packets are needed to update MAC address entries and ARP entries, the transmit end and receive end must be configured to send and receive Flush packets, and the two ends must be in the same control VLAN. In addition, Smart Link allows you to configure a password on the receive end for Flush packets to enhance the security of packets. Simple, SHA, and HMAC SHA256 authentication modes are supported. HMAC-SHA256 authentication is recommended because it is an irreversible encryption algorithm.

The format of Flush packets varies according to device vendors. The Flush packets configured in this document are used for communication between Huawei switching devices only. You only need to configure interfaces on the primary and secondary Smart Link links to receive Flush packets.


#### Procedure

1. Configure the device to send Flush packets.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the Smart Link group view.
      
      
      ```
      [smart-link group](cmdqueryname=smart-link+group) group-id
      ```
   3. Configure the Smart Link group to send Flush packets, and configure the encryption mode, control VLAN ID, and password for Flush packets.
      
      
      ```
      [flush send](cmdqueryname=flush+send) [control-vlan](cmdqueryname=control-vlan) vlan-id [ [password](cmdqueryname=password) { simple | sha | hmac-sha256 } password ]
      ```
      
      The VLAN ID specified by *vlan-id* must already exist on the device. If the specified VLAN ID does not exist, Flush packets cannot be sent.
      
      Devices that send and receive Flush packets must have the same encryption mode, control VLAN ID, and password.
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      * This command does not add an interface to the control VLAN. You must configure the interface to allow packets of the control VLAN to pass through.
      * SHA and HMAC-SHA256 authentication provide higher security than simple authentication.
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
2. Configure interfaces on the primary and secondary links to receive Flush packets.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the interface view.
      
      
      ```
      [interface](cmdqueryname=interface) interface-type interface-number
      ```
   3. Configure the interface to receive Flush packets, and set the encryption mode, control VLAN ID, and password for receiving Flush packets.
      
      
      ```
      [smart-link flush](cmdqueryname=smart-link+flush) [receive](cmdqueryname=receive) control-vlan vlan-id [ password { simple | sha | hmac-sha256 } password ]
      ```
      
      The password is optional. If it is not configured, no password is used for authentication. If you reconfigure the control VLAN ID, you also need to reconfigure the password.
      
      The devices that send and receive Flush packets must have the same encryption mode, control VLAN ID, and password.
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      SHA and HMAC-SHA256 authentication provide higher security than simple authentication.
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```