Configuring an SA
=================

Configure a Security Association (SA) and specify a security protocol, a security parameter index (SPI), and authentication keys.

#### Context

An SA is unidirectional. Incoming and outgoing protocol packets are processed by different SAs. To ensure smooth SA negotiation, configure the same parameters for the SAs that apply to incoming protocol packets and outgoing protocol packets of the same flow, respectively. The parameters are as follows:

* Security proposal: defines the specific protection, including the authentication and encryption algorithms.
* SPI: is a Security Parameter Index that identifies an SA.
* Key: is used to calculate message digests and encrypt protocol packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipsec sa**](cmdqueryname=ipsec+sa) *sa-name*
   
   
   
   An SA is created, and the SA view is displayed.
3. Run [**proposal**](cmdqueryname=proposal) *proposal-name*
   
   
   
   A security proposal is applied to the SA.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A security proposal must be configured before it can be associated with protocol packet flows.
   
   One SA can use only one security proposal. If a security proposal has been applied to an SA, the SA can use another security proposal only after the original one is deleted.
4. Run [**sa spi**](cmdqueryname=sa+spi+inbound+outbound+ah+esp) { **inbound** | **outbound** } { **ah** | **esp** } *spi-number*
   
   
   
   An SPI is set.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SPI uniquely identifies an SA. The inbound and outbound SPIs are set, and the inbound SPI on the local end must be the same as the outbound SPI on the peer end.
5. To configure the authentication key, run either of the following commands:
   1. Run [**sa authentication-hex**](cmdqueryname=sa+authentication-hex+inbound+outbound+ah+esp+cipher) { **inbound** | **outbound** } { **ah** | **esp** } [ **cipher** ] *key-cipher-key*
      
      
      
      An authentication key in hexadecimal format or ciphertext is set.
   2. Run [**sa string-key**](cmdqueryname=sa+string-key+inbound+outbound+ah+esp+cipher) { **inbound** | **outbound** } { **ah** | **esp** } [ **cipher** ] *string-cipher-key*
      
      
      
      An authentication key in string format is set.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An authentication key for outgoing protocol packets on the local end must be identical with that for incoming protocol packets on the peer end.
   
   If multiple authentication keys are configured, the latest one takes effect.
   
   Updating keys periodically is recommended.
6. (Optional) Run [**sa encryption-hex**](cmdqueryname=sa+encryption-hex+inbound+outbound+esp+cipher) { **inbound** | **outbound** } **esp** [ **cipher** ] *hex-cipher-key*
   
   
   
   An encryption key is set.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.