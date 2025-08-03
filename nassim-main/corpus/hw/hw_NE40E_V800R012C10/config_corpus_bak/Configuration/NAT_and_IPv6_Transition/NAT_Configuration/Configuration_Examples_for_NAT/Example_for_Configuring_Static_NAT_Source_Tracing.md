Example for Configuring Static NAT Source Tracing
=================================================

This section provides an example for configuring static NAT source tracing to implement many-to-one translation between private and public addresses and allow PCs only on a specified network segment to access the Internet.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374609__fig_dc_ne_cfg_nat_009701), the CPE performs NAT on the packets sent by PCs on the intranet and sends the packets to the BRAS. The BRAS connects to the RADIUS server and to the IPv4 network through the CR. The NAT device connects to the CR in off-path mode. The NAT device is connected to the CR through GE 0/2/0. The enterprise has 100 public IP addresses ranging from 11.11.11.1/24 to 11.11.11.100/24.

It is required that only PCs on the network segment ranging from 10.0.0.1/24 to 10.0.0.255/24 access the Internet.

**Figure 1** Static NAT source tracing![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/2/0.


  
![](images/fig_dc_ne_nat_cfg_0015.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure NAT resources.
2. Configure a service-instance-group.
3. Configure a NAT instance named **nat1** and bind it to the NAT service board.
4. Configure the NAT static source tracing algorithm mapping.
5. Bind the NAT static source tracing algorithm to the NAT instance.
6. Configure a NAT traffic diversion policy.

#### Data Preparation

* Index of the service-location group: 1; name of the service-instance-group: group 1; index of the NAT instance named **nat1**: 1
* IDs of the private and public address pools for the static source tracing algorithm
* Name and IP address of each interface to which a NAT traffic diversion policy is applied
* Private network address segment for NAT static source tracing: 10.0.0.1 to 10.0.0.255; public network address segment for NAT static source tracing 11.11.11.1 to 11.11.11.100
* Port number range for the public address pool: 256 to 1023; port segment size: 256
* ACL number: 3001; traffic classifier name: c1; traffic behavior name: b1; traffic policy name: p1

#### Procedure

1. Set the maximum number of sessions that can be created on the service board in slot 1 to 6M.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] vsm on-board-mode disable
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~HUAWEI] license
   ```
   ```
   [~HUAWEI-license] active nat session-table size 6 slot 1
   ```
   ```
   [*HUAWEI-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*HUAWEI-license] commit
   ```
   ```
   [~HUAWEI-license] quit
   ```
2. Configure a service-instance-group.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] service-location 1
   ```
   ```
   [*HUAWEI-service-location-1] location slot 1
   ```
   ```
   [*HUAWEI-service-location-1] commit
   ```
   ```
   [~HUAWEI-service-location-1] quit
   ```
   ```
   [~HUAWEI] service-instance-group group1
   ```
   ```
   [*HUAWEI-service-instance-group-group1] service-location 1
   ```
   ```
   [*HUAWEI-service-instance-group-group1] commit
   ```
   ```
   [~HUAWEI-service-instance-group-group1] quit
   ```
3. Configure a NAT instance named **nat1** and bind it to the NAT service board.
   
   
   ```
   [~HUAWEI] nat instance nat1 id 1
   ```
   ```
   [*HUAWEI-nat-instance-nat1] service-instance-group group1
   ```
   ```
   [*HUAWEI-nat-instance-nat1] commit
   ```
   ```
   [~HUAWEI-nat-instance-nat1] quit
   ```
4. Configure a group of NAT static source tracing algorithm parameters, with the private address pool containing IP addresses from 10.0.0.1 to 10.0.0.255, the public address pool containing IP addresses from 11.11.11.1 to 11.11.11.100, the port range from 256 to 1023, and port segment size as 256.
   
   
   ```
   [~HUAWEI] nat static-mapping
   ```
   ```
   [*HUAWEI-nat-static-mapping] inside-pool 1
   ```
   ```
   [*HUAWEI-nat-static-mapping-inside-pool-1] section 1 10.0.0.1 10.0.0.255
   ```
   ```
   [*HUAWEI-nat-static-mapping-inside-pool-1] quit
   ```
   ```
   [*HUAWEI-nat-static-mapping] global-pool 1
   ```
   ```
   [*HUAWEI-nat-static-mapping-global-pool-1] section 1 11.11.11.1 11.11.11.100
   ```
   ```
   [*HUAWEI-nat-static-mapping-global-pool-1] quit
   ```
   ```
   [*HUAWEI-nat-static-mapping] static-mapping 10 inside-pool 1 global-pool 1 port-range 256 1023 port-size 256
   ```
   ```
   [*HUAWEI-nat-static-mapping] commit
   ```
   ```
   [~HUAWEI-nat-static-mapping] quit
   ```
5. Enable the NAT static source tracing algorithm in the NAT instance named **nat1** and specify the algorithm ID as 10.
   
   
   ```
   [~HUAWEI] nat instance nat1
   ```
   ```
   [~HUAWEI-nat-instance-nat1] nat bind static-mapping 10
   ```
   ```
   [*HUAWEI-nat-instance-nat1] commit
   ```
   ```
   [~HUAWEI-nat-instance-nat1] quit
   ```
6. Configure a traffic classification rule and NAT behavior.
   1. Configures an ACL rule to allow only PCs on internal network segment 10.0.0.0/24 to access the Internet.
      
      
      ```
      [~HUAWEI] acl 3001
      ```
      ```
      [*HUAWEI-acl4-advance-3001] rule 1 permit ip source 10.0.0.0 0.0.0.255
      ```
      ```
      [*HUAWEI-acl4-advance-3001] commit
      ```
      ```
      [~HUAWEI-acl4-advance-3001] quit
      ```
   2. Configure a traffic classifier and define an ACL-based matching rule.
      
      
      ```
      [~HUAWEI] traffic classifier c1
      ```
      ```
      [*HUAWEI-classifier-c1] if-match acl 3001
      ```
      ```
      [*HUAWEI-classifier-c1] commit
      ```
      ```
      [~HUAWEI-classifier-c1] quit
      ```
   3. Configure a traffic behavior, which binds traffic to the NAT instance named **nat1**.
      
      
      ```
      [~HUAWEI] traffic behavior b1 
      ```
      ```
      [*HUAWEI-behavior-b1] nat bind instance nat1
      ```
      ```
      [*HUAWEI-behavior-b1] commit
      ```
      ```
      [~HUAWEI-behavior-b1] quit
      ```
   4. Defines a NAT traffic policy to associate the ACL rule with the traffic behavior.
      
      
      ```
      [~HUAWEI] traffic policy p1
      ```
      ```
      [*HUAWEI-trafficpolicy-p1] classifier c1 behavior b1
      ```
      ```
      [*HUAWEI-trafficpolicy-p1] commit
      ```
      ```
      [~HUAWEI-trafficpolicy-p1] quit
      ```
   5. Apply the NAT traffic diversion policy in the interface view.
      
      
      ```
      [~HUAWEI] interface gigabitEthernet 0/2/0
      ```
      ```
      [~HUAWEI-GigabitEthernet0/2/0] traffic-policy p1 inbound
      ```
      ```
      [*HUAWEI-GigabitEthernet0/2/0] commit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/2/0] quit
      ```
7. Verify the configuration.
   
   
   
   # Check NAT user information on the device.
   
   ```
   <HUAWEI> display nat user-information slot 1 verbose
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break ...                                                                 
   Slot: 1            
   Total number:  1.          
     ---------------------------------------------------------------------------     
     User Type                             :  NAT444               
     CPE IP                                :  10.0.0.1      
     User ID                               :  -       
     VPN Instance                          :  -       
     Address Group                         :  -       
     NoPAT Address Group                   :  -      
     NAT Instance                          :  nat1     
     Public IP                             :  11.11.11.1   
     NoPAT Public IP                       :  -         
     Start Port                            :  256    
     Port Range                            :  256      
     Port Total                            :  256  
     Radius Specific PCP Port              :  NO     
     Extend Port Alloc Times               :  0      
     Extend Port Alloc Number              :  0       
     First/Second/Third Extend Port Start  :  0/0/0    
     Total/TCP/UDP/ICMP Session Limit      :  8192/10240/10240/512  
     Total/TCP/UDP/ICMP Session Current    :  1/0/1/0           
     Total/TCP/UDP/ICMP Rev Session Limit  :  8192/10240/10240/512  
     Total/TCP/UDP/ICMP Rev Session Current:  0/0/0/0     
     Total/TCP/UDP/ICMP Port Limit         :  0/0/0/0    
     Total/TCP/UDP/ICMP Port Current       :  1/0/1/0     
     Nat ALG Enable                        :  NULL   
     Port Reuse                            :  False     
     Token/TB/TP                           :  0/0/0      
     Port Forwarding Flag                  :  Non Port Forwarding   
     Port Forwarding Ports                 :  0 0 0 0 0  
     Create Time                           :  2022-12-15 11:15:28     
     Aging Time(s)                         :  -      
     Left Time(s)                          :  -    
     Port Limit Discard Count              :  0     
     Session Limit Discard Count           :  0   
     Fib Miss Discard Count                :  0    
     -->Transmit Packets                   :  150156628   
     -->Transmit Bytes                     :  19699109016  
     -->Drop Packets                       :  0     
     <--Transmit Packets                   :  0     
     <--Transmit Bytes                     :  0    
     <--Drop Packets                       :  0     
     Fast-forwarding Statistics ID         :  -   
     -->Hit Fast-fwd session Packets       :  -       
     -->NP transmit to multi-core Packets  :  -  
     <--Hit Fast-fwd session Packets       :  -  
     <--NP transmit to multi-core Packets  :  -                              
   
     ---------------------------------------------------------------------------  
   ```

#### Configuration Files

NAT device configuration file

```
#
sysname HUAWEI
#
vsm on-board-mode disable
#
license
 active nat session-table size 6 slot 1 engine 0
 active nat bandwidth-enhance 40 slot 1
#
nat static-mapping
 inside-pool 1
  section 1 10.0.0.1 10.0.0.255
 global-pool 1
  section 1 11.11.11.1 11.11.11.100
 static-mapping 10 inside-pool 1 global-pool 1 port-range 256 1023 port-size 256
#
service-location 1
 location slot 1
#
service-instance-group group1
 service-location 1
#
nat instance nat1 id 1
 service-instance-group group1 
 nat bind static-mapping 10
#
acl number 3001
 rule 1 permit ip source 10.0.0.0 0.0.0.255
#
traffic classifier c1 operator or
 if-match acl 3001 precedence 1 
#
traffic behavior b1
 nat bind instance nat1
#
traffic policy p1
 share-mode
 classifier c1 behavior b1 precedence 1
#
interface GigabitEthernet 0/2/0
 undo shutdown
 ip address 10.1.1.1 255.255.255.0
 traffic-policy p1 inbound
#
return
```