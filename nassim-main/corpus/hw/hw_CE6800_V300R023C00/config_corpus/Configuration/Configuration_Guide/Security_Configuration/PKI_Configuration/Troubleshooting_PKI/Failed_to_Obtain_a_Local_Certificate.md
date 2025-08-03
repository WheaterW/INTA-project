Failed to Obtain a Local Certificate
====================================

Failed to Obtain a Local Certificate

#### Fault Symptom

* A local certificate has been manually obtained in offline mode but does not exist in the device storage. The possible causes are as follows:
  
  + The PKI entity is incorrect.
  + The challenge password is incorrect or not configured.
  + The configuration for local certificate download using LDAP is incorrect.
* A local certificate has been manually obtained using CMPv2 but does not exist in the device storage. The possible causes are as follows:
  
  + No CA certificate exists in the PKI realm.
  + The PKI entity is incorrectly configured or not configured.
  + The trusted CA name is incorrect or not configured.
  + The certificate enrollment server URL is incorrect or not configured.
  + The RSA key pair is not configured.
  + The source interface for TCP connection is incorrect.
  + The digest algorithm used for signing the certificate enrollment request is incorrect.
  + The challenge password is incorrect or not configured.
  + The reference and secret values of the message authentication code are incorrect or not configured.
  + The certificate for identity verification is incorrect.

#### Procedure

* If the local certificate is obtained manually:
  1. Check whether the PKI entity is correct.
     
     
     
     To view the configuration of a PKI entity in a PKI realm, run the [**display pki entity**](cmdqueryname=display+pki+entity) command.
     
     Modify the incorrect configurations, such as the country code.
  2. Check whether the challenge password is correct.
     
     
     
     Check whether the CA server requires a challenge password. If so, configure the challenge password to be the same as that of the CA server. To set the challenge password, run the [**pki enroll-certificate**](cmdqueryname=pki+enroll-certificate) command.
  3. Check whether the configuration for local certificate download using LDAP is correct.
     
     
     
     If not, correct the configuration by running the [**pki ldap-server-template**](cmdqueryname=pki+ldap-server-template) *template-name* **attribute** *attr-value* *save-name* **dn** *dn-value* command.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* If the local certificate is obtained using CMPv2:
  1. Check whether the CA certificate has been imported into the device memory.
     
     
     
     To view the CA certificate in the device memory, run the [**display pki certificate**](cmdqueryname=display+pki+certificate) command.
     
     If no CA certificate exists, obtain a CA certificate and run the [**pki import-certificate**](cmdqueryname=pki+import-certificate) command to import the CA certificate into the device memory.
  2. Check whether the PKI entity is correct.
     
     
     
     To view the configuration of a PKI entity in a PKI realm, run the [**display pki entity**](cmdqueryname=display+pki+entity) command.
     
     Modify the incorrect configurations, such as the country code.
  3. Check whether the CA certificate application configuration is correct in the PKI realm.
     
     
     
     Run the [**display this**](cmdqueryname=display+this) command in the CMP session view.
     
     The following is a sample of CA certificate application configuration:
     ```
     pki cmp session cmp                                                             
      cmp-request ca-name "C=cn,ST=beijing,L=SD,O=BB,OU=BB,CN=BB"   //Configure a CA name. The field sequence in the CA name must be the same as that in the actual CA certificate.  
      cmp-request authentication-cert local.cer   //Configure a certificate for identity authentication in a CMPv2 request, which is used to update a certificate or apply for a certificate for another device.  
      cmp-request entity user01   //Specify the PKI entity to be used.  
      cmp-request server url http://10.3.0.1:8080   //Configure the URL of the CMPv2 server.  
      cmp-request rsa local-key-pair rsa regenerate   //Specify the RSA key pair to be used.  
      cmp-request message-authentication-code 1234 %^%#ZodFBGH[^BkU2(~>[NRBv|#b>se|@I7"'A,llG_B%^%#   //Configure the reference value and secret value of the message authentication code to be the same as those on the CA server.
     ```
     
     Correct the configuration if it is incorrect.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```