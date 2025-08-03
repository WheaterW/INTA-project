Configuring an IKE Proposal
===========================

An IKE proposal defines a set of attribute data to describe how IKE negotiation implements security communications. Configuring an IKE proposal involves creating an IKE proposal, selecting an encryption algorithm, authentication mode, authentication algorithm, and Diffie-Hellman identifier, and setting the lifetime of the SA.

#### Context

Parameters defined by an IKE proposal are used to negotiate IKE SA establishment. You can configure multiple IKE proposals on each end. During the negotiation, parameters to be negotiated are matched against each IKE proposal in descending order by priority and match a local IKE proposal that is the same as that on the peer end. The match rule is as follows: Both parties use the same encryption algorithm, authentication algorithm, authentication method, and DH group ID to negotiate with each other. The lifetime is determined by the party that initiates the negotiation and does not need to be identical on both ends.

If the negotiation initiating party specifies an IKE proposal on the IKE peer, only the specified IKE protocol can be sent during the IKE negotiation. The response party matches the specified IKE protocol against its IKE proposals. If no IKE proposal is matched, the negotiation fails.

If the negotiation initiating party does not specify any IKE proposal on the IKE peer, all IKE proposals of the initiating party are sent during the IKE negotiation. The response party matches the IKE proposals against its IKE proposals in sequence.

The system provides three default IKE proposals. If no IKE proposal is created, default1, default2, and default3 are used.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

The default IKE proposals contain insecure algorithms. To ensure better security, you are advised not to use the default IKE proposals.

* default1: The encryption algorithm is AES-CBC-256, the authentication algorithm is SHA2-256, the authentication method is Pre-Shared Key, the Diffie-Hellman group ID is group14, and the lifetime is 86400 seconds.
* default2: The encryption algorithm is AES-CBC-256, the authentication algorithm is SHA2-256, the authentication method is Pre-Shared Key, the Diffie-Hellman group ID is group2, and the lifetime is 86400 seconds.
* default3: The encryption algorithm is AES-CBC-256, the authentication algorithm is SHA1, the authentication method is Pre-Shared Key, the Diffie-Hellman group ID is group1, and the lifetime is 86400 seconds.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function first.

You can run the [**display ike proposal**](cmdqueryname=display+ike+proposal) command to view the configured IKE proposals (including the default IKE proposals).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ike proposal**](cmdqueryname=ike+proposal) *proposal-number*
   
   
   
   IKE proposals are created, and the IKE proposal view is displayed.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For a newly created IKE proposal, the default encryption algorithm is AES-CBC-256, the default authentication algorithm is SHA2-256, the default authentication method is Pre-Shared Key, the default Diffie-Hellman group ID is not configured, and the default lifetime is 86400 seconds. Change the values of these parameters as required. The new values take effect in the next tunnel negotiation instead of tunnels that have been negotiated.
3. Run [**authentication-method**](cmdqueryname=authentication-method+pre-share+rsa-sig+rsassa-pss+sha2-256) { **pre-share** | **rsa-sig** | **rsassa-pss** { **sha2-256** | **sha2-384** } }
   
   
   
   An authentication mode is configured.
4. Run [**authentication-algorithm**](cmdqueryname=authentication-algorithm+md5+sha1+sha2-256+sha2-384+sha2-512) { **md5** | **sha1** | **sha2-256** | **sha2-384** | **sha2-512** }
   
   
   
   An authentication algorithm is configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To help improve the system security, do not use the MD5 or SHA1 authentication algorithm for IKE negotiation.
5. Run [**encryption-algorithm**](cmdqueryname=encryption-algorithm+3des-cbc+aes-cbc+128+192+256+des-cbc) { **3des-cbc** | **aes-cbc** { **128** | **192** | **256** } | **des-cbc** | **aes-gcm-128** { **128** | **192** | **256**} }
   
   
   
   An encryption algorithm is configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To help improve the system security, do not use the DES-CBC or 3DES-CBC encryption algorithm for IKE negotiation.
6. Run [**dh**](cmdqueryname=dh+group1+group2+group5+group14+group19+group20+group21){ **group1** | **group2** | **group5** | **group14** | **group15** | **group16** | **group19** | **group20** | **group21** }
   
   
   
   A DH group ID is set.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To help improve system security, using the group1, group2, and group5 for the DH group ID is not recommended.
7. (Optional) Run [**integrity-algorithm**](cmdqueryname=integrity-algorithm+aes-xcbc-96+hmac-md5-96+hmac-sha1-96) { **aes-xcbc-96** | **hmac-md5-96** | **hmac-sha1-96** | **hmac-sha2-256** | **hmac-sha2-384** | **hmac-sha2-512** }
   
   
   
   An integrity algorithm is configured.
   
   The configuration is valid only for the IKEv2 protocol.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To help improve the system security, using the AES-XCBC-96, HMAC-MD5-96, and HMAC-SHA1-96 integrity algorithms for IKEv2 negotiation is not recommended.
8. Run [**sa duration**](cmdqueryname=sa+duration) *sa-duration*
   
   
   
   An SA duration is set.
9. (Optional) Run [**re-authentication interval**](cmdqueryname=re-authentication+interval) *reauth-time*
   
   
   
   The re-authentication duration of an IKEv2 SA is set.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.