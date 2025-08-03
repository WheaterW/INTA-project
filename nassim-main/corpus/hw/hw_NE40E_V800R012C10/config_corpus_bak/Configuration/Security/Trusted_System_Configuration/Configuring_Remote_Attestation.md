Configuring Remote Attestation
==============================

This section describes how to configure the remote attestation (RA) function to allow an RA server to authenticate a device and determine whether the device is trustworthy.

#### Pre-configuration Tasks

In a trusted environment, after the RA function is enabled on a device that supports trusted startup, the device sends information to a remote RA server. The remote RA server then compares the information it receives with locally stored information to determine whether the device is trustworthy. Therefore, RA provides users with a method of remotely checking device trustworthiness.

Before configuring RA, complete the following tasks:

* Configure the device to communicate with the RA server, and configure the RA function on the RA server.
* Obtain the CA certificate chain used to issue the LAK certificate as well as the Huawei root certificates and Huawei level-2 CA certificates used to issue IAK certificates, and transfer these certificates to the **home** directory of the device through FTP.
  
  Huawei provides two sets of certificates, each with one Huawei root certificate and one Huawei level-2 CA certificate, for issuing IAK certificates. The two sets of certificates are as follows:
  
  + Huawei root certificate: Huawei Equipment CA; Huawei level-2 CA certificate: Huawei Enterprise Network Product CA
  + Huawei root certificate: Huawei RSA Equipment Root CA 2; Huawei level-2 CA certificate: Huawei DataCom RSA Equipment CA 2
  
  You are advised to load the two sets of certificates on the RA server. To download Huawei root certificates and Huawei level-2 CA certificates, visit [https://support.huawei.com/pki/pkidetail](https://support.huawei.com/additionalres/pki).
  
  You can perform the following steps to view the IAK certificate currently used by the RA client, so as to obtain the matching Huawei root certificate and Huawei level-2 CA certificate.
  
  1. Run the **display remote-attestation iak certificate slot** *slotid* command in the diagnostic view to check IAK certificate information. Copy the content from **-----BEGIN CERTIFICATE-----** to **-----END CERTIFICATE-----** in the command output, including **-----BEGIN CERTIFICATE-----** and **-----END CERTIFICATE-----**, and save such information to the user PC in .pem format.
  2. Install OpenSSL on the user PC.
  3. On the CLI of the PC, run the **openssl x509 -in** *filename* **-text -noout** command to check the CN in the **Issue****r** field. *filename* specifies a certificate path (including the certificate name).
  4. Download the Huawei level-2 CA certificate at [https://support.huawei.com/pki/pkidetail](https://support.huawei.com/additionalres/pki) based on the queried CN, and then download the Huawei root certificate based on the Huawei level-2 CA certificate.
* (Optional) Create a public key infrastructure (PKI) domain on the device to implement PKI certificate management between the CA and device through the Certificate Management Protocol (CMP).

#### Procedure

1. Run **system-view**
   
   
   
   The system view is displayed.
2. Run [**trustem**](cmdqueryname=trustem)
   
   
   
   The trusted management view is displayed.
3. Run [**remote-attestation enable**](cmdqueryname=remote-attestation+enable)
   
   
   
   RA is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Run **quit**
   
   
   
   Return to the system view.
6. (Optional) Apply for an LAK certificate for RA.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the RA client uses an LAK certificate, you also need to obtain the CA certificate chain used to issue the LAK certificate. Then, upload the obtained certificate chain file to the RA server.
   
   
   
   1. Run the [**pki entity**](cmdqueryname=pki+entity) *entity-name* command to create a PKI entity and enter its view.
   2. Run the [**common-name**](cmdqueryname=common-name) *common-name* command to configure a common name for the entity.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Run the **quit** command to return to the system view.
   5. Run the [**pki domain**](cmdqueryname=pki+domain) *domain-name* command to create a PKI domain and enter the PKI domain name configuration view.
   6. Run the [**pki cmp session**](cmdqueryname=pki+cmp+session) *session-name* command to create a PKI CMP session and enter its view.
   7. Run the [**cmp request entity**](cmdqueryname=cmp+request+entity) *entity-name* command to specify a PKI entity used to initiate a CMP request.
   8. Run the [**cmp request ca-name**](cmdqueryname=cmp+request+ca-name) *ca-name* command to specify the name of the CA server receiving the CMP request.
   9. Run the [**cmp request server url**](cmdqueryname=cmp+request+server+url) *url-address* command to specify the URL of the CMP server receiving the CMP request.
   10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   11. Run the **quit** command to return to the PKI domain name configuration view.
   12. Run the **quit** command to return to the system view.
   13. Run the [**pki import-certificate ca file-name**](cmdqueryname=pki+import-certificate+ca+file-name) *file-name* command to import the CA certificate chain used to issue the LAK certificate as well as the Huawei root certificates and Huawei level-2 CA certificates used to issue IAK certificates to the device.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       You are advised to import the two sets of certificates, each with one Huawei root certificate and one Huawei level-2 CA certificate. The same CA certificate cannot be imported repeatedly.
       
       If the current CA server does not verify IAK certificates, you do not need to import Huawei root certificates and Huawei level-2 CA certificates.
   14. Run the [**trustem**](cmdqueryname=trustem) command to enter the trusted management view.
   15. (Optional) Run the [**remote-attestation pki bind domain**](cmdqueryname=remote-attestation+pki+bind+domain) *domainName* command to bind the created PKI domain to RA.
   16. (Optional) If the LAK certificate is invalid, run the [**remote-attestation**](cmdqueryname=remote-attestation) **pki update-request** { **all** | **slot** *slotID* } command to update LAK certificate information.
   17. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   18. Run the **quit** command to return to the system view.
7. Run **quit**
   
   
   
   Return to the user view.
8. (Optional) Run [**set tpm password**](cmdqueryname=set+tpm+password) { **slot** *slotId* | **all** }
   
   
   
   The TPM password is changed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the device needs to be rolled back to a version that does not support TPM password configuration, run the [**set tpm password**](cmdqueryname=set+tpm+password) { **slot** *slotId* | **all** } command to restore the TPM password to the default value **Changeme\_123** before performing the rollback.
   
   After running the [**set tpm password**](cmdqueryname=set+tpm+password) { **slot** *slotId* | **all** } command, restart the device. Otherwise, the TPM cannot be accessed, and the RA function is unavailable.

#### Verifying the Configuration

Run the [**display trustem remote-attestation bd-status**](cmdqueryname=display+trustem+remote-attestation+bd-status) { **slot** *slotId* | **all** } command to check the RA status.