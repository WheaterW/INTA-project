display pki cert-req
====================

display pki cert-req

Function
--------



The **display pki cert-req** command displays the content of a certificate request file.




Format
------

**display pki cert-req filename** *file-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **filename** *file-name* | Specifies the name of a certificate request file. | The certificate request file name must already exist. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command displays content of a certificate request file, including the subject, public key algorithm, key modulus, attributes, and signature algorithm.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the content of a certificate request file named test.req.
```
<HUAWEI> display pki cert-req filename test.req
2024-05-22 17:01:34.302
Certificate Request:
    Data:
        Version: 1 (0x0) 
        Subject: C=cn, ST=hangzhou, O=huawei, OU=GW, CN=test
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (3072 bit)
                Modulus:
                    00:ba:8b:38:ca:d6:89:d2:e2:20:8b:32:1c:c5:81:
                    5c:44:3f:0c:8a:32:e1:5a:96:82:09:bb:21:66:31:
                    36:50:3c:10:be:b0:60:4d:0e:31:2c:c1:37:e9:44:
                    1c:f8:d3:48:0b:34:2d:2b:bf:ec:d8:ce:77:1a:62:
                    9b:2a:ef:d7:1f:a5:7d:2f:cd:90:6e:47:d1:52:3e:
                    c0:89:bb:9e:24:72:8d:67:9e:93:32:97:34:8b:16:
                    20:9d:d1:f1:9e:25:3c:41:ca:4e:7a:9a:7a:1e:bb:
                    83:32:b5:7b:14:76:d5:16:57:d4:81:25:1f:da:ea:
                    3e:22:f0:97:c3:a9:bc:64:08:ce:1e:d3:fe:d3:5b:
                    a1:de:cf:f7:95:da:23:81:cd:c7:6f:7c:21:05:95:
                    72:9b:2e:c1:8e:fb:10:73:3d:aa:d9:e1:c2:6c:33:
                    8d:69:9e:9a:63:20:74:00:b7:df:dd:19:58:9f:96:
                    c1:74:0d:d2:12:3f:fc:a2:a7:61:e7:83:a1:51:3d:
                    9c:e1:ac:e2:1c:d8:fe:51:ce:2d:5f:cc:ea:f9:f7:
                    f8:fa:e1:29:e4:0f:63:e5:9a:25:69:ac:23:2d:bc:
                    e3:6d:d2:e4:01:bf:9a:b1:5a:80:32:cd:b3:48:3e:
                    d3:f4:83:f6:74:ba:30:a4:90:3c:8d:21:84:f8:7e:
                    2e:c1:af:7a:7c:37:14:80:c2:ed:81:5b:06:27:85:
                    96:0f:13:36:fd:a8:55:de:4f:e9:66:b6:a3:f5:00:
                    2d:03:90:53:01:a9:f4:3e:28:19:fc:05:b1:d2:88:
                    28:fc:5a:d6:75:3b:e0:f5:3e:0a:0d:d2:65:ca:30:
                    60:7b:07:bf:38:eb:b8:bc:6b:0a:d2:9b:76:b9:5b:
                    5d:6d:1c:a1:76:cc:5e:50:8c:e0:ca:52:da:6b:f2:
                    5e:70:66:a7:89:1c:59:72:77:f5:8b:14:ed:38:f1:
                    9e:07:f9:6b:62:93:31:9b:3f:f7:0f:2c:37:a4:b4:
                    8d:46:36:3d:eb:02:a9:47:3a:ed
                Exponent: 65537 (0x10001) 
        Attributes:
            challengePassword        :******
            Requested Extensions:
                X509v3 Key Usage:
                    Digital Signature, Non Repudiation, Key Encipherment, Data Encipherment
                X509v3 Subject Alternative Name:
                    IP Address:10.1.1.1, DNS:test.abc.com, email:test@example.com
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        79:f5:04:62:75:ac:d0:ed:38:da:d5:7a:85:81:23:38:5b:19:   
        04:b8:d0:0f:58:26:a2:8a:56:fc:f6:b7:6c:58:b5:92:83:72:     
        f3:6c:f3:12:e9:c1:0d:c5:f0:c5:d8:12:70:28:a3:8c:88:43:      
        29:74:67:d3:32:c9:17:1b:8d:8b:dd:ff:6c:fb:63:29:28:d5:    
        84:99:4f:d0:47:0c:bd:e8:ea:c2:e9:57:de:74:c1:31:fb:cf:
        30:6d:54:bb:88:5c:4e:8e:f5:4a:3f:4d:30:00:61:a1:17:f2:
        1c:03:b6:ab:d4:d0:17:8a:58:71:97:80:78:35:26:b1:27:07:
        74:01:3b:8c:ac:72:77:cb:ec:b9:36:b7:17:7a:c9:f3:fd:62:
        5f:a2:de:32:f9:92:62:6c:f6:3f:b8:b0:87:17:85:94:ba:6a:
        d2:70:0f:1d:03:16:50:3e:9f:24:d0:ff:41:23:df:81:99:22:
        34:7d:db:49:90:8f:9c:82:10:3c:37:cf:f2:2e:33:f2:9a:d4:
        16:c0:2d:15:05:1d:9d:d0:53:23:8e:d7:e2:a5:68:07:73:3c:
        cf:e2:e6:23:46:d3:51:e2:e6:66:66:e4:e3:5f:f6:de:4b:f9:
        35:f0:ca:47:38:dc:e7:64:25:1a:31:6e:1c:ca:8c:5c:b1:01:
        1e:84:ad:bd:e0:6c:50:41:5d:56:aa:db:22:fe:96:14:63:33:
        79:c3:13:0a:b6:12:40:55:9e:1c:df:9c:17:04:b1:21:f0:31:
        74:68:08:00:be:0e:50:1f:5f:a0:93:29:09:50:c9:a5:f9:73:
        48:52:5d:53:da:8a:73:a3:b5:37:03:9a:cf:21:e1:e8:90:73:
        29:f1:ad:b3:6a:62:b7:f0:3d:29:a9:27:3d:f5:82:04:e7:86:
        fa:33:f5:85:61:7a:c3:7d:47:b2:c9:f1:9e:96:e0:26:7a:35:
        b7:03:47:a2:e5:78:52:c9:bc:ad:e2:86:ff:21:53:8e:79:f3:
        85:ed:91:f6:59:7f

```

**Table 1** Description of the **display pki cert-req** command output
| Item | Description |
| --- | --- |
| Certificate Request | Information of the CSR file. |
| Subject | Subject of a certificate request file. The subject includes the following attributes:   * C: country code of a PKI entity. It is configured using the country (PKI entity view) command. * ST: name of the state or province to which a PKI entity belongs. It is configured using the state (PKI entity view) command. * L: geographic area where a PKI entity is located. It is configured using the locality command. * O: organization to which a PKI entity belongs. It is configured using the organization command. * OU: department to which a PKI entity belongs. It is configured using the organization-unit command. * CN: common name of a PKI entity. It is configured using the common-name command. |
| Subject Public Key Info | Information about the public key of the CSR file. |
| Public Key Algorithm | Algorithm of the public key. |
| challengePassword | The challenge password used in certificate application. It is configured using the pki enroll-certificate command. |
| Requested Extensions | Certificate request extension. |
| X509v3 Subject Alternative Name | Alternative name of the X.509v3 subject. |
| Data | Data of the CSR file. |
| IP Address | IP address of a PKI entity. It is configured using the ip-address command. |
| Signature Algorithm | Signature algorithm. It is configured using the enrollment-request signature message-digest-method command. |
| Version | Version of the CSR file. |
| Modulus | Key modulus. |
| Exponent | Key exponent. |
| Attributes | Attributes of the CSR file. |
| DNS | DNS name of a PKI entity. It is configured using the fqdn command. |
| email | Email address of a PKI entity. It is configured using the email command. |