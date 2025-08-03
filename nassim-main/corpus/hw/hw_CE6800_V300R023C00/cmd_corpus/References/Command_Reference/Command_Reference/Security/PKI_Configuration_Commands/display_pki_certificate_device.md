display pki certificate device
==============================

display pki certificate device

Function
--------



The **display pki certificate device** command displays the contents of the initial certificates (including the local certificate and CA certificate) loaded on the device.




Format
------

**display pki certificate device slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Displays information about the initial certificate in a specified slot. | The value is a string and depends on the device configuration. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command displays detailed information about the initial certificates (including the local certificate and CA certificate) loaded on the device, including the signature algorithm, issuer, validity period, subject, and subject public key.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the initial local certificate and CA certificate.
```
<HUAWEI> display pki certificate device slot 5
05-30-2023 23:13:19.239 +08:00
Slot:5 CPU:0 Certificate information:
Device Certificate:

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            11:3e:3b:0b:74:01:71:8e:7b:8f:a1:3f:a0:d9:3b:08:1e
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: O=Huawei, CN=Huawei DataCom RSA Equipment CA 2
        Validity
            Not Before: May 30 06:49:46 2023 GMT
            Not After : Aug 28 06:49:46 2023 GMT
        Subject: C=CN, O=Huawei, OU=DataCom, CN=033CES10K9000294.huawei.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (3072 bit)
                Modulus:
                    00:bf:11:11:d7:b4:3b:38:69:d5:0f:0c:b1:2f:8d:
                    13:4e:13:41:c0:bd:c5:1c:24:2e:11:5e:8e:cb:14:
                    18:ba:98:92:ea:0a:78:e6:0d:08:e7:d4:e3:43:fb:
                    f8:b7:47:b7:7b:5e:0b:04:4b:27:e2:62:f6:30:2b:
                    c1:44:1b:95:65:ab:86:80:4d:55:d7:d4:e2:d5:15:
                    5d:26:e2:3b:65:b0:41:ed:47:72:f2:d2:fb:55:08:
                    d1:ba:f5:38:c2:ad:3b:55:c7:eb:c1:48:96:f1:11:
                    b4:25:74:40:55:6a:49:c3:66:14:7a:3e:c9:73:9f:
                    4b:25:17:76:99:bf:26:11:f2:4e:7f:0b:ed:d4:f9:
                    cf:41:49:bb:60:72:83:8a:39:42:5d:c4:49:3f:77:
                    69:ea:dd:8b:d3:59:f5:c9:8c:1a:d1:70:28:17:cf:
                    4f:3e:e3:8f:fb:cc:22:ec:9c:33:d8:8a:86:1c:67:
                    60:96:d2:bc:1a:d5:0a:99:54:c9:0c:b7:81:85:55:
                    a7:47:84:b7:76:4a:22:c4:88:ce:51:bd:00:b2:70:
                    14:0e:f6:5b:18:e0:18:7d:c2:09:5d:bf:60:2f:51:
                    0b:a3:02:c9:2c:e6:2d:5d:ba:72:34:a1:07:28:28:
                    10:7b:0a:b1:de:32:58:d1:6d:50:b6:db:c5:66:14:
                    c4:3d:c6:d5:7b:82:ac:2d:1c:b8:24:3d:43:75:18:
                    6c:1e:32:68:6b:7e:b9:42:14:a9:22:63:51:46:4c:
                    18:ae:a0:39:ce:20:94:61:a3:87:13:66:ec:58:4b:
                    dd:87:75:5a:50:6d:a5:b4:67:ae:80:02:4c:6a:42:
                    a2:c1:71:10:19:d8:a3:1f:fd:df:fd:bb:28:25:57:
                    31:1e:a6:1b:88:a8:65:86:56:da:2d:6a:4a:ea:1b:
                    fb:50:3e:18:7a:2b:9d:fe:d8:e4:ed:85:d0:3e:99:
                    63:93:3b:87:55:d6:c8:16:0b:1d:ad:b3:c6:d6:d8:
                    c9:9e:d0:f3:12:8d:bc:c9:e2:cf
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Authority Key Identifier: 
                FA:0C:B9:F9:80:C3:A2:80:6C:8D:0E:C1:04:EA:5F:24:CB:83:33:F5
            X509v3 Subject Key Identifier: 
                8A:6D:F2:F3:E7:A7:23:B6:09:86:06:F6:1C:6B:A8:39:5C:10:DE:98
            X509v3 Subject Alternative Name: 
                othername: 1.3.6.1.4.1.2011.7.6.102::629e09d30220f11ce75b99933ba7040a480004c0005700c203a409d5000000000000000019000000000000c200000008606e0000080000039c2300003951459558c455340000044ff4e80000044d584200000000000000000000000000000000880000000003e3a800000000000000000, othername: 1.3.6.1.4.1.2011.7.6.104::0641659322910e009486de533f0e0d0a000804c0
            X509v3 Basic Constraints: 
                CA:FALSE
            X509v3 Certificate Policies: 
                Policy: 1.3.6.1.4.1.2011.201.1.4.2
                  CPS:  https://support.huawei.com/pki
            X509v3 Key Usage: critical
                Digital Signature, Key Encipherment
            X509v3 CRL Distribution Points: 
                Full Name:
                  URI:https://support.huawei.com/support/pki/DataCom_RSA_CA2_crl.crl
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        5c:83:2a:9d:fc:67:62:0f:05:90:d1:1c:c0:80:93:01:8a:b3:
        da:19:64:32:03:d8:be:83:7d:86:81:fb:d6:72:66:54:83:07:
        28:1e:76:71:a2:d9:25:56:71:56:37:73:11:a6:ea:f6:bd:77:
        87:a2:bd:cb:eb:bb:fe:44:4e:27:de:19:0b:f0:1e:f5:34:c6:
        b7:cb:03:cd:d4:97:67:1b:41:b5:ab:84:3a:f5:21:1f:e8:ed:
        6e:2b:b2:fe:d3:ff:54:b5:8f:58:5b:9b:11:50:58:1d:32:85:
        6e:d4:5f:7d:b4:39:dd:85:76:45:41:43:bb:fb:a2:92:34:b8:
        bc:11:df:7e:d2:1f:0d:26:bd:de:4c:4c:3f:07:77:dc:6d:2d:
        b3:1e:cb:f2:97:b6:7c:ef:67:0d:97:74:08:0d:b0:ed:6e:e6:
        4a:0e:66:ef:fb:e4:9a:5d:5a:04:2d:ce:5c:21:f5:fe:f2:54:
        2c:6e:81:7f:14:0a:31:c9:0e:1a:84:17:ac:06:be:1b:d4:8f:
        f2:21:2b:40:33:cd:d5:a3:40:e3:21:ba:e2:2d:c1:a3:24:af:
        e9:13:86:e8:c8:b2:cb:71:f1:2a:3a:c8:8c:0f:3a:0b:51:4e:
        d6:09:fd:39:6d:79:03:35:33:81:9e:3d:b0:ac:b5:ac:05:70:
        a7:b4:74:69:59:b0:62:a5:26:9f:f2:d9:f5:b0:f4:c5:ba:98:
        11:41:70:78:3f:12:aa:59:ca:6f:d1:98:f6:36:f0:36:2b:66:
        77:d3:13:f3:fb:11:60:fe:cf:3d:7c:c9:41:22:9d:0f:60:63:
        94:c7:ad:7b:59:bd:df:9f:62:9e:96:df:7a:81:cb:b2:b3:05:
        f5:97:23:27:02:e1:8b:b2:c8:00:e1:db:3a:b4:5e:c7:df:ac:
        f7:9e:c8:7f:66:a0:0b:b9:71:f6:b0:f6:b0:72:74:86:d4:b3:
        dc:d8:52:7f:56:a0:05:64:ee:60:6a:a7:c6:39:83:c9:5c:42:
        9e:e5:da:bb:af:21:f0:25:31:5b:3a:d4:ad:cc:32:5f:54:35:
        6d:9c:66:70:15:f2:15:b0:d5:d9:84:2c:08:82:1c:dc:57:1b:
        91:70:d0:eb:3b:c5:b7:7a:d9:07:87:4a:11:c3:33:4b:da:ee:
        9a:e1:a7:1a:26:3d:39:27:10:f2:4f:4d:50:a6:9f:9c:57:fe:
        bc:dd:53:e7:ce:58:14:0a:59:65:6a:df:fb:5a:9b:d9:20:21:
        4f:c7:63:4d:b1:c4:79:f9:46:23:ee:40:62:93:fe:08:12:b5:
        3f:cc:4e:de:a8:dc:c2:e6:a0:6d:e1:9f:7b:46:4e:7d:47:2a:
        51:fc:c5:9e:45:c6:d2:56
    CPU ID:0641659322910e009486de533f0e0d0a000804c0
    NP ID:629e09d30220f11ce75b99933ba7040a480004c0005700c203a409d5000000000000000019000000000000c200000008606e0000080000039c2300003951459558c455340000044ff4e80000044d584200000000000000000000000000000000880000000003e3a800000000000000000

CA Certificate:

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            11:20:1c:47:11:86:f4:b6:d4:bc:06:e1:ce:24:6c:c0:56
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: O=Huawei, CN=Huawei RSA Equipment Root CA 2
        Validity
            Not Before: Jul 31 13:17:08 2021 GMT
            Not After : Jul 30 13:17:08 2071 GMT
        Subject: O=Huawei, CN=Huawei DataCom RSA Equipment CA 2
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (4096 bit)
                Modulus:
                    00:b6:1d:aa:32:06:e7:29:e8:4d:70:9c:7b:29:6c:
                    d7:c4:d7:e0:78:48:73:b7:78:3c:50:b8:08:6b:f9:
                    df:df:5d:06:9d:7d:e0:0f:86:b5:af:bf:a6:af:7b:
                    9a:d3:1a:e5:79:0c:c0:d6:55:0e:f3:02:d1:94:ae:
                    85:32:e5:2d:49:f3:98:6c:ce:37:5f:21:8a:f9:18:
                    3f:fb:71:02:e6:c4:e7:ee:8e:94:e1:06:9d:b9:91:
                    a7:c2:7c:ce:eb:a0:af:7e:3a:71:2c:6b:35:12:de:
                    d0:53:e5:19:d5:ea:6c:ca:2e:08:68:54:19:5e:f8:
                    b0:2d:b3:49:b6:2d:34:9a:99:46:00:10:67:84:ad:
                    09:a1:e4:8f:f3:30:4a:0f:9f:7e:ea:45:cb:82:5a:
                    44:2d:d5:39:35:ee:3b:9f:6e:8c:51:88:84:b3:18:
                    02:a8:c9:c8:eb:01:25:ca:a6:a1:23:79:b3:70:53:
                    5b:f9:30:ae:f3:15:db:ea:61:7c:c6:ed:ca:57:1b:
                    c0:2f:15:fa:0c:4e:9b:53:d8:5a:36:63:eb:eb:4a:
                    92:02:5d:59:03:6a:fe:1b:74:48:df:0f:86:9c:61:
                    7e:ac:c9:32:99:64:b8:4c:45:ee:0c:d1:db:cf:83:
                    56:52:78:98:d5:df:a6:94:9a:99:a5:9d:ad:d5:c8:
                    96:1b:2a:a1:d5:7c:33:8d:a0:75:04:26:a8:7d:53:
                    03:0f:20:0e:10:5f:c6:ed:c3:ab:31:11:5f:f7:79:
                    a8:07:11:2b:84:4a:77:42:0b:99:92:71:98:d1:f6:
                    30:90:44:57:6b:42:d5:38:be:31:eb:4c:35:f2:a0:
                    4e:3f:cd:f7:51:ce:cc:ab:d3:b8:cf:6f:47:6f:35:
                    25:aa:ac:eb:4a:bf:66:a5:71:39:db:66:64:6e:76:
                    7b:fd:7b:8a:0c:f1:62:c4:f2:f2:e5:71:2f:ab:68:
                    87:a1:5a:e2:3c:1c:4f:bc:0c:30:9d:7e:3c:31:8c:
                    c6:f6:5f:e2:b5:dd:e2:4d:a2:30:20:b8:71:39:6b:
                    b7:f4:6f:8c:a7:c8:07:f4:27:22:fd:6e:b9:e2:3a:
                    13:5b:58:af:c6:98:b4:14:02:65:f4:cd:97:0b:de:
                    de:ce:cd:9f:1d:6a:35:10:f7:25:64:c7:26:60:62:
                    9d:0c:c9:77:fd:4c:62:b2:11:b6:ed:bc:14:3d:5b:
                    8b:46:da:db:7b:cf:7d:a7:d8:8b:f8:0f:14:97:25:
                    55:a1:58:d6:b2:dd:71:e9:0c:a6:de:f7:e1:8b:1e:
                    d8:77:60:97:69:f2:bf:72:40:d5:c4:00:24:ab:76:
                    20:fa:75:05:19:ff:fa:0a:46:78:b3:fc:f2:ba:aa:
                    62:58:39
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Authority Key Identifier: 
                63:88:0A:64:93:C6:3E:AC:15:6D:77:01:8E:FF:E9:10:2F:0B:25:34
            X509v3 Subject Key Identifier: 
                FA:0C:B9:F9:80:C3:A2:80:6C:8D:0E:C1:04:EA:5F:24:CB:83:33:F5
            X509v3 Certificate Policies: 
                Policy: 1.3.6.1.4.1.2011.201.1.4.2
                  CPS: https://support.huawei.com/pki
            X509v3 Basic Constraints: critical
                CA:TRUE, pathlen:0
            X509v3 Key Usage: critical
                Certificate Sign, CRL Sign
            X509v3 CRL Distribution Points: 
                Full Name:
                  URI:https://support.huawei.com/support/pki/Huawei_RSA_Equipment_Root_CA2_crl.crl
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        88:16:1e:16:28:3a:0a:1d:ec:96:2d:dc:e2:10:78:a7:4a:44:
        1c:56:21:94:99:0a:2d:2d:32:4c:34:f5:23:03:5c:83:b2:d0:
        1b:cb:58:07:24:c4:e1:a7:db:31:0f:b9:71:09:0c:09:92:ca:
        5e:f5:5c:4b:19:81:80:ee:0f:b5:38:a9:56:7a:91:6d:92:c2:
        5f:4a:d1:fd:1e:3e:1c:bd:21:dd:68:54:6b:27:a4:30:cb:db:
        5a:b9:9a:48:b7:04:0c:5b:c0:e2:ae:35:87:40:4b:d6:cc:e5:
        5d:1a:f0:ef:d8:e4:c9:24:68:e5:e5:91:86:cb:aa:da:19:1a:
        83:23:82:f9:c1:f6:99:0d:93:e1:f3:7f:3f:7a:52:67:75:0e:
        43:8a:d0:5d:f2:d4:01:18:53:ad:d9:79:59:75:79:1b:cb:34:
        68:dd:cb:9c:b2:8c:8d:ca:7f:66:8a:e8:98:f7:3e:35:49:25:
        f0:8a:d7:82:1b:a5:bc:e5:42:ba:9e:4f:6a:6e:1c:88:c0:fc:
        93:2a:8f:bc:e5:e0:e3:29:b8:8a:79:1b:99:60:65:71:d7:64:
        cd:b4:e8:7c:2c:2e:06:f2:f5:3a:d9:61:08:96:ee:ba:5a:7c:
        3c:2e:42:cc:b6:a4:5e:82:84:0a:81:63:67:78:00:60:44:09:
        f8:9a:4d:d2:72:e2:f3:89:b7:4f:02:88:99:a3:c0:b0:d5:50:
        12:71:bf:af:c5:29:29:43:37:0d:cd:5f:dd:03:7d:5c:eb:5d:
        e1:fe:4b:52:18:3e:55:4e:81:7b:e4:32:ef:79:0f:d8:34:75:
        36:3f:e8:e0:bd:d5:cd:df:b2:d1:28:bb:93:56:39:12:65:f5:
        8d:7c:61:1f:83:6c:a3:7a:fa:ed:0a:7e:a6:51:99:97:77:11:
        81:57:3a:33:34:71:3c:60:1d:2d:5b:04:c3:82:b5:6c:fe:43:
        e8:57:2b:e7:4d:e4:40:3a:28:4c:09:bc:c2:d7:d3:1e:2a:ae:
        e9:3b:5d:e9:5e:18:c4:b2:5f:c1:a3:87:82:94:98:43:f5:cb:
        e7:81:c6:1b:8a:95:ff:8c:2e:d6:6e:e4:f9:bb:d3:27:15:0c:
        4a:10:40:f9:96:86:b1:a3:8d:41:2d:0c:16:9a:3c:91:3b:e6:
        8d:00:3a:77:f0:00:95:a6:44:70:45:e0:e7:5d:93:0b:d1:b8:
        39:60:be:eb:61:45:a7:fe:da:93:dd:0f:b0:86:a3:b3:96:c7:
        2b:78:c9:ab:42:0e:a4:24:6c:11:f3:e2:8e:61:df:cb:ec:1a:
        c6:86:de:65:de:72:ed:ee:44:d1:55:3b:be:d0:14:ad:67:f3:
        7a:32:bb:1f:02:c3:bb:de

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 3296431 (0x324caf)
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: O=Huawei, CN=Huawei RSA Equipment Root CA 2
        Validity
            Not Before: Jul 31 13:01:18 2021 GMT
            Not After : Jul 31 13:01:18 2071 GMT
        Subject: O=Huawei, CN=Huawei RSA Equipment Root CA 2
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (4096 bit)
                Modulus:
                    00:c2:de:10:bf:38:d5:b6:3a:99:8c:7d:68:c0:74:
                    91:81:53:23:f9:c4:c2:b4:7e:54:b4:08:5e:72:de:
                    f3:50:49:75:09:5c:74:76:0d:95:3e:a8:f2:a8:51:
                    3e:10:a6:6e:30:ca:27:36:6a:20:9e:92:26:df:10:
                    54:d8:ff:3b:b4:12:35:ba:a4:92:a8:5c:6d:92:70:
                    19:f6:a7:04:a1:5f:cb:47:bc:a4:f5:84:6d:ec:70:
                    27:ae:f0:1f:89:6a:2e:05:8d:ee:58:c5:6f:57:2b:
                    74:59:ea:f6:39:c8:72:6e:5e:85:62:0b:2b:36:83:
                    9a:90:56:87:95:8e:f1:bc:9d:93:36:7b:11:4a:d0:
                    4f:10:44:4e:88:43:76:fb:dd:71:55:83:5c:57:41:
                    b2:b4:4d:db:e0:da:0f:3a:63:00:49:e0:4e:08:0c:
                    f6:69:7b:c9:03:8a:76:34:ce:c1:75:ac:d4:10:24:
                    68:39:ea:f6:7b:ed:eb:4a:e7:61:1c:06:7b:8c:48:
                    11:47:0f:bc:27:9d:0f:88:1c:b9:ae:4f:01:f5:87:
                    39:0a:71:7c:b9:55:46:78:a5:2e:9e:81:29:14:ae:
                    c0:de:b4:9e:85:b4:00:9c:94:55:dd:ee:bd:a7:37:
                    05:21:13:7c:f9:28:65:ce:a3:b3:e7:5d:6c:8c:d6:
                    ee:8e:22:72:56:cd:9f:4d:e0:1a:0c:21:d9:36:7d:
                    ef:bd:32:47:d3:08:aa:3c:03:ec:63:e6:67:46:43:
                    2e:c6:9c:f5:a8:ce:ff:2a:52:5c:97:5d:d1:b9:47:
                    6d:bc:ac:df:25:64:bf:ea:62:4c:78:2a:d9:29:67:
                    38:69:ee:a4:bd:92:91:55:1a:fd:da:ad:1a:5a:09:
                    75:f2:7d:c1:d4:7b:f0:f2:6b:ee:66:4a:fd:e0:9f:
                    cf:3d:d8:b8:4c:63:57:ad:c8:2e:53:a8:93:78:7a:
                    9d:09:b7:87:ec:aa:20:07:7a:d4:b8:ff:2c:b1:7c:
                    d5:73:8b:46:5a:71:1d:66:48:30:9d:3b:21:bb:e7:
                    6a:6f:ef:78:03:54:8e:c1:f2:a7:ff:4b:4d:3c:18:
                    32:75:26:7d:6b:00:20:e1:c9:9b:88:d9:5c:4d:de:
                    b8:de:66:20:84:0a:83:4e:fa:fe:bd:96:56:42:33:
                    a2:32:84:63:d4:0b:90:c3:70:27:4c:59:a3:b3:ed:
                    a4:31:ad:b0:f7:e3:30:13:d5:ad:fe:5e:63:d0:45:
                    5b:49:08:47:8f:54:20:f3:01:c9:7f:81:fe:d5:ad:
                    04:6a:15:e2:cd:c4:31:d0:ca:ba:4f:28:5f:a8:a9:
                    7c:00:49:3f:5b:86:8c:ac:36:85:f1:f6:a2:4e:40:
                    89:fa:77
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Basic Constraints: critical
                CA:TRUE
            X509v3 Subject Key Identifier: 
                63:88:0A:64:93:C6:3E:AC:15:6D:77:01:8E:FF:E9:10:2F:0B:25:34
            X509v3 Key Usage: critical
                Certificate Sign, CRL Sign
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        49:af:93:50:54:13:90:a3:8b:eb:1c:6e:24:5b:81:f5:56:f7:
        b0:40:1c:ea:c7:57:1d:57:36:d1:de:fd:e2:e9:af:96:93:ae:
        10:f0:47:13:5f:4b:6c:2c:69:05:fc:aa:f9:ae:19:07:f2:39:
        71:b2:ab:69:06:55:a8:3f:62:83:b6:32:53:7c:72:ae:82:bd:
        ec:e5:52:69:6e:7a:8c:dc:a1:0a:d3:68:56:fd:4d:a1:c9:f0:
        26:90:47:c4:49:4a:14:1f:f8:60:5e:2c:04:4d:5d:86:d2:2e:
        1c:eb:1f:35:b3:bc:de:25:a7:4e:8b:25:92:1c:e7:f0:fa:1c:
        af:ac:5d:e5:64:f3:b3:98:42:ba:d4:f5:05:54:51:5d:51:5a:
        e7:3a:8e:17:27:63:40:2f:27:5d:75:d1:df:cf:db:a3:3f:4d:
        45:c0:82:1d:65:1f:3a:e5:06:94:5a:3a:47:f7:e8:14:23:3a:
        fa:d6:7a:09:a1:e1:6a:50:1e:15:0a:53:56:45:db:48:c8:19:
        23:f6:42:82:14:ec:00:13:45:59:2f:d6:a7:cd:71:a9:c4:32:
        a0:cc:b9:b4:b0:bc:b3:e2:c5:54:3a:0c:63:06:86:18:a6:00:
        96:4d:7c:ce:a8:a7:fb:53:32:0a:0c:2b:76:50:cb:50:1c:7b:
        8c:03:64:8d:48:55:e7:e6:6b:5f:f9:0d:35:ff:9e:a0:89:93:
        f6:47:3a:4c:42:f5:14:a9:87:69:38:e3:a4:05:b4:ed:5a:e3:
        f9:e6:41:c8:af:2f:50:b7:07:69:f1:6f:0b:11:00:06:67:cb:
        18:e8:2e:0d:25:fb:8f:cf:93:af:2f:88:37:2a:35:d1:f4:df:
        fc:3c:af:c8:5d:48:e4:90:5c:cb:dc:f1:eb:8f:67:97:b8:18:
        b4:31:0d:13:ae:7f:ae:a5:99:55:33:c9:f7:d0:84:39:9f:cc:
        74:26:1a:c8:88:84:18:5a:87:fe:25:30:0c:03:7d:7b:44:ce:
        eb:f6:98:5a:af:e3:20:2e:ac:5b:4a:06:ad:5b:09:34:fd:7a:
        c4:40:85:83:45:d6:74:98:f2:ed:fe:92:d0:76:90:5b:e9:5f:
        cf:20:74:56:02:5d:f2:bf:66:60:65:7f:ba:21:61:d2:95:5b:
        52:6f:e7:c4:8c:be:f7:08:c6:87:cd:dc:8c:25:eb:11:c9:f8:
        7c:63:67:50:a6:f4:6c:2e:14:8b:84:86:8d:84:4f:18:30:96:
        76:10:ad:c2:a5:6e:12:f3:7c:8d:42:2f:18:9f:32:90:71:66:
        71:90:12:6b:e4:21:74:46:bd:90:f5:f5:25:2c:54:2a:0b:a9:
        9c:53:d4:00:4c:bd:c9:16

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            76:6f:8b:55:df:52:6c:16:0d:8d:97:33:0d:e8:ea:96:7e
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=CN, O=Huawei, CN=Huawei Equipment CA
        Validity
            Not Before: Oct 17 08:22:14 2016 GMT
            Not After : Oct 11 08:22:14 2041 GMT
        Subject: C=CN, O=Huawei, CN=Huawei Enterprise Network Product CA
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:ac:17:cf:4d:fe:ef:c9:df:80:18:ee:25:f7:9c:
                    bb:dd:5f:74:e8:e9:a2:fa:6a:90:d5:cc:23:80:92:
                    16:86:49:c3:95:e2:6f:e4:12:1d:58:3a:e3:c6:52:
                    56:fd:52:6b:f8:ea:80:5a:83:a7:79:8c:36:2e:88:
                    ba:9a:01:3c:5a:73:3d:23:3a:7f:cb:59:81:a2:5b:
                    b3:d1:77:8e:d5:56:4d:0b:e2:e7:0b:fe:b5:56:9a:
                    6d:dc:d2:90:2a:27:56:43:ad:ce:89:54:76:2d:65:
                    cb:7d:79:6d:91:14:04:62:3d:70:e9:8c:c7:90:f4:
                    ca:b6:e5:1f:90:76:86:4d:dc:40:bc:e4:ae:48:d7:
                    cf:52:15:dd:1c:46:b6:94:dd:71:81:06:31:f6:8c:
                    c6:95:a0:5b:71:38:1a:f1:fa:f6:6e:f9:c7:1d:cd:
                    0f:cf:0b:34:4e:76:3d:8c:33:b5:e7:be:21:26:92:
                    a7:68:ca:55:bc:f2:9c:7f:9e:29:22:9b:de:f9:22:
                    3d:7f:0e:1a:55:87:73:bb:e0:60:eb:3c:1c:3d:19:
                    82:a8:6f:1d:f3:2b:10:e7:53:d7:76:a8:3f:d6:63:
                    97:1a:1a:d6:50:46:75:ca:0d:c4:d0:6e:3e:dd:d6:
                    9f:e8:13:6b:a4:be:15:41:78:64:1d:55:b9:95:e1:
                    6c:f1
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Authority Key Identifier: 
                2A:F8:10:59:27:80:35:1F:A7:7C:BA:3B:9F:2A:E4:4A:AA:9B:92:EA
            X509v3 Certificate Policies: 
                Policy: X509v3 Any Policy
                  CPS: https://support.huawei.com/support/pki
            X509v3 Basic Constraints: 
                CA:TRUE, pathlen:0
            X509v3 Key Usage: critical
                Certificate Sign, CRL Sign
            X509v3 Subject Key Identifier: 
                73:9F:C7:5F:E1:96:A8:0E:79:71:79:DC:69:CB:0A:F1:BC:E0:F4:E5
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        56:a1:67:8a:ad:64:75:09:f1:0e:95:04:ae:0a:57:9d:12:04:
        4b:ef:f5:1b:b0:fd:ee:01:62:d2:13:61:48:26:69:a2:44:c2:
        f0:1d:f6:03:8c:f2:50:a4:21:ad:3f:05:08:a8:62:7f:f4:1f:
        e4:50:7a:aa:17:88:53:82:b2:20:83:9b:aa:39:7a:f0:0d:74:
        bc:51:12:2f:e9:43:2e:cd:07:d3:0f:46:62:24:2f:0b:66:e2:
        fb:9e:29:4f:d9:f2:a4:2c:8f:bf:fe:28:6c:15:6d:9f:55:4d:
        fc:78:d6:b4:46:b4:5f:a3:b8:92:5f:50:9d:0a:af:33:9c:e7:
        56:e8:3c:4d:a2:55:bd:ed:95:78:06:0c:ce:10:70:89:bd:2c:
        54:9a:1a:d8:1d:50:4a:4d:e0:47:db:a9:e2:93:89:14:d8:84:
        d0:fc:0a:8a:1b:4d:6e:e2:76:59:0e:08:21:a1:04:ec:32:bc:
        48:5b:e8:c8:86:f1:c9:59:25:24:5c:00:89:d7:21:58:0a:ce:
        d6:95:03:71:6e:9e:cf:86:1a:25:59:37:77:c4:26:f0:c1:d9:
        0a:23:a4:24:d8:0f:72:33:3c:3a:e7:24:ff:9c:49:99:69:89:
        38:36:1f:37:a1:b8:ad:11:d7:77:94:65:c1:f5:ea:bd:1c:6a:
        9d:9b:92:01:c9:f0:c5:b1:03:e1:63:24:5f:3f:6c:7a:d9:2b:
        96:cf:97:77:9a:07:c1:3b:e5:dd:61:fd:26:16:db:98:a8:5d:
        8f:0b:fd:66:64:bd:13:f0:71:20:0b:a3:c3:9d:11:00:6a:00:
        08:0e:bb:ea:97:9b:25:8e:18:9d:71:27:68:a6:01:01:06:f1:
        7b:d9:c4:74:9c:21:a5:3c:e0:5a:c2:3d:0e:68:ab:2b:48:71:
        b8:2f:ba:5c:3c:b2:91:aa:88:ba:57:44:ed:1d:93:35:3f:49:
        aa:e3:20:bf:dc:aa:b7:e7:2c:7f:8f:ad:72:07:e1:05:94:10:
        25:19:44:9c:bb:a5:23:6a:0d:6c:41:3d:09:10:2e:a7:2f:67:
        b4:00:63:7b:62:9f:92:d1:c7:05:69:67:98:34:78:a6:ee:43:
        40:50:1f:8a:32:2d:70:3b:53:5c:68:2e:ec:41:3e:51:01:9c:
        d1:eb:c0:cb:2b:ba:9a:67:c1:a8:2a:a6:b5:6c:c7:e6:c7:8e:
        37:ee:31:6f:33:2f:4a:c5:6a:2e:a9:14:de:c0:5b:ba:69:f2:
        63:77:69:c1:bb:8a:eb:22:fc:f9:a0:2b:58:1d:90:44:a8:ff:
        40:a3:63:ce:57:25:76:b4:7e:0b:ba:e7:85:6f:18:0e:cb:62:
        a5:7d:51:66:d0:46:d6:3a

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            76:25:60:02:2a:47:5e:ec:a6:2b:7c:68:ac:9b:3f:29:86
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=CN, O=Huawei, CN=Huawei Equipment CA
        Validity
            Not Before: Dec  6 07:34:23 2011 GMT
            Not After : Nov 28 07:34:23 2041 GMT
        Subject: C=CN, O=Huawei, CN=Huawei Equipment CA
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (4096 bit)
                Modulus:
                    00:a2:89:84:27:0b:f3:29:f6:86:e6:02:75:e6:bb:
                    f3:63:ea:b7:1c:4a:41:10:25:79:59:8a:93:af:f2:
                    d2:23:be:bd:01:f0:e6:e9:15:49:d4:fa:a2:e8:8d:
                    95:18:94:d9:97:1f:c4:60:46:01:41:d6:c0:52:c8:
                    eb:86:8a:23:f4:b8:db:49:d2:53:cb:6f:29:6c:73:
                    ed:9f:af:64:65:b7:fa:9b:62:cd:68:40:6c:fe:a0:
                    d9:7e:51:d0:0e:b6:6f:e5:3f:38:20:50:e5:55:b2:
                    dd:79:3a:f7:f4:61:fe:8b:43:70:90:6a:53:76:54:
                    95:a0:2a:91:54:b9:d0:ca:59:0d:9f:cd:b1:53:e5:
                    84:9f:be:11:71:be:db:d6:7e:07:67:b4:a0:09:b7:
                    7b:05:be:42:ab:f5:0c:3e:d0:46:0d:a5:08:b0:e4:
                    40:0b:78:b5:82:65:26:14:ec:0f:77:f6:9b:aa:61:
                    1e:9a:34:0e:38:ed:2d:4a:f1:28:16:a1:ab:fc:d8:
                    fe:14:63:fc:a4:2d:78:dc:81:37:82:9e:f4:51:b5:
                    48:1a:d6:07:48:c2:6e:5d:fe:f4:65:07:98:a5:e7:
                    0b:29:18:b2:de:b3:84:a8:9b:35:18:ae:f9:ef:1e:
                    2a:39:e7:93:59:3e:9b:e6:a4:85:cd:a2:5c:2f:61:
                    6e:68:a4:0c:98:cc:4d:39:a5:54:8e:98:77:ff:45:
                    8f:dd:1e:da:3c:5d:67:b1:38:9a:bf:50:01:41:33:
                    28:87:e0:d4:f8:71:9a:56:8d:85:91:ed:6f:46:c5:
                    15:c0:a6:64:2b:ac:b5:ed:7b:50:85:fc:8c:d7:58:
                    13:00:da:d4:8b:d1:69:d1:27:3e:47:45:c2:b3:b0:
                    e0:ba:16:4b:22:aa:c6:2c:b4:58:dc:08:4e:c9:ec:
                    d8:9c:af:70:70:ab:91:6b:66:2a:86:49:d2:e6:2d:
                    19:fd:ed:7a:95:95:67:4d:df:51:d7:d7:a7:f3:46:
                    16:4c:88:e9:2f:41:ef:ae:61:3f:81:5d:b8:54:d5:
                    f6:48:87:a4:51:00:7d:d5:d4:03:e8:6d:59:42:5e:
                    1e:4f:0e:af:02:6b:87:42:94:73:47:62:9e:51:3f:
                    43:db:e7:30:68:c1:3a:81:cd:2b:fb:b2:c1:eb:35:
                    c7:90:b1:60:de:36:35:fd:b7:9f:4d:c2:f8:9a:22:
                    55:c8:94:f8:96:10:42:5c:db:65:ed:32:6e:2c:73:
                    ff:bc:9a:03:85:30:d5:eb:e0:55:ae:f2:f7:46:d9:
                    f8:11:a5:e5:89:3b:41:34:df:90:fa:4c:29:6e:e1:
                    2a:36:1a:53:7f:7c:87:1c:a7:9c:15:60:05:85:d5:
                    68:71:49
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Basic Constraints: 
                CA:TRUE
            X509v3 Key Usage: 
                Certificate Sign, CRL Sign
            X509v3 Subject Key Identifier: 
                2A:F8:10:59:27:80:35:1F:A7:7C:BA:3B:9F:2A:E4:4A:AA:9B:92:EA
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        40:c7:64:9e:2f:bf:1d:a4:3e:61:c4:b0:dd:ce:24:e7:85:da:
        75:7a:72:18:c5:d5:06:5c:53:09:68:8e:15:2d:22:ff:63:b5:
        ef:66:72:2e:6a:96:5b:d8:45:4e:66:89:af:6b:61:98:8f:eb:
        55:df:76:bc:0e:45:ff:10:74:97:08:eb:74:20:ac:88:fb:32:
        d9:c9:50:b7:14:52:49:34:4a:3f:45:cf:aa:ec:c1:f8:65:6a:
        ab:51:8c:3a:76:96:38:b3:0a:5f:5b:99:4c:ca:65:39:78:d2:
        6f:d2:31:b2:2d:6d:2c:98:5e:f2:ab:81:23:d3:c2:03:e8:fc:
        ca:da:96:aa:49:72:ea:14:91:ff:89:0d:92:0f:dc:06:88:cb:
        eb:de:72:4b:09:c2:6a:05:21:cd:0e:ab:03:fb:b8:d0:b9:e6:
        4a:fc:93:1e:f4:78:7d:d0:29:a8:80:53:ef:02:2f:73:7b:82:
        d3:05:04:bd:8c:00:b9:64:de:f1:44:20:21:00:85:6b:cc:1a:
        b6:0d:b5:2c:c1:50:42:4d:4e:ca:71:fa:a5:71:11:10:6a:c4:
        92:26:06:c3:c6:0f:b2:e1:2c:e6:8f:95:2c:df:6d:4e:82:0f:
        70:bc:1b:dd:98:ee:be:27:09:c4:3e:48:e4:2f:e2:4e:93:4d:
        19:fc:a4:e8:f9:73:4a:32:dd:9d:bc:0d:e6:46:bb:34:97:34:
        fb:16:ba:bd:da:45:5c:04:d2:63:98:f1:c2:c1:92:08:a8:ec:
        04:23:a8:80:26:75:ba:39:be:27:bb:5f:5c:ec:87:21:1c:03:
        b1:5a:13:59:89:74:d4:b7:59:50:af:94:cc:13:17:0c:a0:ab:
        5d:ec:bc:b4:39:33:01:8f:49:ec:6c:1e:e7:59:e4:93:f9:e6:
        d1:d7:91:0c:8f:46:ac:5d:84:5a:fe:83:10:f0:e6:88:af:fc:
        b9:71:02:90:7c:e4:cc:04:7d:34:ec:fe:ec:d2:e8:54:96:01:
        40:b4:20:0c:56:c9:9d:cc:ca:d5:40:00:be:d2:8b:06:69:fd:
        e3:83:58:1c:0b:5c:44:e5:20:a7:2e:fd:f7:61:4d:f3:79:ab:
        53:26:f5:38:cc:8c:99:83:12:8a:b3:20:34:63:0e:e5:51:e2:
        ff:f7:73:34:71:30:e9:0a:b5:41:c9:b7:68:b1:7a:28:9d:87:
        d8:63:63:a6:9e:eb:af:41:aa:90:51:5b:47:79:77:23:68:cf:
        2f:88:25:c5:28:ec:68:36:f8:5d:40:85:32:f0:bc:f8:98:94:
        92:ec:34:66:59:be:a5:df:86:99:69:c1:c0:27:be:da:06:26:
        f0:23:f9:09:0b:89:6e:33

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            11:15:c1:7b:e8:50:7b:cd:9e:6b:46:96:87:f9:d4:1e:ad
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=CN, O=Huawei, CN=Huawei Equipment CA
        Validity
            Not Before: Sep 14 07:49:02 2021 GMT
            Not After : Nov 27 07:49:02 2041 GMT
        Subject: O=Huawei, CN=Huawei RSA Equipment Root CA 2
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (4096 bit)
                Modulus:
                    00:c2:de:10:bf:38:d5:b6:3a:99:8c:7d:68:c0:74:
                    91:81:53:23:f9:c4:c2:b4:7e:54:b4:08:5e:72:de:
                    f3:50:49:75:09:5c:74:76:0d:95:3e:a8:f2:a8:51:
                    3e:10:a6:6e:30:ca:27:36:6a:20:9e:92:26:df:10:
                    54:d8:ff:3b:b4:12:35:ba:a4:92:a8:5c:6d:92:70:
                    19:f6:a7:04:a1:5f:cb:47:bc:a4:f5:84:6d:ec:70:
                    27:ae:f0:1f:89:6a:2e:05:8d:ee:58:c5:6f:57:2b:
                    74:59:ea:f6:39:c8:72:6e:5e:85:62:0b:2b:36:83:
                    9a:90:56:87:95:8e:f1:bc:9d:93:36:7b:11:4a:d0:
                    4f:10:44:4e:88:43:76:fb:dd:71:55:83:5c:57:41:
                    b2:b4:4d:db:e0:da:0f:3a:63:00:49:e0:4e:08:0c:
                    f6:69:7b:c9:03:8a:76:34:ce:c1:75:ac:d4:10:24:
                    68:39:ea:f6:7b:ed:eb:4a:e7:61:1c:06:7b:8c:48:
                    11:47:0f:bc:27:9d:0f:88:1c:b9:ae:4f:01:f5:87:
                    39:0a:71:7c:b9:55:46:78:a5:2e:9e:81:29:14:ae:
                    c0:de:b4:9e:85:b4:00:9c:94:55:dd:ee:bd:a7:37:
                    05:21:13:7c:f9:28:65:ce:a3:b3:e7:5d:6c:8c:d6:
                    ee:8e:22:72:56:cd:9f:4d:e0:1a:0c:21:d9:36:7d:
                    ef:bd:32:47:d3:08:aa:3c:03:ec:63:e6:67:46:43:
                    2e:c6:9c:f5:a8:ce:ff:2a:52:5c:97:5d:d1:b9:47:
                    6d:bc:ac:df:25:64:bf:ea:62:4c:78:2a:d9:29:67:
                    38:69:ee:a4:bd:92:91:55:1a:fd:da:ad:1a:5a:09:
                    75:f2:7d:c1:d4:7b:f0:f2:6b:ee:66:4a:fd:e0:9f:
                    cf:3d:d8:b8:4c:63:57:ad:c8:2e:53:a8:93:78:7a:
                    9d:09:b7:87:ec:aa:20:07:7a:d4:b8:ff:2c:b1:7c:
                    d5:73:8b:46:5a:71:1d:66:48:30:9d:3b:21:bb:e7:
                    6a:6f:ef:78:03:54:8e:c1:f2:a7:ff:4b:4d:3c:18:
                    32:75:26:7d:6b:00:20:e1:c9:9b:88:d9:5c:4d:de:
                    b8:de:66:20:84:0a:83:4e:fa:fe:bd:96:56:42:33:
                    a2:32:84:63:d4:0b:90:c3:70:27:4c:59:a3:b3:ed:
                    a4:31:ad:b0:f7:e3:30:13:d5:ad:fe:5e:63:d0:45:
                    5b:49:08:47:8f:54:20:f3:01:c9:7f:81:fe:d5:ad:
                    04:6a:15:e2:cd:c4:31:d0:ca:ba:4f:28:5f:a8:a9:
                    7c:00:49:3f:5b:86:8c:ac:36:85:f1:f6:a2:4e:40:
                    89:fa:77
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Authority Key Identifier: 
                2A:F8:10:59:27:80:35:1F:A7:7C:BA:3B:9F:2A:E4:4A:AA:9B:92:EA
            X509v3 Subject Key Identifier: 
                63:88:0A:64:93:C6:3E:AC:15:6D:77:01:8E:FF:E9:10:2F:0B:25:34
            X509v3 Basic Constraints: critical
                CA:TRUE
            X509v3 Key Usage: critical
                Certificate Sign, CRL Sign
            X509v3 CRL Distribution Points: 
                Full Name:
                  URI:https://support.huawei.com/support/pki/RootCA_crl.crl
            1.3.6.1.4.1.2011.201.1.2.1: 
                ..
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        7d:ce:58:56:d9:be:04:a0:df:58:be:42:57:ce:bc:a1:2c:aa:
        d4:73:75:0c:8b:7b:95:5b:ac:24:e4:23:eb:fb:5c:b6:f7:97:
        84:d3:fe:20:c3:b0:51:d9:50:e9:11:82:60:9c:5a:d9:92:93:
        59:22:eb:0f:10:7f:b5:5e:4b:c7:ca:32:f5:a9:64:38:4a:9a:
        8a:82:5b:93:a0:fe:f4:26:77:84:1c:21:ad:8c:cf:e1:4f:92:
        c9:af:0e:a1:3c:98:06:0d:a1:60:c2:65:b7:00:dd:ce:b1:e1:
        31:28:70:43:f4:89:53:5c:89:a4:1f:a8:42:93:65:48:1b:4a:
        8d:dc:7e:83:ff:ac:50:1d:6c:96:0f:e0:62:1d:cf:0e:c7:5d:
        1e:a3:cb:ff:2d:07:f7:17:be:77:e1:fe:60:cd:18:62:c8:d0:
        38:a9:9c:3e:eb:0b:35:2c:36:3f:24:af:40:a8:56:72:cc:40:
        02:4a:d2:b2:df:e9:e8:b3:0d:1e:29:33:f3:b8:e4:dc:8b:73:
        08:54:f6:46:5d:60:71:71:5c:b9:ad:62:fd:d6:3f:cb:25:f2:
        16:a1:c8:d3:3a:af:25:da:03:3c:b9:58:83:eb:fb:bd:29:01:
        07:2d:88:cc:e0:b0:1e:79:00:6c:94:9d:b3:af:2b:70:4f:c1:
        3d:20:5f:72:af:0e:42:a2:6b:21:8a:5b:4c:ac:30:68:6f:5f:
        24:05:42:03:d0:2a:9f:30:9b:b3:5b:11:c7:0a:70:b7:12:ab:
        1e:b9:51:15:49:60:35:53:6d:98:68:6a:4c:3b:b6:7d:9d:20:
        66:48:27:60:16:a8:a5:ed:b3:67:a0:39:69:60:0c:c7:cc:02:
        20:46:d6:79:b8:c6:dd:44:53:50:86:be:73:45:c1:f2:18:b1:
        64:b2:b0:d6:01:91:28:2b:4e:19:0c:76:84:dc:5a:13:ab:01:
        25:34:6e:53:f1:99:a5:3b:3c:5c:54:9c:88:46:5d:b9:a4:19:
        dc:98:18:61:b4:0e:e0:cd:70:2e:4c:49:e3:54:7c:4d:63:eb:
        0f:1e:d7:04:e8:66:9c:e5:07:91:c7:c2:ea:11:a2:58:70:e0:
        93:8a:52:ba:c0:b2:0b:46:1c:05:55:61:6b:a5:45:54:26:09:
        98:c8:33:6e:60:b2:74:a1:d3:be:ea:9a:54:01:d7:26:db:ea:
        23:82:c8:1e:03:17:68:e9:31:33:c0:c8:da:73:79:f1:c4:b6:
        b3:8f:b6:da:90:6e:91:69:69:13:14:16:2d:95:ea:ce:26:9f:
        1f:47:68:35:03:c0:b8:01:73:d7:ad:5a:5f:d1:1e:f6:40:a9:
        ba:c1:db:e9:bc:e5:b3:be

```

**Table 1** Description of the **display pki certificate device** command output
| Item | Description |
| --- | --- |
| Certificate | Information about a certificate. |
| Serial Number | Serial number of a certificate. |
| Signature Algorithm | Signature algorithm of a certificate. |
| CA | Whether the CA can be trusted. |
| Validity | Validity period of a certificate. |
| Subject | Subject of a certificate. The subject includes the following attributes:   * C: country code of a PKI entity. * ST: name of the state or province to which a PKI entity belongs.   -L: geographic area where a PKI entity is located.   * O: organization to which a PKI entity belongs. * OU: department to which a PKI entity belongs. * CN: common name of a PKI entity. |
| Subject Public Key Info | Information about the public key of a certificate. |
| Public Key Algorithm | Public key algorithm. |
| X509v3 extensions | X.509v3 certificate extensions. |
| X509v3 Key Usage | X.509v3 key usage. |
| X509v3 Basic Constraints | Basic constraints. |
| X509v3 Subject Key Identifier | Identifier of a subject key. |
| X509v3 Authority Key Identifier | Authority key identifier. |
| X509v3 CRL Distribution Points | CRL distribution points. |
| X509v3 Certificate Policies | Certificate policies. |
| Full Name | Full name of the CRL distributor. |
| CPU ID | CPU ID information in the certificate. |
| NP ID | NP module ID in the certificate. |
| Data | Data of a certificate. |
| Version | Version of a certificate. |
| Issuer | Issuer of a certificate. |
| Public-Key | Public key. |
| Modulus | Key modulus. |
| Exponent | Key exponent. |