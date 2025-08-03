gRPC
====

gRPC

#### Security Policy

* Supports authentication
  
  A gRPC server supports AAA authentication. Only authenticated users can log in to a device and perform related operations. If a user repeatedly logs in and cracks the password, the server rejects the login based on the password authentication timeout period.
* Supports the SSL service
  
  A gRPC server supports SSL certificate authentication.
* Supports function disabling
  
  If a gRPC server is enabled, the socket listening is enabled for devices. In this case, the devices are easily scanned by attackers. If a gRPC server is not used, the gRPC server and the port listened can be disabled. The gRPC server is disabled by default.
* Supports port number changing
  
  The port of a gRPC server can be changed to a private port to reduce the probability of being scanned and attacked.
* Supports ACLs
  
  ACLs can be configured for a gRPC server in the system view. ACLs are used to limit the client IP addresses that can access a device.
* Supports source interface configuration
  
  Source interfaces supported by a gRPC server can be configured. Users must access a device using the IP addresses of the configured source interfaces. In this way, the access range is controlled and the device security is enhanced.

#### Attack Methods

* DoS Attack
  
  A gRPC server supports a limited number of users. When the number of admitted users reaches the upper limit, other users cannot access the device. This situation may appear when users normally use the gRPC server or when the gRPC server is attacked.

#### Configuration and Maintenance Methods

* Disable the gRPC service.
  
  ```
  [~HUAWEI-grpc-server] undo server enable
  ```
  ```
  [*HUAWEI-grpc-server] commit
  ```
* Change the port number of the gRPC server.
  
  ```
  [~HUAWEI-grpc-server] server-port 5000
  ```
  ```
  [*HUAWEI-grpc-server] commit
  ```
* Configure an ACL.
  
  ```
  [~HUAWEI] acl 2000
  ```
  ```
  [~HUAWEI-acl-basic-2000] display this
  ```
  ```
  #
  acl number 2000
   rule 15 permit source 10.1.1.1 0
   rule 20 deny
  #
  return
  ```
  ```
  [~HUAWEI-acl-basic-2000] quit
  ```
  ```
  [~HUAWEI] grpc
  ```
  ```
  [~HUAWEI-grpc] grpc server
  ```
  ```
  [~HUAWEI-grpc-server] acl 2000
  ```
  ```
  [*HUAWEI-grpc-server] commit
  ```
* Configure a source interface, SSL policy, and idle timeout period.
  
  ```
  [~HUAWEI] ssl policy huawei2018
  ```
  ```
  [*HUAWEI-ssl-policy-huawei2018] certificate load asn1-cert servercert.der key-pair rsa key-file serverkey.der
  ```
  ```
  [*HUAWEI-ssl-policy-huawei2018] crl load pem-crl server.pem
  ```
  ```
  [*HUAWEI-ssl-policy-huawei2018] trusted-ca load asn1-ca servercert.der
  ```
  ```
  [*HUAWEI-ssl-policy-huawei2018] commit
  ```
  ```
  [~HUAWEI-ssl-policy-huawei2018] quit
  ```
  ```
  [~HUAWEI] grpc
  ```
  ```
  [~HUAWEI-grpc] grpc server
  ```
  ```
  [~HUAWEI-grpc-server] source-ip 10.1.1.1
  ```
  ```
  [*HUAWEI-grpc-server] ssl-policy huawei2018
  ```
  ```
  [*HUAWEI-grpc-server] ssl-verify peer
  ```
  ```
  [*HUAWEI-grpc-server] idle-timeout 60
  ```
  ```
  [*HUAWEI-grpc-server] display this
  ```
  ```
   #
   grpc server
    source-ip 10.1.1.1
    server-port 5000
    idle-timeout 60
    ssl-policy huawei2018
    ssl-verify peer
    server enable
  #
  return
  ```
  ```
  [*HUAWEI-grpc-server] commit
  ```

#### Verifying the Security Hardening Result

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration** **grpc** command to check the gRPC configuration.


#### Configuration and Maintenance Suggestions

* Disable the gRPC server when not using it.
* Change the port number of the gRPC server.
* Configure ACLs.
* Use the TLS certificate by default.