Example for Configuring a NAT Easy IP Address Pool and a GRE Tunnel to Share an Interface Address
=================================================================================================

Configure a NAT Easy IP address pool and a GRE tunnel to share an interface address, which helps conserve public addresses.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0178419521__fig525772717815), a PC on the intranet of a company is connected to DeviceA through interface 1. DeviceB is connected to server 1 on the Internet. A GRE tunnel is deployed between DeviceA and DeviceB. Packets from the internal PC to server 1 are forwarded through the tunnel interface of the GRE tunnel. The NAT service is deployed on DeviceA. The internal PC can access server 2 on the Internet after NAT is performed on DeviceA.

**Figure 1** Configuring a NAT Easy IP address pool and a GRE tunnel to share an interface address![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/2/1 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0178419771.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a GRE tunnel between DeviceA and DeviceB.
2. Configure basic NAT functions on DeviceA.
3. Configure a NAT traffic diversion policy on DeviceA.
4. Configure a NAT conversion policy on DeviceA.
5. Configure static routes on DeviceA and DeviceB to enable them to communicate.


#### Data Preparation

To complete the configuration, you need the following data:

* Source and destination IP address on each end of a GRE tunnel, and IP addresses of a tunnel interface
* Slot ID of a NAT service board, index of a service-location group, and name of a service-instance group on DeviceA
* Name and index of a NAT instance on DeviceA
* Name and number of a public address pool and Easy IP mode for public address segments in the NAT address pool on DeviceA
* ACL number, traffic classifier name, traffic behavior name, and traffic policy name on DeviceA
* Number and IP address of an interface to which a NAT traffic diversion policy is applied on DeviceA


#### Procedure

1. Create a GRE tunnel.
   
   1. Configure a GRE tunnel on DeviceA.
      
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
      [~DeviceA] interface GigabitEthernet 0/2/0
      ```
      ```
      [~DeviceA-GigabitEthernet0/2/0] ip address 172.20.1.1 255.255.255.0 
      ```
      ```
      [*DeviceA-GigabitEthernet0/2/0] binding tunnel gre
      ```
      ```
      [*DeviceA-GigabitEthernet0/2/0] commit
      ```
      ```
      [~DeviceA-GigabitEthernet0/2/0] quit
      ```
      ```
      [~DeviceA] interface tunnel 1
      ```
      ```
      [*DeviceA-Tunnel1] tunnel-protocol gre
      ```
      ```
      [*DeviceA-Tunnel1] ip address 172.22.1.1 255.255.255.0 
      ```
      ```
      [*DeviceA-Tunnel1] source GigabitEthernet 0/2/0
      ```
      ```
      [*DeviceA-Tunnel1] destination 172.20.1.2
      ```
      ```
      [*DeviceA-Tunnel1] commit
      ```
      ```
      [~DeviceA-Tunnel1] quit
      ```
   2. Configure a GRE tunnel on DeviceB.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname DeviceB
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~DeviceB] interface GigabitEthernet 0/2/0
      ```
      ```
      [~DeviceB-GigabitEthernet0/2/0] ip address 172.20.1.2 255.255.255.0 
      ```
      ```
      [*DeviceB-GigabitEthernet0/2/0] binding tunnel gre
      ```
      ```
      [*DeviceB-GigabitEthernet0/2/0] commit
      ```
      ```
      [~DeviceB-GigabitEthernet0/2/0] quit
      ```
      ```
      [~DeviceB] interface tunnel 1
      ```
      ```
      [*DeviceB-Tunnel1] tunnel-protocol gre
      ```
      ```
      [*DeviceB-Tunnel1] ip address 172.22.1.2 255.255.255.0 
      ```
      ```
      [*DeviceB-Tunnel1] source 172.20.1.2 
      ```
      ```
      [*DeviceB-Tunnel1] destination 172.20.1.1
      ```
      ```
      [*DeviceB-Tunnel1] commit
      ```
      ```
      [~DeviceB-Tunnel1] quit
      ```
2. Configure basic NAT functions on DeviceA.
   
   # In a dedicated board scenario, perform the following operations:
   
   1. Enable dedicated NAT.
      ```
      [~DeviceA] vsm on-board-mode disable
      ```
      ```
      [*DeviceA] commit
      ```
   2. Load a license file and set the number of session resources supported by the NAT service board in slot 1 to 6M.
      ```
      [~DeviceA] license
      ```
      ```
      [~DeviceA-license] active nat session-table size 6 slot 1
      ```
      ```
      [*DeviceA-license] active nat bandwidth-enhance 40 slot 1
      ```
      ```
      [*DeviceA-license] commit
      ```
      ```
      [~DeviceA-license] quit
      ```
   3. Create a service-location group and a service-instance group, and bind the NAT service board to the service-location group. Create a NAT instance named **nat1** and bind it to the service-instance group so that the NAT instance is automatically bound to the service board.
      ```
      [~DeviceA] service-location 1
      ```
      ```
      [*DeviceA-service-location-1] location slot 1
      ```
      ```
      [*DeviceA-service-location-1] commit
      ```
      ```
      [~DeviceA-service-location-1] quit
      ```
      ```
      [~DeviceA] service-instance-group group1
      ```
      ```
      [*DeviceA-service-instance-group-group1] service-location 1
      ```
      ```
      [*DeviceA-service-instance-group-group1] commit
      ```
      ```
      [~DeviceA-service-instance-group-group1] quit
      ```
      ```
      [~DeviceA] nat instance nat1 id 1
      ```
      ```
      [*DeviceA-nat-instance-nat1] service-instance-group group1
      ```
      ```
      [*DeviceA-nat-instance-nat1] commit
      ```
      ```
      [~DeviceA-nat-instance-nat1] quit
      ```
   4. Configure a NAT address pool that works in Easy IP mode.
      ```
      [~DeviceA] nat instance nat1
      ```
      ```
      [~DeviceA-nat-instance-nat1] nat address-group address-group1 group-id 1 unnumbered interface GigabitEthernet0/2/0 
      ```
      ```
      [*DeviceA-nat-instance-nat1] commit
      ```
      ```
      [~DeviceA-nat-instance-nat1] quit
      ```# In an on-board scenario, perform the following operations:
   1. Create a service-location group and a service-instance group, and bind the NAT service board to the service-location group. Create a NAT instance named **nat1** and bind it to the service-instance group so that the NAT instance is automatically bound to the service board.
      ```
      [~DeviceA] service-location 1
      ```
      ```
      [*DeviceA-service-location-1] location slot 1 
      ```
      ```
      [*DeviceA-service-location-1] commit
      ```
      ```
      [~DeviceA-service-location-1] quit
      ```
      ```
      [~DeviceA] service-instance-group group1
      ```
      ```
      [*DeviceA-service-instance-group-group1] service-location 1
      ```
      ```
      [*DeviceA-service-instance-group-group1] commit
      ```
      ```
      [~DeviceA-service-instance-group-group1] quit
      ```
      ```
      [~DeviceA] nat instance nat1 id 1
      ```
      ```
      [*DeviceA-nat-instance-nat1] service-instance-group group1
      ```
      ```
      [*DeviceA-nat-instance-nat1] commit
      ```
      ```
      [~DeviceA-nat-instance-nat1] quit
      ```
   2. Configure a NAT address pool that works in Easy IP mode.
      ```
      [~DeviceA] nat instance nat1
      ```
      ```
      [~DeviceA-nat-instance-nat1] nat address-group address-group1 group-id 1 unnumbered interface GigabitEthernet0/2/0 
      ```
      ```
      [*DeviceA-nat-instance-nat1] commit
      ```
      ```
      [~DeviceA-nat-instance-nat1] quit
      ```
3. Configure a NAT traffic diversion policy on the inbound interface of DeviceA.
   1. Configure an ACL rule named **rule1** so that traffic from the internal PC to server 2 is diverted to the NAT service board for NAT processing.
      ```
      [~DeviceA] acl 3001
      ```
      ```
      [*DeviceA-acl4-advance-3001] rule 1 permit ip destination 2.1.1.0 0.0.0.255
      ```
      ```
      [*DeviceA-acl4-advance-3001] commit
      ```
      ```
      [~DeviceA-acl4-advance-3001] quit
      ```
   2. Configure a traffic classifier named **classifier1** and define an ACL-based matching rule.
      ```
      [~DeviceA] traffic classifier classifier1
      ```
      ```
      [*DeviceA-classifier-classifier1] if-match acl 3001
      ```
      ```
      [*DeviceA-classifier-classifier1] commit
      ```
      ```
      [~DeviceA-classifier-classifier1] quit
      ```
   3. Configure a traffic behavior named **behavior1** and bind it to the NAT instance.
      ```
      [~DeviceA] traffic behavior behavior1
      ```
      ```
      [*DeviceA-behavior-behavior1] nat bind instance nat1
      ```
      ```
      [*DeviceA-behavior-behavior1] commit
      ```
      ```
      [~DeviceA-behavior-behavior1] quit
      ```
   4. Define a NAT traffic policy named **policy1** to associate the traffic classifier with the traffic behavior.
      ```
      [~DeviceA] traffic policy policy1
      ```
      ```
      [*DeviceA-trafficpolicy-policy1] classifier classifier1 behavior behavior1
      ```
      ```
      [*DeviceA-trafficpolicy-policy1] commit
      ```
      ```
      [~DeviceA-trafficpolicy-policy1] quit
      ```
   5. Apply the NAT traffic diversion policy in the interface view.
      ```
      [~DeviceA] interface GigabitEthernet 0/2/1
      ```
      ```
      [~DeviceA-GigabitEthernet0/2/1] traffic-policy policy1 inbound
      ```
      ```
      [*DeviceA-GigabitEthernet0/2/1] commit
      ```
      ```
      [~DeviceA-GigabitEthernet0/2/1] quit
      ```
4. Configure a NAT conversion policy on DeviceA. (This configuration is required only by dedicated boards.)
   
   ```
   [~DeviceA] nat instance nat1 
   ```
   ```
   [~DeviceA-nat-instance-nat1] nat outbound 3001 address-group address-group1
   ```
   ```
   [*DeviceA-nat-instance-nat1] commit
   ```
   ```
   [~DeviceA-nat-instance-nat1] quit
   ```
5. Configure static routes.
   
   1. Configure a static route on DeviceA so that the internal PC can access server 1 at 1.1.1.1 through the GRE tunnel.
      
      ```
      [~DeviceA] ip route-static 1.1.1.0 255.255.255.0 Tunnel1
      ```
      ```
      [*DeviceA] commit
      ```
   2. Configure another static route on DeviceA so that the internal PC can access server 2 at 2.1.1.1 through GE 0/2/0.
      ```
      [~DeviceA] ip route-static 2.1.1.0 255.255.255.0 172.20.1.2
      ```
      ```
      [*DeviceA] commit
      ```
   3. Configure a static route on DeviceB so that server 1 can access the internal PC at 10.1.1.1 through the GRE tunnel.
      
      ```
      [~DeviceB] ip route-static 10.1.1.0 255.255.255.0 Tunnel1
      ```
      ```
      [*DeviceB] commit
      ```

#### Configuration Files

DeviceA configuration file

```
#
sysname DeviceA
#
interface GigabitEthernet 0/2/0  
 undo shutdown  
 ip address 172.20.1.1 255.255.255.0  
 binding tunnel gre 
# 
interface Tunnel1  
 tunnel-protocol gre  
 ip address 172.22.1.1 255.255.255.0  
 source GigabitEthernet 0/2/0  
 destination 172.20.1.2 
\
vsm on-board-mode disable//This configuration is generated in the dedicated board scenario.
# 
license  
 active nat session-table size 6 slot 1//This configuration is generated in the dedicated board scenario.
 active nat bandwidth-enhance 40 slot 1//This configuration is generated in the dedicated board scenario.
# 
service-location 1  
 location slot 1
# 
service-instance-group group1  
 service-location 1 
# 
nat instance nat1 id 1  
 service-instance-group group1  
 nat address-group address-group1 group-id 1 unnumbered interface GigabitEthernet 0/2/0   
 nat outbound 3001 address-group address-group1//This configuration is generated in the dedicated board scenario.
# 
acl number 3001  
 rule 1 permit ip destination 2.1.1.0 0.0.0.255 
# 
traffic classifier classifier1 operator or
 if-match acl 3001 precedence 1
# 
traffic behavior behavior1  
 nat bind instance nat1 
# 
traffic policy policy1  
 share-mode
 classifier classifier1 behavior behavior1 precedence 1
# 
interface GigabitEthernet 0/2/1  
 undo shutdown  
 ip address 10.1.1.2 255.255.255.0  
 traffic-policy policy1 inbound 
# 
ip route-static 1.1.1.0 255.255.255.0 Tunnel1 
ip route-static 2.1.1.0 255.255.255.0 172.20.1.2
# 
return
```

DeviceB configuration file

```
#
 sysname DeviceB
#
interface GigabitEthernet 0/2/0   
 undo shutdown  
 ip address 172.20.1.2 255.255.255.0  
 binding tunnel gre 
# 
interface Tunnel1  
 tunnel-protocol gre  
 ip address 172.22.1.2 255.255.255.0  
 source 172.20.1.2
 destination 172.20.1.1 
#
ip route-static 10.1.1.0 255.255.255.0 Tunnel1
#
return
```