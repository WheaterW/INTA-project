Verifying the Configuration
===========================

After configuring PKI certificates, you can check the configuration.

#### Procedure

1. Run the [**display { rsa | sm2 } pki local-key-pair**](cmdqueryname=display+%7B+rsa+%7C+sm2+public) [ *file-name* ] **public** command to check the public key in an RSA/SM2 key pair.
2. Run the [**display pki cert-req**](cmdqueryname=display+pki+cert-req) [**filename**](cmdqueryname=filename) *file-name* command to check the content of a certificate request file.
3. Run the [**display pki certificate**](cmdqueryname=display+pki+certificate) [**filename**](cmdqueryname=filename) *file-name* command to check the content of a certificate.
4. Run the [**display pki ca\_list**](cmdqueryname=display+pki+ca_list+domain) [ **domain** *domainName* ] command to check the content of a CA certificate imported to the memory.
5. Run the [**display pki cert\_list**](cmdqueryname=display+pki+cert_list+domain) [ **domain** *domainName* ] command to check the content of a local certificate imported to the memory.