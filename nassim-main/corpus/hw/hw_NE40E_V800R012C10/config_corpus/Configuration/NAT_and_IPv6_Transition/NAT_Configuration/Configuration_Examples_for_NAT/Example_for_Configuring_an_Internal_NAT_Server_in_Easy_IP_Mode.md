Example for Configuring an Internal NAT Server in Easy IP Mode
==============================================================

This section provides an example for configuring bidirectional NAT and using easy IP to create an internal server so that traffic of public network users and the public network server can be forwarded through NAT-Device.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172374648__w1), an enterprise deploys an FTP server on the Internet, and NAT-Device functions as the gateway of the enterprise network. To secure traffic transmission, the enterprise wants that traffic exchanged between public network users and the FTP server is forwarded by NAT-Device and that public network users and the FTP server are not aware of IP addresses of one another.

**Figure 1** Networking for configuring bidirectional NAT and using easy IP to create an internal server![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/2/1 and GE 0/2/2, respectively.


  
![](images/fig_dc_ne_nat_cfg_00750001.png)

#### Configuration Roadmap

1. Configure basic NAT functions.
2. Configure an internal server.
3. Enable the FTP ALG function.
4. Configure a NAT diversion policy.
5. Apply the NAT diversion policy.

#### Data Preparation

* NAT instance names (**nat1** and **nat2**) and indexes (1 and 2)
* NAT-Device's address pool names (address-group1 and address-group2) and address pool numbers (1 and 2), and Easy IP address range
* ACL number (3001)
* Names (GE 0/2/1 and GE 0/2/2) and IP addresses (1.1.1.1/24 and 2.1.1.1/24) of interfaces that apply a NAT diversion policy

#### Procedure

1. Configure basic NAT functions.
   1. Create NAT instances named **nat1** and **nat2**.
   2. Assign IP addresses to interfaces.
      
      
      ```
      [~NAT-Device] interface gigabitEthernet 0/2/1
      [~NAT-Device-GigabitEthernet0/2/1] ip address 1.1.1.1 24
      [*NAT-Device-GigabitEthernet0/2/1] commit
      [~NAT-Device-GigabitEthernet0/2/1] quit
      [~NAT-Device] interface gigabitEthernet 0/2/2
      [~NAT-Device-GigabitEthernet0/2/2] ip address 2.1.1.1 24
      [*NAT-Device-GigabitEthernet0/2/2] commit
      [~NAT-Device-GigabitEthernet0/2/2] quit
      ```
   3. Configure a NAT address pool in Easy IP mode.
      
      
      ```
      [~NAT-Device] nat instance nat1 id 1
      [~NAT-Device-nat-instance-nat1] nat address-group address-group1 group-id 1 unnumbered interface GigabitEthernet0/2/1
      [*NAT-Device-nat-instance-nat1] commit
      [~NAT-Device-nat-instance-nat1] quit
      [~NAT-Device] nat instance nat2 id 2
      [~NAT-Device-nat-instance-nat2] nat address-group address-group2 group-id 2 unnumbered interface GigabitEthernet0/2/2
      [*NAT-Device-nat-instance-nat2] commit
      [~NAT-Device-nat-instance-nat2] quit
      ```
2. Configure an internal server.
   
   
   ```
   [~NAT-Device] nat instance nat1 id 1
   [~NAT-Device-nat-instance-nat1] nat server protocol tcp global unnumbered interface GigabitEthernet0/2/1 ftp inside 2.1.1.2 ftp
   [*NAT-Device-nat-instance-nat1] commit
   [~NAT-Device-nat-instance-nat1] quit
   [~NAT-Device] nat instance nat2 id 2
   [~NAT-Device-nat-instance-nat2] nat server protocol tcp global unnumbered interface GigabitEthernet0/2/2 ftp inside 1.1.1.2 ftp
   [*NAT-Device-nat-instance-nat2] commit
   [~NAT-Device-nat-instance-nat2] quit
   ```
3. Enable the FTP ALG function.
   
   
   ```
   [~NAT-Device] nat instance nat1
   [~NAT-Device-nat-instance-nat1] nat alg ftp  
   [*NAT-Device-nat-instance-nat1] commit 
   [~NAT-Device-nat-instance-nat1] quit
   [~NAT-Device] nat instance nat2
   [~NAT-Device-nat-instance-nat2] nat alg ftp  
   [*NAT-Device-nat-instance-nat2] commit 
   [~NAT-Device-nat-instance-nat2] quit
   ```
4. Configure a NAT diversion policy. Configure an ACL numbered 3001, an ACL rule numbered 1, and an ACL-based traffic classification rule to allow hosts to access the Internet.
   
   
   ```
   [~NAT-Device] acl 3001
   [*NAT-Device-acl4-advance-3001] rule 1 permit ip source any
   [*NAT-Device-acl4-advance-3001] commit
   [~NAT-Device-acl4-advance-3001] quit
   ```
5. Apply the NAT diversion policy. Apply the ACL-based traffic classification rule to the view of the outbound interface named GE 0/2/1 and GE 0/2/2.
   
   
   ```
   [~NAT-Device] interface gigabitEthernet 0/2/1
   [*NAT-Device-GigabitEthernet0/2/1] nat bind acl 3001 instance nat1
   [*NAT-Device-GigabitEthernet0/2/1] commit
   [~NAT-Device-GigabitEthernet0/2/1] quit
   [~NAT-Device] interface gigabitEthernet 0/2/2
   [*NAT-Device-GigabitEthernet0/2/2] nat bind acl 3001 instance nat2
   [*NAT-Device-GigabitEthernet0/2/2] commit
   [~NAT-Device-GigabitEthernet0/2/2] quit
   ```
6. Verify the configuration.
   
   
   
   # Run the [**display nat server-map**](cmdqueryname=display+nat+server-map) command to check server mapping entries of all users accessing the internal server.
   
   ```
   [~NAT-Device] display nat server-map
   This operation will take a few minutes. Press 'Ctrl+C' to break ...     
   Slot: 3 
   Total number:  4.     
     NAT Instance: nat1       
     Protocol:TCP, VPN:--->-     
     Server reverse:ANY->1.1.1.1:21[2.1.1.2:21]                        
     Tag:0x0, TTL:-, Left-Time:-         
     CPE IP:2.1.1.2                 
     extendable:false                                               
     NAT Instance: nat1  
     Protocol:TCP, VPN:--->-    
     Server:2.1.1.2:21[1.1.1.1:21]->ANY                                            
     Tag:0x0, TTL:-, Left-Time:-      
     CPE IP:2.1.1.2           
     extendable:false                                              
     NAT Instance: nat2   
     Protocol:TCP, VPN:--->-      
     Server reverse:ANY->2.1.1.1:21[1.1.1.2:21]                         
     Tag:0x0, TTL:-, Left-Time:-       
     CPE IP:1.1.1.2         
     extendable:false
     NAT Instance: nat2         
     Protocol:TCP, VPN:--->-     
     Server:1.1.1.2:21[2.1.1.1:21]->ANY    
     Tag:0x0, TTL:-, Left-Time:-    
     CPE IP:1.1.1.2
     extendable:false                 
     ---------------------------------------------------------------------------
   ```

#### Configuration File

```
# 
sysname NAT-Device
#
service-location 1 
 location slot 3
# 
service-instance-group group1  
 service-location 1 
#
nat instance nat1 id 1
 service-instance-group group1
 nat address-group address-group1 group-id 1 unnumbered interface GigabitEthernet0/2/1
 nat server protocol tcp global unnumbered interface GigabitEthernet0/2/1 ftp inside 2.1.1.2 ftp
 nat alg ftp
# 
nat instance nat2 id 2
 service-instance-group group1
 nat address-group address-group2 group-id 2 unnumbered interface GigabitEthernet0/2/2
 nat server protocol tcp global unnumbered interface GigabitEthernet0/2/2 ftp inside 1.1.1.2 ftp
 nat alg ftp
#
acl number 3001
 rule 1 permit ip source any  
# 
interface GigabitEthernet 0/2/1 
 undo shutdown 
 ip address 1.1.1.1 24
 nat bind acl 3001 instance nat1 
# 
interface GigabitEthernet 0/2/2 
 undo shutdown 
 ip address 2.1.1.1 24
 nat bind acl 3001 instance nat2
#
return
```