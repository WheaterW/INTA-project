Configuring an HTTP Server
==========================

Configuring an HTTP Server

#### Prerequisites

Before configuring RESTCONF to manage devices, configure a routing protocol to ensure that there are reachable routes between the devices and NMS.


#### Context

RESTCONF ensures both security and expansibility. When a web application is used for device management, use RESTCONF to ensure the communications between the client and device.

On the network shown in [Figure 1](#EN-US_TASK_0000001563771133__fig_dc_vrp_netconf_cfg_000201), an HTTP-capable client is used. The server receives the connection request from the client and sets up a connection, achieving configuration file management through RESTCONF.

To ensure normal communication between the RESTCONF client and server, enable the HTTP server function on the RESTCONF server. This section describes how to perform configuration on the server.

**Figure 1** Network diagram for configuring RESTCONF  
![](figure/en-us_image_0000001563890801.png)

HTTP is an application-layer protocol that transports hypertext from WWW servers to local browsers. HTTP uses the client/server model in which requests and replies are exchanged.

![](public_sys-resources/note_3.0-en-us.png) 

HTTP involves security risks; therefore, HTTPS is recommended. If HTTPS is used, you need to prepare a digital certificate in advance. The device has an initial certificate. To ensure security, you are advised to apply for a digital certificate.

HTTPS is secure HTTP that uses SSL's sound security mechanism to authenticate users and encrypt data exchanged between a client and a server, thereby improving the transmission security of HTTP.

A RESTCONF client and a RESTCONF server communicate using HTTP or HTTPS.

A RESTCONF client encapsulates a request packet in HTTP format and sends it to a RESTCONF server. Upon receiving the packet, an HTTP server converts the request packet into a CAMLCSI message and sends it to the RESTCONF server. The RESTCONF server parses and processes the request packet, and sends a response packet to the HTTP server. The HTTP server encapsulates the response packet in HTTP format and sends it to the RESTCONF client.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the AAA view.
   
   
   ```
   [aaa](cmdqueryname=aaa)
   ```
3. Configure the local username and password.
   
   
   ```
   [local-user](cmdqueryname=local-user) user-name  { password irreversible-cipher password | access-limit max-number | ftp-directory directory | idle-timeout minutes [ seconds ] | privilege level level | state { block | active } } *
   ```
4. Configure an access type for the local user.
   
   
   ```
   [local-user](cmdqueryname=local-user) user-name service-type http
   ```
   
   The access type of the local user is set to HTTP.
5. Configure a privilege level for the local user.
   
   
   ```
   [local-user](cmdqueryname=local-user) user-name privilege level level
   ```
6. Exit the AAA view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
8. Configure password authentication as the default authentication mode for SSH login.
   
   
   ```
   [ssh authentication-type default password](cmdqueryname=ssh+authentication-type+default+password)
   ```
   
   By default, password authentication is used for SSH login.
9. Enable HTTP or HTTPS.
   
   
   * To enable HTTPS, perform the following operations:
     
     You can use any of the following methods to configure an SSL policy. Method 1 and method 3 are recommended.
     
     # Configure an SSL policy. (Method 1: Load a certificate using PKI and use the digital certificate applied for.)
     
     Upload the obtained digital certificate to the **/pki/public** directory of the device through SFTP. For details about how to apply for a digital certificate in PKI mode, see *Configuration Guide - PKI Configuration*.
     
     ```
     [pki realm](cmdqueryname=pki+realm) pki-domain
     [quit](cmdqueryname=quit)
     [pki import-certificate](cmdqueryname=pki+import-certificate)  local [ [ realm realm-name ] { pkcs12 | pem } ] filename file-name [ cert-name cert-name ] [ no-check-same-name ] { include-rsa-key } [ exportable ] [ password password ]  
     (Optional) [pki import-certificate](cmdqueryname=pki+import-certificate) ca [ [ realm realm-name ] { pkcs12 | pem } ] filename file-name [ cert-name cert-name ] [ no-check-same-name ] { include-rsa-key } [ exportable ] [ password password ] //If the peer's local certificate needs to be verified, import the CA certificate corresponding to the peer's local certificate in this step.
     (Optional) [pki import rsa-key-pair](cmdqueryname=pki+import+rsa-key-pair) keyname [ exclude-cert ] { pem | pkcs12 } filename [ exportable ] [ password password ]  //Skip this step if the private key file is generated on the local device.
     [ssl policy](cmdqueryname=ssl+policy) policy-name
     [pki-domain](cmdqueryname=pki-domain) pki-domain     //The value of pki-domain must be the same as that of pki-domain in the pki realm pki-domain command.
     (Optional) [ssl minimum version](cmdqueryname=ssl+minimum+version) { tls1.1 | tls1.2 | tls1.3 } //By default, TLS1.2 is used.
     (Optional) [signature algorithm-list](cmdqueryname=signature+algorithm-list) { ecdsa-secp256r1-sha256 | ecdsa-secp384r1-sha384 | ecdsa-secp521r1-sha512 | ed25519 | ed448 | rsa-pss-pss-sha256 | rsa-pss-pss-sha384 | rsa-pss-pss-sha512 | rsa-pss-rsae-sha256 | rsa-pss-rsae-sha384 | rsa-pss-rsae-sha512 | rsa-pkcs1-sha256 | rsa-pkcs1-sha384 | rsa-pkcs1-sha512 | ecdsa-sha1 | ecdsa-sha224 | rsa-sha1 | rsa-sha224 | dsa-sha1 | dsa-sha224 | dsa-sha256 | dsa-sha384 | dsa-sha512 } *   //By default, the configured signature algorithms are ed25519, ed448rsa-pss-pss-sha256, rsa-pss-pss-sha384, rsa-pss-pss-sha512, rsa-pss-rsae-sha256, rsa-pss-rsae-sha384, and rsa-pss-rsae-sha512. If the peer certificate algorithms do not include the preceding ones, add the signature algorithm supported by the SSL handshake process.
     [quit](cmdqueryname=quit)
     [commit](cmdqueryname=commit)
     ```
     
     # Configure an SSL policy. (Method 2: Load a certificate using PKI and use the initial certificate.)
     
     Using the initial certificate in the default domain poses security risks. You are advised to use the digital certificate applied for.
     
     ```
     (Optional) [pki import-certificate](cmdqueryname=icssearchname) ca realm default { pkcs12 | pem } filename file-name [ cert-name cert-name ] [ no-check-same-name ] { include-rsa-key } [ exportable ] [ password password ] //If the peer's local certificate needs to be verified, import the CA certificate corresponding to the peer's local certificate in this step.
     [ssl policy](cmdqueryname=ssl+policy) policy-name
     [pki-domain](cmdqueryname=pki-domain) default
     (Optional) [ssl minimum version](cmdqueryname=ssl+minimum+version) { tls1.1 | tls1.2 | tls1.3 } //By default, TLS1.2 is used.
     (Optional) [signature algorithm-list](cmdqueryname=signature+algorithm-list) { ecdsa-secp256r1-sha256 | ecdsa-secp384r1-sha384 | ecdsa-secp521r1-sha512 | ed25519 | ed448 | rsa-pss-pss-sha256 | rsa-pss-pss-sha384 | rsa-pss-pss-sha512 | rsa-pss-rsae-sha256 | rsa-pss-rsae-sha384 | rsa-pss-rsae-sha512 | rsa-pkcs1-sha256 | rsa-pkcs1-sha384 | rsa-pkcs1-sha512 | ecdsa-sha1 | ecdsa-sha224 | rsa-sha1 | rsa-sha224 | dsa-sha1 | dsa-sha224 | dsa-sha256 | dsa-sha384 | dsa-sha512 } *   //By default, the configured signature algorithms are ed25519, ed448, rsa-pss-pss-sha256, rsa-pss-pss-sha384, rsa-pss-pss-sha512, rsa-pss-rsae-sha256, rsa-pss-rsae-sha384, and rsa-pss-rsae-sha512. If the peer certificate algorithms do not include the preceding ones, add the signature algorithm supported by the SSL handshake process.
     [quit](cmdqueryname=quit)
     [commit](cmdqueryname=commit)
     ```
     
     # Configure an SSL policy. (Method 3: Manually load a certificate.)
     
     Upload the obtained digital certificate to the **/security** directory of the device through SFTP. If the **/security** directory does not exist on the device, run the [**mkdir**](cmdqueryname=mkdir) **security** command to create it. For details about how to apply for a digital certificate in PKI mode, see *Configuration Guide - PKI Configuration*.
     
     ```
     [ssl policy](cmdqueryname=ssl+policy) policy-name
     [certificate load](cmdqueryname=certificate+load) { pem-cert | pem-chain } certFile key-pair { dsa | rsa } key-file keyFile auth-code [ cipher authCode ]
     (Optional) [trusted-ca](cmdqueryname=trusted-ca) load pem-ca caFile //If the peer's local certificate needs to be verified, import the CA certificate corresponding to the peer's local certificate in this step.
     (Optional) [ssl minimum version](cmdqueryname=ssl+minimum+version) { tls1.1 | tls1.2 | tls1.3 } //By default, TLS1.2 is used.
     (Optional) [signature algorithm-list](cmdqueryname=signature+algorithm-list) { ecdsa-secp256r1-sha256 | ecdsa-secp384r1-sha384 | ecdsa-secp521r1-sha512 | ed25519 | ed448 | rsa-pss-pss-sha256 | rsa-pss-pss-sha384 | rsa-pss-pss-sha512 | rsa-pss-rsae-sha256 | rsa-pss-rsae-sha384 | rsa-pss-rsae-sha512 | rsa-pkcs1-sha256 | rsa-pkcs1-sha384 | rsa-pkcs1-sha512 | ecdsa-sha1 | ecdsa-sha224 | rsa-sha1 | rsa-sha224 | dsa-sha1 | dsa-sha224 | dsa-sha256 | dsa-sha384 | dsa-sha512 } *   //By default, the configured signature algorithms are ed25519, ed448, rsa-pss-pss-sha256, rsa-pss-pss-sha384, rsa-pss-pss-sha512, rsa-pss-rsae-sha256, rsa-pss-rsae-sha384, and rsa-pss-rsae-sha512. If the peer certificate algorithms do not include the preceding ones, add the signature algorithm supported by the SSL handshake process.
     [quit](cmdqueryname=quit)
     [commit](cmdqueryname=commit)
     ```
     
     You cannot run the [**certificate load**](cmdqueryname=certificate+load) command to load an initial certificate. If you need to use the initial certificate, use the PKI domain mode.
     
     # Enable the HTTP server function.
     
     ```
     [http](cmdqueryname=http)
     [service restconf](cmdqueryname=service+restconf)
     [secure-server enable](cmdqueryname=secure-server+enable)
     [server-source](cmdqueryname=server-source) { interface-name | interface-type interface-number }
     (Optional) [secure-server port](cmdqueryname=secure-server+port) port-number
     (Optional) [max-tcp-num](cmdqueryname=max-tcp-num) num
     [ssl-policy](cmdqueryname=ssl-policy) policy-name
     (Optional) [ssl-verify peer](cmdqueryname=ssl-verify+peer)   //The server performs SSL verification on the client. If no certificate is applied for and imported to the HTTP server and client, this function cannot be enabled.
     ```
   * To enable HTTP, perform the following operations:
     ```
     [http](cmdqueryname=http)
     [service restconf](cmdqueryname=service+restconf)
     [server enable](cmdqueryname=server+enable)
     [server-source](cmdqueryname=server-source) { interface-name | interface-type interface-number }
     (Optional) [server port](cmdqueryname=server+port) port-number
     ```![](public_sys-resources/note_3.0-en-us.png) 
   
   The following commands can be used only after the weak security algorithm/protocol feature package (WEAKEA) is installed using the [**install feature-software WEAKEA**](cmdqueryname=install+feature-software+WEAKEA) command:
   
   * [**ssl minimum version**](cmdqueryname=ssl+minimum+version) **tls1.1**
   * [**signature algorithm-list**](cmdqueryname=signature+algorithm-list)
   * [**server enable**](cmdqueryname=server+enable)
10. (Optional) Configure an ACL to be referenced by HTTP.
    
    
    ```
    [acl](cmdqueryname=acl) { acl-name | acl-number }
    ```
    
    By default, no HTTP ACL is configured.
11. (Optional) Configure a timeout period for an idle HTTP connection.
    
    
    ```
    [idle-timeout](cmdqueryname=idle-timeout) minutes
    ```
    
    By default, the timeout period of an idle HTTP connection is 20 minutes.
12. (Optional) Configure the client IP address locking function.
    
    
    * Enable the client IP address locking function on the HTTP server.
      ```
      undo [http server ip-block disable](cmdqueryname=http+server+ip-block+disable)
      ```
      
      By default, the client IP address locking function is enabled on an HTTP server.
    * Set the number of consecutive authentication failures and the period in which consecutive authentication failures are counted.
      ```
      [http server ip-block failed-times](cmdqueryname=http+server+ip-block+failed-times) failed-times-value period period-value
      ```
      
      By default, a maximum of 6 consecutive authentication failures is allowed within 5 minutes.
    * Set a period after which the system automatically unlocks a client IP address.
      ```
      [http server ip-block reactive](cmdqueryname=http+server+ip-block+reactive) reactive-period
      ```
      
      By default, the period is 5 minutes.
13. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

Run the [**display tcp status**](cmdqueryname=display+tcp+status) command to check the status of the TCP connection for RESTCONF communication.

Run the [**display http server ip-block**](cmdqueryname=display+http+server+ip-block) **list** command to check client IP addresses that are locked because of authentication failures.