Configuring a Security Proposal
===============================

A security proposal can be configured to define the security protocol, authentication and encryption algorithms for protocol packets, and encapsulation mode.

#### Context

Before using IPsec to authenticate and encrypt protocol packets, you must create a security proposal and define the security protocol type, authentication and encryption algorithms, and encapsulation mode in the security proposal.

The security protocols, authentication and encryption algorithms for protocol packets, and encapsulation modes must be the same on IPsec peers.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function first.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipsec proposal**](cmdqueryname=ipsec+proposal) *proposal-name*
   
   
   
   A security proposal is created and the security proposal view is displayed.
3. Run [**encapsulation-mode**](cmdqueryname=encapsulation-mode+transport) **transport**
   
   The protocol packet encapsulation mode is configured.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Manual IPsec supports only the transport mode, the tunnel mode is not supported.
4. (Optional) Run [**transform**](cmdqueryname=transform+ah+esp) { **ah** | **esp** | **ah-esp** }
   
   
   
   A security protocol is configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Because AH does not support encryption in IPsec scenarios, ESP is recommended.
5. An authentication algorithm and an encryption algorithm are configured based on the selected security protocol.
   
   
   * If Authentication Header (AH) is configured, run the [**ah authentication-algorithm**](cmdqueryname=ah+authentication-algorithm+md5+sha1+sha2-256+sha2-384+sha2-512) { **md5** | **sha1** | **sha2-256** | **sha2-384** | **sha2-512** } command to configure an authentication algorithm.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To help provide high security, do not use the MD5 or SHA1 algorithm as an AH authentication algorithm.
   * If ESP is configured, run the [**esp authentication-algorithm**](cmdqueryname=esp+authentication-algorithm+md5+sha1+sha2-256+sha2-384+sha2-512) { **md5** | **sha1** | **sha2-256** | **sha2-384** | **sha2-512** } command to configure an authentication algorithm.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To help provide high security, do not use the MD5 or SHA1 algorithm as an ESP authentication algorithm.
   * If ESP is configured, run the [**esp encryption-algorithm**](cmdqueryname=esp+encryption-algorithm+des+3des+aes+128+192+256) { **des** | **3des** | **aes** { **128** | **192** | **256** } } command to configure an ESP encryption algorithm.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To help provide high security, do not use the DES or 3DES algorithm as an ESP encryption algorithm.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.