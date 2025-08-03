display pki peer-certificate (all views)
========================================

display pki peer-certificate (all views)

Function
--------



The **display pki peer-certificate** command displays the imported certificates of the remote device.




Format
------

**display pki peer-certificate** { **name** *peer-name* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *peer-name* | Specifies the name of peer certificate. | The value must be an existing peer certificate file name. |
| **all** | Displays brief information about all certificates of the remote device. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command shows information about imported certificates of the remote device, including signature algorithm, issuer, validity period, subject, public key, and PKI realm.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about all certificates of the remote device.
```
<HUAWEI> display pki peer-certificate all
Total Number: 1

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            78:e3:b0:a1:84:0f:df:3f:31:9f:4a:a8:df:17:d1:e8:5f:e0:b3:7e
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=CN, ST=ZJ, L=HZ, O=HW, OU=ICT, CN=PKI_TEST_CA/emailAddress=test@huawei.com
        Validity
            Not Before: Mar 30 01:46:07 2023 GMT
            Not After : Mar 29 01:46:07 2024 GMT
        Subject: C=CN, ST=ZJ, L=HZ, O=HW, OU=ICT, CN=PKI_TEST_LOCAL_1/emailAddress=test@huawei.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (3072 bits)
                Modulus:
                    00:bb:e8:d7:2e:99:28:5c:75:a2:77:1d:8f:03:bb:
                    ec:5a:62:31:2e:d8:4c:24:cf:aa:9d:bf:d2:11:87:
                    5b:b6:39:d4:b5:37:f0:9a:28:40:94:19:09:83:c3:
                    89:98:39:ec:9d:43:b9:1e:9b:ce:bd:2a:c8:79:0f:
                    fb:24:01:f6:3e:ee:15:dc:f1:29:40:8f:67:4e:69:
                    a4:07:ad:95:24:a8:2b:05:2d:5b:c4:27:17:22:8a:
                    08:4a:3c:c4:24:f8:b4:d5:24:18:68:9b:f1:f7:80:
                    06:56:12:49:b7:31:3d:8c:a8:78:78:92:b7:8f:35:
                    4a:a5:66:a2:18:88:df:50:dc:0f:96:31:c7:a5:df:
                    be:b6:37:d5:62:56:30:13:a2:1b:3b:96:5d:5b:51:
                    eb:d0:65:34:0f:b7:d6:7e:cd:90:b6:83:6d:9e:c0:
                    29:1a:40:94:8d:d3:1c:48:ef:fd:5f:c8:a7:b2:50:
                    69:f3:c7:7e:e3:99:67:bd:9e:87:d2:a0:f6:26:fa:
                    a1:07:9f:7a:6f:52:da:62:74:0c:64:4b:44:af:67:
                    f3:f3:2f:a9:ce:42:39:5a:51:bc:d2:bc:97:60:06:
                    98:33:27:a7:ef:65:00:49:50:8a:9d:d4:18:22:26:
                    05:83:23:d2:81:58:24:9d:b0:13:f4:9a:86:59:28:
                    d1:a3:ed:5a:65:33:d8:3b:c1:91:d5:b9:1c:0b:9f:
                    4e:cb:aa:84:38:e8:07:d8:25:87:ce:df:b5:c7:ed:
                    c1:bb:8c:bf:63:86:0f:73:fe:9f:42:45:25:8b:8f:
                    63:64:50:78:8a:a9:e6:8e:4d:60:f0:5f:16:b8:0d:
                    52:55:ab:0b:9f:1a:cb:66:b8:d4:2b:83:75:0c:65:
                    0c:0d:a3:1a:a2:09:44:d4:4c:f7:b6:b6:bb:1d:80:
                    b3:95:c6:4e:49:11:6c:df:9f:05:ad:88:dd:d7:f4:
                    5b:80:b5:cc:7d:53:59:5d:06:d1:a0:71:d1:7f:ea:
                    ce:6f:48:8a:bf:dc:3d:93:4e:e7
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Basic Constraints:
                CA:FALSE
            X509v3 Subject Key Identifier:
                7D:7A:7E:92:FB:5A:2D:B5:5A:FE:AC:B7:63:83:98:76:C1:2E:2A:7B
            X509v3 Authority Key Identifier:
                keyid:B6:14:3D:26:13:B1:33:B7:FC:02:82:09:01:7A:81:C5:1F:DA:42:8D
                DirName:/C=CN/ST=ZJ/L=HZ/O=HW/OU=ICT/CN=PKI_TEST_CA/emailAddress=test@huawei.com
                serial:07:EA:58:48:ED:F8:8C:4A:49:66:FB:71:2F:C1:B3:E6:D9:A7:D3:8C

            X509v3 Key Usage:
                Digital Signature, Non Repudiation, Key Encipherment, Data Encipherment, Key Agreement
            X509v3 Extended Key Usage:
                1.3.6.1.5.5.8.2.2, TLS Web Server Authentication, TLS Web Client Authentication
            X509v3 Subject Alternative Name:
                DNS:abc.com, IP Address:1.1.1.1
            Authority Information Access:
                CA Issuers - URI:http://test.test.com/test_ca.cer;
                OCSP - URI:http://test.test.com/ocsp;

            X509v3 CRL Distribution Points:

                Full Name:
                  URI:http://test.test.com/test_crl.crl

    Signature Algorithm: sha256WithRSAEncryption
         78:86:96:f3:af:dc:b0:bc:69:dd:59:e9:21:50:e4:28:f5:52:
         3c:f4:39:b3:6e:80:96:b2:d5:46:91:1b:8f:a1:70:f4:dd:a7:
         11:a0:22:d8:d0:18:00:54:fa:e7:cf:5f:7a:ef:6a:ca:37:f2:
         f1:cb:06:94:f7:47:0e:a5:77:98:c5:86:b8:32:9b:05:2c:d5:
         87:48:95:04:85:06:ad:0e:12:83:b9:ae:b1:d1:7c:e9:b3:d9:
         dd:f0:a8:1f:d7:4a:64:a1:9c:64:5c:d6:da:50:d7:35:d3:42:
         f9:ef:3f:60:a7:82:76:55:ff:1f:43:ec:2c:22:b1:a4:36:66:
         f4:3b:c5:6e:d0:21:9d:bd:23:63:9c:d7:2c:9e:57:4c:98:b2:
         cf:be:f6:4c:10:f5:d1:e2:72:ea:9e:e0:d9:4b:04:1f:89:06:
         91:e7:98:40:5a:23:9c:85:e6:14:2f:03:bd:fe:84:c2:c0:d7:
         70:bf:da:f4:68:74:8a:51:86:b1:90:ea:31:ec:25:02:16:5f:
         bd:6c:82:14:29:b1:3f:f6:05:fc:65:e6:3f:0d:5a:92:9f:8f:
         f7:56:86:de:47:d9:f2:75:87:c7:46:f9:d1:5f:2b:03:a9:97:
         0c:74:ef:e4:0a:a3:91:90:ed:c0:42:24:d9:39:dd:c9:da:9f:
         c4:44:57:79:13:46:aa:23:76:25:55:92:5d:87:84:f9:e0:db:
         b9:a7:ee:03:f0:f3:bb:42:04:e6:86:3b:cb:e6:68:c2:88:6a:
         60:76:a4:c2:4c:5e:f6:44:26:d5:3a:ae:39:eb:cd:b4:21:09:
         85:a1:ae:35:20:f9:c1:87:83:a7:3c:01:22:74:76:6a:9c:93:
         0c:07:b1:8c:b0:9a:e0:12:5c:52:62:60:4c:f9:47:90:68:c7:
         96:24:93:86:c2:e6:af:df:7b:b8:e9:f2:0a:a4:7d:0e:c3:61:
         9d:8c:ce:3f:17:8a:7c:df:f3:05:95:69:9f:e8:7e:64:07:a2:
         bd:a7:f3:85:49:18


Pki realm name: -
Certificate file name: pki_test.cer
Certificate peer name: abcd

```

# Display detailed information about the certificate abcd of the remote device.
```
<HUAWEI> display pki peer-certificate name abcd
Total Number: 1

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            78:e3:b0:a1:84:0f:df:3f:31:9f:4a:a8:df:17:d1:e8:5f:e0:b3:7e
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=CN, ST=ZJ, L=HZ, O=HW, OU=ICT, CN=PKI_TEST_CA/emailAddress=test@huawei.com
        Validity
            Not Before: Mar 30 01:46:07 2023 GMT
            Not After : Mar 29 01:46:07 2024 GMT
        Subject: C=CN, ST=ZJ, L=HZ, O=HW, OU=ICT, CN=PKI_TEST_LOCAL_1/emailAddress=test@huawei.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (3072 bits)
                Modulus:
                    00:bb:e8:d7:2e:99:28:5c:75:a2:77:1d:8f:03:bb:
                    ec:5a:62:31:2e:d8:4c:24:cf:aa:9d:bf:d2:11:87:
                    5b:b6:39:d4:b5:37:f0:9a:28:40:94:19:09:83:c3:
                    89:98:39:ec:9d:43:b9:1e:9b:ce:bd:2a:c8:79:0f:
                    fb:24:01:f6:3e:ee:15:dc:f1:29:40:8f:67:4e:69:
                    a4:07:ad:95:24:a8:2b:05:2d:5b:c4:27:17:22:8a:
                    08:4a:3c:c4:24:f8:b4:d5:24:18:68:9b:f1:f7:80:
                    06:56:12:49:b7:31:3d:8c:a8:78:78:92:b7:8f:35:
                    4a:a5:66:a2:18:88:df:50:dc:0f:96:31:c7:a5:df:
                    be:b6:37:d5:62:56:30:13:a2:1b:3b:96:5d:5b:51:
                    eb:d0:65:34:0f:b7:d6:7e:cd:90:b6:83:6d:9e:c0:
                    29:1a:40:94:8d:d3:1c:48:ef:fd:5f:c8:a7:b2:50:
                    69:f3:c7:7e:e3:99:67:bd:9e:87:d2:a0:f6:26:fa:
                    a1:07:9f:7a:6f:52:da:62:74:0c:64:4b:44:af:67:
                    f3:f3:2f:a9:ce:42:39:5a:51:bc:d2:bc:97:60:06:
                    98:33:27:a7:ef:65:00:49:50:8a:9d:d4:18:22:26:
                    05:83:23:d2:81:58:24:9d:b0:13:f4:9a:86:59:28:
                    d1:a3:ed:5a:65:33:d8:3b:c1:91:d5:b9:1c:0b:9f:
                    4e:cb:aa:84:38:e8:07:d8:25:87:ce:df:b5:c7:ed:
                    c1:bb:8c:bf:63:86:0f:73:fe:9f:42:45:25:8b:8f:
                    63:64:50:78:8a:a9:e6:8e:4d:60:f0:5f:16:b8:0d:
                    52:55:ab:0b:9f:1a:cb:66:b8:d4:2b:83:75:0c:65:
                    0c:0d:a3:1a:a2:09:44:d4:4c:f7:b6:b6:bb:1d:80:
                    b3:95:c6:4e:49:11:6c:df:9f:05:ad:88:dd:d7:f4:
                    5b:80:b5:cc:7d:53:59:5d:06:d1:a0:71:d1:7f:ea:
                    ce:6f:48:8a:bf:dc:3d:93:4e:e7
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Basic Constraints:
                CA:FALSE
            X509v3 Subject Key Identifier:
                7D:7A:7E:92:FB:5A:2D:B5:5A:FE:AC:B7:63:83:98:76:C1:2E:2A:7B
            X509v3 Authority Key Identifier:
                keyid:B6:14:3D:26:13:B1:33:B7:FC:02:82:09:01:7A:81:C5:1F:DA:42:8D
                DirName:/C=CN/ST=ZJ/L=HZ/O=HW/OU=ICT/CN=PKI_TEST_CA/emailAddress=test@huawei.com
                serial:07:EA:58:48:ED:F8:8C:4A:49:66:FB:71:2F:C1:B3:E6:D9:A7:D3:8C

            X509v3 Key Usage:
                Digital Signature, Non Repudiation, Key Encipherment, Data Encipherment, Key Agreement
            X509v3 Extended Key Usage:
                1.3.6.1.5.5.8.2.2, TLS Web Server Authentication, TLS Web Client Authentication
            X509v3 Subject Alternative Name:
                DNS:abc.com, IP Address:1.1.1.1
            Authority Information Access:
                CA Issuers - URI:http://test.test.com/test_ca.cer;
                OCSP - URI:http://test.test.com/ocsp;

            X509v3 CRL Distribution Points:

                Full Name:
                  URI:http://test.test.com/test_crl.crl

    Signature Algorithm: sha256WithRSAEncryption
         78:86:96:f3:af:dc:b0:bc:69:dd:59:e9:21:50:e4:28:f5:52:
         3c:f4:39:b3:6e:80:96:b2:d5:46:91:1b:8f:a1:70:f4:dd:a7:
         11:a0:22:d8:d0:18:00:54:fa:e7:cf:5f:7a:ef:6a:ca:37:f2:
         f1:cb:06:94:f7:47:0e:a5:77:98:c5:86:b8:32:9b:05:2c:d5:
         87:48:95:04:85:06:ad:0e:12:83:b9:ae:b1:d1:7c:e9:b3:d9:
         dd:f0:a8:1f:d7:4a:64:a1:9c:64:5c:d6:da:50:d7:35:d3:42:
         f9:ef:3f:60:a7:82:76:55:ff:1f:43:ec:2c:22:b1:a4:36:66:
         f4:3b:c5:6e:d0:21:9d:bd:23:63:9c:d7:2c:9e:57:4c:98:b2:
         cf:be:f6:4c:10:f5:d1:e2:72:ea:9e:e0:d9:4b:04:1f:89:06:
         91:e7:98:40:5a:23:9c:85:e6:14:2f:03:bd:fe:84:c2:c0:d7:
         70:bf:da:f4:68:74:8a:51:86:b1:90:ea:31:ec:25:02:16:5f:
         bd:6c:82:14:29:b1:3f:f6:05:fc:65:e6:3f:0d:5a:92:9f:8f:
         f7:56:86:de:47:d9:f2:75:87:c7:46:f9:d1:5f:2b:03:a9:97:
         0c:74:ef:e4:0a:a3:91:90:ed:c0:42:24:d9:39:dd:c9:da:9f:
         c4:44:57:79:13:46:aa:23:76:25:55:92:5d:87:84:f9:e0:db:
         b9:a7:ee:03:f0:f3:bb:42:04:e6:86:3b:cb:e6:68:c2:88:6a:
         60:76:a4:c2:4c:5e:f6:44:26:d5:3a:ae:39:eb:cd:b4:21:09:
         85:a1:ae:35:20:f9:c1:87:83:a7:3c:01:22:74:76:6a:9c:93:
         0c:07:b1:8c:b0:9a:e0:12:5c:52:62:60:4c:f9:47:90:68:c7:
         96:24:93:86:c2:e6:af:df:7b:b8:e9:f2:0a:a4:7d:0e:c3:61:
         9d:8c:ce:3f:17:8a:7c:df:f3:05:95:69:9f:e8:7e:64:07:a2:
         bd:a7:f3:85:49:18


Pki realm name: -
Certificate file name: pki_test.cer
Certificate peer name: abcd

```

**Table 1** Description of the **display pki peer-certificate (all views)** command output
| Item | Description |
| --- | --- |
| Serial Number | Serial number of a certificate. |
| Signature Algorithm | Signature algorithm of a certificate. |
| Validity | Validity period of the certificate. |
| Subject | Subject of a certificate. |
| Subject Public Key Info | Public key of the certificate. |
| Public Key Algorithm | Public key algorithm. |
| X509v3 extensions | X509v3 certificate extensions. |
| X509v3 Subject Key Identifier | Identifier of a subject key. |
| X509v3 CRL Distribution Points | CDP information. |
| Authority Information Access | Authority information access. |
| Data | Certificate data. |
| Full Name | Full name of the CDP. |
| Pki realm name | PKI realm name. |
| Certificate | Information about a certificate. |
| Certificate file name | Certificate file name. |
| Certificate peer name | Peer certificate name. |
| Version | Version of a certificate. |
| Issuer | Issuer of a certificate. |
| Public-Key | Information about the RSA public key. |
| Modulus | Key modulus. |
| Exponent | Key exponent. |