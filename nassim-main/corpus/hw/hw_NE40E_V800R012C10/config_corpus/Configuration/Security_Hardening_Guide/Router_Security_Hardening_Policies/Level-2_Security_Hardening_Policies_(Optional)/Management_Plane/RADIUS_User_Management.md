RADIUS User Management
======================

RADIUS is the most commonly used protocol for implementing AAA on remote dial-up users. RADIUS runs over UDP, and its authentication and accounting port numbers are 1812 and 1813, respectively. RADIUS over DTLS runs over DTLS, with authentication and accounting port numbers both being 2083. RADIUS uses the client/server model for communication between the RADIUS client and server and provides AAA functions for different types of users.

#### Security Policy

* The server can be disabled.
* RADIUS over UDP packets can be authenticated using a shared key.
  
  RADIUS transmits packets over UDP connections. A shared key, which is not transmitted over the network, is used for authentication between the RADIUS client and server. Moreover, passwords transmitted between the RADIUS client and server are encrypted using the shared key to prevent user passwords from being intercepted on an insecure network.
* The DTLS service is supported.
  
  RADIUS over DTLS supports DTLS certificate authentication.

#### Attack Methods

* Tampering
  
  An attacker can change the content of packets in transit. RADIUS over DTLS provides integrity protection to prevent packets from being tampered with.
* Information leakage
* An attacker can sniff the RADIUS packets transmitted in plaintext. The password attribute is only contained in a RADIUS request packet. RADIUS over DTLS provides an identity authentication mechanism to prevent information leakage.

#### Configuration and Maintenance Methods

1. Disable the RADIUS server.
   ```
   [~HUAWEI] undo radius enable
   [*HUAWEI] commit
   ```
2. Configure a shared key for the RADIUS over UDP server based on the server group.
   ```
   [~HUAWEI] radius-server group test
   [*HUAWEI-radius-test] radius-server authentication 10.1.1.1 1812 shared-key YsHsjx_202206
   [*HUAWEI-radius-test] commit
   ```
3. Configure a shared key for the RADIUS over UDP server based on the server.
   ```
   [~HUAWEI] radius-server group test
   [*HUAWEI-radius-test] radius-server shared-key YsHsjx_202206
   [*HUAWEI-radius-test] commit
   ```
4. Configure a RADIUS over DTLS server.
   
   # Configure a PKI entity.
   
   ```
   [~HUAWEI] pki entity entity1
   [*HUAWEI-pki-entity-entity1] common-name test
   [*HUAWEI-pki-entity-entity1] country CN
   [*HUAWEI-pki-entity-entity1] locality HZ
   [*HUAWEI-pki-entity-entity1] organization HW
   [*HUAWEI-pki-entity-entity1] organization-unit HW
   [*HUAWEI-pki-entity-entity1] state ZJ
   [*HUAWEI-pki-entity-entity1] commit
   [~HUAWEI-pki-entity-entity1] quit
   ```
   
   # Create a private-public key pair.
   
   ```
   [~HUAWEI] rsa pki local-key-pair key1 create
   [*HUAWEI] commit
   ```
   
   # Configure a PKI domain.
   
   ```
   [~HUAWEI] pki domain domain1
   [*HUAWEI-pki-domain-domain1] certificate request entity entity1
   [*HUAWEI-pki-domain-domain1] pki cmp session session1
   [*HUAWEI-pki-domain-domain1-pki-cmp-session-session1] cmp request rsa local-key-pair key1
   [*HUAWEI-pki-domain-domain1-pki-cmp-session-session1] commit
   [~HUAWEI-pki-domain-domain1-pki-cmp-session-session1] quit 
   [~HUAWEI-pki-domain-domain1] quit
   ```
   
   # Import the local certificate (root-cert.cer) and CA certificate (local-cert.cer).
   
   For details about how to apply for a certificate, see section: Configuration > Security > PKI Configuration > Configuring Offline Certificate Application.
   
   ```
   [~HUAWEI] pki import-certificate ca domain domain1 filename root-cert.cer
   [~HUAWEI] pki import-certificate local domain domain1 filename local-cert.cer
   ```
   
   # Configure an SSL cipher suite.
   
   ```
   [~HUAWEI] ssl cipher-suite-list suite1
   [*HUAWEI-ssl-cipher-suite-suite1] set cipher-suite tls12_ck_ecdhe_rsa_with_aes_128_gcm_sha256
   [*HUAWEI-ssl-cipher-suite-suite1] commit
   [~HUAWEI-ssl-cipher-suite-suite1] quit
   ```
   
   # Configure a DTLS policy.
   
   ```
   [~HUAWEI] dtls policy policy1
   [*HUAWEI-dtls-policy-policy1] pki-domain domain1
   [*HUAWEI-dtls-policy-policy1] diffie-hellman modulus 2048
   [*HUAWEI-dtls-policy-policy1] binding cipher-suite-customization suite1
   [*HUAWEI-dtls-policy-policy1] signature algorithm-list rsa-pkcs1-sha256
   [*HUAWEI-dtls-policy-policy1] commit
   [~HUAWEI-dtls-policy-policy1] quit
   ```
   
   # Configure a RADIUS over DTLS server.
   
   ```
   [~HUAWEI] radius-server group group1
   [*HUAWEI-radius-group1] radius-server authentication 1.1.1.1 dtls-policy policy1 2083
   [*HUAWEI-radius-group1] radius-server accounting 1.1.1.1 dtls-policy policy1 2083
   [*HUAWEI-radius-group1] commit
   ```

#### Configuration and Maintenance Suggestions

You are advised to configure a complex shared key for the RADIUS over UDP server.

You are advised to use secure certificates, cipher suites, and signature algorithms for RADIUS over DTLS servers.

Using the RADIUS over DTLS server is recommended.


#### Verifying the Security Hardening Result

Run the [**display radius-server configuration**](cmdqueryname=display+radius-server+configuration) [ **group** *group-name* ] command to check the RADIUS server configuration.