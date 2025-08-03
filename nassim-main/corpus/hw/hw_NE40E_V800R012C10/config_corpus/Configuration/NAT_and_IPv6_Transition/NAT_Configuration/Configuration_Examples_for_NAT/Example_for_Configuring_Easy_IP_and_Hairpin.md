Example for Configuring Easy IP and Hairpin
===========================================

This section provides an example for configuring NAT Easy IP on an outbound interface and the hairpin function. The function combination allows internal hosts to access the Internet through the outbound NAT function and to access an internal server that is created using the easy IP function.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172374657__fig_dc_ne_cfg_nat_005701), a host on a private network is connected to the Internet through the Router on which NAT traffic distribution on an outbound interface is configured. The host uses a public IP address to access an internal server that is created in Easy IP mode on the same NAT device. The Router is connected to the private network through 0/2/1. The Router's GE 0/2/2 is connected to the Internet. The public IP addresses 11.1.1.2/32 and 11.1.1.3/32 are available.

[Figure 1](#EN-US_TASK_0172374657__fig_dc_ne_cfg_nat_005701) shows IP addresses of interfaces. The configuration requirements are as follows:

* PCs on the private network segment of 10.1.1.4/32 can access the Internet.
* PCs on the private network segment of 10.1.1.4/32 can access the internal server using a public IP address.
* External Internet computers can access the internal server using a public IP address.

**Figure 1** Scenario in which NAT traffic distribution on an outbound interface, easy IP, and the hairpin function are configured![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/2/1 and GE 0/2/2, respectively.


  
![](images/fig_dc_ne_cfg_nat_0111.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic NAT functions.
2. Configure an internal server in Easy IP mode.
3. Configure a NAT traffic diversion policy.
4. Configure a NAT traffic conversion policy.

#### Data Preparation

To complete the configuration, you need the following data:

* NAT instance name (nat1) and index (1)
* NAT Device's NAT address pool name (address-group1), address pool number (1), a range of public IP addresses (11.1.1.2 and 11.1.1.3)
* ACL number (3001) to match traffic that a private network host sends to the Internet
* ACL number (3001) to match traffic that a private network host sends to the private network server
* Name and IP address of each interface to which a NAT traffic diversion policy is applied


#### Procedure

1. Configure basic NAT functions.
   1. Configure a NAT instance named **nat1**.
      
      
      ```
      [~NAT Device] service-location 1
      ```
      ```
      [*NAT Device-service-location-1] location slot 3
      ```
      ```
      [*NAT Device-service-location-1] commit
      ```
      ```
      [~NAT Device-service-location-1] quit
      ```
      ```
      [~NAT Device] service-instance-group group1
      ```
      ```
      [*NAT Device-service-instance-group-group1] service-location 1
      ```
      ```
      [*NAT Device-service-instance-group-group1] commit
      ```
      ```
      [~NAT Device-service-instance-group-group1] quit
      ```
      ```
      [~NAT Device] nat instance nat1 id 1
      ```
      ```
      [*NAT Device-nat-instance-nat1] service-instance-group group1
      ```
      ```
      [*NAT Device-nat-instance-nat1] commit
      ```
      ```
      [~NAT Device-nat-instance-nat1] quit
      ```
   2. Configure a NAT address pool and specify a range of IP addresses 11.1.1.2 to 11.1.1.3 in the pool.
      
      
      ```
      [~NAT Device] nat instance nat1
      ```
      ```
      [~NAT Device-nat-instance-nat1] nat address-group address-group1 group-id 1 11.1.1.2 11.1.1.3
      ```
      ```
      [*NAT Device-nat-instance-nat1] commit
      ```
      ```
      [~NAT Device-nat-instance-nat1] quit
      ```
2. Configure a NAT server in Easy IP mode.
   1. Configure the public network interface.
      
      
      ```
      [~NAT Device] interface gigabitEthernet 0/2/2
      ```
      ```
      [~NAT Device-GigabitEthernet0/2/2] ip address 11.1.1.1 255.255.255.0
      ```
      ```
      [*NAT Device-GigabitEthernet0/2/2] commit
      ```
      ```
      [~NAT Device-GigabitEthernet0/2/2] quit
      ```
   2. Configure an internal server and the public IP address of the server to reuse the IP address of interface 0/2/2. In this example, TCP port 80 is used on an internal server.
      
      
      ```
      [~NAT Device] nat instance nat1
      ```
      ```
      [~NAT Device-nat-instance-nat1] nat server protocol tcp global unnumbered interface GigabitEthernet0/2/2 80 inside 10.1.1.254 80
      ```
      ```
      [*NAT Device-nat-instance-nat1] commit
      ```
      ```
      [~NAT Device-nat-instance-nat1] quit
      ```
3. Configure a NAT traffic diversion policy on an outbound interface.
   1. Configure an ACL to allow the PC at 10.1.1.4/32 to access the Internet and communicate with the private network server.
      
      
      ```
      [~NAT Device] acl 3001
      ```
      ```
      [*NAT Device-acl4-advance-3001] rule 1 permit ip source 10.1.1.4 0.0.0.0
      ```
      ```
      [*NAT Device-acl4-advance-3001] rule 2 permit tcp source 10.1.1.254 0.0.0.0
      ```
      ```
      [*NAT Device-acl4-advance-3001] commit
      ```
      ```
      [~NAT Device-acl4-advance-3001] quit
      ```
   2. Configure a NAT diversion policy on the public network outbound interface.
      
      
      ```
      [~NAT Device] interface gigabitEthernet 0/2/2
      ```
      ```
      [*NAT Device-GigabitEthernet0/2/2] nat bind acl 3001 instance nat1
      ```
      ```
      [*NAT Device-GigabitEthernet0/2/2] commit
      ```
      ```
      [~NAT Device-GigabitEthernet0/2/2] quit
      ```
   3. Configure a NAT diversion policy on the private network outbound interface.
      
      
      ```
      [~NAT Device] interface gigabitEthernet 0/2/1
      ```
      ```
      [*NAT Device-GigabitEthernet0/2/1] ip address 10.1.1.2 255.255.255.0
      ```
      ```
      [*NAT Device-GigabitEthernet0/2/1] nat bind acl 3001 instance nat1
      ```
      ```
      [*NAT Device-GigabitEthernet0/2/1] commit
      ```
      ```
      [~NAT Device-GigabitEthernet0/2/1] quit
      ```

#### Configuration Files

```
# 
sysname NAT Device 
# 
service-location 1  
 location slot 3
# 
service-instance-group group1       
 service-location 1       
# 
acl number 3001 
 rule 1 permit ip source 10.1.1.4 0.0.0.0
 rule 2 permit tcp source 10.1.1.254 0.0.0.0
#
nat instance nat1 id 1       
 service-instance-group group1       
 nat address-group address-group1 group-id 1 11.1.1.2 11.1.1.3
 nat server protocol tcp global unnumbered interface GigabitEthernet0/2/2 80 inside 10.1.1.254 80
#
interface gigabitEthernet 0/2/1
 undo shutdown 
 ip address 10.1.1.2 255.255.255.0
 nat bind acl 3001 instance nat1
# 
interface gigabitEthernet 0/2/2
 undo shutdown 
 ip address 11.1.1.1 255.255.255.0
 nat bind acl 3001 instance nat1
# 
return 
```