Configuring PCEP Session Authentication
=======================================

PCEP session authentication can be configured to improve network security and defend against attacks.

#### Usage Scenario

To ensure the security of sessions between PCE clients and servers and prevent unauthorized access, configure PCEP session authentication for enhanced network security.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   The PCE client view is displayed.
3. Run [**connect-server**](cmdqueryname=connect-server) *ip-address*
   
   
   
   A candidate PCE server is configured for the PCE client, and the PCE server connection view is displayed.
4. Perform any of the following steps to configure PCEPv4 session authentication:
   * Run the [**bind ssl-policy**](cmdqueryname=bind+ssl-policy) *ssl-policy-name* [ **pceps** ] command to bind an SSL policy to the PCEP session. A PCEP session is a common TCP connection, which has security risks. To establish a secure SSL connection between the PCE client and server, perform this step to bind an SSL policy to the PCEP session.
     
     The **pceps** parameter specifies the PCEPS mode for TLS negotiation. In this mode, the client and server perform StartTLS negotiation (compliant with RFC 8253) before starting TLS negotiation.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The specified SSL policy must have been created before you perform this step.
   * Run the [**authentication keychain**](cmdqueryname=authentication+keychain) *keychain-name* command to configure keychain session authentication between the PCE client and server.
   * Run the [**authentication tcp-ao**](cmdqueryname=authentication+tcp-ao) *tcp-ao-name* command to configure TCP-AO authentication for establishing a PCEP session between the PCE client and server.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To use TCP-AO authentication, you need to create a TCP-AO first. For details, see [Configuring a TCP-AO and Binding It to a Keychain](cfg_tcpao_0008.html).
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.