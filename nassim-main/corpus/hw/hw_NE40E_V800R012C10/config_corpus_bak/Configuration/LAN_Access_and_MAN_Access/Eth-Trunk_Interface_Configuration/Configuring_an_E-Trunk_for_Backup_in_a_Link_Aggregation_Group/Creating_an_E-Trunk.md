Creating an E-Trunk
===================

Eth-Trunk interfaces can be added only to a created E-Trunk. E-Trunk provides device-level reliability.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
   
   
   
   An E-Trunk is configured, and its view is displayed.
3. Run [**security-key**](cmdqueryname=security-key) { **simple** *simple-key* | **cipher** *cipher-key* }
   
   
   
   A password for encrypting packets is configured for the E-Trunk.
   
   
   
   The passwords for encrypting packets on the two ends in an E-Trunk must be the same.
   
   You can specify **simple** or **cipher** as required.
   * If **simple** is specified, the password is displayed in clear text in the configuration file.
   * If **cipher** is specified, the password is displayed as garbled characters in the configuration file.
     
     + *cipher-key1*: If the password is entered in ciphertext, the value must be a string of 32 to 432 consecutive characters.
     + *cipher-key2*: A 24-character ciphertext password configured in an earlier version is also supported in this version.
     + *cipher-key3*: If the password is entered in clear text, the value must be a string of 1 to 255 case-sensitive characters. It cannot contain spaces.
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   If **simple** is specified, the password is displayed in clear text in the configuration file. In this case, users with the least privilege can obtain the password by querying the configuration file, which poses a security risk. As such, you are advised to select **cipher** to save the password in cipher text.
   
   Two devices in the same E-Trunk must have the same password for encrypting E-Trunk packets. After an E-Trunk is created, you must manually set an encryption password. Otherwise, E-Trunk negotiation fails.
   
   For security purposes, you are advised not to use the **simple** weak security algorithm. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command first to enable the weak security algorithm function.
4. Run either of the following commands to configure local and peer IP addresses for the E-Trunk:
   
   
   * For an IPv4 network, run the [**peer-address**](cmdqueryname=peer-address) *peer-ip-address* **source-address** *source-ip-address* [ **vpn-instance** *vpn-instance-name* ] command.
   * For an IPv6 network, run the [**peer-ipv6**](cmdqueryname=peer-ipv6) *peer-ipv6-address* **source-ipv6** *source-ipv6-address* [ **vpn-instance** *vpn-instance-name* ] command.
   
   The local and peer IP addresses on one device are the peer and local IP addresses of its peer device, respectively. The configured IP addresses must be reachable. For example, an E-Trunk is set up between device A and device B. On device A, the peer IP address is IP2 and the local IP address is IP1. Then, on device B, the peer IP address is IP1 and the local IP address is IP2.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When you change the local or peer IP address on a device, you must change the corresponding address on the remote device. Otherwise, protocol packets will be discarded.
   
   It is recommended that you configure the local and peer IP addresses of an E-Trunk as loopback interface addresses and ensure that the IP addresses are reachable.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.