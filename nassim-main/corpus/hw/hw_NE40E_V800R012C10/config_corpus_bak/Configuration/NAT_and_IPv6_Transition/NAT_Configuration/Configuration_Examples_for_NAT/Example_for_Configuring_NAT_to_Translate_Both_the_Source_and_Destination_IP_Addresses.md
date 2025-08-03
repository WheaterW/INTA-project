Example for Configuring NAT to Translate Both the Source and Destination IP Addresses
=====================================================================================

This section provides an example for configuring NAT to translate both the source and destination IP addresses when Internet users access an internal server.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001139936999__en-us_task_0172374642_w1), NAT-Device functions as a gateway of an enterprise, and the FTP server is an internal server. Internet users need to access the FTP server on the intranet, and external IP addresses can be translated so that the intranet does not need to import external routes. The peer device connected to NAT-Device is assigned an IP address of 1.1.1.2.

[Figure 1](#EN-US_TASK_0000001139936999__en-us_task_0172374642_w1) shows IP addresses of interfaces. The configuration requirements are as follows:

* PCs on the Internet can access the FTP server inside the enterprise network.
* NAT-Device does not import public network routes.

**Figure 1** Networking for configuring NAT to translate both the source and destination IP addresses![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/2/0 and GE 0/2/1, respectively.


  
![](images/fig_dc_ne_nat_cfg_00710001.png)

#### Configuration Roadmap

1. Configure basic NAT functions.
2. Configure the mapping between the public and private IP addresses of the internal NAT server.
3. Enable the NAT ALG function for FTP.
4. Configure a NAT traffic diversion policy.
5. Apply the NAT traffic diversion policy.
6. Configure a NAT traffic conversion policy. (Required in dedicated board mode)
7. Configure a static route.

#### Data Preparation

* NAT instance names (**nat1** and **nat2**) and indexes (1 and 2)
* Name (address-group1), number (1), and IP address range (11.11.11.10â11.11.11.15) of an address pool in the NAT instance named **nat1** Name (address-group2), number (2), and IP address range (11.11.11.16â11.11.11.20) of an address pool in the NAT instance named **nat2**
* ACL names: 3001 and 3002.
* Private network-side interface (GE0/2/0 with IP address 192.168.1.1/24) and public network-side interface (GE0/2/1 with IP address 11.11.11.1) to which a NAT traffic diversion policy is applied
* External IP address 11.11.11.10 advertised by the internal server and internal IP address 192.168.1.2

#### Procedure

1. Configure basic NAT functions.
   1. Create a service-location group and a service-instance group and bind the NAT service board to the service-location group.
      
      
      
      # The configuration is as follows in dedicated board mode.
      
      
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname NAT-Device
      [*HUAWEI] commit
      [~NAT-Device] vsm on-board-mode disable
      [*NAT-Device] commit
      [~NAT-Device] license
      [~NAT-Device-license] active nat session-table size 6 slot 1
      [*NAT-Device-license] active nat bandwidth-enhance 40 slot 1
      [*NAT-Device-license] commit
      [~NAT-Device-license] quit
      [~NAT-Device] service-location 1
      [*NAT-Device-service-location-1] location slot 1
      [*NAT-Device-service-location-1] commit
      [~NAT-Device-service-location-1] quit
      [~NAT-Device] service-instance-group group1
      [*NAT-Device-service-instance-group-group1] service-location 1
      [*NAT-Device-service-instance-group-group1] commit
      [~NAT-Device-service-instance-group-group1] quit
      ```
      
      # The configuration is as follows in on-board mode.
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname NAT-Device
      [*HUAWEI] commit
      [~NAT-Device] service-location 1
      [*NAT-Device-service-location-1] location follow-forwarding-mode
      [*NAT-Device-service-location-1] commit
      [~NAT-Device-service-location-1] quit
      [~NAT-Device] service-instance-group group1
      [*NAT-Device-service-instance-group-group1] service-location 1
      [*NAT-Device-service-instance-group-group1] commit
      [~NAT-Device-service-instance-group-group1] quit
      ```
   2. Create NAT instances named **nat1** and **nat2** and bind the service-instance group to the NAT instances so that service traffic can be processed by the NAT service board.
      
      
      ```
      [~NAT-Device] nat instance nat1 id 1
      [*NAT-Device-nat-instance-nat1] service-instance-group group1
      [*NAT-Device-nat-instance-nat1] commit
      [~NAT-Device-nat-instance-nat1] quit
      [~NAT-Device] nat instance nat2 id 2
      [*NAT-Device-nat-instance-nat2] service-instance-group group1
      [*NAT-Device-nat-instance-nat2] commit
      [~NAT-Device-nat-instance-nat2] quit
      ```
   3. Configure a NAT address pool.
      
      
      ```
      [~NAT-Device] nat instance nat1 id 1
      [~NAT-Device-nat-instance-nat1] nat address-group address-group1 group-id 1 11.11.11.10 11.11.11.15
      [*NAT-Device-nat-instance-nat1] commit
      [~NAT-Device-nat-instance-nat1] quit
      [~NAT-Device] nat instance nat2 id 2
      [~NAT-Device-nat-instance-nat1] nat address-group address-group2 group-id 2 11.11.11.16 11.11.11.20
      [*NAT-Device-nat-instance-nat1] commit
      [~NAT-Device-nat-instance-nat1] quit
      ```
2. Configure the mapping between the public and private IP addresses of the NAT internal server.
   
   
   ```
   [~NAT-Device] nat instance nat1
   [~NAT-Device-nat-instance-nat1] nat server-mode enable
   [*NAT-Device-nat-instance-nat1] nat server global 11.11.11.10 inside 192.168.1.2
   [*NAT-Device-nat-instance-nat1] commit
   [~NAT-Device-nat-instance-nat1] quit
   ```
3. Enable NAT ALG to translate the application-layer IP addresses and port numbers of traffic in the NAT instance named **nat1**.
   
   
   ```
   [~NAT-Device] nat instance nat1
   [~NAT-Device-nat-instance-nat1] nat alg ftp
   [*NAT-Device-nat-instance-nat1] commit
   [~NAT-Device-nat-instance-nat1] quit
   ```
4. Configure a NAT traffic diversion policy.
   
   
   * Configure an ACL numbered **3001** and an ACL rule numbered **1** to allow hosts only within the network segment 192.168.1.0/24 to access the Internet.
   * Configure an ACL numbered **3002** and an ACL rule numbered **2** to permit any packets.
   ```
   [~NAT-Device] acl 3001
   [*NAT-Device-acl4-advance-3001] rule 1 permit ip source 192.168.1.0 0.0.0.255
   [*NAT-Device-acl4-advance-3001] commit
   [~NAT-Device-acl4-advance-3001] quit
   [~NAT-Device] acl 3002
   [*NAT-Device-acl4-advance-3002] rule 2 permit ip source any
   [*NAT-Device-acl4-advance-3002] commit
   [~NAT-Device-acl4-advance-3002] quit
   ```
5. Configure a traffic classifier named **nat1**.
   
   
   ```
   [~NATA] traffic classifier nat1 
   ```
   ```
   [*NATA-classifier-nat1] if-match acl 3001  
   ```
   ```
   [*NATA-classifier-nat1] commit
   ```
   ```
   [~NATA-classifier-nat1] quit
   ```
6. Configure a traffic classifier named **nat2**.
   
   
   ```
   [~NATA] traffic classifier nat2 
   ```
   ```
   [*NATA-classifier-nat2] if-match acl 3002 
   ```
   ```
   [*NATA-classifier-nat2] commit
   ```
   ```
   [~NATA-classifier-nat2] quit
   ```
7. Configure a traffic behavior named **behavior1**, which binds traffic to the NAT instance named **nat1**.
   
   
   ```
   [~NATA] traffic behavior nat1
   ```
   ```
   [*NATA-behavior-nat1] nat bind instance nat1
   ```
   ```
   [*NATA-behavior-nat1] commit
   ```
   ```
   [~NATA-behavior-nat1] quit
   ```
8. Configure a traffic behavior named **behavior2**, which binds traffic to the NAT instance named **nat2**.
   
   
   ```
   [~NATA] traffic behavior nat2
   ```
   ```
   [*NATA-behavior-nat2] nat bind instance nat2
   ```
   ```
   [*NATA-behavior-nat2] commit
   ```
   ```
   [~NATA-behavior-nat2] quit
   ```
9. Configure a NAT traffic policy named **policy1** to associate the ACL rule with the traffic behavior.
   
   
   ```
   [~NATA] traffic policy nat1
   ```
   ```
   [*NATA-trafficpolicy-nat1] classifier nat1 behavior nat1 
   ```
   ```
   [*NATA-trafficpolicy-nat1] commit
   ```
   ```
   [~NATA-trafficpolicy-nat1] quit
   ```
10. Configure a NAT traffic policy named **policy2** to associate the ACL rule with the traffic behavior.
    
    
    ```
    [~NATA] traffic policy nat2
    ```
    ```
    [*NATA-trafficpolicy-nat2] classifier nat2 behavior nat2 
    ```
    ```
    [*NATA-trafficpolicy-nat2] commit
    ```
    ```
    [~NATA-trafficpolicy-nat2] quit
    ```
11. Apply the NAT traffic diversion policy.
    
    
    * Configure an IP address for GE 0/2/0 on the private network side and apply the traffic classification policy with ACL 3001.
    * Configure an IP address for GE 0/2/1 on the public network side and apply the traffic classification policy with ACL 3002.
    ```
    [~NAT-Device] interface gigabitEthernet 0/2/0
    [~NAT-Device-GigabitEthernet0/2/0] ip address 192.168.1.1 24
    [*NAT-Device-GigabitEthernet0/2/0] traffic-policy nat1 inbound
    [*NAT-Device-GigabitEthernet0/2/0] commit
    [~NAT-Device-GigabitEthernet0/2/0] quit
    [~NAT-Device] interface gigabitEthernet 0/2/1 
    [~NAT-Device-GigabitEthernet0/2/1] ip address 11.11.11.1 24
    [*NAT-Device-GigabitEthernet0/2/1] traffic-policy nat2 inbound
    [*NAT-Device-GigabitEthernet0/2/1] commit
    [~NAT-Device-GigabitEthernet0/2/1] quit
    ```
12. Configure a NAT traffic conversion policy. (This step is required only in dedicated board mode.)
    
    
    ```
    [~NAT-Device] nat instance nat1 id 1
    [~NAT-Device-nat-instance-nat1] nat outbound 3001 address-group address-group1
    [*NAT-Device-nat-instance-nat1] commit
    [~NAT-Device-nat-instance-nat1] quit
    [~NAT-Device] nat instance nat2 id 2
    [~NAT-Device-nat-instance-nat2] nat outbound 3002 address-group address-group2
    [*NAT-Device-nat-instance-nat2] commit
    [~NAT-Device-nat-instance-nat2] quit
    ```
13. Configure a default route as a static route and set the next hop address of the default route to 11.11.11.2.
    
    
    ```
    [~NAT-Device] ip route-static 0.0.0.0 0.0.0.0 11.11.11.2
    [*NAT-Device] commit
    ```
14. Verify the configuration.
    
    
    
    # Check NAT server information.
    
    ```
    [~R06] display nat server-map
    This operation will take a few minutes. Press 'Ctrl+C' to break ...              
    Slot: 3
    Total number:  2.
      NAT Instance: nat1         
      Protocol:ANY, VPN:--->-    
      Server reverse:ANY->11.11.11.10[192.168.1.2]                                                
      Tag:0x0, TTL:-, Left-Time:-        
      CPE IP:192.168.1.2
      outbound: false
      extendable:false
    
      NAT Instance: nat1      
      Protocol:ANY, VPN:--->-      
      Server:192.168.1.2[11.11.11.10]->ANY                                  
      Tag:0x0, TTL:-, Left-Time:-   
      CPE IP:192.168.1.2
      outbound: false
      extendable:false
    
    
    ```

#### Configuration Files

```
# 
sysname NAT-Device 
#
vsm on-board-mode disable //Dedicated board configuration
#
license //Dedicated board configuration
 active nat session-table size 6 slot 1 //Dedicated board configuration
 active nat bandwidth-enhance 40 slot 1//Dedicated board configuration
# 
service-location 1
 location slot 1 //Dedicated board configuration
 location follow-forwarding-mode //On-board configuration
#
service-instance-group group1
 service-location 1 
#
nat instance nat1 id 1
 service-instance-group group1
 nat server-mode enable
 nat address-group address-group1 group-id 1 11.11.11.10 11.11.11.15
 nat server global 11.11.11.10 inside 192.168.1.2
 nat outbound 3001 address-group address-group1 //Dedicated board configuration
 nat alg ftp
#
nat instance nat2 id 2
 service-instance-group group1
 nat address-group address-group2 group-id 2 11.11.11.16 11.11.11.20
 nat outbound 3002 address-group address-group2 //Dedicated board configuration
 nat alg ftp
#
acl number 3001 
 rule 1 permit ip source 192.168.1.0 0.0.0.255
#
acl number 3002 
 rule 2 permit ip 
#
traffic classifier nat1 operator or
 if-match acl 3001 precedence 1
#
traffic classifier nat2 operator or
 if-match acl 3002 precedence 1
#
traffic behavior nat1
 nat bind instance nat1
#
traffic behavior nat2
 nat bind instance nat2
#
traffic policy nat1
 share-mode
 classifier nat1 behavior nat1 precedence 1
#
traffic policy nat2
 share-mode
 classifier nat2 behavior nat2 precedence 1
#
interface GigabitEthernet 0/2/0 
 undo shutdown 
 ip address 192.168.1.1 255.255.255.0 
 traffic-policy nat1 inbound
#
interface GigabitEthernet 0/2/1  
 undo shutdown 
 ip address 11.11.11.1 255.255.255.0 
 traffic-policy nat2 inbound
#
ip route-static 0.0.0.0 0.0.0.0 11.11.11.2
#
return
```