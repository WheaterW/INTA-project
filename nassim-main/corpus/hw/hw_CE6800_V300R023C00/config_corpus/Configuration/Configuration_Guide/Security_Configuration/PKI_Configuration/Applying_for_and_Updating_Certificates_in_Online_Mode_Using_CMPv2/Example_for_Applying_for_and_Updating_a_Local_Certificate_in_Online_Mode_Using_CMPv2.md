Example for Applying for and Updating a Local Certificate in Online Mode Using CMPv2
====================================================================================

Example for Applying for and Updating a Local Certificate in Online Mode Using CMPv2

#### Networking Requirements

On an enterprise network shown in [Figure 1](#EN-US_TASK_0000001564006237__fig_dc_cfg_pki_003901), DeviceA located at the network border functions as the egress gateway, which uses CMPv2 to apply for a local certificate in online mode for the first time from the CA server located on the public network. The local certificate is automatically downloaded to DeviceA's storage medium after being obtained. The local certificate is automatically updated when 80% of the certificate validity period has elapsed.

**Figure 1** Applying for a local certificate for a PKI entity in online mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1 and Interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001512686894.png)![](public_sys-resources/note_3.0-en-us.png) 

Ensure that there are reachable routes between devices before the configuration.




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces.
2. Create an RSA key pair so that the local certificate application request contains the public key.
3. Configure a PKI entity and its related information to identify the PKI entity.
4. Configure application and automatic update of certificates using CMPv2 and use the message authentication code (MAC) to authenticate messages, so that the device can automatically download the CA and local certificates.
5. Install the local certificate to make it effective. That is, the device can use the certificate to protect communication data.

#### Data Preparation

To complete the configuration, you need the following data:

* CA name: subject field of the CA certificate.
* Reference value and secret value of the MAC: obtained from the CMPv2 server.
* CA certificate of the CA server to be imported to the device.

#### Procedure

1. Configure IP addresses for interfaces.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] [undo portswitch](cmdqueryname=undo+portswitch)
   [*DeviceA-100GE1/0/1] ip address 10.2.0.2 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] [undo portswitch](cmdqueryname=undo+portswitch)
   [*DeviceA-100GE1/0/2] ip address 10.1.0.2  24
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
2. Create an RSA key pair.
   
   
   
   Create a 3072-bit RSA key pair named **rsa\_cmp** and allow it to be exported from the device.
   
   ```
   [~DeviceA] pki rsa local-key-pair create rsa_cmp exportable
    Info: The name of the new key-pair will be: rsa_cmp                             
    The size of the public key ranges from 2048 to 4096.                            
    Input the bits in the modules:3072                                             
    Generating key-pairs...                                                        
    Generating key-pairs finished 
   [*DeviceA] commit 
   ```
3. Configure a PKI entity to identify a certificate applicant.
   
   
   
   Configure a PKI entity named **user01**.
   
   ```
   [~DeviceA] pki entity user01
   [*DeviceA-pki-entity-user01] common-name hello
   [*DeviceA-pki-entity-user01] country cn
   [*DeviceA-pki-entity-user01] email user@test.abc.com
   [*DeviceA-pki-entity-user01] fqdn test.abc.com
   [*DeviceA-pki-entity-user01] ip-address 10.2.0.2
   [*DeviceA-pki-entity-user01] state jiangsu
   [*DeviceA-pki-entity-user01] organization huawei
   [*DeviceA-pki-entity-user01] organization-unit info
   [*DeviceA-pki-entity-user01] quit
   [*DeviceA] commit
   ```
4. Configure a CMP session.
   
   
   
   # Create a CMP session named **cmp**.
   
   ```
   [~DeviceA] pki cmp session cmp
   ```
   
   # Specify the PKI entity name referenced by the CMP session.
   
   ```
   [*DeviceA-pki-cmp-session-cmp] cmp-request entity user01
   ```
   
   # Configure a CA name, for example, **C=cn,ST=beijing,L=SD,O=BB,OU=BB,CN=BB**.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The field order in the CA name must be the same as that in the CA certificate; otherwise, the server considers the CA name invalid.
   
   ```
   [*DeviceA-pki-cmp-session-cmp] cmp-request ca-name "C=cn,ST=beijing,L=SD,O=BB,OU=BB,CN=BB"
   ```
   
   # Configure the URL for certificate application.
   
   ```
   [*DeviceA-pki-cmp-session-cmp] cmp-request server url http://10.3.0.1:8080
   ```
   
   # Specify the RSA key pair used for certificate application and configure the device to update the RSA key pair together with the certificate.
   
   ```
   [*DeviceA-pki-cmp-session-cmp] cmp-request rsa local-key-pair rsa_cmp regenerate
   ```
   
   # Use the MAC for initial certificate application. Set the MAC reference value to **1234** and MAC secret value to **Huawei@RSA1234**.
   
   ```
   [*DeviceA-pki-cmp-session-cmp] cmp-request message-authentication-code 1234 Huawei@RSA1234
   [*DeviceA-pki-cmp-session-cmp] quit
   [*DeviceA] pki cmp initial-request session cmp
   [*DeviceA] commit
   ```
   
   The CA and local certificates obtained are named **cmp\_ca1.cer** and **cmp\_ir.cer** respectively, and are stored in the device's storage medium.
5. Install certificates.
   
   
   
   After the certificates are imported, the **cmp\_ca1.cer** and **cmp\_ir.cer** files are deleted from the storage medium by default. To keep them, select **N** as prompted.
   
   # Import the CA certificate to memory.
   ```
   [~DeviceA] pki import-certificate ca filename cmp_ca1.cer
    The CA's Subject is /C=cn/ST=beijing/L=BB/O=BB/OU=BB/CN=BB
    The CA's fingerprint is:
      SHA1   fingerprint:2C:2B:C0:31:66:A6:95:A0:7A:AC:EF:3D:37:1C:9A:4D:01:BA:09:4D
      SHA256 fingerprint:CA:FC:6B:94:53:E9:E3:D7:D3:E1:F4:75:3F:DB:C4:0F:0A:B9:F1:AD:03:0B:A8:0D:EE:73:4A:83:54:EF:1F:81
    Is the fingerprint correct?(Y/N):y
    Info: Succeeded in importing the certificate.  
    Warning: The file in the flash will be deleted. Please select 'N' if you want to keep it. Please select [Y/N]:y 
    Info: Delete Success.
   [*DeviceA] commit
   ```
   
   # Import the local certificate to memory.
   
   ```
   [~DeviceA] pki import-certificate local filename cmp_ir.cer 
    Info: Succeeded in importing the certificate.
    Warning: The file in the flash will be deleted. Please select 'N' if you want to keep it. Please select [Y/N]:y 
    Info: Delete Success.
   [*DeviceA] commit
   ```
6. Configure automatic certificate update.
   
   
   
   # In the CMP session view, enable automatic certificate update using CMPv2.
   
   
   
   ```
   [~DeviceA] pki cmp session cmp
   [*DeviceA-pki-cmp-session-cmp] cmp-request authentication-cert cmp_ir.cer
   [*DeviceA-pki-cmp-session-cmp] certificate auto-update enable
   [*DeviceA-pki-cmp-session-cmp] [quit](cmdqueryname=quit)
   [*DeviceA] commit
   ```
   # In the CMP session view, set the automatic certificate update time to 80% of the current certificate validity period.
   ```
   [~DeviceA] pki cmp session cmp
   [*DeviceA-pki-cmp-session-cmp] certificate update expire-time 80
   [*DeviceA-pki-cmp-session-cmp] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

* After a local certificate is obtained and imported to memory, run the **display pki certificate local** command to view the content of the certificate.
  ```
  [~DeviceA] display pki certificate local filename cmp_ir.cer
   The  x509_obj type is Cert:                                                    
  Certificate:                                                                    
      Data:                                                                       
          Version: 3 (0x2)                                                        
          Serial Number: 1144733510 (0x443b3f46)                                  
          Signature Algorithm: sha1WithRSAEncryption                              
          Issuer: C=cn, ST=beijing, L=BB, O=BB, OU=BB, CN=BB
          Validity                                                                
              Not Before: Jun 12 09:33:10 2012 GMT                                
              Not After : Aug 13 02:38:27 2016 GMT                                
          Subject: C=cn, ST=jiangsu, O=huawei, OU=info, CN=hello
          Subject Public Key Info:                                                
              Public Key Algorithm: rsaEncryption                                 
                  RSA Public-Key: (3072 bit)                                          
                  Modulus:                                                        
                      00:d3:12:fe:57:48:c6:a5:10:12:e9:2f:f9:2a:ff:               
                      7b:2a:d8:45:69:11:c4:85:30:c4:9a:4d:0f:ad:58:               
                      e7:56:cd:5c:f0:18:e1:c3:6d:44:c2:c3:5e:64:22:               
                      d1:28:c9:c3:37:3c:34:ed:28:04:7f:62:9e:8b:94:               
                      af:bc:72:de:f6:72:7f:e4:d8:45:31:fd:f9:ac:ce:               
                      5a:b9:c7:1b:23:53:00:28:a6:3b:f5:61:69:5d:ab:               
                      67:cb:bb:e8:96:2f:ce:ab:2c:6b:91:5b:26:91:86:               
                      8f:80:a9:b0:66:c1:16:3d:31:55:a2:d4:b5:5a:af:               
                      85:88:6e:99:f8:f8:53:58:77:26:91:ed:0e:94:ad:               
                      c5:8d:53:67:67:55:08:8d:90:38:e0:5e:96:37:b9:               
                      64:0e:36:e7:cf:9a:d2:77:e4:b0:24:05:a6:eb:03:               
                      6e:ff:f7:ab:be:93:9e:8c:66:7d:31:66:be:6d:c8:               
                      f3:17:9d:86:19:88:21:2d:d9:69:86:5f:b2:55:a4:               
                      db:bc:d7:d0:6b:ac:66:ac:e4:63:9c:66:79:9c:42:               
                      5c:83:b8:9e:4b:6e:67:85:a2:47:19:f1:5c:c0:3c:               
                      c9:a3:47:02:a8:53:69:59:9e:d9:c7:5e:90:83:8d:               
                      ac:cd:21:3c:d5:31:39:49:84:e6:f8:f4:e0:44:dd:               
                      5d:7b                                                       
                  Exponent: 65537 (0x10001)                                       
          X509v3 extensions:                                                      
              X509v3 Subject Alternative Name:                                    
                  IP Address:10.2.0.2, DNS:test.abc.com, email:user@test.abc.com                   
      Signature Algorithm: sha1WithRSAEncryption                                  
          53:d5:79:31:7b:40:52:aa:ec:a9:35:ed:07:62:32:c4:ce:22:                  
          d3:37:0e:83:0c:4c:fa:61:dd:8c:db:a8:d3:fd:6a:ca:0e:3c:                  
          91:2c:91:ab:92:31:34:b5:87:1e:30:a4:ff:94:9c:d2:71:3c:                  
          6b:1f:4f:be:a7:20:f2:e1:c2:ad:71:8b:c2:79:0f:50:1f:3c:                  
          f9:87:df:1d:ee:3d:38:8c:f3:30:b7:3b:00:9b:72:38:b0:68:                  
          e1:c0:08:f4:02:91:81:a8:fa:51:9e:53:0d:03:b3:6b:0e:e2:                  
          62:80:ef:2a:a0:cb:9b:9b:91:21:7c:df:fe:6a:38:cc:03:36:                  
          9c:fc 
                                                                                  
  Pki realm name: -abc      
  Certificate file name: cmp_ir.cer
  Certificate peer name: -  
  ```
* After a CA certificate is obtained and imported to memory, run the **display pki certificate ca** command to view the content of the certificate.
  ```
  [~DeviceA] display pki certificate ca filename cmp_ca1.cer
   The x509 object  type is certificate:                                          
  Certificate:                                                                    
      Data:                                                                       
          Version: 3 (0x2)                                                        
          Serial Number: 2 (0x2)                                                  
          Signature Algorithm: sha1WithRSAEncryption                              
          Issuer: C=cn, ST=beijing, L=BB, O=BB, OU=BB, CN=BB 
          Validity                                                                
              Not Before: Aug 15 02:38:27 2011 GMT                                
              Not After : Aug 13 02:38:27 2016 GMT                                
          Subject: C=cn, ST=jiangsu, O=huawei, OU=info, CN=hello                     
          Subject Public Key Info:                                                
              Public Key Algorithm: rsaEncryption                                 
                  RSA Public-Key: (1024 bit)                                          
                  Modulus:                                                        
                      00:b7:3e:65:7f:3b:3c:18:b8:87:34:39:76:3c:87:               
                      39:f7:a9:b3:35:9b:e0:e0:5b:c7:4f:3c:bb:fa:dd:               
                      da:93:0b:55:6e:eb:ba:52:c8:86:d1:cf:14:1e:1c:               
                      35:c6:53:68:f3:51:e7:2c:d4:b8:fa:0f:b3:04:ef:               
                      3f:a0:b3:4d:78:c1:26:88:26:15:41:3d:14:7f:67:               
                      3e:2f:35:32:ce:c7:73:73:43:5c:12:d3:0f:a0:ec:               
                      96:ae:55:61:27:32:39:a4:f8:32:a1:68:50:e6:3d:               
                      2b:39:6d:42:e8:09:5d:4f:98:46:6e:fc:80:87:0e:               
                      36:ca:09:7a:ca:2f:dd:ad:d3                                  
                  Exponent: 65537 (0x10001)                                       
          X509v3 extensions:                                                      
              X509v3 Basic Constraints: critical                                  
                  CA:TRUE                                                         
              X509v3 Subject Key Identifier:                                      
                  4F:67:F4:CB:F4:C3:F7:61:2C:BD:FF:1D:D1:29:FD:39:28:9F:3B:8B     
              X509v3 Key Usage:                                                   
                  Certificate Sign, CRL Sign                                      
              Netscape Cert Type:                                                 
                  SSL CA, S/MIME CA, Object Signing CA                            
              Netscape Comment:                                                   
                  xca certificate                                                 
      Signature Algorithm: sha1WithRSAEncryption                                  
          75:43:24:eb:db:ee:7d:05:30:88:b8:1b:d5:32:ca:51:49:74:                  
          04:94:fe:d0:31:29:6f:72:c7:4a:86:ac:2a:4c:45:24:9d:3c:                  
          b4:30:b5:d1:43:88:29:f7:b4:88:b8:37:dc:dd:f4:fa:42:34:                  
          1c:e6:a5:bc:bb:0b:37:ef:db:8c:b2:b0:bd:97:7f:15:ae:6c:                  
          71:1b:ff:f1:90:13:74:a4:1f:7c:f7:4e:80:5b:42:aa:6b:22:                  
          2a:cf:04:48:29:20:c0:b2:95:38:11:06:be:76:f0:cb:8d:4a:                  
          c6:1a:50:af:31:81:58:ac:14:fe:89:f2:e0:bb:95:3c:94:d0:                  
          54:96  
                                                                                  
  Pki realm name: -
  Certificate file name: cmp_ca1.cer
  Certificate peer name: -  
  ```

#### Configuration Scripts

DeviceA configuration file

```
#
sysname DeviceA
#
pki entity user01
 country cn
 state jiangsu
 organization huawei
 organization-unit info
 common-name hello
 fqdn user@test.abc.com
 ip-address 10.2.0.2
 email user@user@test.abc.com
#
interface 100GE1/0/1
 ip address 10.2.0.2 255.255.255.0
#
interface 100GE1/0/2
 ip address 10.1.0.2 255.255.255.0
#
pki import-certificate ca filename cmp_cal.cer
pki import-certificate local filename cmp_ir.cer
pki cmp session cmp                                                             
 cmp-request ca-name "C=cn,ST=beijing,L=SD,O=BB,OU=BB,CN=BB"                    
 cmp-request authentication-cert cmp_ir.cer
 cmp-request entity user01                                                      
 cmp-request server url http://10.3.0.1:8080                                    
 cmp-request rsa local-key-pair rsa_cmp regenerate                             
 cmp-request message-authentication-code 1234 %@%##!!!!!!!!!"!!!!'!!!!*!!!!#~Yt'T`/_H5O<-:ydTz$hk./U,Huq3[u0w8!!!!!!!!!!!!!!!~!!!!h#a6(1U`jWv[fB3ZRI\7~b5jYCD+l0/R)RMFWV,:%@%# 
 certificate auto-update enable                                                 
 certificate update expire-time 80  
#
return
```