PCEP
====

PCEP

#### Security Policy

* PCEP keychain authentication
  
  Keychain is an enhanced encryption algorithm. It calculates a digest for a piece of information to prevent PCEP packets from being tampered with.
  
  During keychain authentication, a group of passwords is defined to form a password string, and each password is assigned encryption and decryption algorithms, for example, SHA-2, and an expiration period. The system selects a valid password before sending or receiving a packet. Within the validity period of the password, the system uses the encryption algorithm matching the password to encrypt the packet before sending it. The system also uses the decryption algorithm matching the password to decrypt the packet before accepting the packet. In addition, the system can automatically use a new password after the previous password expires, preventing the password from being decrypted.
  
  The password of keychain authentication, the encryption and decryption algorithms, and the expiration period of the password can be configured separately on a keychain configuration node. A keychain configuration node at least requires one password and has the encryption and decryption algorithms specified.
  
  PCEP session authentication can be configured to improve network security and defend against attacks. Keychain authentication can be configured when a session is established between the PCE server and client.
* PCEP TLS authentication
  
  Transport Layer Security (TLS) is an SSL-based security protocol that ensures data integrity and confidentiality. It prevents the communication between the client and server from being eavesdropped.
  
  TLS authentication can be configured when a session is established between the PCE server and client to improve network security and prevent network attacks.
* TCP-AO authentication
  
  A TCP authentication option (TCP-AO) is used to authenticate received and to-be-sent packets during TCP session establishment and data exchange. It supports packet integrity check to prevent TCP replay attacks. After a TCP-AO is created, PCEP can be configured to reference the TCP-AO in order to implement PCEP session encryption. Different PCEP sessions can reference the same TCP-AO.
  
  A TCP-AO uses the passwords configured in the bound keychain, and these passwords can be automatically switched based on the configuration. However, the configuration process is complex and applies to networks with high security requirements.
* PCEP whitelist
  
  The application layer association module checks protocol packets to be sent to the CPU and sends protocol packets that match the whitelist at a high rate to the CPU. The PCEP whitelist feature is enabled by default and does not need to be configured.
* Session-CAR
  
  The whitelist session-CAR function is enabled for PCEP by default. It isolates packet channels between PCEP sessions.
* Micro-isolation CAR
  
  Micro-isolation CAR for PCEP is enabled by default to implement micro-isolation protection for PCEP connection establishment packets. If a device is attacked, packets of different PCEP sessions may preempt the bandwidth. Therefore, you are advised to keep this function enabled.

#### Attack Methods

None.



#### Procedure

* Configure PCEP keychain authentication.
  
  
  
  Before configuring PCEP keychain authentication, configure keychain globally. For details, see *NE40E Configuration Guide - Security*.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**pce-client**](cmdqueryname=pce-client)
     
     The PCE client view is displayed.
  3. Run [**connect-server**](cmdqueryname=connect-server)*ip-address*
     
     A candidate server is specified, and the PCE server connection view is displayed.
  4. Run **[**authentication keychain**](cmdqueryname=authentication+keychain)** *keychain-name*
     
     Session authentication between the PCE client and server is configured.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure PCEP TLS authentication.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**ssl policy**](cmdqueryname=ssl+policy) *policy-name*
     
     An SSL policy is created and the SSL policy view is displayed.
  3. Run [**ssl minimum version**](cmdqueryname=ssl+minimum+version) { **tls1.1** | **tls1.2** | **tls1.3** }
     
     The minimum version is set for the current SSL policy.
     
     For details about other configurations in the SSL policy view, see "Configuring and Binding an SSL Policy" in *NE40E Configuration Guide - Basic Configuration - User Login Configuration*.
  4. Run [**quit**](cmdqueryname=quit)
     
     Return to the system view.
  5. Run [**pce-client**](cmdqueryname=pce-client)
     
     The PCE client view is displayed.
  6. Run [**connect-server**](cmdqueryname=connect-server)*ip-address*
     
     A candidate server is specified, and the PCE server connection view is displayed.
  7. Run [**bind ssl-policy**](cmdqueryname=bind+ssl-policy)*ssl-policy-name* [ **pceps** ]
     
     A policy name is specified.
     
     The **pceps** parameter specifies the PCEPS mode for TLS negotiation. In this mode, the client and server perform StartTLS negotiation (compliant with RFC 8253) before starting TLS negotiation.
  8. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure PCEP TCP-AO authentication.
  
  
  
  Before configuring TCP-AO authentication, you need to configure TCP-AO. For details, see "TCP-AO Configuration" in NE40E Configuration Guide > Security.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**pce-client**](cmdqueryname=pce-client)
     
     The PCE client view is displayed.
  3. Run [**connect-server**](cmdqueryname=connect-server)*ip-address*
     
     A candidate server is specified, and the PCE server connection view is displayed.
  4. Run [**authentication tcp-ao**](cmdqueryname=authentication+tcp-ao) *tcp-ao-name*
     
     PCEP TCP-AO authentication is enabled.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure whitelist session-CAR for PCEP.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**whitelist session-car pcep-ipv4 disable**](cmdqueryname=whitelist+session-car+pcep-ipv4+disable)
     
     Whitelist session-CAR is disabled for PCEP.
     
     Disable this function only if it encounters an exception. In normal cases, you are advised to keep whitelist session-CAR enabled for PCEP.
  3. (Optional) Run [**whitelist session-car pcep-ipv4**](cmdqueryname=whitelist+session-car+pcep-ipv4) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
     
     Whitelist session-CAR parameters are configured for PCEP.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure micro-isolation CAR for PCEP.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**micro-isolation protocol-car pcep-ipv4**](cmdqueryname=micro-isolation+protocol-car+pcep-ipv4) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
     
     Micro-isolation CAR parameters are configured for PCEP.
     
     In normal cases, you are advised to use the default values of these parameters. *pir-value* must be greater than or equal to *cir-value*, and *pbs-value* must be greater than or equal to *cbs-value*.
  3. (Optional) Run [**micro-isolation protocol-car pcep-ipv4 disable**](cmdqueryname=micro-isolation+protocol-car+pcep-ipv4+disable)
     
     Micro-isolation CAR is disabled for PCEP.
     
     By default, micro-isolation CAR is enabled for PCEP. To disable this function for PCEP, run the [**micro-isolation protocol-car pcep-ipv4 disable**](cmdqueryname=micro-isolation+protocol-car+pcep-ipv4+disable) command. In normal cases, you are advised to keep micro-isolation CAR enabled for PCEP.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Configuration

* Run the **display pce protocol session** [ *ip-address* | **verbose** ] command to check PCEP session information, including the peer IP address, parameters on both ends, session status, and causes for session errors.
* Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **pcep** **statistics** **slot** *slot-id* command to check whitelist session-CAR statistics about PCEP packets on a specified interface board.