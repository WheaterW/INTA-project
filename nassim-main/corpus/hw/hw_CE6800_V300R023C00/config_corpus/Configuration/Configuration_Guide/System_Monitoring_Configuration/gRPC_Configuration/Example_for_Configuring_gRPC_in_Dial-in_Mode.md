Example for Configuring gRPC in Dial-in Mode
============================================

Example for Configuring gRPC in Dial-in Mode

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001564006065__fig168713817385), DeviceA functioning as a gRPC server connects to the collector functioning as a gRPC client. You need to configure gRPC in dial-in mode on DeviceA to enable it to send collected data to the collector.

**Figure 1** Network diagram of gRPC in dial-in mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001563885801.png)

#### Procedure

1. Configure an IP address for interface 1.
   
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname DeviceA 
   [*DeviceA] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 192.168.1.1 255.255.255.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
2. Configure an SSL policy.
   
   
   
   # Upload the obtained digital certificate to the **/pki/public** directory of the device through SFTP. For details about how to apply for a digital certificate in PKI mode, see Configuration Guide > PKI Configuration.
   
   # Configure a PKI realm and import the local certificate and private key file.
   
   ```
   
   [~DeviceA] pki realm domain1
   [*DeviceA-pki-realm-domain1] commit
   [~DeviceA-pki-realm-domain1] quit
   [~DeviceA] pki import-certificate local realm domain1 pem filename restconf_local.pem
   [~DeviceA] pki import rsa-key-pair restconf-key pem restconf.pem //Skip this step if the private key file is generated on the local device.
   ```
   
   # Import the CA certificate of the peer collector to verify the validity of the local certificate for the collector.
   
   ```
   [~DeviceA] pki import-certificate ca realm domain1 pem filename restconf_ca.pem
   ```
   
   # Configure an SSL policy and bind it to the PKI realm.
   
   
   
   ```
   [~DeviceA] ssl policy policy1
   [*DeviceA-ssl-policy-policy1] pki-domain domain1
   [*DeviceA-ssl-policy-policy1] commit
   [~DeviceA-ssl-policy-policy1] quit
   ```
3. Configure AAA authentication.
   
   
   ```
   [~DeviceA] aaa
   [~DeviceA-aaa] local-user admin1234 password
   Please configure the login password (8-128)
   It is recommended that the password consist of four types of characters, including lowercase letters, uppercase letters, numerals and special characters. 
   Please enter password:                                      
   Please confirm password:                               
   [*DeviceA-aaa] local-user admin1234 service-type http
   [*DeviceA-aaa] local-user admin1234 user-group manage-ug
   [*DeviceA-aaa] quit
   [*DeviceA] commit
   ```
4. Configure the gRPC server function.
   
   
   ```
   [~DeviceA] grpc
   [~DeviceA-grpc] grpc server
   [~DeviceA-grpc-server] source-ip 192.168.1.1
   [~DeviceA-gRPC-server] server-port 20000
   [*DeviceA-grpc-server] ssl-policy policy1
   [*DeviceA-grpc-server] ssl-verify peer
   [*DeviceA-grpc-server] server enable
   [*DeviceA-grpc-server] quit
   [*DeviceA-grpc] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Verify the configuration in the gRPC server view.

```
[~DeviceA-grpc-server] display this
 #    
 grpc server                  
  source-ip 192.168.1.1    
  server-port 20000
  ssl-policy policy1
  ssl-verify peer
  server enable 
#       
return      
```

#### Configuration Scripts

DeviceA
```
#
sysname DeviceA
#
pki realm domain1
#
ssl policy policy1
 pki-domain domain1
#
aaa
 local-user admin1234 password irreversible-cipher $1d$g8wLJ`LjL!$CyE(V{3qg5DdU:PM[6=6O$UF-.fQ,Q}>^)OBzgoU$
 local-user admin1234 service-type http
 local-user admin1234 user-group manage-ug
#
grpc
 #
 grpc server                                                                    
  source-ip 192.168.1.1 
  server-port 20000
  ssl-policy policy1
  ssl-verify peer                                                           
  server enable
#
interface 100GE1/0/1
 undo portswitch
 ip address 192.168.1.1 255.255.255.0
#
return
```