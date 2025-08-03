Applying for and Updating a Local Certificate in Online Mode Using CMPv2
========================================================================

Applying for and Updating a Local Certificate in Online Mode Using CMPv2

#### Prerequisites

You have completed the preconfiguration for a certificate application. For details, see [Preconfiguration for Certificate Application](security_pki_cfg_0041.html).


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the file format in which the device stores the certificate.
   
   
   ```
   [pki file-format](cmdqueryname=pki+file-format) { der | pem }
   ```
3. Enter the CMP session view. If no CMP session exists, create one first.
   
   
   ```
   [pki cmp session](cmdqueryname=pki+cmp+session) session-name
   ```
   
   
   
   A CMP session is locally available. It is not available to the CA and other devices.
4. Configure the PKI entity name used for CMPv2-based certificate application.
   
   
   ```
   [cmp-request entity](cmdqueryname=cmp-request+entity) entity-name
   ```
5. Configure a CA name for the CMP session.
   
   
   ```
   [cmp-request ca-name](cmdqueryname=cmp-request+ca-name) ca-name
   ```
   
   
   
   The field sequence in the CA name must be the same as that in the CA certificate; otherwise, the CMPv2 server considers the CA name invalid.
6. Configure the CMPv2 server URL.
   
   
   ```
   [cmp-request server url](cmdqueryname=cmp-request+server+url) [ esc ] url-addr 
   ```
7. Configure the RSA key pair used for CMPv2-based certificate application.
   
   
   ```
   [cmp-request rsa local-key-pair](cmdqueryname=cmp-request+rsa+local-key-pair) key-name [ regenerate [ key-bit ] ]
   ```
   
   
   
   If the **regenerate** parameter is specified, the system generates a new RSA key pair to apply for a new certificate and uses the new certificate and RSA key pair to replace the previous ones during automatic certificate update. If **regenerate** is not specified, the system uses the original RSA key pair during automatic certificate update.
8. **Optional:** Configure the source IP address used to establish a TCP connection.
   
   
   ```
   [source](cmdqueryname=source) { interface interface-type interface-number | ip-address }
   ```
   
   
   
   If the **interface** parameter is specified, ensure that the interface is a Layer 3 interface and has an IP address configured.
9. **Optional:** Configure the encryption mode of CMPv2-based certificate application packets.
   
   
   ```
   [cmp-request integrity-algorithm](cmdqueryname=cmp-request+integrity-algorithm) { hmac-sha256 | hmac-sha1 }
   ```
   
   When CMPv2 is used to apply for a certificate, packets need to be encrypted using the hash algorithm. By default, the encryption algorithm SHA256 is used when CMPv2 is used to apply for a certificate.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   For security purpose,you are not advised to use the weak security algorithm or weak security protocols provided by this feature. If you need to use the weak security algorithm or protocols, run the **install feature-software WEAKEA** command to install the weak security algorithm or protocol feature package WEAKEA. By default, the device provides the weak security algorithm or protocol feature package WEAKEA. For details about how to install or uninstall the feature package, see "Upgrade Maintenance Configuration" in Configuration Guide > System Management Configuration.
10. **Optional:** Configure the certificate file used to verify the CA response signature.
    
    
    
    Perform this step when applying for a local certificate in signature mode, in which case the device needs to check whether the local certificate is issued by a valid CA. Skip this step if the message authentication code is used.
    
    
    
    ```
    [cmp-request verification-cert](cmdqueryname=cmp-request+verification-cert) cert-file-name
    ```
    * If this command is configured and the CMPv2 server signs its certificate response, the device uses the certificate (*cert-file-name*) configured using this command to verify the CMPv2 server's response signature. The configured certificate is a CA certificate used to verify a CA's identity.![](public_sys-resources/note_3.0-en-us.png) 
      
      If an RA exists and the certificate enrollment request is issued by the RA, *cert-file-name* must be set to the CA certificate of the RA. Otherwise, the certificate verification fails, which in turn causes the certificate application to fail.
    * If this command is not configured and the CMPv2 server signs its certificate response, the device uses the certificates on the device and in the CMPv2 server's response to build a certificate chain, and then verifies the CMPv2 server's response signature based on the certificate chain.
11. Configure the mode for applying for a local certificate based on the site requirements.
    
    
    * Initial local certificate application (IR) using a message authentication code
      1. Configure the authentication mode of CMPv2-based initial local certificate application.
         ```
         [cmp-request origin-authentication-method](cmdqueryname=cmp-request+origin-authentication-method) message-authentication-code 
         ```
         
         By default, the authentication mode of CMPv2-based initial local certificate application is message authentication code.
      2. Configure the reference value and secret value of the message authentication code.
         ```
         [cmp-request message-authentication-code](cmdqueryname=cmp-request+message-authentication-code) reference-value [ secret-value ]
         [quit](cmdqueryname=quit)
         ```
         ![](public_sys-resources/note_3.0-en-us.png) 
         
         The secret value of the message authentication code is the value of **CMP secret key** on the web UI of the CMPv2 server. The reference value is configurable, and must be a string of case-sensitive characters excluding question marks (?). The value is a string of 1 to 128 characters in clear text or a string of 48 to 188 characters in ciphertext.
      3. In the system view, submit an initial certificate enrollment request to the CMPv2 server based on the CMP session configuration.
         ```
         [pki cmp initial-request session](cmdqueryname=pki+cmp+initial-request+session) session-name
         ```
         
         After this command is configured, the system first checks the CMP session configuration to determine whether the certificate application condition is met. If the condition is not met, an error message is displayed. If the condition is met, the system initiates an initial certificate enrollment request according to the configuration. The certificate obtained is saved in a file to the device storage without being imported to the memory. If the server provides a CA certificate in a response, the CA certificate is also saved in a file.
    * Initial local certificate application (IR) using a signature
      1. Configure the authentication mode of CMPv2-based initial local certificate application.
         ```
         [cmp-request origin-authentication-method](cmdqueryname=cmp-request+origin-authentication-method) signature
         ```
      2. Configure the certificate carried in a CMPv2 request for identity authentication.
         ```
         [cmp-request authentication-cert](cmdqueryname=cmp-request+authentication-cert) cert-name
         [quit](cmdqueryname=quit)
         ```
         
         This certificate is an additional certificate (known as the external identity certificate) and must be issued by another trusted CA.
      3. In the system view, submit an initial certificate enrollment request to the CMPv2 server based on the CMP session configuration.
         ```
         [pki cmp initial-request session](cmdqueryname=pki+cmp+initial-request+session) session-name
         ```
         
         After this command is configured, the system first checks the CMP session configuration to determine whether the certificate application condition is met. If the condition is not met, an error message is displayed. If the condition is met, the system initiates an initial certificate enrollment request according to the configuration. The obtained certificate is saved in a file to the **flash:/pki/public** directory without being imported to the memory. If the server provides a CA certificate in a response, the CA certificate is also saved in a file.
    * Signature-based non-initial local certificate application (CR)
      1. Configure the certificate carried in a CMPv2 request for identity authentication.
         ```
         [cmp-request authentication-cert](cmdqueryname=cmp-request+authentication-cert) cert-name
         [quit](cmdqueryname=quit)
         ```
         
         This certificate is an additional certificate (known as the external identity certificate) and must be issued by another trusted CA.
      2. In the system view, submit a certificate enrollment request to the CMPv2 server based on the CMP session configuration.
         ```
         [pki cmp certificate-request session](cmdqueryname=pki+cmp+certificate-request+session) session-name
         ```
         
         After this command is configured, the system first checks the CMP session configuration to determine whether the certificate application condition is met. If the condition is not met, an error message is displayed. If the condition is met, the system initiates a certificate enrollment request according to the configuration. The certificate obtained is saved in a file to the device storage without being imported to the memory.
12. Configure the mode for updating the local certificate based on the site requirements.
    
    
    * Manual update
      1. Enter the CMP session view and configure the certificate for identity authentication in a CMPv2 request.
         ```
         [pki cmp session](cmdqueryname=pki+cmp+session) session-name
         [cmp-request authentication-cert](cmdqueryname=cmp-request+authentication-cert) cert-name
         [quit](cmdqueryname=quit)
         ```
         
         This certificate is the local certificate that the CA has issued to the device and needs to be replaced by a new local certificate.
      2. In the system view, submit a Key Update Request (KUR) to the CMPv2 server based on the CMP session configuration.
         ```
         [pki cmp keyupdate-request session](cmdqueryname=pki+cmp+keyupdate-request+session) session-name
         ```
         
         When the device requests to update the key with the CMPv2 server, it also applies for a new local certificate.
         
         After this command is configured, the system first checks the CMP session configuration to determine whether the certificate update condition is met. If the condition is not met, an error message is displayed. If the condition is met, the system initiates a certificate update request according to the configuration. The certificate obtained is saved in a file to the device storage without being imported to the memory.
    * Automatic update
      1. Enter the CMP session view and configure the certificate for identity authentication in a CMPv2 request.
         ```
         [pki cmp session](cmdqueryname=pki+cmp+session) session-name
         [cmp-request authentication-cert](cmdqueryname=cmp-request+authentication-cert) cert-name
         ```
         
         This certificate is the local certificate that the CA has issued to the device and needs to be replaced by a new local certificate.
      2. Enable CMPv2-based automatic certificate update.
         ```
         certificate auto-update enable
         ```
      3. Configure the time when the local certificate is updated automatically. The value is expressed as the percentage of the certificate validity period.
         ```
         certificate update expire-time valid-percent
         [quit](cmdqueryname=quit)
         ```
         
         By default, the certificate update time is 50% of the certificate validity period.
         
         After this command is configured, the system initiates a certificate update request and determines whether to create an RSA key pair according to the **cmp-request rsa local-key-pair** command configuration when finding that the automatic certificate update time reaches the value specified by *valid-percent*. After the new certificate is obtained, the system replaces the previous certificate and RSA key pair with the new ones.
13. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

Run the [**display pki cmp statistics**](cmdqueryname=display+pki+cmp+statistics) [ **session** *session-name* ] command to check CMP session statistics.