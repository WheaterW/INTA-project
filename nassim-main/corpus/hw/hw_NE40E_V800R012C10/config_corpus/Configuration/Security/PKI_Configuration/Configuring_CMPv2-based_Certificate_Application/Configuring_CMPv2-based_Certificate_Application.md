Configuring CMPv2-based Certificate Application
===============================================

CMPv2-based certificate application involves two types of CMP requests: initialization requests (IRs) and key update requests (KURs).

#### Prerequisites

Before configuring CMPv2-based certificate application, verify functions to ensure that the network and server are working properly.


#### Context

The NE40E supports IRs and KURs.

* IR: When the NE40E does not obtain a certificate authorized by a carrier, it needs to send an IR to request an identity authentication certificate.
* KUR: Each certificate has a validity period with definite start and end dates. The IKE negotiation fails if either device's certificate expires. The NE40E needs to update its certificate before the certificate expires. Automatic certificate update can be configured on the NE40E.

Certificates obtained using IRs are stored on the CF card but do not take effect. These certificates take effect only after they are imported to the memory using a command. Certificates obtained using KURs can be automatically saved in the memory if the KUR function is enabled.

Perform the following steps on the NE40E where you need to apply for a certificate.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pki domain**](cmdqueryname=pki+domain) *domain-name*
   
   
   
   The PKI domain name configuration view is displayed.
3. Run [**pki cmp initial-request**](cmdqueryname=pki+cmp+initial-request)
   
   
   
   The device is configured to send IRs to apply for certificates.
4. (Optional) Stop the process of polling a CMP request.
   
   
   
   If the NE40E does not receive any response from the connected CA server after sending a CMP request, it polls the CMP request. You can perform the following steps to stop the CMP request polling process.
   
   
   
   1. Run the [**pki cmp session**](cmdqueryname=pki+cmp+session) *session-name* command to enter the CMP session view.
   2. Run the [**cmp poll-request stop**](cmdqueryname=cmp+poll-request+stop) command to manually stop the process of polling a CMP request.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the PKI domain name configuration view.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**pki import-certificate**](cmdqueryname=pki+import-certificate+local+domain+filename) **local** [ **domain** *domainName* ] **filename** *file-name*
   
   
   
   The local certificate is imported.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To ensure high security, you are advised not to import certificates that use the MD5 or SHA1 algorithm. The recommended key length of a certificate is 2048 bits or more.
   
   The default domain of PKI is reserved. For the default domain, you can run the [**pki import-certificate**](cmdqueryname=pki+import-certificate) command to install the downloaded user certificate or run the **pki load** **preset-local** **domain** **default** command to load the preset local certificate. By default, the preset local certificate has been loaded to the default domain.
7. Run [**pki domain**](cmdqueryname=pki+domain) *domain-name*
   
   
   
   The PKI domain name configuration view is displayed.
8. Run [**pki cmp session**](cmdqueryname=pki+cmp+session) *session-name*
   
   
   
   The CMP session view is displayed.
9. Run [**cmp request authentication-cert**](cmdqueryname=cmp+request+authentication-cert) *cert-name*
   
   
   
   A certificate to be carried in a CMP request for identity authentication is configured.
10. Run [**quit**](cmdqueryname=quit)
    
    
    
    The PKI domain name configuration view is displayed.
11. Run [**quit**](cmdqueryname=quit)
    
    
    
    Return to the system view.
12. Run [**pki import-certificate**](cmdqueryname=pki+import-certificate+ca+domain+filename) **ca** [ **domain** *domainName* ] **filename** *file-name*
    
    
    
    The CA certificate is imported.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    To ensure high security, you are advised not to import certificates that use the MD5 or SHA1 algorithm. The recommended key length of a certificate is 2048 bits or more.
    
    The default domain of PKI is reserved. For the default domain, you can run the [**pki import-certificate**](cmdqueryname=pki+import-certificate) command to install the downloaded user certificate or run the **pki load** **preset-ca** **domain** **default** command to load the preset CA certificate.
13. (Optional) Enable the automatic certificate update function.
    1. Run the [**pki domain**](cmdqueryname=pki+domain) *domain-name* command to enter the PKI domain name configuration view.
    2. Run the [**pki cmp session**](cmdqueryname=pki+cmp+session) *session-name* command to enter the CMP session view.
    3. Run the [**certificate auto-update enable**](cmdqueryname=certificate+auto-update+enable) command to enable the automatic certificate update.
    4. (Optional) Run the [**certificate update expire-time**](cmdqueryname=certificate+update+expire-time) *valid-percent* command to configure the percentage of the time for automatic certificate update.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       When automatic update of local certificates is triggered, the system checks whether the file names of the CA certificates corresponding to the local certificates exist in the memory. If the file names do not exist in the memory, the CA certificates are not automatically imported. In addition, services may be interrupted because the local certificates and CA certificates are not updated synchronously. Therefore, if the corresponding CA certificates are not automatically imported, you need to run the [**pki import-certificate**](cmdqueryname=pki+import-certificate+ca+domain+filename) **ca** [ **domain** *domainName* ] **filename** *file-name* command to manually import the CA certificates. During the import, do not change the device-generated file names of the CA certificates. Otherwise, the certificates cannot be automatically imported even if automatic certificate update is enabled.
14. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
15. Verify the configuration.
    
    
    
    If IR-based certificate application succeeds, **session-name\_ir.cer** and **session-name\_cax.cer** files are generated on the CF card. There may be multiple **session-name\_cax.cer** files, such as **session-name\_ca0.cer**, **session-name\_ca1.cer**, and **session-name\_ca2.cer**.