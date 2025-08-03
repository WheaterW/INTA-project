Updating the Expired Local Certificate and CRL Certificate
==========================================================

If the local certificate or CRL certificate expires, you need to update it.

#### Context

A local certificate has a validity period and has a specific start date and end date. During certificate verification, the system checks whether the certificate is within the validity period. If the certificate is not within the validity period, the certificate verification fails. The CRL certificate has a validity period. If the validity period expires, the CRL certificate cannot be used for verification, causing security risks.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The local certificate and CRL certificate must be updated before they expire. Otherwise, service loss or security risks may occur.



#### Procedure

* Update an expired local certificate in offline mode.
  1. Run the **[**system-view**](cmdqueryname=system-view)** command to enter the system view.
  2. Run the **[**pki delete-certificate**](cmdqueryname=pki+delete-certificate)** ****local**** [ **domain** *domainName* ] **filename** *file-name* command to configure the device to delete the expired local certificate file with the specified name from the memory.
  3. Obtain the certificate. For details, see [Obtaining Certificates](dc_vrp_pki_cfg_0006.html).
* Configure CMP to update the expired local certificate.
  1. Run the **[**system-view**](cmdqueryname=system-view)** command to enter the system view.
  2. Run the **[**pki delete-certificate**](cmdqueryname=pki+delete-certificate)** ****local****[ **domain** *domainName* ] **filename** *file-name* command to configure the device to delete the expired local certificate file with the specified name from the memory.
  3. Configure CMP certificate application. For details, see [Configuring CMPv2-based Certificate Application](dc_vrp_cfg_cmp_0004.html).
* Configure CMP-based update of expired certificates for device identity verification.
  1. Manually apply for a new device identity certificate file from the CA server of the CMP. For details, see [Obtaining Certificates](dc_vrp_pki_cfg_0006.html).
  2. Upload the new license file to cfcard:/.
  3. Run the **[**system-view**](cmdqueryname=system-view)** command to enter the system view.
  4. Run the **[**pki domain**](cmdqueryname=pki+domain)** **domain-name** command to enter the PKI domain name configuration view.
  5. Run the [**pki cmp**](cmdqueryname=pki+cmp+session) **session** *session-name* command to create a CMP session and enter the PKI CMP session view.
  6. Run the **[**cmp request authentication-cert**](cmdqueryname=cmp+request+authentication-cert)** **cert-name** command to update the certificate in a specified certificate request file.
  7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. The new identity certificate is replaced.
* Update expired CRL certificates.
  1. Run the **[**system-view**](cmdqueryname=system-view)** command to enter the system view.
  2. Run the **[**pki delete-certificate**](cmdqueryname=pki+delete-certificate)** ****crl****[ **domain** *domainName* ] **filename** *file-name* command to configure the device to delete expired CRL files with specified names from the memory.
  3. Configure the CRL certificate. For details, see [Configuring the CRL Function](dc_vrp_cfg_cmp_0009.html).