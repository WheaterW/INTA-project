Configuring HTTPS Redirect for Web Authentication
=================================================

This section describes how to configure a BRAS to redirect HTTPS access requests.

#### Context

HTTPS redirection refers to the process of redirecting users' HTTPS access requests to a specified URL during web authentication. Upon receipt of an access request packet from a client, a BRAS takes the place of the website to establish a TCP connection with the client. The BRAS then completes SSL handshake negotiation using the specified encryption algorithm and key, and returns an HTTPS redirection packet carrying the redirect URL to the client. In this way, the client is redirected to the specified URL, and HTTPS redirection is complete. After the web authentication server is configured, you can perform the following operations on the BRAS to implement HTTPS redirection.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

When using HTTPS redirection, pay attention to the following points. Otherwise, the web authentication page may not be displayed on the client.

* When a user accesses an HTTPS website to trigger web authentication, the browser displays a security warning. The user needs to click **Continue** to complete web authentication. Otherwise, the web authentication page is not displayed.
* The browser or website that runs the HTTP Strict Transport Security (HSTS) protocol cannot perform HTTPS redirection.
* HTTPS redirection supports request packets whose destination port is the well-known port 443. If the destination port is not 443, HTTPS redirection cannot be performed.
* HTTPS redirection supports TLS1.2 and TLS1.3, but does not support versions earlier than TLS1.2.


#### Procedure

1. Configure HTTPS redirection so that online users can be redirected to a web authentication page.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run **[**traffic behavior**](cmdqueryname=traffic+behavior)** **behavior-name**
      
      
      
      A traffic behavior is configured, and the traffic behavior view is displayed.
   3. Run [**https-redirect**](cmdqueryname=https-redirect)
      
      
      
      HTTPS redirection is configured so that online users can be redirected to a web authentication page.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before the [**quit**](cmdqueryname=quit) command is run, you need to complete the basic configuration for user access. In addition, the configured traffic behavior must be added to the corresponding traffic policy, which must be applied globally.
2. Enable HTTPS redirection and configure a cipher suite.
   1. Run [**access https-redirect**](cmdqueryname=access+https-redirect)
      
      
      
      HTTPS redirection is enabled, and its view is displayed.
   2. Run **[**cipher-suite support**](cmdqueryname=cipher-suite+support)** **suite-code** &<1-6>
      
      
      
      A cipher suite supported by HTTPS redirection is configured.
      
      
      
      For security purposes, you are advised not to use weak security algorithms. If you have to use a weak security algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable it first.
      
      If a self-signed ECDSA certificate is used, set the IANA code of the cipher suite to c02b.
3. Configure a self-signed certificate or import a certificate.
   
   
   
   You can either configure a self-signed certificate or import a certificate. If neither of them exists, the HTTPS redirection function is unavailable.
   
   
   
   * Configure a self-signed certificate.
     1. Run [**self-signed rsa modulus**](cmdqueryname=self-signed+rsa+modulus) **number** or [**self-signed ecdsa modulus**](cmdqueryname=self-signed+ecdsa+modulus) *number*
        
        A self-signed RSA or ECDSA certificate is generated for HTTPS interaction with the client.
        
        The self-signed ECDSA certificate is more secure than the self-signed RSA certificate. As such, using the self-signed ECDSA certificate is recommended.
     2. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
   
   
   * Import a certificate.
     1. Run **access https-redirect import certificate***certificate-file-name* ****key**** { **der** *der-file-name* | **pem** **pem-file-name** ****password**** **password** }
        
        A certificate and the private key are imported for the HTTPS interaction with the client.
     2. (Optional) Run **access https-redirect delete certificate**
        
        The imported certificate and private key are deleted. In this case, if the BRAS has been configured with a self-signed RSA certificate, this certificate is used instead. If the BRAS has not been configured with a self-signed RSA certificate, you must either configure such a self-signed RSA certificate or import another certificate and the private key.
   * Obtain the certificate and private key in the PKI domain.
     1. Run [**pki domain**](cmdqueryname=pki+domain) **domain-name**
        
        A PKI domain is created.
     2. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     4. Run [**access https-redirect**](cmdqueryname=access+https-redirect)
        
        The HTTPS redirection view is displayed.
     5. Run [**pki-domain**](cmdqueryname=pki-domain) *pki-domain-name*
        
        The PKI domain is bound. The device then obtains the certificate and private key in the PKI domain and exchanges HTTPS packets with the client.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Using an imported certificate is recommended. If a self-signed RSA certificate already exists when a certificate is being imported, the BRAS uses the imported certificate by default and will not delete the existing self-signed RSA certificate.
   * If a certificate and the private key have been imported, you can still configure a self-signed RSA certificate but this certificate will not take effect. For the self-signed RSA certificate to take effect, run the **access https-redirect delete certificate** command to delete the imported certificate and private key.
   * After obtaining the certificate and private key in a PKI domain, you need to unbind the PKI domain from the HTTPS redirection view before running the [**access https-redirect import certificate**](cmdqueryname=access+https-redirect+import+certificate) command to import the certificate and private key. You are advised to use the PKI domain to obtain the certificate and private key in the domain to enable HTTPS redirection.
4. (Optional) Enable the function to insert a JavaScript during HTTPS redirection.
   
   
   1. Run [**access https-redirect**](cmdqueryname=access+https-redirect)
      
      The HTTPS redirection view is displayed.
   2. Run [**js enable**](cmdqueryname=js+enable)
      
      The function to insert a JavaScript during HTTPS redirection is enabled.
5. (Optional) Configure blacklist parameters for HTTPS redirection.
   1. (Optional) Run [**blacklist packet-rate**](cmdqueryname=blacklist+packet-rate) **packet-rate**
      
      
      
      The maximum number of times a user can use HTTPS to visit a destination address is configured. If the number of times a user uses HTTPS to visit a destination address exceeds the upper limit, the destination address will be added to the HTTPS redirection blacklist.
   2. (Optional) Run [**blacklist retry-times**](cmdqueryname=blacklist+retry-times) **retry-times** ****interval**** **interval**
      
      
      
      The maximum number of times a destination address can be added to the cache blacklist and the detection interval are configured.
   3. (Optional) Delete IP addresses from the HTTPS redirection blacklist.
      
      
      
      You can manually delete an IP address from the HTTPS redirection blacklist or configure the device to delete an IP address from the HTTPS redirection blacklist after the aging time expires.
      
      
      
      * Run **[**delete blacklist ip**](cmdqueryname=delete+blacklist+ip)** { *ip-address* | **all** } or **[**delete blacklist ipv6**](cmdqueryname=delete+blacklist+ipv6)** { *ipv6-address* | **all** }
        
        The IP address which incorrectly matches the HTTPS redirection blacklist is deleted.
      * Run [**blacklist aging-time**](cmdqueryname=blacklist+aging-time) *aging-time*
        
        The aging time of an IP address in the HTTPS redirection blacklist is configured. After the aging time expires, the IP address is deleted from the blacklist.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The blacklist function can be configured only after the function to insert a JavaScript during HTTPS redirection is enabled using the **js enable** command.
6. (Optional) Configure the HTTPS chasten function.
   
   
   
   The HTTPS chasten function suppresses flow creation during HTTPS redirection, allowing the device to correctly identify the HTTPS flows that can be successfully redirected. In this way, the device can implement HTTPS redirection and prevent users from occupying too many resources. It is recommended that the HTTPS chasten function be used together with the blacklist function. If they are not used together, users may be incorrectly restricted by the HTTPS chasten function.
   
   
   
   1. Configure the HTTPS chasten function.
      
      
      
      You can configure either or both of the HTTPS flow number limiting and packet number limiting functions.
      
      
      
      * To configure the number of seconds during which an HTTPS redirection user is blocked because the number of TCP SYN packets received by the user for HTTPS flow creation exceeds a specified threshold within the specified time, run the [**chasten flow**](cmdqueryname=chasten+flow) *connection-sessions* *connection-period* *blocking-period* *blocking-rate* [ **slot** *slotid* ] command. During the blocking period, the device discards the excess HTTPS TCP SYN packets.
      * To configure the number of seconds during which an HTTPS redirection user is blocked because the number of HTTPS redirection packets replied by the device to the user exceeds a specified threshold within the specified time, run the [**chasten redirect-packet**](cmdqueryname=chasten+redirect-packet) **send-number** **send-period** **blocking-period** *blocking-rate* [ ****slot**** **slotid** ] command. During the blocking period, the device discards the excess HTTPS TCP SYN packets.
   2. (Optional) Run [**delete chasten-user slot**](cmdqueryname=delete+chasten-user+slot) **slotid** [ { ****ip-address**** *ip-address* | ****ipv6-address**** *i*pv6-address*/*length** } [ ****vpn-instance**** **instance-name** ] ]
      
      
      
      Information about the user for whom the HTTPS chasten function is enabled and a slot ID is specified is deleted, and the user is unblocked from HTTPS flow creation.
7. (Optional) Configure the CPU usage threshold for HTTPS redirection avalanche prevention.
   1. Run [**quit**](cmdqueryname=quit)
      
      
      
      The system view is displayed.
   2. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   3. Run [**access-speed adjustment system-state threshold https-redirect cpu-usage alarm**](cmdqueryname=access-speed+adjustment+system-state+threshold+https-redirect+cpu-usage+alarm) **threshold-value** ****resume**** **threshold-value**
      
      
      
      The CPU usage threshold for decreasing the rate at which flows are created for HTTPS redirection and the CPU usage threshold for restoring the rate at which flows are created for HTTPS redirection are configured.
      
      If the CPU usage is greater than the alarm threshold, the device decreases the rate at which flows are created for HTTPS redirection. If the CPU usage falls below the alarm clearance threshold, the device restores the rate at which flows are created for HTTPS redirection.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.