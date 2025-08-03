Configuring Certificate Revocation Status Check
===============================================

Configuring Certificate Revocation Status Check

#### Context

During an attempt to establish a secure connection between two PKI entities, the two entities must check each other's local certificate. If the certificate is invalid, a secure connection cannot be established. However, the CA sometimes needs to unbind a public key from related PKI entities due to factors such as user name change, private key leak, or service interruption. A PKI entity must obtain the certificate status of the peer entity in a timely manner to ensure communication security.

The device provides the following certificate status check modes: CRL and None.

If multiple methods are configured, the system checks the certificate revocation status in the configured sequence. The latter mode is used only when the current mode is unavailable (for example, the server cannot be connected). When the configured CRL mode is unavailable and None is configured, the certificate is considered valid. For example, if the [**certificate-check**](cmdqueryname=certificate-check) **crl** **ocsp** **none** command is configured, the device checks whether a certificate is valid using the CRL mode. If the CRL mode is unavailable, the device considers the certificate valid.

You can select a mode for checking the certificate revocation status as required.

* CRL
  
  The status of a certificate is determined by checking whether the certificate is included in the CRL that is saved in the CRL database. After a certificate is revoked, the SN of the certificate is recorded in the CRL. When a PKI entity authenticates the local certificate of the peer entity, it searches for the certificate in the CRL stored in local memory. If the certificate is included in the CRL, it indicates that the certificate has been revoked. If no CRL is available in local memory, the CRL needs to be downloaded and installed into the local memory.
  
  **Figure 1** Certificate status check in the CRL mode  
  ![](figure/en-us_image_0000001563886049.png)
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  A PKI entity can download a CRL using an LDAPv3 template. A PKI entity must frequently download the CRL to keep it up to date. By default, the device allocates about 5 KB memory space for processing and caching the CRL. If the reserved memory space is insufficient, new certificate revocation data cannot be imported. If you want to import new certificate revocation data, delete the old data first.
* None
  
  If no CRL is available for the PKI entity, or the local certificate status of the PKI entity does not need to be checked, you can use the None mode, which does not check whether the certificate is revoked.

![](public_sys-resources/note_3.0-en-us.png) 

The global certificate revocation status can be checked in CRL mode or None mode.

The certificate revocation status in a PKI realm can be checked in CRL or None mode.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a PKI realm and enter its view, or enter the view of an existing PKI realm.
   
   
   ```
   [pki realm](cmdqueryname=pki+realm) realm-name
   ```
   
   By default, the system has a PKI realm named **default**. This realm can be modified but cannot be deleted.
3. Configure the mode of checking certificate revocation status in the PKI realm.
   
   
   ```
   [certificate-check](cmdqueryname=certificate-check) { { crl | ocsp } * [ none ] | none }
   ```
   
   By default, the mode of checking certificate revocation status is not configured in a PKI realm.
   
   If this command is not configured, the global certificate revocation status check mode is used. That is, the configuration of the [**pki certificate-check crl**](cmdqueryname=pki+certificate-check+crl) [ **none** ], [**pki certificate-check none**](cmdqueryname=pki+certificate-check+none), or [**undo pki certificate-check**](cmdqueryname=undo+pki+certificate-check) command in the system view takes effect.
4. Select a mode to check peer certificate status according to the service types provided by the CA:
   
   
   * Manual CRL update
     1. Return to the system view.
        
        ```
        [quit](cmdqueryname=quit)
        ```
     2. Configure the file format in which the device saves the CRL.
        ```
        [pki file-format](cmdqueryname=pki+file-format) { der | pem }
        ```
     3. Configure CRL download through LDAP.
        ```
        [pki ldap-server-template](cmdqueryname=pki+ldap-server-template) template-name attribute attr-value save-name dn dn-value
        ```
     4. Import the CRL to the device memory.
        ```
        [pki import-crl](cmdqueryname=pki+import-crl) [ realm realm-name ] filename file-name
        ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display pki crl**](cmdqueryname=display+pki+crl) [ **realm** *realm-name* | **filename** *file-name* ] command to check the CRL content on the device.
* Run the [**display pki certificate**](cmdqueryname=display+pki+certificate) **ocsp** [ **realm** *realm-name* | **filename** *file-name* ] command to check the OCSP server certificate loaded on the device.

#### Follow-up Procedure

If a CRL expires or is not used, run the [**pki delete-crl**](cmdqueryname=pki+delete-crl) { **realm** *realm-name* | **filename** *filename* } command to delete the CRL from the device memory.