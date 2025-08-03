Example for Configuring Dynamic Subscription (IPv4 Collector)
=============================================================

Example for Configuring Dynamic Subscription (IPv4 Collector)

#### Networking Requirements

As the network scale increases, you need to optimize networks and rectify faults based on device information in a timely manner. For example, if you want to monitor an interface for a period of time, configure dynamic telemetry subscription. To stop monitoring, tear down the connection. The subscription is then automatically canceled and cannot be restored. This mitigates loads on devices and simplifies the interaction between you and devices.

As shown in [Figure 1](#EN-US_TASK_0000001513154194__en-us_task_0275777959_fig117736513266), DeviceA supports telemetry and establishes a gRPC connection with the collector. Interface 1 of DeviceA needs to be monitored, and related data needs to be reported to the collector.

**Figure 1** Network diagram of configuring gRPC-based dynamic subscription![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001563874229.png)

#### Procedure

1. Configure an SSL policy.
   
   
   
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
2. Configure AAA authentication.
   
   
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
3. Configure a source IP address to be listened during dynamic subscription, and bind the source IP address to a VPN instance.
   
   
   
   # Enable the gRPC service on DeviceA, set the source IP address to be listened during dynamic subscription to 192.168.1.1, and bind the source IP address to the VPN instance named **vpn1**.
   
   ```
   [~DeviceA] grpc
   [~DeviceA-grpc] grpc server
   [*DeviceA-grpc-server] source-ip 192.168.1.1 vpn-instance vpn1
   [*DeviceA-grpc-server] commit
   ```
4. Configure the number of the port to be listened during dynamic subscription.
   
   
   
   # Configure port 20000 to be listened during dynamic subscription.
   
   ```
   [~DeviceA-gRPC-server] server-port 20000
   [*DeviceA-gRPC-server] commit
   ```
5. Configure an SSL policy to be bound for dynamic telemetry subscription.
   
   
   
   # Bind the SSL policy **policy1** for dynamic telemetry subscription and perform SSL verification on the collector.
   
   ```
   [~DeviceA-grpc-server] ssl-policy policy1
   [*DeviceA-grpc-server] ssl-verify peer
   [*DeviceA-grpc-server] commit
   ```
6. Enable the gRPC service.
   
   
   
   # Enable the gRPC service on DeviceA.
   
   ```
   [~DeviceA-grpc-server] server enable
   [*DeviceA-grpc-server] commit
   ```

#### Verifying the Configuration

Check dynamic subscription information after completing the preceding configuration and setting parameters such as the sampling path on the collector.

```
[~DeviceA] display telemetry dynamic-subscription
------------------------------------------------------------------------------
Sub-name                    :_dyn_grpc_1_8001
Sub-id                      :32769
Request-id                  :0
Sample-interval(ms)         :60000
Heartbeat-interval(s)       :-
Suppress-redundant          :false
Delay-time(ms)              :1000
Originated-qos-marking      :0
Encoding                    :GPB 
------------------------------------------------------------------------------
SampleInterval(ms)  Depth  Sensor-path
60000               1      huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info
60000               3      huawei-cpu-memory:cpu-memory/board-memory-infos/board-memory-info
------------------------------------------------------------------------------
Dest-ip           Dest-port Vpn-name                        Protocol 
192.168.1.1       20000     vpn1                            GRPC     
------------------------------------------------------------------------------
Sub-state:SUCCESS 
------------------------------------------------------------------------------
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
gRPC
 #
 gRPC server
  source-ip 192.168.1.1 vpn-instance vpn1
  server-port 20000
  ssl-policy policy1
  ssl-verify peer
  server enable
#
return
```