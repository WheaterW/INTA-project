Configuring CMP Sessions
========================

To configure a CMP session, specify an RSA key pair, a CA server name, and PKI entity information used to obtain a certificate using CMPv2.

#### Context

If you run the [**authentication-method**](cmdqueryname=authentication-method+rsassa-pss) **rsassa-pss** { **sha2-256** | **sha2-384** }command to use certificates for identity authentication, configure a mode for obtaining certificates.

If CMP is used to obtain and manage certificates, the NE40E and CA server establish a CMP session to exchange the information required for generating certificates. Before a CMP session is established, ensure that the NE40E has the following information to establish the CMP session:

* PKI entity
* Key pair
* Name of the CA server that establishes a CMP session with the NE40E
* Certificate for proving the identity of the NE40E
* URL of the CMP server that receives CMP requests

Each digital certificate has a validity period. To ensure service availability, apply for a new certificate before the existing certificate expires. However, manual update may leave certain certificates not updated. The NE40E supports automatic certificate update. When the system detects that the configured automatic certificate update time expires, the system automatically sends a certificate update request to the CMPv2 server. The new certificate overrides the certificate file in the CF card, configuration used in IKE negotiation, and certificate in the memory.

Perform the following steps on the NE40E that needs to obtain a certificate in CMP mode:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pki domain**](cmdqueryname=pki+domain) *domain-name*
   
   
   
   A PKI domain is created, and the PKI domain name configuration view is displayed.
3. Run [**pki cmp session**](cmdqueryname=pki+cmp+session) *session-name*
   
   
   
   A CMP session is created, and the PKI CMP session view is displayed.
4. Run [**cmp request entity**](cmdqueryname=cmp+request+entity) *entity-name*
   
   
   
   A PKI entity is specified to initiate CMP requests.
5. Run [**cmp request rsa local-key-pair**](cmdqueryname=cmp+request+rsa+local-key-pair+regenerate) *key-pair-name* [ **regenerate** [ *key-bit* ] ]
   
   
   
   A local RSA key pair to be used by CMP requests is specified.
6. ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   An RSA key pair can be referenced by only one CMP session or PKI domain.
7. Run [**cmp request ca-name**](cmdqueryname=cmp+request+ca-name) *ca-name*
   
   
   
   A CA server is specified by its name to receive CMP requests.
8. Run [**cmp request authentication-cert**](cmdqueryname=cmp+request+authentication-cert) *cert-name*
   
   
   
   A certificate to be carried in a CMP request for identity authentication is configured.
9. Run [**cmp request server url**](cmdqueryname=cmp+request+server+url) *url-address*
   
   
   
   A URL is specified for the CMP server used to process CMP requests.
10. (Optional) Run [**cmp source interface**](cmdqueryname=cmp+source+interface) *interface-type* *interface-number*
    
    
    
    The source interface of CMPv2 packets is configured. To be specific, the IP address of the configured source interface is used as the source IP address of the CMPv2 packets sent from the device to the CMPv2 server.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.