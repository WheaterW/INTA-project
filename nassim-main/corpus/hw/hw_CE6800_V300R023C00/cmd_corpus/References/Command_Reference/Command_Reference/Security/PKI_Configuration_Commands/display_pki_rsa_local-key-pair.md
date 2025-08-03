display pki rsa local-key-pair
==============================

display pki rsa local-key-pair

Function
--------



The **display pki rsa local-key-pair** command displays the public key in the RSA key pair.




Format
------

**display pki rsa local-key-pair** { **pem** | **pkcs12** } *file-name* [ **password** *password* ]

**display pki rsa local-key-pair** [ **name** *key-name* ] **public**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **pem** | Indicates that the file format is PEM. | - |
| **pkcs12** | Indicates that the file format is PKCS12. | - |
| *file-name* | Specifies the name of the file that contains the RSA key pair. | The file name must already exist. |
| **password** *password* | Specifies the decryption password of RSA key pair. The value must be the same as the password set when it was exported. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **name** *key-name* | Specifies the RSA key pair name. | The RSA key pair name must already exist. |
| **public** | Displays information about public keys. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command shows information about the RSA key pair and public key, including key pair creation time, key pair name, whether the key can be exported, and public key information.If key-name is not specified, all RSA key pairs and public keys are displayed. If key-name is specified, the specified RSA key pair and public key are displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all RSA key pairs.
```
<HUAWEI> display pki rsa local-key-pair public
Info: It will take a few seconds or more. Please wait a moment.
Total Number: 2
=====================================================
Time of Key pair created: 09:42:42  2023/5/29
Key Name: ca .key
Key Modules: 3072 bits
Key Exportable: No
=====================================================
RSA Public-Key: (3072 bits)
Modulus:
    00:8e:29:b9:f1:94:39:7c:a8:16:47:9f:96:eb:61:
    98:63:68:95:57:fe:87:99:0d:d0:e0:db:12:0b:58:
    81:0f:b7:66:10:f8:1e:6a:58:0f:45:b5:87:f1:25:
    c8:ee:73:47:c7:ed:a3:f5:d9:ed:72:a4:04:b8:8d:
    49:8a:e8:b5:1d:3f:b6:04:93:96:ae:e6:97:b8:3a:
    ac:60:f4:4d:02:b0:85:41:73:4d:47:f1:23:c6:71:
    53:05:2d:c6:22:b7:2a:00:74:f2:bb:eb:8e:1d:c7:
    6b:cc:a0:64:f8:2b:51:ba:94:a2:55:a6:05:a9:97:
    61:21:f6:96:73:9a:5e:a6:ab:ee:da:25:32:ab:23:
    69:86:bf:c9:26:5c:9d:c4:f7:ad:d3:02:9f:89:3e:
    e8:1a:0b:fc:7b:6d:8b:5a:b0:9e:82:2d:2f:f4:7e:
    b3:fc:9b:9c:59:9c:e3:48:37:7b:6a:c2:b6:85:e9:
    10:99:39:22:94:9b:c0:5f:89:28:b5:78:16:b2:49:
    5b:7e:ea:cb:57:f7:4a:11:29:88:06:2f:7c:09:07:
    e8:d0:ff:24:13:10:99:51:e8:33:50:88:34:78:92:
    6f:37:30:7e:23:e8:fb:24:bb:02:0d:e2:c7:23:61:
    ae:aa:80:35:40:47:15:f4:68:6b:92:ce:62:2d:4d:
    fa:fc:71:07:40:45:26:a4:f0:e1:ad:14:b0:9d:23:
    42:57:58:f3:96:e0:8b:3b:8e:7c:da:2b:e8:da:a9:
    a5:3a:3f:37:ed:06:89:48:36:24:e1:21:75:fa:04:
    c0:07:83:e6:f2:18:ed:7c:c1:c5:88:13:71:d8:b1:
    62:5b:d4:c3:7b:c1:8a:dd:dd:ae:90:fd:c6:6b:ac:
    69:e5:7f:65:fd:88:18:0a:e7:8e:36:d9:16:60:49:
    1a:ef:62:d3:d2:6d:4e:22:67:b2:35:2f:c9:c7:d5:
    df:6d:74:b0:e4:38:56:8c:d8:e2:76:92:ff:2b:74:
    ed:ab:92:dc:f2:27:9b:63:fd:2f
Exponent: 65537 (0x10001)
=====================================================
Time of Key pair created: 09:42:44  2023/5/29
Key Name: local .key
Key Modules: 3072 bits
Key Exportable: No
=====================================================
RSA Public-Key: (3072 bits)
Modulus:
    00:90:55:7a:19:4e:9f:f7:be:e7:b5:98:fe:fc:2b:
    7c:65:fa:fd:8b:6b:96:2c:42:5b:7d:fd:d4:05:f2:
    4a:f3:ae:ef:58:23:c2:24:fe:e0:6f:ae:b3:47:79:
    d6:55:91:f9:fb:ad:40:66:b4:a0:7b:3b:98:0d:9a:
    df:9d:44:a1:9b:f8:95:a8:d3:82:24:c3:99:1e:0c:
    79:6a:26:66:b2:a4:c4:9d:2f:e7:32:37:67:78:83:
    b3:f5:7a:f2:d4:81:e9:ef:92:3a:43:57:4a:5e:06:
    c7:71:6a:1d:f2:6f:39:59:49:78:15:43:6a:43:6d:
    55:49:a9:e1:4b:57:5a:b6:d8:e9:d7:f6:fd:a6:f4:
    39:df:8c:24:d3:ea:cd:0a:69:8b:cc:75:6f:2a:72:
    5b:e6:bc:ab:d1:84:7d:f1:e4:77:5a:91:e1:2b:0d:
    e3:4b:36:46:44:89:9a:2e:b0:69:46:3d:9a:9e:b9:
    c4:f0:6a:1d:7c:23:6d:dc:59:d4:0b:b1:3c:45:4f:
    1c:4d:dc:4c:5b:8e:95:52:de:80:c8:89:b0:3f:9f:
    0d:c5:84:49:fe:e4:39:ec:55:f9:8b:7b:cc:fc:44:
    6b:77:6c:0b:e6:b9:78:c7:06:c7:12:ca:50:9a:ee:
    82:8b:88:bb:34:b6:19:72:eb:23:86:4a:12:09:f5:
    62:52:ea:06:21:54:86:4c:b6:4a:7c:79:76:7d:11:
    3f:cf:10:91:af:49:fc:60:bd:8b:11:fb:f3:ee:08:
    ba:3b:d3:16:c9:b5:e5:31:3f:d2:24:21:4c:c2:d1:
    3b:4c:33:42:37:2e:26:f2:f3:14:1a:6a:3c:c9:f2:
    4b:7b:4e:df:fc:f8:18:2d:25:ca:fe:69:a4:79:19:
    55:36:99:88:fd:0d:e6:71:8d:34:42:8b:52:34:7c:
    d9:9a:68:77:e1:0e:b6:86:03:0c:da:98:42:2d:74:
    94:f7:ef:53:4c:60:8c:fb:36:22:fb:6c:b2:4e:7b:
    11:c8:d9:49:a9:d0:9e:11:f3:ad
Exponent: 65537 (0x10001)

```

**Table 1** Description of the **display pki rsa local-key-pair** command output
| Item | Description |
| --- | --- |
| Total Number | Total number of keys. |
| Time of Key pair created | Time when the RSA key pair is created. |
| Key Name | Name of a key pair. It is configured using the pki rsa local-key-pair create command. |
| Key Modules | Number of bits of the key. |
| Key Exportable | Whether the key can be exported. |
| RSA Public-Key | Indicates the RSA public key. |
| Modulus | Modulus information in the key pair. |
| Exponent | Exponent information in the key pair. |