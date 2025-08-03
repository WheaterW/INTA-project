Configuring RA
==============

Configuring RA

#### Context

An RA system consists of the RA server and RA client. The administrator needs to configure both the RA server and RA client to implement the RA function. This section describes how to configure the RA client. For details about how to configure the RA server, see the product documentation of related NMS devices.

Huawei provides two sets of certificates, each with one Huawei root certificate and one Huawei level-2 CA certificate, for issuing IAK certificates. The two sets of certificates are as follows:

* Huawei root certificate: Huawei Equipment CA; Huawei level-2 CA certificate: Huawei Enterprise Network Product CA
* Huawei root certificate: Huawei RSA Equipment Root CA 2; Huawei level-2 CA certificate: Huawei DataCom RSA Equipment CA 2

You are advised to load the two sets of certificates on the RA server. To download Huawei root certificates and Huawei level-2 CA certificates, visit <https://support.huawei.com/additionalres/pki>.

You can perform the following steps to view the IAK certificate currently used by the RA client, so as to obtain the matching Huawei root certificate and Huawei level-2 CA certificate.

1. Run the **display remote-attestation iak certificate slot** *slotid* command in the diagnostic view to check IAK certificate information. Copy the content from **-----BEGIN CERTIFICATE-----** to **-----END CERTIFICATE-----** in the command output, including **-----BEGIN CERTIFICATE-----** and **-----END CERTIFICATE-----**, and save such information to the user PC in .pem format.
2. Install OpenSSL on the user PC.
3. On the CLI of the PC, run the **openssl x509 -in** *filename* **-text -noout** command to check the CN in the **Issue****r** field. *filename*: specifies that the certificate path contains the certificate name.
4. Download the Huawei level-2 CA certificate at <https://support.huawei.com/additionalres/pki> based on the queried CN, and then download the Huawei root certificate based on the Huawei level-2 CA certificate.

#### Prerequisites

Before configuring RA, complete the following tasks:

* Configure the device to communicate with the RA server, and configure the RA function on the RA server.
* Obtain the baseline file, Huawei root certificate, and Huawei level-2 CA certificate. If the RA client uses the LAK certificate, you also need to obtain the CA certificate chain that issues the LAK certificate. Upload the obtained file to the RA server.
* Configure NETCONF on the device so that the RA server can establish a NETCONF session with the device.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the trusted management view and configure RA.
   
   
   ```
   [trustem](cmdqueryname=trustem)
   ```
   
   By default, no trusted management view is created. After you enter the trusted management view, the device automatically enables RA.
3. (Optional) Return to the user view.
   
   
   ```
   [return](cmdqueryname=return)
   ```
4. (Optional) Configure a password for the HTM.
   
   
   ```
   [set htm password](cmdqueryname=set+htm+password) { slot slot-id | all }
   ```
   
   By default, the HTM uses a random password generated before hardware delivery. The device encrypts the configured password and stores it in a secure location to improve the security of the RA function.
5. (Optional) Apply for a LAK certificate for the HTM.
   1. Create a PKI entity and enter the PKI entity view or enter the PKI entity view directly.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      [pki entity](cmdqueryname=pki+entity) entity-name
      ```
      
      By default, no PKI entity is configured.
   2. Configure a common name for the PKI entity.
      
      
      ```
      [common-name](cmdqueryname=common-name) common-name
      ```
      
      By default, no common name is configured for a PKI entity.
   3. Exit the PKI entity view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Create a PKI CMP session and enter the PKI CMP session view, or enter the PKI CMP session view directly.
      
      
      ```
      [pki cmp session](cmdqueryname=pki+cmp+session) session-name
      ```
      
      By default, no PKI CMP session is created.
   5. Specify the PKI entity name used by a device to apply for a certificate through CMPv2.
      
      
      ```
      [cmp-request entity](cmdqueryname=cmp-request+entity) entity-name
      ```
      
      *entity-name* must be the PKI entity name in step [5.a](#EN-US_TASK_0000001513034938__substep3300184513173).
   6. Configure a CA name for the PKI CMP session.
      
      
      ```
      [cmp-request ca-name](cmdqueryname=cmp-request+ca-name) ca-name
      ```
      
      The sequence of each field in the configured CA name must be the same as that in the CA certificate. Otherwise, the CMPv2 server considers the CA name incorrect.
   7. Configure a URL for the CMPv2 server.
      
      
      ```
      [cmp-request server url](cmdqueryname=cmp-request+server+url) [ esc ] url-addr 
      ```
   8. Set the authentication mode for a CMPv2-based initialization request (IR) to signature.
      
      
      ```
      [cmp-request origin-authentication-method](cmdqueryname=cmp-request+origin-authentication-method) signature
      ```
      
      By default, the authentication mode for a CMPv2-based IR is set to message authentication code. In RA scenarios, the authentication mode for a CMPv2-based IR must be set to signature.
   9. Exit the PKI CMP session view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   10. Obtain the CA certificate chain that issues the LAK certificate as well as the Huawei level-2 CA certificate of the IAK certificate, and upload them to the **flash:/pki/public** directory of the device through SFTP.
   11. Import the CA certificate chain of the LAK certificate as well as the Huawei level-2 CA certificate of the IAK certificate.
       
       
       ```
       [pki import-certificate](cmdqueryname=pki+import-certificate) ca { der | pem } filename file-name
       ```
       ![](../public_sys-resources/note_3.0-en-us.png) 
       
       You are advised to import the two sets of certificates, each with one Huawei root certificate and one Huawei level-2 CA certificate. The same CA certificate cannot be imported repeatedly.
       
       If the current CA server does not verify the IAK certificate, you do not need to import the Huawei level-2 CA certificate.
   12. Bind the RA to a PKI CMP session.
       
       
       ```
       [trustem](cmdqueryname=trustem)
       [remote-attestation pki bind cmp-session](cmdqueryname=remote-attestation+pki+bind+cmp-session) session-name
       ```
       
       By default, the RA is not bound to a PKI CMP session.
       
       *session-name* must be the same as the CMP session name in step [5.d](#EN-US_TASK_0000001513034938__substep1198315311203).
       
       If the certificate application is successful, the device automatically applies to the CA server for updating the certificate when the certificate validity period exceeds the 50% by default.
6. (Optional) Manually update the LAK certificate for the HTM.
   
   
   ```
   [remote-attestation pki update-request](cmdqueryname=remote-attestation+pki+update-request) { all | slot slotID }
   ```
   
   When the RA is configured, if a PKI certificate becomes invalid (for example, the certificate is revoked due to certificate information disclosure), you must update the PKI certificate. After this command is executed, the device immediately applies to the CA server for certificate update.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display htm status**](cmdqueryname=display+htm+status) { **slot** *slot-id* | **all** } command to check the HTM chip status.