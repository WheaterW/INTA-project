display pki sm2 local-key-pair public
=====================================

display pki sm2 local-key-pair public

Function
--------



The **display pki sm2 local-key-pair public** command displays information about SM2 key pairs and public keys.




Format
------

**display pki sm2 local-key-pair** [ **name** *key-name* ] **public**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *key-name* | Specifies the name of the SM2 key pair that you want to view. If this parameter is not specified, information about all SM2 keys and public keys is displayed. If this parameter is specified, information about only the specified SM2 key and public key is displayed. | The value must be an existing SM2 key pair name. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command shows information about SM2 key pairs and public keys, including the creation time, key pair name, whether the key can be exported, and public key information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all SM2 key pairs.
```
<HUAWEI> display pki sm2 local-key-pair public
=====================================================
Time of Key pair created: 20:28:50  2020/9/8 
Key Name: signkey
Key Index: 0 
Key Modulus: - 
Key Exportable: Yes
=====================================================
Public-Key: (256 bit)
pub:
    04:89:2c:fe:9f:3b:52:9e:ac:34:22:1c:da:22:31:
    c7:f4:2c:84:be:96:57:64:e3:88:94:93:9e:35:c6: 
    bb:8c:fe:76:bf:89:cf:cd:e8:5d:8a:9d:01:4a:7a: 
    d2:4c:5a:54:7e:90:fd:2e:cd:22:d4:05:c8:57:0e:
    ec:fc:db:a3:6e
ASN1 OID: SM2
             
            
=====================================================
Time of Key pair created: 16:40:28  2020/9/3
Key Name: sig_privkey1 
Key Index: 1
Key Modulus: -    
Key Exportable: Yes
===================================================== 
Public-Key: (256 bit) 
pub:   
    04:89:2c:fe:9f:3b:52:9e:ac:34:22:1c:da:22:31: 
    c7:f4:2c:84:be:96:57:64:e3:88:94:93:9e:35:c6: 
    bb:8c:fe:76:bf:89:cf:cd:e8:5d:8a:9d:01:4a:7a: 
    d2:4c:5a:54:7e:90:fd:2e:cd:22:d4:05:c8:57:0e:
    ec:fc:db:a3:6e 
ASN1 OID: SM2

```

**Table 1** Description of the **display pki sm2 local-key-pair public** command output
| Item | Description |
| --- | --- |
| Time of Key pair created | Time when the SM2 key pair is created. |
| Key Name | Name of the SM2 key pair. |
| Key Index | SM2 Key pair index. |
| Key Modulus | SM2 Key modulus. |
| Key Exportable | Whether the SM2 key pair can be exported. |
| Public-Key | SM2 Public key information. |
| pub | Public key in the SM2 key pair. |