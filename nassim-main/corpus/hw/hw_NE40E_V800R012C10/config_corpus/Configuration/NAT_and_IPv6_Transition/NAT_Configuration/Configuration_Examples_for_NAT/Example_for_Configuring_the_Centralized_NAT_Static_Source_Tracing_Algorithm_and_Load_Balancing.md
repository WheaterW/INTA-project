Example for Configuring the Centralized NAT Static Source Tracing Algorithm and Load Balancing
==============================================================================================

This section provides an example for configuring the centralized NAT source tracing algorithm and load balancing, which implements many-to-many translation between a company's private IP addresses and public IP addresses and allows PCs only on a specified network segment to access the Internet.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.

In [Figure 1](#EN-US_TASK_0000001139936997__en-us_task_0172374612_fig_dc_ne_cfg_nat_005701), the Router performs the NAT function to help PCs within the enterprise network access the Internet. The Router uses GE 0/2/0 to connect to the enterprise network. The Router is connected to the Internet through GE 0/2/1. The enterprise is assigned 100 public IP addresses of 11.11.11.101/32 through 11.11.11.200/32. When NAT load balancing is not used, a NAT service can be bound to only one CPU of a service board. As a result, the forwarding performance of a service board in a NAT instance will easily reach the upper limit. In NAT load balancing mode, multiple service board CPUs can be bound to a NAT instance to increase the NAT bandwidth of the same type of users. This saves instance configurations and reduces manual allocation of address pools and manual intervention on traffic. In addition, by using the static source tracing algorithm to find the private IP address based on the public IP address and port number, the device does not need to send source tracing logs to record information about intranet users' access to the external network, which enhances network security.

[Figure 1](#EN-US_TASK_0000001139936997__en-us_task_0172374612_fig_dc_ne_cfg_nat_005701) shows IP addresses of interfaces. The configuration requirements are as follows:

* Only PCs on the network segment of 192.168.10.0/24 can access the Internet.
* Many-to-many NAT needs to be performed for IP addresses between the private and public networks.

**Figure 1** Network diagram of centralized NAT load balancing![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/2/0 and GE0/2/1, respectively.


  
![](images/fig_dc_ne_cfg_nat_0120.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a NAT load balancing instance.
2. Configure a NAT traffic diversion policy.
3. Configure a NAT conversion policy.
4. Configure the NAT static source tracing algorithm mapping.
5. Bind the NAT static source tracing algorithm to the NAT instance.

#### Data Preparation

To complete the configuration, you need the following data:

* NAT load balancing instance
* Information about the NAT traffic diversion policy
* IDs of the private and public address pools for the static source tracing algorithm
* Private and public address segments of the static source tracing algorithm
* Port number range and port range size of the public address pool in the static source tracing algorithm


#### Procedure

1. Create a NAT load balancing instance.
   
   1. Set the maximum number of sessions that can be created on the CPU of the NAT service board to 6M.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname CGNA
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~CGNA] vsm on-board-mode disable
      ```
      ```
      [*CGNA] commit
      ```
      ```
      [~CGNA] license
      ```
      ```
      [~CGNA-license] active nat session-table size 6 slot 1
      ```
      ```
      [*CGNA-license] active nat session-table size 6 slot 2 
      ```
      ```
      [*CGNA-license] active nat bandwidth-enhance 40 slot 1
      ```
      ```
      [*CGNA-license] active nat bandwidth-enhance 40 slot 2
      ```
      ```
      [*CGNA-license] commit
      ```
      ```
      [~CGNA-license] quit
      ```
   2. Create a service-instance group named **groupa** and bind it to service-location groups **1** and **2**.
      
      ```
      [~CGNA] service-location 1
      ```
      ```
      [*CGNA-service-location-1] location slot 1
      ```
      ```
      [*CGNA-service-location-1] commit
      ```
      ```
      [~CGNA-service-location-1] quit
      ```
      ```
      [~CGNA] service-location 2
      ```
      ```
      [*CGNA-service-location-2] location slot 2
      ```
      ```
      [*CGNA-service-location-2] commit
      ```
      ```
      [~CGNA-service-location-2] quit
      ```
      ```
      [~CGNA] service-instance-group groupa
      ```
      ```
      [*CGNA-service-instance-group-groupa] service-location 1
      ```
      ```
      [*CGNA-service-instance-group-groupa] service-location 2
      ```
      ```
      [*CGNA-service-instance-group-groupa] commit
      ```
      ```
      [~CGNA-service-instance-group-groupa] quit
      ```
   3. Bind a NAT instance named **cpe1** to the service-instance-group named **groupa**.
      
      ```
      [~CGNA] nat instance cpe1 id 11
      ```
      ```
      [*CGNA-nat-instance-cpe1] service-instance-group groupa
      ```
      ```
      [*CGNA-nat-instance-cpe1] commit
      ```
      ```
      [~CGNA-nat-instance-cpe1] quit
      ```
2. Configure a NAT traffic diversion policy.
   
   1. Configure an ACL numbered **3001** and an ACL rule numbered **1** to allow hosts only within the network segment 192.168.10.0/24 to access the Internet.
      
      ```
      [~CGNA] acl 3001
      ```
      ```
      [*CGNA-acl4-advance-3001] rule 1 permit ip source 192.168.10.0 0.0.0.255
      ```
      ```
      [*CGNA-acl4-advance-3001] commit
      ```
      ```
      [~CGNA-acl4-advance-3001] quit
      ```
   2. Configure a traffic classifier.
      
      ```
      [~CGNA] traffic classifier c1
      ```
      ```
      [*CGNA-classifier-c1] if-match acl 3001
      ```
      ```
      [*CGNA-classifier-c1] commit
      ```
      ```
      [~CGNA-classifier-c1] quit
      ```
   3. Configure a traffic behavior named **b1**, which binds traffic to the NAT instance named **cpe1**.
      
      ```
      [~CGNA] traffic behavior b1
      ```
      ```
      [*CGNA-behavior-b1] nat bind instance cpe1
      ```
      ```
      [*CGNA-behavior-b1] commit
      ```
      ```
      [~CGNA-behavior-b1] quit
      ```
   4. Define a NAT policy to associate the ACL rule with the traffic behavior.
      
      ```
      [~CGNA] traffic policy p1
      ```
      ```
      [*CGNA-trafficpolicy-p1] classifier c1 behavior b1
      ```
      ```
      [*CGNA-trafficpolicy-p1] commit
      ```
      ```
      [~CGNA-trafficpolicy-p1] quit
      ```
   5. Apply the NAT traffic diversion policy in the interface view.
      
      ```
      [~CGNA] interface gigabitEthernet 0/2/0
      ```
      ```
      [~CGNA-GigabitEthernet0/2/0] traffic-policy p1 inbound
      ```
      ```
      [*CGNA-GigabitEthernet0/2/0] commit
      ```
      ```
      [~CGNA-GigabitEthernet0/2/0] quit
      ```
3. Configure a group of static source tracing algorithm parameters. The private address pool contains IP addresses 192.168.10.128 through 192.168.10.255, the public address pool contains IP addresses 11.11.11.101 through 11.11.11.200, the port numbers are in the range of 256 to 1279, and the port range size is 256.
   
   ```
   [~HUAWEI] nat static-mapping
   ```
   ```
   [*HUAWEI-nat-static-mapping] inside-pool 1
   ```
   ```
   [*HUAWEI-nat-static-mapping-inside-pool-1] section 1 192.168.10.128 192.168.10.255
   ```
   ```
   [*HUAWEI-nat-static-mapping-inside-pool-1] quit
   ```
   ```
   [*HUAWEI-nat-static-mapping] global-pool 1
   ```
   ```
   [*HUAWEI-nat-static-mapping-global-pool-1] section 1 11.11.11.101 11.11.11.200
   ```
   ```
   [*HUAWEI-nat-static-mapping-global-pool-1] quit
   ```
   ```
   [*HUAWEI-nat-static-mapping] static-mapping 10 inside-pool 1 global-pool 1 port-range 256 1279 port-size 256
   ```
   ```
   [*HUAWEI-nat-static-mapping] commit
   ```
   ```
   [~HUAWEI-nat-static-mapping] quit
   ```
4. Enable the static source tracing algorithm in the NAT instance named **cpe1** and set the algorithm parameter ID to **10**.
   
   ```
   [~HUAWEI] nat instance cpe1
   ```
   ```
   [~HUAWEI-nat-instance-cpe1] nat bind static-mapping 10
   ```
   ```
   [*HUAWEI-nat-instance-cpe1] commit
   ```
   ```
   [~HUAWEI-nat-instance-cpe1] quit
   ```

#### Configuration Files

CGNA configuration file

```
#
sysname CGNA
#
vsm on-board-mode disable
#
license
 active nat session-table size 6 slot 1
 active nat session-table size 6 slot 2
 active nat bandwidth-enhance 40 slot 1
 active nat bandwidth-enhance 40 slot 2
#
nat static-mapping
 inside-pool 1
  section 1 192.168.10.128 192.168.10.255
 global-pool 1
  section 1 11.11.11.101 11.11.11.200
 static-mapping 10 inside-pool 1 global-pool 1 port-range 256 1279 port-size 256
#
service-location 1      
 location slot 1
#
service-location 2      
 location slot 2
#
service-instance-group groupa      
 service-location 1      
 service-location 2
#
nat instance cpe1 id 11     
 service-instance-group groupa      
 nat bind static-mapping 10
#
acl number 3001
 rule 1 permit ip source 192.168.10.0 0.0.0.255
#
traffic classifier c1 operator or
 if-match acl 3001 precedence 1 
#
traffic behavior b1
 nat bind instance cpe1
#
traffic policy p1
 share-mode
 classifier c1 behavior b1 precedence 1 
#
interface GigabitEthernet 0/2/0
 ip address 192.168.10.1 255.255.255.0
 undo shutdown
 traffic-policy p1 inbound
#
return

```