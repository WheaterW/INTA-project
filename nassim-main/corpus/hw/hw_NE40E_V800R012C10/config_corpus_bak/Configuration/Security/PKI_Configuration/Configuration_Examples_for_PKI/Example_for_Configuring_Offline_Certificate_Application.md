Example for Configuring Offline Certificate Application
=======================================================

This section provides an example for applying for certificates in offline mode and replacing expired local and CA certificates.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001830027842__fig1), configure offline certificate application from the CA server for authenticating the identity of DeviceA.

**Figure 1** Network diagram of offline certificate application  
![](images/fig_dc_vrp_pki_cfg_001401.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a public-private key pair (a non-default key pair is used in this example).
2. Configure entity information.
3. Obtain certificates, which involves generating an offline certificate request file, sending the file to the CA server, and downloading and installing certificates.

When certificates are about to expire or have expired, perform the following operations to replace them:

1. Delete the existing certificates.
2. Import new certificates.
3. Check whether the certificates are imported successfully.

#### Data Preparation

To complete the configuration, you need the following data:

* Entity information, PKI domain, and certificate download mode

#### Procedure

1. Create an RSA key pair (a non-default key pair is used in this example).
   
   
   ```
   <DeviceA> system-view
   [~DeviceA] rsa pki local-key-pair rsa create
   [*DeviceA] commit
   ```
2. Configure entity information.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   During entity information configuration, you must configure a common entity name. Determine whether to configure other attributes based on the certificate issuing policy on the CA server. If the attributes used to filter certificates do not match the certificate issuing policy, certificate application may fail.
   
   
   
   ```
   [~DeviceA] pki entity entitya
   [*DeviceA--pki-entity-entitya] common-name DeviceA
   [*DeviceA--pki-entity-entitya] quit
   [*DeviceA] commit
   ```
3. Configure a PKI domain and associate certificate information with the domain.
   
   
   ```
   [~DeviceA] pki domain domaina
   [*DeviceA-pki-domaina] certificate request entity entitya
   [*DeviceA-pki-domaina] commit
   [~DeviceA] quit
   [~DeviceA] pki domain domaina
   [*DeviceA-pki-domaina] pki cmp session domaina
   [*DeviceA-pki-domaina-cmp-session-domaina] cmp request rsa local-key-pair rsa
   [*DeviceA-pki-domaina-cmp-session-domaina] commit
   [~DeviceA-pki-domaina-cmp-session-domaina] quit
   ```
4. Generate an offline certificate request file named **domaina.req**.
   
   
   ```
   [~DeviceA] pki request-certificate domain domaina pkcs10
   ```
5. Send the certificate request file to the CA server through email, FTP, or disk to apply for a local certificate. The CA server then generates a local certificate (for example, **domaina.cer**) and a CA certificate (for example, **ca.cer**).
6. Download the CA certificate and local certificate to the local device through email, FTP, or disk.
7. Import the local certificate and CA certificate into the memory of the device.
   
   
   ```
   [~DeviceA] pki import-certificate local filename domaina.cer
   [~DeviceA] pki import-certificate ca filename ca.cer
   ```
8. Check whether the certificates are imported successfully.
   
   
   ```
   [~DeviceA] display pki cert_list
   Certificate:                                                                                                                        
       Data:                                                                                                                           
           Version: 3 (0x2)                                                                                                            
           Serial Number:                                                                                                              
               08:d3:5e:92:f9:4d:77:ad                                                                                                 
           Signature Algorithm: sha256WithRSAEncryption                                                                                
           Issuer: CN=DeviceB                                                                 
           Validity                                                                                                                    
               Not Before: May  26  05:35:00 2021 GMT                                                                                  
               Not After: May  24  09:44:00 2031 GMT                                                                                   
           Subject: CN=local0123456789test004,OU=test,O=hw,L=hz,ST=zj,C=cn                                                             
           Subject Public Key Info:                                                                                                    
               Public Key Algorithm: rsaEncryption                                                                                     
               RSA Public Key: (2048 bit)                                                                                              
                   Modulus (2048 bit):                                                                                                 
                       00:ca:c5:63:f6:bc:17:3b:db:eb:64:ca:8d:7c:4b:                                                                   
                       d6:85:11:0e:6d:24:13:94:3a:90:57:68:e5:3f:07:                                                                   
                       09:1b:a7:c8:fc:91:30:c9:26:79:eb:8e:54:f8:83:                                                                   
                       84:33:12:59:aa:1c:f5:71:bc:9a:11:67:80:2d:b8:                                                                   
                       47:ba:26:02:03:05:be:ce:f4:6b:61:34:1f:fe:92:                                                                   
                       54:9b:fd:74:09:cc:a4:2a:4f:57:4a:57:47:be:9c:                                                                   
                       84:52:bb:18:79:59:a9:64:56:b6:cb:57:87:9a:29:                                                                   
                       77:1a:6a:bb:5e:41:79:c8:bd:cf:c1:60:3c:87:5b:                                                                   
                       bb:23:63:03:3e:6e:3e:42:e8:1e:c5:f5:1b:2d:dd:                                                                   
                       ae:a3:61:dc:0a:61:b5:c0:76:5c:2d:c8:a3:43:5e:                                                                   
                       97:6b:52:b1:3d:21:c9:1a:04:90:ec:a5:94:06:64:                                                                   
                       be:14:4f:f9:8d:5e:02:7b:97:74:db:ee:e6:f0:98:                                                                   
                       bc:ec:f7:4e:0a:01:85:57:e3:ec:3b:2e:5f:5f:38:                                                                   
                       f0:f6:67:c1:a1:51:96:c6:6c:f7:bc:29:bb:16:be:                                                                   
                       f7:54:19:96:c9:d2:92:09:45:e5:96:25:cc:65:f0:                                                                   
                       75:31:27:a3:b2:23:7b:05:e7:1b:66:50:8f:81:a1:                                                                   
                       84:dd:b8:7b:1d:2d:ba:c7:5a:53:70:fb:14:04:83:                                                                   
                       3a:b3                                                                                                           
                   Exponent:  65537 (0x010001)                                                                                         
            X509v3 extensions:                                                                                                         
                X509v3 Basic Constraints: critical                                                                                     
                    CA:FALSE                                                                                                           
                X509v3 Key Usage:                                                                                                      
                    Key Agreement, Key Encipherment (e0), Non-Repudiation, Digital Signature,                                          
                X509v3 Extended Key Usage:                                                                                             
                    TLS Web Server Authentication,                                                                                     
                                                                                                                                       
                X509v3 Subject Alternative Name:                                                                                       
                    DNS:local0123456789test004                                                                                         
                X509v3 Subject Key Identifier:                                                                                         
                  0C:2C:5E:61:40:96:F5:4D:9E:95:92:50:FC:95:F4:5B:F2:92:23:7A                                                          
       Signature Algorithm: sha256WithRSAEncryption                                                                                    
           8d:17:87:5b:93:21:4f:c2:1a:f5:bf:e5:09:18:e2:e3:14:21:                                                                      
           76:81:c7:cd:81:6c:ec:18:1a:58:83:0a:38:54:ef:be:ab:b2:                                                                      
           8c:42:cd:19:15:84:32:d2:94:a2:f4:35:e3:ae:2e:d3:02:95:                                                                      
           f7:94:c7:d4:40:0f:ba:ae:19:fe:55:10:29:74:da:08:c3:66:                                                                      
           55:41:42:12:7b:dd:6b:68:fa:9f:cd:a2:fc:64:06:de:07:df:                                                                      
           83:6b:a1:24:23:bc:7b:92:d7:69:e1:37:0a:26:03:b3:49:fd:                                                                      
           47:f0:2e:01:14:c1:56:db:af:50:63:b4:1d:ea:ab:ce:87:3c:                                                                      
           ea:0e:8e:d6:e9:17:64:a5:ce:80:97:dd:1e:65:ee:6b:22:d2:                                                                      
           05:15:21:12:dc:92:a6:ef:47:ec:88:5f:95:21:3f:02:2a:a4:                                                                      
           2a:44:55:a2:7d:3a:87:5c:69:d8:7e:27:fb:93:76:ca:44:17:                                                                      
           5e:8f:25:f3:a6:95:a7:1d:a2:92:bc:8d:ad:2d:c1:1b:d3:f6:                                                                      
           78:89:59:9e:a2:f7:6f:64:ee:1f:29:e1:25:9d:74:40:bd:d8:                                                                      
           8b:fa:89:f0:6d:62:fc:6c:13:8d:24:22:47:29:ad:05:2b:a1:                                                                      
           8e:4f:67:f7:ca:c3:71:be:d1:b7:66:7c:e6:bb:24:d4:3c:30:                                                                      
           68:37:f1:c7                                                                                                                 
       Certificate file name:domaina.cer                                             
   ```
9. When the local certificate is about to expire or has expired, repeat the preceding steps to generate a new certificate request file and send it to the CA server to generate new certificates (for example, **domaina1.cer** and **ca1.cer**).
10. Download the CA certificate and local certificate to the local device through email, FTP, or disk.
11. Delete the CA certificate and local certificate to be replaced.
    
    
    ```
    [~DeviceA] pki delete-certificate local filename domaina.cer
    [~DeviceA] pki delete-certificate ca filename ca.cer
    ```
12. Import the new CA certificate and local certificate.
    
    
    ```
    [~DeviceA] pki import-certificate local filename domaina1.cer
    [~DeviceA] pki import-certificate ca filename ca1.cer
    ```
13. Check whether the certificates are imported successfully.
    
    
    ```
    [~DeviceA] display pki cert_list
    Certificate:                                                                                                                        
        Data:                                                                                                                           
            Version: 3 (0x2)                                                                                                            
            Serial Number:                                                                                                              
                08:d3:5e:92:f9:4d:77:ad                                                                                                 
            Signature Algorithm: sha256WithRSAEncryption                                                                                
            Issuer: CN=DeviceB                                                                 
            Validity                                                                                                                    
                Not Before: May  26  05:35:00 2021 GMT                                                                                  
                Not After: May  24  09:44:00 2031 GMT                                                                                   
            Subject: CN=local0123456789test004,OU=test,O=hw,L=hz,ST=zj,C=cn                                                             
            Subject Public Key Info:                                                                                                    
                Public Key Algorithm: rsaEncryption                                                                                     
                RSA Public Key: (2048 bit)                                                                                              
                    Modulus (2048 bit):                                                                                                 
                        00:ca:c5:63:f6:bc:17:3b:db:eb:64:ca:8d:7c:4b:                                                                   
                        d6:85:11:0e:6d:24:13:94:3a:90:57:68:e5:3f:07:                                                                   
                        09:1b:a7:c8:fc:91:30:c9:26:79:eb:8e:54:f8:83:                                                                   
                        84:33:12:59:aa:1c:f5:71:bc:9a:11:67:80:2d:b8:                                                                   
                        47:ba:26:02:03:05:be:ce:f4:6b:61:34:1f:fe:92:                                                                   
                        54:9b:fd:74:09:cc:a4:2a:4f:57:4a:57:47:be:9c:                                                                   
                        84:52:bb:18:79:59:a9:64:56:b6:cb:57:87:9a:29:                                                                   
                        77:1a:6a:bb:5e:41:79:c8:bd:cf:c1:60:3c:87:5b:                                                                   
                        bb:23:63:03:3e:6e:3e:42:e8:1e:c5:f5:1b:2d:dd:                                                                   
                        ae:a3:61:dc:0a:61:b5:c0:76:5c:2d:c8:a3:43:5e:                                                                   
                        97:6b:52:b1:3d:21:c9:1a:04:90:ec:a5:94:06:64:                                                                   
                        be:14:4f:f9:8d:5e:02:7b:97:74:db:ee:e6:f0:98:                                                                   
                        bc:ec:f7:4e:0a:01:85:57:e3:ec:3b:2e:5f:5f:38:                                                                   
                        f0:f6:67:c1:a1:51:96:c6:6c:f7:bc:29:bb:16:be:                                                                   
                        f7:54:19:96:c9:d2:92:09:45:e5:96:25:cc:65:f0:                                                                   
                        75:31:27:a3:b2:23:7b:05:e7:1b:66:50:8f:81:a1:                                                                   
                        84:dd:b8:7b:1d:2d:ba:c7:5a:53:70:fb:14:04:83:                                                                   
                        3a:b3                                                                                                           
                    Exponent:  65537 (0x010001)                                                                                         
             X509v3 extensions:                                                                                                         
                 X509v3 Basic Constraints: critical                                                                                     
                     CA:FALSE                                                                                                           
                 X509v3 Key Usage:                                                                                                      
                     Key Agreement, Key Encipherment (e0), Non-Repudiation, Digital Signature,                                          
                 X509v3 Extended Key Usage:                                                                                             
                     TLS Web Server Authentication,                                                                                     
                                                                                                                                        
                 X509v3 Subject Alternative Name:                                                                                       
                     DNS:local0123456789test004                                                                                         
                 X509v3 Subject Key Identifier:                                                                                         
                   0C:2C:5E:61:40:96:F5:4D:9E:95:92:50:FC:95:F4:5B:F2:92:23:7A                                                          
        Signature Algorithm: sha256WithRSAEncryption                                                                                    
            8d:17:87:5b:93:21:4f:c2:1a:f5:bf:e5:09:18:e2:e3:14:21:                                                                      
            76:81:c7:cd:81:6c:ec:18:1a:58:83:0a:38:54:ef:be:ab:b2:                                                                      
            8c:42:cd:19:15:84:32:d2:94:a2:f4:35:e3:ae:2e:d3:02:95:                                                                      
            f7:94:c7:d4:40:0f:ba:ae:19:fe:55:10:29:74:da:08:c3:66:                                                                      
            55:41:42:12:7b:dd:6b:68:fa:9f:cd:a2:fc:64:06:de:07:df:                                                                      
            83:6b:a1:24:23:bc:7b:92:d7:69:e1:37:0a:26:03:b3:49:fd:                                                                      
            47:f0:2e:01:14:c1:56:db:af:50:63:b4:1d:ea:ab:ce:87:3c:                                                                      
            ea:0e:8e:d6:e9:17:64:a5:ce:80:97:dd:1e:65:ee:6b:22:d2:                                                                      
            05:15:21:12:dc:92:a6:ef:47:ec:88:5f:95:21:3f:02:2a:a4:                                                                      
            2a:44:55:a2:7d:3a:87:5c:69:d8:7e:27:fb:93:76:ca:44:17:                                                                      
            5e:8f:25:f3:a6:95:a7:1d:a2:92:bc:8d:ad:2d:c1:1b:d3:f6:                                                                      
            78:89:59:9e:a2:f7:6f:64:ee:1f:29:e1:25:9d:74:40:bd:d8:                                                                      
            8b:fa:89:f0:6d:62:fc:6c:13:8d:24:22:47:29:ad:05:2b:a1:                                                                      
            8e:4f:67:f7:ca:c3:71:be:d1:b7:66:7c:e6:bb:24:d4:3c:30:                                                                      
            68:37:f1:c7                                                                                                                 
        Certificate file name:domaina1.cer
    ```
    ```
    [~DeviceA] display pki ca_list
    The x509 object type is certificate:                                                                                               
    Certificate:                                                                                                                        
        Data:                                                                                                                           
            Version: 3 (0x2)                                                                                                            
            Serial Number:                                                                                                              
                6c:b4:69:11:0f:37:d6:c3                                                                                                 
            Signature Algorithm: sha256WithRSAEncryption                                                                                
            Issuer: CN=ca0123456789test007,OU=test,O=hw,L=hz,ST=zj,C=cn                                                                 
            Validity                                                                                                                    
                Not Before: May  24  09:45:00 2021 GMT                                                                                  
                Not After : May  24  09:45:00 2031 GMT                                                                                  
            Subject: CN=ca0123456789test007,OU=test,O=hw,L=hz,ST=zj,C=cn                                                                
            Subject Public Key Info:                                                                                                    
                Public Key Algorithm: rsaEncryption                                                                                     
                RSA Public Key: (2048 bit)                                                                                              
                    Modulus (2048 bit):                                                                                                 
                        00:bf:dc:46:4c:3e:4e:f7:90:1c:2c:3f:6c:fc:5e:                                                                   
                        40:6c:84:8c:46:64:dc:1a:35:99:3a:5b:cb:9b:9d:                                                                   
                        2d:e7:72:73:fa:fe:8e:83:df:54:bc:73:09:e6:47:                                                                   
                        ad:97:f6:02:5d:d0:84:68:a5:f5:95:cb:14:a1:0b:                                                                   
                        3e:6d:4b:2e:b5:75:d7:d5:b9:cd:c0:23:fb:b8:6a:                                                                   
                        af:0d:d1:df:d5:50:d8:95:65:2c:9c:39:47:09:61:                                                                   
                        7f:b7:37:b3:c9:5d:b4:7e:d7:a6:a6:0e:aa:52:66:                                                                   
                        c6:b7:b1:2a:b3:7e:af:c3:f2:1f:f3:71:2b:90:48:                                                                   
                        bb:9d:95:dc:4a:41:a8:9f:ac:91:56:ff:19:bc:2c:                                                                   
                        ac:fe:27:18:f5:ee:f1:b6:f8:2b:49:28:ab:f7:92:                                                                   
                        11:c4:91:46:eb:58:d3:39:41:8a:b2:1c:b9:a5:b6:                                                                   
                        02:1f:e1:53:da:cc:37:b5:80:5b:2c:0b:1f:4d:20:                                                                   
                        3d:78:44:8d:3b:77:7d:2d:6e:48:4d:d0:a2:0a:7b:                                                                   
                        59:0e:cd:84:04:90:73:63:96:43:b8:7d:c0:6c:38:                                                                   
                        bb:7f:70:3b:03:2f:5f:f4:47:f5:7c:ca:f5:09:99:                                                                   
                        6b:9f:9c:35:16:81:6b:98:4b:6b:dd:82:04:94:dd:                                                                   
                        da:24:1e:06:af:0f:01:98:92:8e:3a:09:2b:2e:39:                                                                   
                        ae:9b                                                                                                           
                    Exponent:  65537 (0x010001)                                                                                         
             X509v3 extensions:                                                                                                         
                 X509v3 Basic Constraints: critical                                                                                     
                     CA:TRUE                                                                                                            
                 X509v3 Key Usage:                                                                                                      
                     Certificate Sign,  CRL Sign,                                                                                       
                 X509v3 Subject Key Identifier:                                                                                         
                   97:7F:94:6B:43:D0:BF:11:02:64:1E:7D:09:DD:05:F6:CE:B7:D0:5E                                                          
         Signature Algorithm: sha256WithRSAEncryption                                                                                   
            3b:63:4c:17:f1:c9:a5:7f:68:62:3a:c3:10:80:83:e0:fe:1d:                                                                      
            7f:12:b0:64:70:b8:31:cb:d5:6e:82:5e:21:a9:02:1c:c3:7b:                                                                      
            4e:e5:b0:4d:bc:f9:56:80:5b:47:c7:15:76:b5:56:72:69:41:                                                                      
            92:fd:05:62:91:e1:47:76:89:90:c4:07:41:3a:77:39:49:88:                                                                      
            73:35:96:90:d5:b4:df:75:53:43:5c:a8:5b:19:bc:d6:e2:b4:                                                                      
            c0:cc:2c:39:7f:b3:5d:c8:6f:30:19:74:22:fa:f1:76:69:a2:                                                                      
            52:b5:7e:07:4d:ce:e1:a5:11:a1:a3:24:5c:b6:6c:01:16:df:                                                                      
            b2:ba:22:7f:46:78:1d:7c:37:90:0b:ff:46:78:0d:9a:f8:94:                                                                      
            1e:cc:4b:02:9b:a4:50:12:b2:64:e6:5e:8b:54:4f:00:f3:e3:                                                                      
            43:80:02:d3:b1:aa:e8:09:50:73:97:bf:b0:63:ab:d7:53:15:                                                                      
            e0:d9:74:db:1b:f6:51:4a:18:24:cb:b7:5b:ee:16:43:1e:a8:                                                                      
            05:f9:76:ec:bc:28:e9:cf:80:0a:ed:ba:f9:11:39:3c:77:d8:                                                                      
            5f:c4:be:f3:ee:19:22:dd:5a:b9:01:c6:7c:99:d5:ab:30:7a:                                                                      
            53:b4:7e:cb:71:d5:f1:89:9a:18:8c:6b:4d:d8:52:87:61:cd:                                                                      
            9a:80:a2:2e                                                                                                                 
        Certificate file name: ca1.cer
    ```

#### Configuration Files

DeviceA configuration file

```
#
 sysname DeviceA  
#
pki entity entitya
 common-name DeviceA
#
pki domain domaina
 certificate request entity entitya
 pki cmp session domaina
  cmp request rsa local-key-pair rsa
#
return
```