Configuring OSPF Interface Authentication
=========================================

A DCN runs OSPF and supports packet authentication. After an authentication mode is specified, NEs accept only the OSPF packets that have been authenticated. If packets fail to be authenticated, neighbor relationships cannot be established.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**dcn (interface view)**](cmdqueryname=dcn+%28interface+view%29) or [**dcn mode vlan**](cmdqueryname=dcn+mode+vlan)
   
   
   
   DCN is enabled on the DCN serial interface or sub-interface 4094.
4. Run any of the following commands:
   
   
   * To configure simple authentication, run the [**dcn ospf authentication-mode**](cmdqueryname=dcn+ospf+authentication-mode) **simple** [ [ **plain** ] *plain-text* | **cipher** *cipher-text* ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
     
     For security purposes, you are advised to specify the ciphertext mode. In addition, change the password periodically.
   * To configure Message Digest 5 (MD5) or Secure Hash Algorithm (SHA) authentication, run the [**dcn ospf authentication-mode**](cmdqueryname=dcn+ospf+authentication-mode) { { **md5** | **hmac-md5** | **hmac-sha256** } [ *key-id* { **plain** *plain-text* | [ **cipher** ] *cipher-text* } ] } command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + To ensure high security, do not use the MD5 or HMAC-MD5 algorithm. If you need to use the MD5 or HMAC-MD5 algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function. To prevent security risks, you are advised to use the HMAC-SHA256 algorithm.
     + The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
     + For security purposes, you are advised to specify the ciphertext mode. In addition, change the password periodically.
   * To configure null authentication, run the [**dcn ospf authentication-mode**](cmdqueryname=dcn+ospf+authentication-mode) **null** command. In null authentication mode, OSPF packets are not authenticated.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Interfaces on the same network segment must have the same authentication mode and password. Interfaces on different network segments can have different authentication modes and passwords.
   * The last authentication mode configured on the device is used as the interface authentication mode.
   * By default, no authentication mode is configured for an OSPF interface. You are advised to configure an authentication mode to ensure system security.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.