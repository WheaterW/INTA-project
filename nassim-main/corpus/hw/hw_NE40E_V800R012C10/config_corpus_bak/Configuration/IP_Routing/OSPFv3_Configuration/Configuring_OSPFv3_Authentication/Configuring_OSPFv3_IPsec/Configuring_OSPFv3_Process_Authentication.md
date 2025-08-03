Configuring OSPFv3 Process Authentication
=========================================

OSPFv3 supports packet authentication, with which devices accept only the OSPFv3 packets that are authenticated. If OSPFv3 packets fail to be authenticated, OSPFv3 neighbor relationships cannot be established. Configuring OSPFv3 process authentication improves OSPFv3 network security.

#### Context

With the increase in attacks on TCP/IP networks and inherent defects and flawed implementation of the TCP/IP protocol suite, the attacks have increasing impacts on the networks. Attacks on network devices may even cause a network crash or lead to network unavailability. Configuring OSPFv3 process authentication improves OSPFv3 network security.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

You are advised to configure authentication to ensure system security.

It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.

OSPFv3 authentication takes effect in descending order of priority as follows: interface authentication, area authentication, and process authentication.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. Configure an authentication mode for the OSPFv3 process as required.
   
   
   * To configure the HMAC-SHA256 or HMAC-SM3 authentication mode for the OSPFv3 process, run the [**authentication-mode**](cmdqueryname=authentication-mode) { **hmac-sha256** | **hmac-sm3** } **key-id** *KeyId* { **plain** *PlainText* | [ **cipher** ] *CipherText* } command.
     
     If you choose **plain**, the password will be saved as a plaintext in the configuration file, which provokes high security risks. To improve device security, choose ciphertext authentication and change the password periodically.
   * To configure keychain authentication for the OSPFv3 process, run the [**authentication-mode**](cmdqueryname=authentication-mode) { **keychain** *Keychain-Name* } command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Before configuring keychain authentication, you need to run the [**keychain**](cmdqueryname=keychain) command to create a keychain, and then run the [**key-id**](cmdqueryname=key-id), [**key-string**](cmdqueryname=key-string), and [**algorithm**](cmdqueryname=algorithm) commands to configure a key ID, a password, and an authentication algorithm, respectively, for this keychain. Otherwise, OSPFv3 authentication will fail.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.