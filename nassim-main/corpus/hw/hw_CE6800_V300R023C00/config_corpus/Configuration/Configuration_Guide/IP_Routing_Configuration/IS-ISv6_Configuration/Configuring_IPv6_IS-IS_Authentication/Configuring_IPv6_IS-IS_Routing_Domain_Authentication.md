Configuring IPv6 IS-IS Routing Domain Authentication
====================================================

Configuring IPv6 IS-IS Routing Domain Authentication

#### Context

The routing domain authentication password is encapsulated into Level-2 area IS-IS packets. Only authenticated packets are accepted. To implement Level-2 area authentication, configure IS-IS routing domain authentication.

![](public_sys-resources/note_3.0-en-us.png) 

For security purposes, you are advised not to use the weak security algorithms in IPv6 IS-IS. If you need to use such an algorithm, run the [**install feature-software WEAKEA**](cmdqueryname=install+feature-software+WEAKEA) command first to install the weak security algorithm/protocol feature package WEAKEA.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) process-id
   ```
3. Configure an authentication mode as required.
   
   
   * Configure simple authentication.
     ```
     [domain-authentication-mode](cmdqueryname=domain-authentication-mode) simple { plain simple-plain | [ cipher ] simple-cipher } [ ip | osi ] [ snp-packet { authentication-avoid | send-only } | all-send-only ]
     ```
   * Configure HMAC-MD5 authentication.
     ```
     [domain-authentication-mode](cmdqueryname=domain-authentication-mode) md5 { [ cipher ] md5-cipher | plain md5-plain } [ ip | osi ] [ snp-packet { authentication-avoid | send-only } | all-send-only ]
     ```
   * Configure keychain authentication.
     ```
     [domain-authentication-mode](cmdqueryname=domain-authentication-mode) keychain keychain-name [ snp-packet { authentication-avoid | send-only } | all-send-only ]
     ```
   * Configure HMAC-SHA256 authentication.
     ```
     [domain-authentication-mode](cmdqueryname=domain-authentication-mode) hmac-sha256 key-id key-id { plain plain | [ cipher ] cipher } [ snp-packet { authentication-avoid | send-only } | all-send-only ]
     ```
   
   
   
   You can configure routing domain authentication in any of the following ways:
   
   * Do not specify **snp-packet** or **all-send-only**. In this case, the device encapsulates authentication information in the LSPs and SNPs to be sent, authenticates received LSPs and SNPs, and discards the LSPs and SNPs that fail to be authenticated.
   * Specify **snp-packet** and **authentication-avoid**. In this case, the device encapsulates authentication information in the LSPs to be sent and authenticates received LSPs; the device neither encapsulates authentication information in the SNPs to be sent nor authenticates received SNPs.
   * Specify **snp-packet** and **send-only**. In this case, the device encapsulates authentication information both in the LSPs and SNPs to be sent, but authenticates only received LSPs.
   * Specify **all-send-only**. In this case, the device encapsulates authentication information both in the LSPs and SNPs to be sent, but does not authenticate received LSPs or SNPs.![](public_sys-resources/notice_3.0-en-us.png) 
   
   After the [**domain-authentication-mode**](cmdqueryname=domain-authentication-mode) command is run, IS-IS discards the locally stored Level-2 LSPs and newly received Level-2 LSPs and SNPs when they age out if they fail authentication. To prevent those packets from being discarded due to this command configuration, specify the **send-only** parameter in the command.
   
   Simple or HMAC-MD5 authentication is not recommended if high security is required. To prevent routing information from being tampered with, you are advised to enable authentication and use keychain or HMAC-SHA256 authentication to improve security.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```