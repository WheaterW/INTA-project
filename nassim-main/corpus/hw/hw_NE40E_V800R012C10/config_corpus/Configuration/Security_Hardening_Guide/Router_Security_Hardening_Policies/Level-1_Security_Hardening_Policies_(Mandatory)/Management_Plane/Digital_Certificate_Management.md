Digital Certificate Management
==============================

Digital Certificate Management

#### Function Description

A digital certificate, which a user applies for from a trusted certificate authority (CA), provides multiple services, such as identity authentication, access control, and integrity and confidentiality assurance, for IPsec, SSH, SSL, and other security features.

For security purposes, the validity period of a digital certificate is specified when the digital certificate is issued. An expired digital certificate does not pass verification and therefore cannot be used. Because certificate expiration adversely affects network services, you need to periodically perform command- or alarm-based queries to check whether certificates are about to expire or have expired.

The following table lists the preset digital certificates provided by the device. If a new certificate needs to be configured based on service requirements, you can run commands for certificate configuration and update.

**Table 1** Preset digital certificates
| **Certificate Type** | **Certificate Function** | **Description** |
| --- | --- | --- |
| Preset CA certificate | Used to verify the identity of a peer Huawei device. | Import and query of a preset CA certificate:  To import a preset CA certificate, run the **pki load preset-ca domain** *default* command. By default, no preset CA certificate is imported. To query the certificate content, run the **display pki ca\_list domain** *default* command.  Deletion and replacement of a preset CA certificate:  To remove the preset CA certificate that has been imported to the default domain, run the **undo pki load preset-ca domain** *default* command. If other CA certificates are required, import them to the default domain for certificate authentication. |
| Preset local certificate | Used by other devices to verify the identity of a local device. | Import and query of a preset local certificate:  To import a preset local certificate, run the **pki load preset-local domain** *default* command. By default, a preset local certificate is imported. To query the certificate content, run the **display pki cert\_list domain** *default* command.  Deletion and replacement of a preset local certificate:  To remove the preset local certificate that has been imported to the default domain, run the **undo pki load preset-local domain** *default* command. Other local certificates cannot be imported to the default domain. To replace the preset local certificate with another user certificate, you can create a PKI domain, import the user certificate to the new domain, and then bind services to this domain. |



#### Configuration and Maintenance Methods

**Methods of Certificate Expiration Query**

* Command-based query
  ```
  <HUAWEI> display pki ca_list
   The x509 object type is certificate:
  Certificate:
      Data:
          Version: 3 (0x2)
          Serial Number:
              49:71:c8:f9:31:04:3e:1b:42:bc:29:f6:bb:06:40:33:b3:f7:53:d9
          Signature Algorithm: sha256WithRSAEncryption
          Issuer: CN=root,OU=HW,O=HW,L=NJ,ST=JS,C=CN
          Validity
              Not Before: Jun  16  01:01:45 2021 GMT
              Not After : Jun  16  01:01:45 2022 GMT
  ```
* Alarm-based query
  ```
  <HUAWEI> display alarm active
  1:Critical  2:Major  3:Minor  4:Warning
  -------------------------------------------------------------------------------
  Sequence   AlarmId    Level Date Time  Description
  -------------------------------------------------------------------------------
  1393       0xF10091   1     2024-01-02 The CA certificate is invalid. (CACertSta
                     20:53:26  rtTime=2022-02-14 06:48:00, CACertFinishT
                     ime=2023-02-14 06:48:00, CACertIssuer=CN=
                     11,OU=11,O=11,C=11,E=11, CACertSubject=CN   
                     =11,O=11,C=11, FileName=huawei1.cer, Inva   
                     lidReason=The current time is not within       
                     the validity period of the certificate) 
  -------------------------------------------------------------------------------
  ```

**Certificate Update Procedure**

For details, see "Updating the Expired Local Certificate and CRL Certificate" in Configuration > Security > PKI Configuration > Maintaining PKI.

A certificate can be updated in offline or CMP mode. The following uses the CMP mode as an example to describe how to implement an automatic certificate update. Before performing relevant operations, ensure that the CA server has been configured so that it can automatically issue certificates. In addition, in the case of initial authentication, check that the device has been preconfigured with an external certificate, such as **abc.cer** involved in [1](#EN-US_CONCEPT_0000001221878845__li139131324153213), for mutual authentication with the CA server.

1. Configure certificate application in CMP mode.
   ```
   [~HUAWEI] rsa pki local-key-pair abc create
   Info: The name of the new RSA key will be:abc.
   Info: The name of the new RSA key will be:abc.
   The range of public key size is (2048 ~ 4096).
   NOTES: If the key modulus is greater than 2048,
   it will take a few minutes.
   Input the bits in the modulus[default = 3072]:
   Info: Operating, please wait for a moment.......done.
   Info: Create RSA local-key-pair success.
   <HUAWEI> system-view
   [~HUAWEI] pki entity abc
   [*HUAWEI] commit
   [~HUAWEI-pki-entity-abc] common-name HUAWEI
   [*HUAWEI-pki-entity-abc] commit
   [~HUAWEI-pki-entity-abc] quit
   [~HUAWEI] pki domain abc
   [*HUAWEI-pki-domain-abc] pki cmp session abc
   [*HUAWEI-pki-domain-abc-pki-cmp-session-abc] cmp request entity abc
   [*HUAWEI-pki-domain-abc-pki-cmp-session-abc] cmp request rsa local-key-pair abc regenerate 4096
   [*HUAWEI-pki-domain-abc-pki-cmp-session-abc] cmp request ca-name "/C=CN/O=JIT/CN=CMPSignCert"
   [*HUAWEI-pki-domain-abc-pki-cmp-session-abc] cmp request authentication-cert abc.cer
   [*HUAWEI-pki-domain-abc-pki-cmp-session-abc] cmp request server url http://10.10.10.10:10000/cmp
   [*HUAWEI-pki-domain-abc-pki-cmp-session-abc] commit
   [~HUAWEI-pki-domain-abc-pki-cmp-session-abc] quit
   [~HUAWEI-pki-domain-abc] pki cmp initial-request
   [~HUAWEI-pki-domain-abc] quit
   ```
2. Import CA and local certificates.
   ```
   [~HUAWEI] pki import-certificate local filename abc_ir.cer
   [~HUAWEI] pki import-certificate ca filename abc_ca0.cer
   [~HUAWEI] pki import-certificate ca filename abc_ca1.cer
   ```
3. Enable PKI-based strict check.
   ```
   [~HUAWEI] [pki strict-mode](cmdqueryname=pki+strict-mode)
   ```
4. Enable the automatic certificate update function.
   ```
   [~HUAWEI] pki domain abc
   [~HUAWEI-pki-domain-abc] pki cmp session abc
   [~HUAWEI-pki-domain-abc-pki-cmp-session-abc] cmp request authentication-cert abc_ir.cer
   [~HUAWEI-pki-domain-abc-pki-cmp-session-abc] certificate auto-update enable
   ```

#### Verifying the Security Hardening Result

1. Run the **display rsa pki local-key-pair** **public** command to check information about the RSA key pair.
2. Run the **display pki match-rsa-key certificate-filename file-name** command to check the RSA key pair used by a specific certificate.
3. Run the **display pki cert-req** **filename** *file-name* command to check the content of the certificate request file with a specific name.
4. Run the **display pki certificate** **filename** *file-name* command to check the content of the certificate file with a specific name.
5. Run the **display pki crl** **filename** *file-name* command to check the content of the CRL file with a specific name.
6. Run the **display pki ca\_list** [ **domain** *domainName* ] command to check the content of the CA certificates and CRL imported to the memory.
7. Run the **display pki cert\_list** [ **domain** *domainName* ] command to check the content of the local certificates imported to the memory.