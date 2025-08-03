(Optional) Configuring SBFD Session Authentication Information
==============================================================

You can configure SBFD session authentication information, such as the authentication algorithm, authentication key, and authentication encryption password, to improve network security.

#### Usage Scenario

If a network requires high security, you can configure SBFD session authentication information to improve network security. You are advised to configure SBFD negotiation authentication to reduce security risks.


#### Pre-configuration Tasks

Before configuring SBFD session authentication information, enable SBFD globally.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure SBFD negotiation authentication based on the service scenario.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   
   
   
   * BFD sessions in SBFD for IP scenarios
     
     Run the [**sbfd**](cmdqueryname=sbfd) **multi-hop** **peer-ipv6** *ipv6-address* **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet** command to configure a negotiation authentication mode and authentication information for a multi-hop SBFD for IPv6 session.
   * BFD sessions in SBFD for LSP/Tunnel scenarios
     
     Run the [**sbfd**](cmdqueryname=sbfd) **lsp-tunnel** **peer-ip** *ip-address* **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet** command to configure a negotiation authentication mode and authentication information for an SBFD for LSP/Tunnel session.
   * BFD sessions in SBFD for SR-MPLS TE Policy scenarios
     
     Run the [**sbfd**](cmdqueryname=sbfd) **sr-te-policy segment-list endpoint** *endpoint-address* **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet** command to configure a negotiation authentication mode and authentication information for an SBFD for SR-MPLS TE Policy segment list session.
   * BFD sessions in SBFD for SRv6 TE Policy scenarios
     
     Run the [**sbfd**](cmdqueryname=sbfd) **srv6-te-policy segment-list endpoint** *endpoint-address* **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet** command to configure a negotiation authentication mode and authentication information for an SBFD for SRv6 TE Policy segment list session.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.