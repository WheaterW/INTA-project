Configuring OSPFv3 Authentication Trailer
=========================================

Open Shortest Path First version 3 (OSPFv3) supports packet authentication, enabling OSPFv3 devices to receive only the OSPFv3 packets that are authenticated. If packets fail to be authenticated, OSPFv3 neighbor relationships cannot be established. This section describes how to configure an authentication mode.

#### Usage Scenario

OSPFv3 authentication trailer supports HMAC-SHA256 authentication and HMAC-SM3 authentication.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

You are advised to configure authentication to ensure system security.

It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.

For security purposes, you are advised not to use weak security algorithms in OSPFv3. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.

When configuring an authentication password, select the ciphertext mode because the password is saved in the configuration file as a plaintext if you select the plaintext mode, which has a high risk. To ensure device security, change the password periodically.


#### Procedure

* Configure area authentication.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
     
     
     
     The OSPFv3 view is displayed.
  3. Run [**area**](cmdqueryname=area) *area-id*
     
     
     
     The OSPFv3 area view is displayed.
  4. Run [**authentication-mode**](cmdqueryname=authentication-mode) { **hmac-sha256** | **hmac-sm3** } **key-id** *KeyId* { **plain** *PlainText* | [ **cipher** ] *CipherText* }
     
     
     
     An authentication mode is configured for the OSPFv3 area.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When area authentication is used, all the Routers in the area must have the same area authentication mode and password.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure process authentication.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
     
     
     
     The OSPFv3 view is displayed.
  3. Run [**authentication-mode**](cmdqueryname=authentication-mode) { **hmac-sha256** | **hmac-sm3** } **key-id** *KeyId* { **plain** *PlainText* | [ **cipher** ] *CipherText* }
     
     
     
     An authentication mode is configured for the OSPFv3 process.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure interface authentication.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ospfv3 authentication-mode**](cmdqueryname=ospfv3+authentication-mode){ **hmac-sha256** | **hmac-sm3** } **key-id** *KeyId* { **plain** *PlainText* | [ **cipher** ] *CipherText* } [ **instance***instanceId* ]
     
     
     
     An authentication mode is configured for the OSPFv3 interface.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Interface authentication takes precedence over area authentication. For interfaces on the same subnet, the configured authentication mode and password must be identical. This requirement does not apply to the interfaces on different subnets.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.