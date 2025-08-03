Configuring IS-IS Authentication
================================

After IS-IS authentication is configured, authentication information can be encapsulated into LSPs, SNPs, or Hello packets to ensure packet transmission security.

#### Context

Generally, IS-IS packets do not carry authentication information, and received packets are not authenticated. To prevent malicious packets from attacking the network, configure IS-IS authentication to improve network security.

* Area authentication: Authentication passwords are encapsulated into IS-IS packets in Level-1 areas. The receiver only accepts the packets that have been authenticated. Therefore, you need to configure IS-IS area authentication to authenticate packets in Level-1 areas.
* Routing domain authentication: Authentication passwords are encapsulated into IS-IS packets in Level-2 areas. The receiver only accepts the packets that have been authenticated. Therefore, you need to configure IS-IS routing domain authentication to authenticate packets in Level-2 areas.
* Interface authentication: The authentication information is encapsulated into IS-IS Hello packets. A neighbor relationship can be established only after IS-IS Hello packets are authenticated. Therefore, you need to configure interface authentication to authenticate neighbors.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

When configuring IS-IS authentication, the authentication mode and passwords of the routers in the same area must be consistent so that IS-IS packets can be flooded normally.

An IS-IS neighbor relationship cannot be established if interface authentication fails. An IS-IS neighbor relationship can be established regardless of whether IS-IS area or routing domain authentication succeeds.

When configuring an authentication password, select the ciphertext mode because the password is saved in the configuration file in simple text if you select simple text mode, which has a high risk. To ensure device security, change the password periodically.

It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.

For security purposes, you are advised not to use weak security algorithms in IS-IS. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.



#### Procedure

* Configure IS-IS area authentication.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run one of the following commands based on the encryption type:
     
     
     + [**area-authentication-mode**](cmdqueryname=area-authentication-mode) { **simple** { **plain** *plain* | [ **cipher** ] *cipher* } | **md5** { [ **cipher** ] *cipher* | **plain** *plain* } } [ **ip** | **osi** ] [ **snp-packet** { **authentication-avoid** | **send-only** } | **all-send-only** ]
     + [**area-authentication-mode**](cmdqueryname=area-authentication-mode) **keychain** *keychain-name* [ **snp-packet** { **authentication-avoid** | **send-only** } | **all-send-only** ]
     + [**area-authentication-mode**](cmdqueryname=area-authentication-mode) **hmac-sha256** **key-id** *key-id* { **plain** *plain* | [ **cipher** ] *cipher* } [ **snp-packet** { **authentication-avoid** | **send-only** } | **all-send-only** ]
     
     The area authentication mode is configured for IS-IS.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     After the [**area-authentication-mode**](cmdqueryname=area-authentication-mode) command is run, IS-IS discards the locally stored Level-1 LSPs that fail authentication and newly received Level-1 LSPs and SNPs that fail authentication after they are automatically aged. To prevent packet loss before authentication is configured, you can specify the **send-only** parameter in the command when deploying authentication on a network running services.
     
     The MD5 algorithm is not recommended if high security is required. To prevent routing information from being tampered with, you are advised to enable authentication and use high-security algorithms such as HMAC-SHA256 to improve security.
     
     You can configure area authentication in any of the following ways:
     
     + Do not specify **snp-packet** or **all-send-only**. In this case, the device encapsulates authentication information in the LSPs and SNPs to be sent, authenticates received LSPs and SNPs, and discards the LSPs and SNPs that fail to be authenticated.
     + Specify **snp-packet** and **authentication-avoid**. In this case, the device encapsulates authentication information in the LSPs to be sent and authenticates received LSPs; the device neither encapsulates authentication information in the SNPs to be sent nor authenticates received SNPs.
     + Specify **snp-packet** and **send-only**. In this case, the device encapsulates authentication information both in the LSPs and SNPs to be sent, but authenticates only received LSPs.
     + Specify **all-send-only**. In this case, the device encapsulates authentication information both in the LSPs and SNPs to be sent, but does not authenticate received LSPs or SNPs.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure IS-IS routing domain authentication.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run one of the following commands based on the encryption type:
     
     
     + [**domain-authentication-mode**](cmdqueryname=domain-authentication-mode) { **simple** { **plain** *plain* | **cipher** *cipher* } | **md5** { [ **cipher** ] *cipher* | **plain** *plain* } } [ **ip** | **osi** ] [ **snp-packet** { **authentication-avoid** | **send-only** } | **all-send-only** ]
     + [**domain-authentication-mode**](cmdqueryname=domain-authentication-mode) **keychain** *keychain-name* [ **snp-packet** { **authentication-avoid** | **send-only** } | **all-send-only** ]
     + [**domain-authentication-mode**](cmdqueryname=domain-authentication-mode) **hmac-sha256** **key-id** *key-id* { **plain** *plain* | [ **cipher** ] *cipher* } [ **snp-packet** { **authentication-avoid** | **send-only** } | **all-send-only** ]
     
     The routing domain authentication mode is configured for IS-IS.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     After the [**domain-authentication-mode**](cmdqueryname=domain-authentication-mode) command is run, IS-IS discards the locally stored Level-2 LSPs that fail authentication and newly received Level-2 LSPs and SNPs that fail authentication after they are automatically aged. To prevent packet loss before authentication is configured, you can specify the **send-only** parameter in the command when deploying authentication on a network running services.
     
     The MD5 algorithm is not recommended if high security is required. To prevent routing information from being tampered with, you are advised to enable authentication and use high-security algorithms such as HMAC-SHA256 to improve security.
     
     You can configure routing domain authentication in any of the following ways:
     
     + Do not specify **snp-packet** or **all-send-only**. In this case, the device encapsulates authentication information in the LSPs and SNPs to be sent, authenticates received LSPs and SNPs, and discards the LSPs and SNPs that fail to be authenticated.
     + Specify **snp-packet** and **authentication-avoid**. In this case, the device encapsulates authentication information in the LSPs to be sent and authenticates received LSPs; the device neither encapsulates authentication information in the SNPs to be sent nor authenticates received SNPs.
     + Specify **snp-packet** and **send-only**. In this case, the device encapsulates authentication information both in the LSPs and SNPs to be sent, but authenticates only received LSPs.
     + Specify **all-send-only**. In this case, the device encapsulates authentication information both in the LSPs and SNPs to be sent, but does not authenticate received LSPs or SNPs.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure IS-IS interface authentication.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run one of the following commands based on the encryption type:
     
     
     + [**isis authentication-mode**](cmdqueryname=isis+authentication-mode) { **simple** { **plain** *plain* | **cipher** *cipher* } | **md5** { [ **cipher** ] *cipher* | **plain** *plain* } } [ **level-1** | **level-2** ] [ **ip** | **osi** ] [ **send-only** ]
     + [**isis authentication-mode**](cmdqueryname=isis+authentication-mode) **keychain** *keychain-name* [ **level-1** | **level-2** ] [ **send-only** ]
     + [**isis authentication-mode**](cmdqueryname=isis+authentication-mode) **hmac-sha256** **key-id** *key-id* { **plain** *plain* | [ **cipher** ] *cipher* } [ **level-1** | **level-2** ] [ **send-only** ]
     
     The IS-IS authentication mode and password are configured on the interface.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The MD5 algorithm is not recommended if high security is required. To prevent routing information from being tampered with, you are advised to enable authentication and use high-security algorithms such as HMAC-SHA256 to improve security.
     
     
     
     When you select parameters, note the following rules:
     + If **send-only** is specified, the device encapsulates authentication information to Hello packets to be sent but does not authenticate received Hello packets. The neighbor relationships can be set up when the authentication is not required or packets are authenticated.
     + If **send-only** is not configured, ensure that passwords of all interfaces with the same level in the same network are consistent.
     + **Level-1 areas** and **level-2** can be set only on Ethernet interfaces.
     + When IS-IS interfaces are Level-1-2 interfaces and **Level-1 areas** or **level-2** is not specified in the command, authentication modes and passwords are configured for both Level-1 areas and Level-2 Hello packets.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.