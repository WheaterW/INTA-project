display ssl policy
==================

display ssl policy

Function
--------

The **display ssl policy** command displays the Secure Sockets Layer (SSL) policy configuration.



Format
------

**display ssl policy** [ *policyName* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policyName* | Specifies the name of an SSL policy.  If no SSL policy is specified, the configurations of all SSL policies will be displayed. | The value is a string of 1 to 23 case-insensitive characters, containing letters, digits, and underscores (\_), spaces not supported. |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

After loading SSL policies and certificates, you can run the display ssl policy command to view the configurations, including the SSL policy name, service to which an SSL policy is applied, certificate name, and certificate type. The command output shows whether the SSL policies and certificates are available.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display the configuration of the SSL policy named policy1.
```
<HUAWEI> display ssl policy test1

       SSL Policy Name: test1
            PKI domain:
     Policy Applicants:
         Key-pair Type: RSA
 Certificate File Type: PEM
      Certificate Type: certificate
  Certificate Filename: client_c1.crt
     Key-file Filename: client.key
             Auth-code: ******
                   MAC:
           Issuer name: c1
          Subject name: client
   Validity Not Before: 2022-08-25 11:50:00Z
    Validity Not After: 2023-08-25 11:50:00Z
              CRL File:
       Trusted-CA File:
---------------------------------------------------------------------
File Name 1                  : client_c1.crt
File Type                    : certificate
  Serial Number 1            : 160f1d19707e7329
    Version                  : V3
    Issuer                   : C=CN, CN=c1
    Subject                  : C=CN, ST=SZ, L=SZ, O=HW, OU=IT, CN=client
    Certificate State        : valid
    Start Time               : 2022-08-25 11:50:00Z
    End Time                 : 2023-08-25 11:50:00Z
    Signature Algorithm      : sha256WithRSAEncryption
    Public Key Algorithm     : rsaEncryption(3072 Bits)
    Key Usage                : Data Encipherment, Key Encipherment, Digital Signature(b0)
    Subject Alternative Name :
    Common Name              : client

```


**Table 1** Description of the
**display ssl policy** command output

| Item | Description |
| --- | --- |
| SSL Policy Name | Name of an SSL policy. |
| Policy Applicants | Service to which an SSL policy is applied.  Currently, SSL policies can be applied to HTTP services. |
| PKI domain | PKI Domain. |
| Key-pair Type | Key pair type:   * RSA. * DSA. * ECC.   To ensure high security, do not use the RSA key pair whose length is less than 3072 bits. |
| Certificate File Type | Certificate format:   * PEM. * ASN1. * PFX. |
| Certificate Type | Certificate type:   * Certificate. * Certificate-chain. |
| Certificate Filename | Name of a certificate. |
| Certificate State | Certificate status:   * valid. * abort-to-expire. * expired. |
| File Name 1 | Certificate file name. |
| File Type | Certificate file type:   * certificate. * crl. * trusted-ca. |
| Key-file Filename | Name of a key pair file. |
| Issuer name | Name of the certificate issuer. |
| Issuer | Certificate issuer. |
| Subject name | Subject name of the certificate user. |
| Subject | Certificate user. |
| Subject Alternative Name | Subject alternative name of the certificate. |
| Validity Not Before | Start Time of Validity Period. |
| Validity Not After | End Time of Validity Period. |
| CRL File | CRL File. |
| Trusted-CA File | Trusted-CA file. |
| Serial Number 1 | Serial number of the certificate. |
| Version | Version number of the certificate. |
| Start Time | Time when the certificate takes effect. |
| End Time | Certificate expiration time. |
| Signature Algorithm | Certificate signature algorithm. |
| Public Key Algorithm | Public key algorithm of the certificate. |
| Key Usage | Usage of the certificate key. |
| Common Name | Common name of the certificate. |
| Auth-code | Authentication code of the key pair file. |
| MAC | Message authentication code. |