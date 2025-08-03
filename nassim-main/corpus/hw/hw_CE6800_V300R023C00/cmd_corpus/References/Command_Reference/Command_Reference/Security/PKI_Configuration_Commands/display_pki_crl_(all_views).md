display pki crl (all views)
===========================

display pki crl (all views)

Function
--------



The **display pki crl** command displays the content of the CRL in the device.




Format
------

**display pki crl** [ **realm** *realm-name* | **filename** *file-name* ]

**display pki crl realm** *realm-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **realm** *realm-name* | Specifies the name of the PKI realm to which the CRL belongs. | The value must be an existing PKI realm name. |
| **filename** *file-name* | Specifies the name of a CRL file. | The value must be the name of an imported CRL file. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command shows information about local CRL, including signature algorithm, issuer, update time, revoked certificate, CRL sequence number, and revocation time.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the CRL associated with the PKI realm.
```
<HUAWEI> display pki crl realm abc
 The x509 object type is CRL:   
Certificate Revocation List (CRL):                                              
        Version 2 (0x1)                                                         
    Signature Algorithm: sha1WithRSAEncryption                                  
        Issuer: /CN=ca_root                                                     
        Last Update: Dec 15 08:24:28 2015 GMT                                   
        Next Update: Dec 22 20:44:28 2015 GMT                                   
        CRL extensions:                                                         
            X509v3 Authority Key Identifier:                                    
                keyid:B8:63:72:A4:5E:19:F3:B1:1D:71:E1:37:26:E1:46:39:01:B6:82:C
5                         
            1.3.6.1.4.1.311.21.1:                                               
                ...                                                             
            X509v3 CRL Number:                                                  
                365                                                             
            1.3.6.1.4.1.311.21.4:                                               
151222083428Z   .                                                               
Revoked Certificates:                                                           
    Serial Number: 28C63371000000003E04                                         
        Revocation Date: Dec 15 08:34:27 2015 GMT                               
        CRL entry extensions:                                                   
            X509v3 CRL Reason Code:                                             
                Key Compromise                                                  
    Serial Number: 28C2AB44000000003E01                                         
        Revocation Date: Dec 15 08:30:35 2015 GMT                               
        CRL entry extensions:                                                   
            X509v3 CRL Reason Code:                                             
                Key Compromise                                                  
    Serial Number: 2364247C000000003D48                                         
        Revocation Date: Dec 14 07:29:05 2015 GMT                               
        CRL entry extensions:                                                   
            X509v3 CRL Reason Code:                                             
                Key Compromise                                                  
    Serial Number: 23627E0F000000003D47                                         
        Revocation Date: Dec 14 07:27:29 2015 GMT                               
        CRL entry extensions:                                                   
            X509v3 CRL Reason Code:                                             
                Key Compromise                                                  
    Serial Number: 2360F397000000003D46                                         
        Revocation Date: Dec 14 07:25:48 2015 GMT                               
        CRL entry extensions:                                                   
            X509v3 CRL Reason Code:                                             
                Key Compromise                                                        
    Signature Algorithm: sha1WithRSAEncryption                                  
         7a:71:54:d1:66:13:6f:9f:62:03:ac:9a:5f:42:10:15:87:46:                 
         e2:a1:49:0f:44:19:ce:ed:6f:c3:0e:9f:31:fe:62:d5:08:0b:                 
         a4:a7:7e:80:4d:9a:5b:a9:55:5c:1a:73:30:62:48:e1:28:0e:                 
         5b:bd:ae:04:7e:83:36:43:62:fc:f7:12:0d:f9:f6:ac:2b:be:                 
         9c:50:6c:67:19:43:12:31:67:c2:06:31:97:e1:34:75:1c:87:                 
         53:5f:e6:15:a1:33:ad:00:e7:14:68:59:05:67:28:78:a0:91:                 
         49:7b:ab:87:9f:9e:53:18:4b:54:53:1c:b7:1c:2d:3e:b3:57:                 
         63:95:1d:01:29:9e:6c:41:07:40:2d:28:d8:82:7b:d6:22:e6:                 
         0d:0c:4c:af:84:96:8e:f1:29:28:d4:9e:1c:37:3b:1b:2e:34:                 
         a7:15:e3:29:d1:c0:69:0a:7f:24:b1:ce:00:f1:b3:da:ef:8a:                 
         1b:14:36:f9:14:6c:b0:66:86:a8:92:95:fc:e3:78:aa:d6:d0:                 
         cb:4d:26:b4:bc:41:c4:47:19:d0:2a:0c:ac:c6:aa:95:c2:03:                 
         33:8a:39:45:3e:c3:ad:46:7d:8a:03:4d:08:e2:d0:9a:ae:39:                 
         fa:8d:61:d0:1c:6c:03:d4:48:2e:4d:37:60:a1:06:a4:ea:c8:                 
         0d:20:59:c2                                                            
                                                                                
Pki realm name: -                                                             
CRL file name: abc.crl

```

**Table 1** Description of the **display pki crl (all views)** command output
| Item | Description |
| --- | --- |
| The x509 object type is CRL | x509 object type is CRL. |
| Certificate Revocation List (CRL) | Information about the CRL. |
| Revocation Date | Date when the certificate was revoked. |
| Signature Algorithm | Algorithm of signature. |
| Signature Algorithm | Signature algorithm. It is configured using the enrollment-request signature message-digest-method command. |
| Last Update | Last time the CRL has been updated. |
| Next Update | Next time the CRL will be updated. |
| CRL extensions | CRL extended attribute. |
| CRL entry extensions | CRL entry extensions. |
| CRL file name | CRL file name. It is configured using the pki import-crl command. |
| X509v3 Authority Key Identifier | X509v3 authority key identifier. |
| X509v3 CRL Number | X509v3 CRL number. |
| X509v3 CRL Reason Code | Reason why CRL is revoked. |
| Revoked Certificates | Certificate that is revoked. |
| Serial Number | Serial number of the CRL. |
| Pki realm name | PKI realm name. |
| Issuer | Information of issuer. |