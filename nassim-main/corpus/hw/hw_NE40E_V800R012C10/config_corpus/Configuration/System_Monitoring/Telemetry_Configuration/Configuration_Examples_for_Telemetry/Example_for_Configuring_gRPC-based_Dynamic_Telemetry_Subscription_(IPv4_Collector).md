Example for Configuring gRPC-based Dynamic Telemetry Subscription (IPv4 Collector)
==================================================================================

This section provides an example for configuring dynamic telemetry subscription using gRPC to send sampled data in a scenario where an IPv4 destination collector is deployed.

#### Networking Requirements

As the network scale increases, users need to optimize networks and rectify faults based on device information. For example, if a user wants to monitor an interface for a period of time, dynamic telemetry subscription can be configured. To stop monitoring, tear down the connection. The subscription is automatically canceled and cannot be restored. This avoids long-term loads on devices and simplifies the interaction between users and devices.

As shown in [Figure 1](#EN-US_TASK_0139427990__fig_dc_vrp_telemetry_cfg_001801), telemetry-capable DeviceA establishes a gRPC connection with the collector. It is required that interface1 of DeviceA be monitored and data be sent to the collector as required.

**Figure 1** Configuring gRPC-based dynamic telemetry subscription![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/1 and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_cfg_telemetry_00181.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a local user, and add the user to the administrator group. Configure the service type of the user.
2. Configure an SSL policy.
3. Configure the gRPC server function.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of interface1 to be listened for: 192.168.1.1 (interface1 on DeviceA and the collector must be routable.)
* Number of the port to be listened for: 20000

#### Procedure

1. Configure an IP address and a routing protocol for each interface so that all devices can communicate at the network layer.
2. Create a local user, and add the user to the administrator group. Configure the service type of the user.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] aaa
   ```
   ```
   [~DeviceA-aaa] local-user hhww123 password
   Please configure the password (8-128)
   Enter Password:
   Confirm Password:
   ```
   ```
   [*DeviceA-aaa] local-user hhww123 service-type http
   ```
   ```
   [*DeviceA-aaa] local-user hhww123 user-group manage-ug
   ```
   ```
   [~DeviceA-aaa] commit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
3. Configure an SSL policy.
   
   
   
   # Configure a PKI realm.
   
   ```
   [~DeviceA] pki domain domain1
   ```
   ```
   [*DeviceA-pki-domain-domain1] commit
   ```
   ```
   [~DeviceA-pki-domain-domain1] quit
   ```
   ```
   [~DeviceA] pki import-certificate ca domain domain1 filename test.crt
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The CA certificate is used as an example. During the actual configuration, you need to replace **ca** and **test.crt** with the existing certificate type and name on the device. You can directly upload the certificate to the device for installation, or apply for and download the certificate for installation. For details, see "Obtaining a Certificate" in *PKI Configuration*.
   
   # Configure an SSL policy and bind it to the PKI realm.
   
   ```
   [~DeviceA] ssl policy policy1
   ```
   ```
   [*DeviceA-ssl-policy-policy1] pki-domain domain1
   ```
   ```
   [*DeviceA-ssl-policy-policy1] commit
   ```
   ```
   [~DeviceA-ssl-policy-policy1] quit
   ```
4. Configure the gRPC server function.
   
   
   ```
   [~DeviceA] interface GigabitEthernet0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] ip address 192.168.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] grpc
   ```
   ```
   [*DeviceA-grpc] grpc server
   ```
   ```
   [*DeviceA-grpc-server] source-ip 192.168.1.1
   ```
   ```
   [*DeviceA-grpc-server] server-port 20000
   ```
   ```
   [*DeviceA-grpc-server] ssl-policy policy1
   ```
   ```
   [*DeviceA-grpc-server] ssl-verify peer
   ```
   
   
   ```
   [*DeviceA-grpc-server] server enable
   ```
   
   
   ```
   [*DeviceA-grpc-server] commit
   ```

#### Configuration Files

DeviceA configuration file

```
#
sysname DeviceA
# 
aaa
  local-user hhww123 password irreversible-cipher $1c$%L%X:Jn3hY$5^%T5I\4HG>j|i~s,{.@FpH*2XGM\R;7#$"\i!L0$
  local-user hhww123 service-type http
  local-user hhww123 user-group manage-ug
#
interface GigabitEthernet0/1/1
 undo shutdown
 ip address 192.168.1.1 255.255.255.0
#
ssl policy policy1
 pki-domain domain1
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
pki domain domain1
#
return
```