Verifying Certificates
======================

This section describes how to verify certificates on a local device and its peer device.

#### Prerequisites

CA and local certificates have been installed on a device.


#### Context

If certificate-based IPsec negotiation fails between two devices, run the [**pki validate-certificate**](cmdqueryname=pki+validate-certificate) command to check the signatures and validity periods of certificates for fault locating.

If the CRL check function has been enabled on a device (for detailed configuration, see Step 1 in [Configuring the CRL Function](dc_vrp_cfg_cmp_0009.html)), the device checks whether the serial number of the peer device's certificate is listed in the CRL and then verifies the signature and validity period of the certificate.

The device also periodically and automatically verifies the validity of all installed local and CA certificates. The default check period is 5 minutes. If a fault is detected, an alarm is generated. By default, the certificate expiration prewarning time is 90 days. A prewarning is generated 90 days before the certificate expires, prompting you to obtain a new certificate in advance.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Manually verify certificates using the following commands.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**pki validate-certificate**](cmdqueryname=pki+validate-certificate+ca+domain+filename) **ca** { **domain** *domainName* | **filename** *file-name* } command checks the validity of only the root CA certificate, not subordinate CA certificates. If multiple CA certificates are imported by the NE40E in a multi-level CA environment, subordinate CA certificates can be verified only using the [**pki validate-certificate**](cmdqueryname=pki+validate-certificate+local+domain+filename) **local** { **domain** *domainName* | **filename** *file-name* }command.
   
   If an imported CA file contains multiple certificates, only the first certificate is verified.
   
   
   
   * Run the [**pki validate-certificate**](cmdqueryname=pki+validate-certificate+ca+domain+filename) **ca** { **domain** *domainName* | **filename** *file-name* } command to verify the root CA certificate.
   * Run the [**pki validate-certificate**](cmdqueryname=pki+validate-certificate+local+domain+filename) **local** { **domain** *domainName* | **filename** *file-name* } command to verify the local CA certificate and subordinate CA certificate.
   * Run the [**pki validate-certificate**](cmdqueryname=pki+validate-certificate+peer+domain+filename) **peer** { **domain** *domainName* | **filename** *file-name* } command to verify the peer certificate.
3. (Optional) Run [**pki set-certificate**](cmdqueryname=pki+set-certificate+c+heck-period) **c****heck-period** *period-value*
   
   
   
   An interval at which certificates are automatically verified is configured.
4. (Optional) Run [**pki set-certificate**](cmdqueryname=pki+set-certificate+expire-prewarning) **expire-prewarning** *prewarning-days*
   
   
   
   The certificate expiration prewarning time is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.