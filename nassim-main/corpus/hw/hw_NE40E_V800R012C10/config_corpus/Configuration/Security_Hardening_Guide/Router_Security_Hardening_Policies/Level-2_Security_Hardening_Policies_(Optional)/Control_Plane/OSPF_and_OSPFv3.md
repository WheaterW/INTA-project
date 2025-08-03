OSPF/OSPFv3
===========

OSPF/OSPFv3

#### Security Policy Overview

**OSPF/OSPFv3 packet authentication**

OSPF/OSPFv3 supports packet authentication. Packets are accepted only if they are authenticated. If packets fail to be authenticated, a neighbor relationship cannot be established. If area authentication is used, authentication mode and password configurations on all Routers in the same area must be the same. Interface authentication is implemented by setting an authentication mode and password between neighboring Routers. Interface authentication takes precedence over area authentication.

**OSPFv3 IPsec authentication**

Relevant standards (Authentication/Confidentiality for OSPFv3) define the use of the IP Security (IPsec) mechanism to authenticate OSPFv3 packets.

* Confidentiality: ESP is used to provide confidentiality. After ESP is enabled, OSPFv3 packets that are not protected by ESP and the packets that do not pass the confidentiality check are discarded.
* Data authentication: When OSPFv3 authentication is enabled, a device discards the OSPFv3 packets that are not protected by AH or ESP and the packets that fail authentication checks.

All OSPFv3 instances running over the same interface use the same SA.

OSPFv3 starts sending packets using IPsec authentication and notifies the lower layers to check received packets with IPsec authentication. The lower layers will check all the received packets, and the packets which fail the check will be discarded silently.


#### Attack Methods

**OSPF**

OSPF is attacked mainly through forged packets. To identify and discard these packets, authentication can be configured.

An attacker may use the following methods to initiate attacks:

* Changes the aging time of a packet to the maximum aging time so that all Routers discard this packet.
* Advertises the LSAs with valid Max Sequence Numbers or with sequence numbers close to the Max Sequence Number.
* Changes the sequence number when the state of the encryption sequence number resets during a neighbor Router restart.
* Changes the neighbor list in Hello packets.

**OSPFv3**

* DoS attacks:
  
  When a DoS attack occurs, the Router may obtain OSPFv3 packets from a remote path. These packets will be processed by an I/O board and sent to a main control board, on which they will be dropped by OSPFv3. This wastes bandwidth and CPU resources and reduces system performance.
* Injection of incorrect routing information:
  
  OSPFv3 accepts all packets from valid sources. A device may be attacked by OSPFv3 packets with invalid or incorrect routing information. Such information may cause errors when the route database is running, resulting in network failures. OSPFv3-IPsec authentication can be used to prevent this problem. When IPsec is configured for OSPFv3 on both communicating neighbors, OSPFv3 will process packets only if the packets are authenticated, which prevents OSPFv3 from accepting incorrect routing data from unauthenticated neighbors.


#### Configuration and Maintenance Methods

![](../../../../public_sys-resources/note_3.0-en-us.png) 

It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.

* Configure OSPF area authentication.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
     
     The OSPF view is displayed.
  3. Run [**area**](cmdqueryname=area) *area-id*
     
     The OSPF area view is displayed.
  4. Configure an authentication mode for the OSPF area as required.
     + To configure simple authentication for the OSPF area, run the [**authentication-mode simple**](cmdqueryname=authentication-mode+simple) [ [ **plain** ] *plain-text* | [ **cipher** ] *cipher-text* ] command.
     + To configure ciphertext authentication for the OSPF area, run the [**authentication-mode**](cmdqueryname=authentication-mode) { **md5** | **hmac-md5** | **hmac-sha256** } [ *key-id* { **plain** *plain-text* | [ **cipher** ] *cipher-text* } ] command.
     + To configure keychain authentication for the OSPF area, run the [**authentication-mode**](cmdqueryname=authentication-mode) **keychain** *keychain-name* command.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       Before using keychain authentication, you need to run the [**keychain**](cmdqueryname=keychain) command to create a keychain, and then run the [**key-id**](cmdqueryname=key-id), [**key-string**](cmdqueryname=key-string), and [**algorithm**](cmdqueryname=algorithm) commands to configure a key ID, a password, and an authentication algorithm, respectively, for this keychain. Otherwise, OSPF authentication will fail.
       
       To ensure high security, you are advised to use a more secure algorithm, such as HMAC-SHA256, instead of the MD5 and HMAC-MD5 algorithms.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure OSPF interface authentication.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The OSPF interface view is displayed.
  3. Run any of the following commands:
     + To configure simple authentication for the OSPF interface, run the [**ospf authentication-mode simple**](cmdqueryname=ospf+authentication-mode+simple) [ [ **plain** ] *plain-text* | [ **cipher** ] *cipher-text* ] command.
     + To configure ciphertext authentication for the OSPF interface, run the [**ospf authentication-mode**](cmdqueryname=ospf+authentication-mode) { **md5** | **hmac-md5** | **hmac-sha256** } [ *key-id* { **plain** *plain-text* | [ **cipher** ] *cipher-text* } ] command.
     + To configure keychain authentication for the OSPF interface, run the [**ospf authentication-mode**](cmdqueryname=ospf+authentication-mode) **keychain** *keychain-name* command.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       Before using keychain authentication, you need to run the [**keychain**](cmdqueryname=keychain) command to create a keychain, and then run the [**key-id**](cmdqueryname=key-id), [**key-string**](cmdqueryname=key-string), and [**algorithm**](cmdqueryname=algorithm) commands to configure a key ID, a password, and an authentication algorithm, respectively, for this keychain. Otherwise, OSPF authentication will fail.
       
       To ensure high security, you are advised to use a more secure algorithm, such as HMAC-SHA256, instead of the MD5 and HMAC-MD5 algorithms.
     + Run [**ospf authentication-mode null**](cmdqueryname=ospf+authentication-mode+null)
       
       The OSPF interface does not perform authentication.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure OSPFv3 area authentication.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
     
     The OSPFv3 view is displayed.
  3. Run [**area**](cmdqueryname=area) *area-id*
     
     The OSPFv3 area view is displayed.
  4. Configure an authentication mode for the OSPFv3 area as required.
     + To configure the HMAC-SHA256 or HMAC-SM3 authentication mode for the OSPFv3 area, run the [**authentication-mode**](cmdqueryname=authentication-mode) { **hmac-sha256** | **hmac-sm3** } **key-id** *KeyId* { **plain** *PlainText* | [ **cipher** ] *CipherText* } command.
       
       If you choose **plain**, the password will be saved as a plaintext in the configuration file, which provokes high security risks. To improve device security, choose ciphertext authentication and change the password periodically.
     + To configure the keychain authentication mode for the OSPFv3 area, run the [**authentication-mode**](cmdqueryname=authentication-mode) { **keychain** *Keychain-Name* } command.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       Before using keychain authentication, you need to run the [**keychain**](cmdqueryname=keychain) command to create a keychain, and then run the [**key-id**](cmdqueryname=key-id), [**key-string**](cmdqueryname=key-string), and [**algorithm**](cmdqueryname=algorithm) commands to configure a key ID, a password, and an authentication algorithm, respectively, for this keychain. Otherwise, OSPF authentication will fail.
       
       If area authentication is used, authentication mode and password configurations on all Routers in the same area must be the same.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure OSPFv3 process authentication.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
     
     The OSPFv3 view is displayed.
  3. Configure an authentication mode for the OSPFv3 process as required.
     + To configure the HMAC-SHA256 or HMAC-SM3 authentication mode for the OSPFv3 process, run the **authentication-mode** { **hmac-sha256** | **hmac-sm3** } **key-id** *KeyId* { **plain** *PlainText* | [ **cipher** ] *CipherText* } command.
       
       If you choose **plain**, the password will be saved as a plaintext in the configuration file, which provokes high security risks. To improve device security, choose ciphertext authentication and change the password periodically.
     + To configure the keychain authentication mode for the OSPFv3 process, run the [**authentication-mode**](cmdqueryname=authentication-mode) { **keychain** *Keychain-Name* } command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Before using keychain authentication, you need to run the [**keychain**](cmdqueryname=keychain) command to create a keychain, and then run the [**key-id**](cmdqueryname=key-id), [**key-string**](cmdqueryname=key-string), and [**algorithm**](cmdqueryname=algorithm) commands to configure a key ID, a password, and an authentication algorithm, respectively, for this keychain. Otherwise, OSPFv3 authentication will fail.
  4. Run **commit**
     
     The configuration is committed.
* Configure OSPFv3 interface authentication.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The interface view is displayed.
  3. Configure an authentication mode for the OSPFv3 interface as required.
     + To configure the HMAC-SHA256 or HMAC-SM3 authentication mode for the OSPFv3 interface, run the **authentication-mode** { **hmac-sha256** | **hmac-sm3** } **key-id** *KeyId* { **plain** *PlainText* | [ **cipher** ] *CipherText* } command.
       
       If you choose **plain**, the password will be saved as a plaintext in the configuration file, which provokes high security risks. To improve device security, choose ciphertext authentication and change the password periodically.
     + To configure the keychain authentication mode for the OSPFv3 interface, run the [**ospfv3 authentication-mode**](cmdqueryname=ospfv3+authentication-mode) { **keychain** *Keychain-Name* } command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Before using keychain authentication, you need to run the [**keychain**](cmdqueryname=keychain) command to create a keychain, and then run the [**key-id**](cmdqueryname=key-id), [**key-string**](cmdqueryname=key-string), and [**algorithm**](cmdqueryname=algorithm) commands to configure a key ID, a password, and an authentication algorithm, respectively, for this keychain. Otherwise, OSPFv3 authentication will fail.
     
     Interface authentication takes precedence over area authentication. For interfaces on the same subnet, the configured authentication mode and password must be identical. This requirement does not apply to the interfaces on different subnets.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* OSPFv3 IPsec authentication
  
  1. Configure an IPsec proposal.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**ipsec proposal**](cmdqueryname=ipsec+proposal) *proposal-name*
        
        An IPsec proposal is created, and the IPsec proposal view is displayed.
     3. (Optional) Run [**transform**](cmdqueryname=transform) { **ah** | **esp** | **ah-esp** }
        
        A security protocol is configured.
     4. Run [**esp authentication-algorithm**](cmdqueryname=esp+authentication-algorithm) { **md5** | **sha1** | **sha2-256** | **sha2-384** | **sha2-512** }
        
        An authentication algorithm is configured for ESP.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        For higher security, the MD5 authentication algorithm is not recommended for the ESP protocol.
        
        Before configuring a security algorithm for a security protocol, run the [**transform**](cmdqueryname=transform) command to specify the security protocol.
     5. Run [**esp encryption-algorithm**](cmdqueryname=esp+encryption-algorithm) { **3des** | **des** | **aes** [ **128** | **192** | **256** ] }
        
        An encryption algorithm used for ESP is configured.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The encryption algorithms DES/3DES have a low security, which may bring security risks. If protocols allowed, using more secure encryption algorithms, such as AES, is recommended.
     6. Run [**encapsulation-mode**](cmdqueryname=encapsulation-mode) **transport**
        
        The packet encapsulation mode is configured.
     7. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
  2. Configure an IPsec SA.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**ipsec sa**](cmdqueryname=ipsec+sa) *sa-name*
        
        An SA is created.
     3. Run [**proposal**](cmdqueryname=proposal) *proposal-name*
        
        A proposal is applied to the SA.
     4. Run [**sa spi**](cmdqueryname=sa+spi) { **inbound** | **outbound** } { **ah** | **esp** } *spi-number*
        
        Security parameter indexes (SPIs) are configured.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The SA parameters set at both ends of the IPsec tunnel must be the same. The inbound SPI on the local end must be consistent with the outbound SPI on the peer end, and the outbound SPI on the local end must be consistent with the inbound SPI on the peer end.
     5. Run either of the following commands:
        1. To configure an authentication key in the format of hexadecimal numerals, run the [**sa authentication-hex**](cmdqueryname=sa+authentication-hex) { **inbound** | **outbound** } { **ah** | **esp** } [ **cipher** ] *hex-cipher-key* command.
        2. To configure an authentication key in the format of a character string, run the [**sa string-key**](cmdqueryname=sa+string-key) { **inbound** | **outbound** } { **ah** | **esp** } [ **cipher** ] *string-cipher-key* command.
     6. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
  3. Enable OSPFv3 IPsec.
     + Enable IPsec in the OSPFv3 process.
       1. Run [**system-view**](cmdqueryname=system-view)
          
          The system view is displayed.
       2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
          
          The OSPFv3 view is displayed.
       3. Run [**ipsec sa**](cmdqueryname=ipsec+sa) *sa-name*
          
          The SA is enabled in the OSPFv3 process.
          
          ![](../../../../public_sys-resources/note_3.0-en-us.png) 
          
          An OSPFv3 process can be associated with multiple OSPFv3 areas. An SA applied in the OSPFv3 process can be used in the associated areas.
       4. Run [**commit**](cmdqueryname=commit)
          
          The configuration is committed.
     + Enable IPsec in an OSPFv3 area.
       1. Run [**system-view**](cmdqueryname=system-view)
          
          The system view is displayed.
       2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
          
          The OSPFv3 view is displayed.
       3. Run [**area**](cmdqueryname=area) *area-id*
          
          The OSPFv3 area view is displayed.
       4. Run [**ipsec sa**](cmdqueryname=ipsec+sa) *sa-name*
          
          The SA is enabled in the OSPFv3 area.
          
          ![](../../../../public_sys-resources/note_3.0-en-us.png) 
          
          The SA configured on an OSPFv3 area takes precedence over that configured in an OSPFv3 process.
       5. Run [**commit**](cmdqueryname=commit)
          
          The configuration is committed.

#### Verifying the Security Hardening Result

* Run the [**display this**](cmdqueryname=display+this) command to check packet authentication information.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] command to check the SA applied to the process.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **area** [ *area-id* ] command to check the SA applied to the area.