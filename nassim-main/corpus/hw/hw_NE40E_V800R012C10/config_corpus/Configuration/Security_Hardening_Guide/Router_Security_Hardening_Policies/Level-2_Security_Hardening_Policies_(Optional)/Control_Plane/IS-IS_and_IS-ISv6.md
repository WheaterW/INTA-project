IS-IS/IS-ISv6
=============

IS-IS/IS-ISv6

#### Security Policy Overview

IS-IS authentication encrypts IS-IS packets by adding the authentication field to packets to improve network security. After receiving IS-IS packets from a remote Router, a local Router discards the packets if the authentication passwords in the packets are different from the locally configured one. This mechanism protects the local Router.


#### Attack Methods

Denial of error packets: Attackers can get correct Hello packets or link state packets from a network, forge attack packets with identifiable IS-IS packets, and send these packets to Routers. Although Routers can identify and discard these attack packets based on the authentication information, Routers may also discard correct packets because they cannot immediately process these packets. This affects network stability.


#### Procedure

![](../../../../public_sys-resources/note_3.0-en-us.png) 

It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.

* Configure IS-IS area authentication.
  1. Run **system-view**
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     The IS-IS view is displayed.
  3. Run one of the following commands based on the encryption type to configure IS-IS routing domain authentication:
     + [**area-authentication-mode**](cmdqueryname=area-authentication-mode) { **simple** { **plain** *plain* | [ **cipher** ] *cipher* } | **md5** { [ **cipher** ] *cipher* | **plain** *plain* } } [ **ip** | **osi** ] [ **snp-packet** { **authentication-avoid** | **send-only** } | **all-send-only** ]
     + [**area-authentication-mode**](cmdqueryname=area-authentication-mode) **keychain** *keychain-name* [ **snp-packet** { **authentication-avoid** | **send-only** } | **all-send-only** ]
     + [**area-authentication-mode**](cmdqueryname=area-authentication-mode) **hmac-sha256** **key-id** *key-id* { **plain** *plain* | [ **cipher** ] *cipher* } [ **snp-packet** { **authentication-avoid** | **send-only** } | **all-send-only** ]![](../../../../public_sys-resources/notice_3.0-en-us.png) 
       
       After the [**area-authentication-mode**](cmdqueryname=area-authentication-mode) command is run, IS-IS discards the locally stored Level-1 LSPs that fail authentication and newly received Level-1 LSPs and SNPs that fail authentication after they are automatically aged. To prevent packet loss before authentication is configured, you can specify the **send-only** parameter in the command when deploying authentication on a network running services.
       
       The MD5 algorithm is not recommended if high security is required. To prevent routing information from being tampered with, you are advised to enable authentication and use high-security algorithms such as HMAC-SHA256 to improve security.You can configure area authentication in any of the following ways:
     + Do not specify **snp-packet** or **all-send-only**. In this case, the device encapsulates authentication information in the LSPs and SNPs to be sent, authenticates received LSPs and SNPs, and discards the LSPs and SNPs that fail to be authenticated.
     + Specify **snp-packet** **authentication-avoid**. In this case, the device encapsulates authentication information in the LSPs to be sent and authenticates received LSPs; the device neither encapsulates authentication information in the SNPs to be sent nor authenticates received SNPs.
     + Specify **snp-packet send-only**. In this case, the device encapsulates authentication information both in the LSPs and SNPs to be sent, but authenticates only received LSPs (not received SNPs).
     + Specify **all-send-only**. In this case, the device encapsulates authentication information both in the LSPs and SNPs to be sent, but does not authenticate received LSPs or SNPs.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure IS-IS routing domain authentication.
  1. Run **system-view**
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     The IS-IS view is displayed.
  3. Run one of the following commands based on the encryption type to configure IS-IS routing domain authentication:
     + [**domain-authentication-mode**](cmdqueryname=domain-authentication-mode) { **simple** { **plain** *plain* | **cipher** *cipher* } | **md5** { [ **cipher** ] *cipher* | **plain** *plain* } } [ **ip** | **osi** ] [ **snp-packet** { **authentication-avoid** | **send-only** } | **all-send-only** ]
     + [**domain-authentication-mode**](cmdqueryname=domain-authentication-mode) **keychain** *keychain-name* [ **snp-packet** { **authentication-avoid** | **send-only** } | **all-send-only** ]
     + [**domain-authentication-mode**](cmdqueryname=domain-authentication-mode) **hmac-sha256** **key-id** *key-id* { **plain** *plain* | [ **cipher** ] *cipher* } [ **snp-packet** { **authentication-avoid** | **send-only** } | **all-send-only** ]![](../../../../public_sys-resources/notice_3.0-en-us.png) 
       
       After the [**domain-authentication-mode**](cmdqueryname=domain-authentication-mode) command is run, IS-IS discards the locally stored Level-2 LSPs that fail authentication and newly received Level-2 LSPs and SNPs that fail authentication after they are automatically aged. To prevent packet loss before authentication is configured, you can specify the **send-only** parameter in the command when deploying authentication on a network running services.
       
       The MD5 algorithm is not recommended if high security is required. To prevent routing information from being tampered with, you are advised to enable authentication and use high-security algorithms such as HMAC-SHA256 to improve security.You can configure routing domain authentication in any of the following ways:
     + Do not specify **snp-packet** or **all-send-only**. In this case, the device encapsulates authentication information in the LSPs and SNPs to be sent, authenticates received LSPs and SNPs, and discards the LSPs and SNPs that fail to be authenticated.
     + Specify **snp-packet** **authentication-avoid**. In this case, the device encapsulates authentication information in the LSPs to be sent and authenticates received LSPs; the device neither encapsulates authentication information in the SNPs to be sent nor authenticates received SNPs.
     + Specify **snp-packet send-only**. In this case, the device encapsulates authentication information both in the LSPs and SNPs to be sent, but authenticates only received LSPs (not received SNPs).
     + Specify **all-send-only**. In this case, the device encapsulates authentication information both in the LSPs and SNPs to be sent, but does not authenticate received LSPs or SNPs.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure IS-IS interface authentication.
  1. Run **system-view**
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The interface view is displayed.
  3. Run one of the following commands based on the encryption type to configure the IS-IS authentication mode and password for the interface.
     + [**isis authentication-mode**](cmdqueryname=isis+authentication-mode) { **simple** { **plain** *plain* | **cipher** *cipher* } | **md5** { [ **cipher** ] *cipher* | **plain** *plain* } } [ **level-1** | **level-2** ] [ **ip** | **osi** ] [ **send-only** ]
     + [**isis authentication-mode**](cmdqueryname=isis+authentication-mode) **keychain** *keychain-name* [ **level-1** | **level-2** ] [ **send-only** ]
     + [**isis authentication-mode**](cmdqueryname=isis+authentication-mode) **hmac-sha256** **key-id** *key-id* { **plain** *plain* | [ **cipher** ] *cipher* } [ **level-1** | **level-2** ] [ **send-only** ]![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The MD5 algorithm is not recommended if high security is required. To prevent routing information from being tampered with, you are advised to enable authentication and use high-security algorithms such as HMAC-SHA256 to improve security.
     
     
     When you select parameters, note the following rules:
     + If **send-only** is specified, the device encapsulates authentication information to Hello packets to be sent but does not authenticate received Hello packets. The neighbor relationships can be set up when the authentication is not required or packets are authenticated.
     + If **send-only** is not configured, ensure that passwords of all interfaces with the same level in the same network are consistent.
     + The **level-1** and **level-2** parameters can be set only on Ethernet interfaces.
     + If the IS-IS interface is a Level-1-2 interface, and neither **level-1** nor **level-2** is specified, the authentication mode and password are configured for both Level-1 and Level-2 Hello packets.
  4. Run [**quit**](cmdqueryname=quit)
     
     Return to the system view.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Security Hardening Result

Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) **verbose** command to check IS-IS LSDB information.