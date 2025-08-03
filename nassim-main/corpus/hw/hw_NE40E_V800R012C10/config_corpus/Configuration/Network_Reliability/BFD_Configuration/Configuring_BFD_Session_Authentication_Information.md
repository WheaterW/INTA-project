Configuring BFD Session Authentication Information
==================================================

You can configure BFD session authentication information, such as the authentication algorithm, authentication key, and authentication encryption password, to improve network security.

#### Usage Scenario

If a network requires high security, you can configure BFD session authentication information to improve network security. You are advised to configure BFD negotiation authentication to reduce security risks.


#### Pre-configuration Tasks

Enable BFD globally and create a BFD session before configuring BFD session authentication information.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure BFD negotiation authentication based on the service scenario.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   
   
   
   * BFD sessions in multicast scenarios
     
     1. Run the [**bfd**](cmdqueryname=bfd) *session-name* command to enter the BFD session view.
     2. Run the [**authentication-mode**](cmdqueryname=authentication-mode) **met-sha1** **key-id** *key-id* **cipher** *cipher-text* **nego-packet** [ **enhanced** ] [ **timeout-interval** *interval-value* ] command to configure an authentication mode and authentication password for a BFD session.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The **enhanced** parameter indicates the enhanced authentication mode. In this mode, a BFD session in the up state needs to be authenticated when it receives AdminDown, Down, or P/F packets. In normal authentication mode, a BFD session needs to be authenticated only when it receives Down packets.
        
        Before configuring BFD authentication information, you need to create a multicast BFD session. The BFD session must use the multicast address for detection.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   * BFD sessions in BFD for IP scenarios
     
     + Single-hop BFD for IPv4 sessions
       
       Run the [**bfd**](cmdqueryname=bfd) **single-hop** **peer-ip** *ip-address* [ **vpn-instance** *vpn-name* ] **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet** command to configure negotiation authentication information for a BFD session.
     + Single-hop BFD for IPv6 sessions
       
       Run the [**bfd**](cmdqueryname=bfd) **single-hop** **peer-ipv6** *ipv6-address* [ **vpn-instance** *vpn-name* ] **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet** command to configure negotiation authentication information for a BFD session.
     + Multi-hop BFD for IPv4 sessions
       
       Run the [**bfd**](cmdqueryname=bfd) **multi-hop** **peer-ip** *ip-address* [ **vpn-instance** *vpn-name* ] **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet** command to configure negotiation authentication information for a BFD session.
     + Multi-hop BFD for IPv6 sessions
       
       Run the [**bfd**](cmdqueryname=bfd) **multi-hop** **peer-ipv6** *ipv6-address* [ **vpn-instance** *vpn-name* ] **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet** command to configure a negotiation authentication mode and authentication information for a BFD session.
   * BFD sessions in BFD for LSP scenarios
     
     + Passive BFD for LSP sessions
       
       Run the [**bfd**](cmdqueryname=bfd) **mpls-passive** **peer-ip** *ip-address* **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet** command to configure a negotiation authentication mode and authentication information for a BFD session.
     + Active BFD for LSP sessions
       
       Run the [**bfd**](cmdqueryname=bfd) **lsp-tunnel** **peer-ip** *ip-address* **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet** command to configure a negotiation authentication mode and authentication information for a BFD session.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.