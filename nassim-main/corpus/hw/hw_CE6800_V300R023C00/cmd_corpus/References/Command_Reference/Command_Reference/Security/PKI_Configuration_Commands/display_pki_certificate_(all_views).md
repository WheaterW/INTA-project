display pki certificate (all views)
===================================

display pki certificate (all views)

Function
--------



The **display pki certificate** command displays the content about the CA or local certificate loaded to the device.




Format
------

**display pki certificate ocsp** [ **realm** *realm-name* ]

**display pki certificate** { **ca** | **local** | **ocsp** } [ **filename** *file-name* ]

**display pki certificate default** { **ca** | **local** } [ **key-pair-type** **rsa** ]

**display pki certificate** { **ca** | **local** } [ **realm** *realm-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **realm** *realm-name* | Specifies the PKI realm name of a certificate to be checked. | The PKI realm name must already exist. |
| **ca** | Displays content about the CA certificate. | - |
| **local** | Displays content about the local certificate. | - |
| **ocsp** | Displays content about the Online Certificate Status Protocol (OCSP) server's certificate. | - |
| **filename** *file-name* | The value must be an existing certificate file name. | The value is a string of 1 to 64 case-sensitive characters. It cannot contain spaces. |
| **default** | Specifies the content of the default built-in certificate. | - |
| **key-pair-type** | Indicates the key pair type. | - |
| **rsa** | Sets the key pair type to RSA. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



This command shows information about the CA certificate, local certificate, and OCSP server's certificate, including signature algorithm, issuer, validity period, subject, and subject public key.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the CA certificate.
```
<HUAWEI> display pki certificate ca realm test
2024-05-22 17:18:01.701
Info: It will take a few seconds or more to collect data for displaying. Please wait a moment.
Total Number: 1

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            b2:5a:28:a1:f7:e9:ad:78
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=Self-Sign-Cert-101930058418
        Validity
            Not Before: Apr 17 15:14:11 2023 GMT
            Not After : Apr 17 15:14:11 2043 GMT
        Subject: CN=Self-Sign-Cert-101930058418
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (3072 bit)
                Modulus:
                    00:aa:3d:27:fd:16:fa:0d:19:93:35:53:98:80:b7:
                    28:c0:e1:7c:bb:ce:3a:e8:92:b5:54:a5:fc:a8:fa:
                    37:0f:0a:e4:bc:80:22:41:15:0d:5a:d1:e6:13:ac:
                    61:4e:9a:ba:f1:fd:27:0c:21:2b:4a:44:8e:4a:3b:
                    a7:13:da:dc:f3:52:eb:16:5e:1f:9c:dc:55:8c:e2:
                    77:a5:38:79:f8:90:3f:eb:1a:7e:81:c7:26:cc:86:
                    97:89:f6:98:56:c3:00:16:5b:ba:a1:3e:0d:d4:dd:
                    8e:b6:ad:98:73:b6:bb:34:2e:54:34:cd:4c:21:22:
                    f5:e1:72:e6:19:ee:f5:3e:70:7a:f3:49:52:83:fd:
                    2b:26:80:b1:38:a7:7e:de:bd:77:0c:9d:2c:7b:c9:
                    3c:cd:3f:fc:1f:84:22:fa:3b:b2:74:9e:77:5b:a7:
                    9a:f9:d5:b6:10:1c:ce:9a:8b:a3:62:08:db:51:8c:
                    c6:45:a4:96:0e:e0:e2:82:37:e3:27:d4:c6:9e:2e:
                    fc:a3:3b:85:67:c2:26:1f:fb:25:65:2a:6c:57:e3:
                    40:d1:59:1b:2c:8b:7e:43:36:12:43:1b:36:33:23:
                    eb:20:14:32:03:5a:9b:24:8a:44:8c:35:81:04:89:
                    aa:08:86:31:db:19:b1:e1:c2:4a:b7:e0:0e:3f:00:
                    83:df:07:7c:e5:7f:8b:73:3e:3b:c3:05:60:e6:f2:
                    82:a6:f8:f3:e5:8b:e8:75:03:cb:4f:7f:96:1f:21:
                    45:ed:2d:86:d5:7e:b2:3c:f6:37:94:08:2b:1a:26:
                    f2:5e:c6:96:b1:49:ed:1a:0a:d7:5f:7f:93:5e:08:
                    25:09:d8:5f:ce:74:b7:c0:d5:53:87:54:69:89:9f:
                    f1:c9:50:36:e7:53:7e:b2:37:2d:76:08:f7:d7:38:
                    25:d7:56:89:b0:82:78:64:6c:4f:b2:c7:2a:ee:94:
                    d6:f3:ea:c9:4f:67:da:78:81:df:db:1e:e9:47:52:
                    61:f8:d7:64:5d:01:f4:56:ba:85
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Basic Constraints: critical
                CA:TRUE
            X509v3 Subject Key Identifier:
                F5:CC:EF:26:22:97:20:9A:66:CE:60:F3:10:72:18:14:14:CC:21:E1
            X509v3 Key Usage:
                Digital Signature, Key Encipherment, Key Agreement, Certificate Sign, CRL Sign
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        a1:dd:16:51:6b:03:50:62:f1:bb:fd:71:ba:a3:ff:72:af:79:
        e3:12:84:ef:22:14:3a:e3:80:7c:0b:81:a1:17:31:cf:af:20:
        eb:18:20:f2:8e:5d:49:e1:95:f4:29:7b:0b:6a:b7:5e:14:49:
        36:c2:4d:4b:4a:e1:7c:ed:d0:5a:a1:c4:b9:29:29:06:b4:dd:
        0b:9d:be:8a:5a:ba:52:b3:69:97:85:19:5e:89:c2:1c:22:6e:
        95:46:84:d6:87:8f:89:0f:df:0d:dc:a2:77:41:0c:c2:f6:62:
        80:2f:49:d7:08:9e:49:40:b6:25:14:39:ce:2f:b3:03:28:a6:
        ce:39:38:a2:22:dd:f1:27:cc:5b:01:de:07:51:1f:72:06:bc:
        5e:69:74:fd:4f:26:9f:ba:f7:d1:45:12:1c:ac:fa:82:6c:90:
        da:45:60:9c:50:5a:fa:fc:0d:e3:bc:0a:2e:55:1e:70:3e:08:
        89:31:80:3d:e3:45:3d:70:c1:44:8f:0e:4e:df:4c:2f:26:70:
        77:26:4d:aa:a1:c5:e3:9b:2d:94:2a:6e:d8:d6:21:36:90:83:
        3b:d0:5e:d1:4c:bf:0e:39:c7:09:62:88:d5:56:b9:93:48:74:
        ba:8d:a8:a2:bb:94:9c:58:f2:7e:d7:82:c1:4c:a0:a6:d7:08:
        ed:81:c8:6e:fd:48:5d:ed:1b:2a:74:13:fb:e4:be:ee:e1:09:
        17:e7:74:76:d3:ca:9a:bb:40:eb:b7:8e:60:00:9a:df:6d:9d:
        d4:28:eb:50:0f:e6:0d:6b:87:1d:3a:28:ee:a6:c3:af:83:ee:
        ca:0d:c3:53:16:1e:61:48:3d:58:8d:4e:a2:e6:be:08:94:75:
        f7:a5:06:7a:32:fc:3c:83:ce:d5:d3:04:03:8b:bb:3c:4e:80:
        88:52:ce:71:6e:4b:09:69:b9:b6:74:bc:3f:69:47:fc:bd:12:
        53:12:67:0e:5e:f4:47:ff:0c:57:80:ff:cd:68:74:3c:ae:67:
        04:63:9a:2a:e2:c6


Pki realm name: test
Certificate file name: test.cer
Certificate peer name: -

```

**Table 1** Description of the **display pki certificate (all views)** command output
| Item | Description |
| --- | --- |
| Total Number | Number of queried certificates. |
| Serial Number | Indicates the serial number of the certificate. |
| Signature Algorithm | Signature algorithm of a certificate. |
| Validity | Validity period of a certificate. |
| Subject | Subject of a certificate. The subject includes the following attributes:   * C: country code of a PKI entity. * ST: name of the state or province to which a PKI entity belongs. * L: geographic area where a PKI entity is located. * O: organization to which a PKI entity belongs. * OU: department to which a PKI entity belongs. * CN: common name of a PKI entity. |
| Subject Public Key Info | Information about the public key of a certificate. |
| Public Key Algorithm | Public key algorithm. |
| X509v3 extensions | Indicates the X.509v3 certificate extensions. |
| X509v3 Key Usage | X509v3 key usage. |
| X509v3 Basic Constraints | Basic constraints. |
| X509v3 Subject Key Identifier | Identifier of a subject key. |
| Certificate | Indicates the information of the certificate. |
| Certificate file name | Certificate file name. |
| Certificate peer name | Certificate used by the IKE peer. |
| Pki realm name | PKI realm name. |
| Data | Certificate data. |
| Version | Version of a certificate. |
| Issuer | Issuer of a certificate. |
| Public-Key | Public key. |
| Modulus | Key modulus. |
| Exponent | Indicates the key exponent. |
| CA | Whether the CA can be trusted. |