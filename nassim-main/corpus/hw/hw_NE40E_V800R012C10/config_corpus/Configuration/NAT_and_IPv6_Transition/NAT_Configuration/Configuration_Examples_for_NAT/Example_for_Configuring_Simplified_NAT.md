Example for Configuring Simplified NAT
======================================

This section provides an example for configuring the simplified NAT function to implement many-to-many IP address translation between private and public networks and allow PCs on a specified network segment to access the Internet.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172374585__fig_dc_ne_cfg_nat_005701), the Router performs the NAT function to help PCs within the enterprise network access the Internet. The Router uses GE0/2/0 to connect to the enterprise network and uses GE0/2/1 to connect to the Internet. The enterprise is assigned five public IP addresses: 11.11.11.101/32 through 11.11.11.105/32.

[Figure 1](#EN-US_TASK_0172374585__fig_dc_ne_cfg_nat_005701) shows IP addresses of interfaces. The configuration requirements are as follows:

* Only PCs on the network segment of 192.168.10.0/24 can access the Internet.
* Many-to-many NAT needs to be performed for IP addresses between the private and public networks.

**Figure 1** NAT networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/2/0 and GE0/2/1, respectively.


  
![](images/fig_dc_ne_cfg_nat_0009.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic simplified NAT functions.
2. Configure a simplified NAT traffic diversion policy.

#### Data Preparation

To complete the configuration, you need the following data:

* NAT instance name (nat1) and index (1)
* NATA's NAT address pool name (address-group1), address pool number (1), a range of public IP addresses (11.11.11.101 through 11.11.11.105)
* ACL number: 3001
* Name and IP address of the interface to which a NAT traffic diversion policy is applied


#### Procedure

1. Configure basic NAT functions.
   1. Create a NAT instance named **nat1**.
      
      
      ```
      [~NATA] nat instance nat1 id 1 simple-configuration
      ```
      ```
      [*NATA-nat-instance-nat1] commit
      ```
      ```
      [~NATA-nat-instance-nat1] quit
      ```
   2. Configure a NAT address pool with addresses ranging from 11.11.11.101 to 11.11.11.105.
      
      
      ```
      [~NATA] nat address-group address-group1 group-id 1 11.11.11.101 11.11.11.105
      ```
      ```
      [*NATA] commit
      ```
2. Configure a NAT traffic diversion policy. Simplified NAT supports only outbound interface-based traffic diversion.
   1. Configure an ACL numbered **3001** and an ACL rule numbered **1** to allow hosts only within the network segment 192.168.10.0/24 to access the Internet.
      
      
      ```
      [~NATA] acl 3001
      ```
      ```
      [*NATA-acl4-advance-3001] rule 1 permit ip source 192.168.10.0 0.0.0.255
      ```
      ```
      [*NATA-acl4-advance-3001] commit
      ```
      ```
      [~NATA-acl4-advance-3001] quit
      ```
   2. Apply the ACL-based traffic classification policy in the view of GE 0/2/1. You can bind the traffic diversion policy either to the instance or to the address pool on one interface.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      For simplified NAT, if only one address pool exists, you can bind either an instance or an address pool. If multiple address pools and outbound interfaces exist and address pools are specified in the outbound interface view for public address pool translation, you need to bind address pools.
      
      
      
      * Bind the policy to the address pool.
        ```
        [~NATA] interface gigabitEthernet 0/2/1
        ```
        ```
        [~NATA-GigabitEthernet0/2/1] ip address 1.1.1.1 24
        ```
        ```
        [*NATA-GigabitEthernet0/2/1] nat bind acl 3001 address-group address-group1
        ```
        ```
        [*NATA-GigabitEthernet0/2/1] commit
        ```
        ```
        [~NATA-GigabitEthernet0/2/1] quit
        ```
      * Bind the policy to the NAT instance.
        ```
        [~NATA] interface gigabitEthernet 0/2/1
        ```
        ```
        [~NATA-GigabitEthernet0/2/1] ip address 1.1.1.1 24
        ```
        ```
        [*NATA-GigabitEthernet0/2/1] nat bind acl 3001 instance nat1
        ```
        ```
        [*NATA-GigabitEthernet0/2/1] commit
        ```
        ```
        [~NATA-GigabitEthernet0/2/1] quit
        ```
3. Verify the configuration.
   
   
   
   # Check NAT user information.
   
   ```
   [~NATA] display nat user-information slot 3 verbose
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break ...             
   Slot: 3 
   Total number:  1.                                                          
     ---------------------------------------------------------------------------                                                       
     User Type                             :  NAT444                                                                                   
     CPE IP                                :  192.168.10.100                                                                                 
     User ID                               :  -                                                                                        
     VPN Instance                          :  -                                                                                        
     Address Group                         :  address-group1                                                                                       
     NAT Instance                          :  nat1                                                                                       
     Public IP                             :  11.11.11.101                                                                                
     Total/TCP/UDP/ICMP Session Limit      :  8192/10240/10240/512                                                                                  
     Total/TCP/UDP/ICMP Session Current    :  1/0/1/0                                                                          
     Total/TCP/UDP/ICMP Rev Session Limit  :  8192/10240/10240/512                                                                     
     Total/TCP/UDP/ICMP Rev Session Current:  0/0/0/0                                                                                  
     Nat ALG Enable                        :  NULL                                                                                     
     Aging Time(s)                         :  -                                                                                        
     Left Time(s)                          :  -                                                                                        
     Session Limit Discard Count           :  0                                                                                        
     -->Transmit Packets                   :  9753259                                                                                  
     -->Transmit Bytes                     :  1111770864                                                                               
     -->Drop Packets                       :  0                                                                                        
     <--Transmit Packets                   :  0                                                                                        
     <--Transmit Bytes                     :  0                                                                                        
     <--Drop Packets                       :  0                                                                                        
     --------------------------------------------------------------------------- 
   ```
   
   # Check the address pool of the simplified instance.
   
   ```
   [~HUAWEI] display nat simple-configuration address-group
   ```
   ```
   2019-02-19 10:21:03.156
   nat address-group address-group1 group-id 1 11.11.11.101 11.11.11.105
   ```

#### Configuration Files

NATA configuration file when a NAT traffic diversion policy is used on an outbound interface (In this configuration file, the traffic diversion policy is bound to the NAT address pool.)

```
#
sysname NATA
#
nat instance nat1 id 1 simple-configuration
#
nat address-group address-group1 group-id 1 11.11.11.101 11.11.11.105
#
acl number 3001
 rule 1 permit ip source 192.168.10.0 0.0.0.255
#
interface GigabitEthernet 0/2/1
 undo shutdown
 ip address 1.1.1.1 255.255.255.0
 nat bind acl 3001 address-group address-group1
#
interface GigabitEthernet 0/2/0
 undo shutdown
 ip address 192.168.10.1 255.255.255.0
#
return

```