Example for Configuring gRPC-based Dynamic Telemetry Subscription (IPv6 Collector)
==================================================================================

This section provides an example for configuring dynamic telemetry subscription using gRPC to send sampled data in a scenario where an IPv6 destination collector is deployed.

#### Networking Requirements

As the network scale increases, users need to optimize networks and rectify faults based on device information. For example, if a user wants to monitor an interface for a period of time, dynamic telemetry subscription can be configured. To stop monitoring, tear down the connection. The subscription is automatically canceled and cannot be restored. This avoids long-term loads on devices and simplifies the interaction between users and devices.

On the network shown in [Figure 1](#EN-US_TASK_0175158822__fig_dc_vrp_telemetry_cfg_001801), telemetry-capable DeviceA establishes a gRPC connection with the collector. It is required that interface1 of DeviceA be monitored and data be sent to the collector as required.

DeviceA communicates with the collector using an IPv6 address.

**Figure 1** Configuring gRPC-based dynamic telemetry subscription![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/1 and GE0/1/2, respectively.


  
![](figure/en-us_image_0175163847.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a local user, and add the user to the administrator group. Configure a service type for the user.
2. Configure an SSL policy.
3. Configure the gRPC IPv6 server function.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of interface1 to be listened for: 2001:db8:4::1 (interface1 on DeviceA and the collector must be routable.)
* Number of the port to be listened for: 20000

#### Procedure

1. Configure an IP address and a routing protocol for each interface so that all devices can communicate at the network layer. (The configuration details are not provided here.)
2. Create a local user, and add the user to the administrator group. Configure a service type for the user.
   
   
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
   ```
   ```
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
   
   
   
   # Configure a PKI domain.
   
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
   
   # Configure an SSL policy and bind it to the PKI domain.
   
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
4. Configure the gRPC IPv6 server function.
   
   
   ```
   [~DeviceA] interface GigabitEthernet0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ipv6 address 2001:db8:4::1 64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] ipv6 route-static 2001:db8:3:: 64 GigabitEthernet0/1/1 2001:db8:4::2
   ```
   ```
   [*DeviceA] grpc
   ```
   ```
   [*DeviceA-grpc] grpc server ipv6
   ```
   ```
   [*DeviceA-grpc-server-ipv6] source-ip 2001:db8:4::1
   ```
   
   
   ```
   [*DeviceA-grpc-server-ipv6] server-port 20000
   ```
   ```
   [*DeviceA-grpc-server-ipv6] ssl-policy policy1
   ```
   ```
   [*DeviceA-grpc-server-ipv6] ssl-verify peer
   ```
   
   
   ```
   [*DeviceA-grpc-server-ipv6] server enable
   ```
   ```
   [*DeviceA-grpc-server-ipv6] commit
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
 ipv6 enable
 ipv6 address 2001:DB8:4::1/64
#
ipv6 route-static 2001:DB8:3:: 64 GigabitEthernet0/1/1 2001:DB8:4::2
#
ssl policy policy1
 pki-domain domain1
#
grpc
 #
 grpc server ipv6
  source-ip 2001:DB8:4::1
  server-port 20000
  ssl-policy policy1
  ssl-verify peer
  server enable
#
pki domain domain1
#
return
```