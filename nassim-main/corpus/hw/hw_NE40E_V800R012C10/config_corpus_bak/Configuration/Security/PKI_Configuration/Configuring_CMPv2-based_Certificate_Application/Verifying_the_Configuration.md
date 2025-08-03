Verifying the Configuration
===========================

After configuring CMPv2-based certificate application, check the configuration.

#### Procedure

1. Run the [**display rsa pki local-key-pair**](cmdqueryname=display+rsa+pki+local-key-pair+public) [ *file-name* ] **public** command to check the public key in an RSA key pair.
2. Run the [**display pki { match-rsa-key | match-sm2-key } certificate-filename**](cmdqueryname=display+pki+%7B+match-rsa-key+%7C+match-sm2-key) *file-name* command to check the key used by a certificate.
3. Run the [**display pki cert-req**](cmdqueryname=display+pki+cert-req) [**filename**](cmdqueryname=filename) *file-name* command to check the content of the certificate request file with a specified name.
4. Run the [**display pki certificate**](cmdqueryname=display+pki+certificate) [**filename**](cmdqueryname=filename) *file-name* command to check the content of the certificate with a specified file name.
5. Run the [**display pki crl**](cmdqueryname=display+pki+crl) [**filename**](cmdqueryname=filename) *file-name* command to check the content of the CRL with a specified file name.
6. Run the [**display pki ca\_list**](cmdqueryname=display+pki+ca_list+domain) [ **domain** *domainName* ] command to check the content of a CA certificate and CRL imported to the memory.
7. Run the [**display pki cert\_list**](cmdqueryname=display+pki+cert_list+domain) [ **domain** *domainName* ] command to check the content of a local certificate imported to the memory.