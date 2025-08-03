Example for Configuring Dynamic Subscription (IPv6 Collector)
=============================================================

Example for Configuring Dynamic Subscription (IPv6 Collector)

#### Networking Requirements

As the network scale increases, you need to optimize networks and rectify faults based on device information in a timely manner. For example, if you want to monitor an interface for a period of time, configure dynamic telemetry subscription. To stop monitoring, tear down the connection. The subscription is then automatically canceled and cannot be restored. This mitigates loads on devices and simplifies the interaction between you and devices.

As shown in [Figure 1](galaxy_telemetry_cfg_0017_c.html#EN-US_TASK_0000001513154194__en-us_task_0275777959_fig117736513266), DeviceA supports telemetry and establishes a gRPC connection with the collector. Interface 1 of DeviceA needs to be monitored, and related data needs to be reported to the collector.

Both the device and the collector use IPv6 addresses.

**Figure 1** Network diagram of configuring gRPC-based dynamic subscription![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001513154234.png)

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
   
   
   
   # Enable the gRPC service on DeviceA, and set the source IP address to be listened during dynamic subscription to 2001:db8:4::1.
   
   ```
   [~DeviceA] grpc
   [*DeviceA-grpc] grpc server ipv6
   [*DeviceA-grpc-server-ipv6] source-ip 2001:db8:4::1
   [*DeviceA-grpc-server-ipv6] commit
   ```
4. Configure the number of the port to be listened during dynamic subscription.
   
   
   
   # Configure port 20000 to be listened during dynamic subscription.
   
   ```
   [~DeviceA-grpc-server-ipv6] server-port 20000
   [*DeviceA-grpc-server-ipv6] commit
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
   [~DeviceA-grpc-server-ipv6] server enable
   [*DeviceA-grpc-server-ipv6] commit
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
Dest-ip                       Dest-port Vpn-name                        Protocol 
source-ip 2001:db8:4::1       20000     _public_                        GRPC     
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
interface 100GE1/0/1
 undo portswitch
 ipv6 enable
 ipv6 address 2001:db8:4::1/64
 
#
ipv6 route-static 2001:db8:3:: 64 100GE1/0/1 2001:db8:4::2
#
grpc
 #
 grpc server ipv6
  source-ip 2001:db8:4::1
  server-port 20000
  ssl-policy policy1
  ssl-verify peer
  server enable
#
return
```