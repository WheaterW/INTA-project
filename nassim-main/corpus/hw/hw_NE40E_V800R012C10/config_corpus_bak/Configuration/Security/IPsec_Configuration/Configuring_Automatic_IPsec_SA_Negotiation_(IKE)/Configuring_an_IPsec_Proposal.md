Configuring an IPsec Proposal
=============================

An IPsec proposal is a combination of security protocols, algorithms, and packet encapsulation modes to implement IPsec protection. An IPsec policy determines the security protocols, algorithms, and packet encapsulation modes using the IPsec proposal.

#### Context

During the configuration of an IPsec proposal, the same security protocol, authentication algorithm, encryption algorithm, and packet encapsulation mode must be configured at both ends of the tunnel to be established.

IPsec provides a high-quality and cryptology-based security for IP packets through AH and ESP security protocols.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipsec proposal**](cmdqueryname=ipsec+proposal) *proposal-name*
   
   
   
   An IPsec proposal is created, and the IPsec proposal view is displayed.
3. Run [**transform**](cmdqueryname=transform+ah+ah-esp+esp) { **ah** | **ah-esp** | **esp** }
   
   
   
   A security protocol for data transmission is configured.
   
   AH and ESP must be used independently. The rules for using them are as follows:
   
   * AH provides data source authentication, data integrity check, and the anti-replay function for the protected data.
   * ESP provides encryption, in addition to data source authentication, data integrity check, and anti-replay function, for the protected data.
4. Configure the authentication and encryption algorithms that are used by the security protocol.
   
   
   * If AH is used as a security protocol, you only need to configure the authentication algorithm of AH.
     + Run [**ah authentication-algorithm**](cmdqueryname=ah+authentication-algorithm+md5+sha1+sha2-256+sha2-384+sha2-512) { **md5** | **sha1** | **sha2-256** | **sha2-384** | **sha2-512** }
       
       An authentication algorithm used by AH is configured.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       To help improve system security, do not use the MD5 or SHA1 authentication algorithm for the AH protocol.
   * If ESP is used as a security protocol, you need to configure the authentication and encryption algorithms of ESP.
     + Run [**esp authentication-algorithm**](cmdqueryname=esp+authentication-algorithm+md5+sha1+sha2-256+sha2-384+sha2-512) { **md5** | **sha1** | **sha2-256** | **sha2-384** | **sha2-512** }
       
       An authentication algorithm used by ESP is configured.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       To help improve system security, do not use the MD5 or SHA1 authentication algorithm for the ESP protocol.
     + Run [**esp encryption-algorithm**](cmdqueryname=esp+encryption-algorithm+des+3des+aes+128+192+256) { **des** | **3des** | **aes** { **128** | **192** | **256** } }
       
       An encryption algorithm used by ESP is configured.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       To help improve system security, do not use the DES or 3DES encryption algorithm for the ESP protocol.
5. Run [**encapsulation-mode**](cmdqueryname=encapsulation-mode+transport+tunnel) { **transport** | **tunnel** }
   
   
   
   A packet encapsulation mode is configured.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.