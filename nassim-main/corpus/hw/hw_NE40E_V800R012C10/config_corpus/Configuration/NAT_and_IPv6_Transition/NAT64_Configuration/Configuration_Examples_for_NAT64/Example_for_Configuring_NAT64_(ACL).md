Example for Configuring NAT64 (ACL)
===================================

This section provides an example for configuring NAT64 to implement multiple-to-multiple translation from internal IPv6 addresses of enterprise users to external IPv4 addresses and allow only PCs on a specified network segment to access the IPv4 Internet.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374935__fig_dc_ne_cfg_nat64_004201), DeviceA connects to a CR attached to a NAT64 device. An IPv6 user is assigned a private network address from the CPE through DeviceA. When the IPv6 user needs to access the IPv4 Internet over the IPv6 network, the NAT64 device translates the user's IPv6 address to an external IPv4 address.

**Figure 1** NAT64 networking diagram![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 in this example represents GE0/2/1.


  
![](images/fig_dc_ne_nat64_cfg_0003.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic NAT64 functions.
2. Configure a NAT64 traffic diversion policy.

#### Data Preparation

* Slot ID and CPU ID of a service board
* ID of a service-location group
* NAT64 instance name and ID
* NAT64 address pool number and start and end IP addresses
* NAT64 IPv6 prefix (64:FF9B::/96)
* ACL number and ACL rule
* Traffic classifier name, traffic behavior name, and traffic policy name

#### Procedure

1. Configure the NAT64 license function on a service board, configure a service-location group, and bind the CPU of the service board to the group.
   1. Configure the NAT64 license function.
      
      
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
      [*HUAWEI-license] active nat64 vsuf slot 1
      ```
      ```
      [*HUAWEI-license] active nat session-table size 16 slot 1
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
   2. Configure a service-location group and bind the CPU of the service board to it.
      
      
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
2. Create a service-instance group and bind it to the service-location group.
   
   
   ```
   [~HUAWEI] service-instance-group instance-group1
   ```
   ```
   [*HUAWEI-instance-group-instance-group1] service-location 1
   ```
   ```
   [*HUAWEI-instance-group-instance-group1] commit
   ```
   ```
   [~HUAWEI-instance-group-instance-group1] quit
   ```
3. Configure a NAT64 instance and bind it to the service-instance group so that the NAT64 instance is bound to the CPU of the service board.
   
   
   ```
   [~HUAWEI] nat64 instance nat1 id 1
   ```
   ```
   [*HUAWEI-nat64-instance-nat1] service-instance-group instance-group1
   ```
4. Configure a NAT64 public address pool ranging from 11.11.11.100 to 11.11.11.105.
   
   
   ```
   [*HUAWEI-nat64-instance-nat1] nat64 address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
   ```
5. Configure a NAT64 IPv6 prefix of 64:FF9B::/96. This prefix must be the same as the prefix of the DNS64 server.
   
   
   ```
   [*HUAWEI-nat64-instance-nat1] nat64 prefix 64:FF9B:: prefix-length 96 1
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This IPv6 prefix is set according to a standard. The prefix of the DNS64 server must be the same as the IPv6 prefix.
6. Configure a traffic classification rule, a NAT64 traffic behavior, and a NAT64 traffic diversion policy, and apply the NAT64 traffic diversion policy.
   1. Configure an ACL traffic classification rule.
      
      
      ```
      [~HUAWEI] acl ipv6 number 3003
      ```
      ```
      [*HUAWEI-acl6-adv-3003] rule 5 permit ipv6 source 2001:db8::1:1112/126 destination 64:FF9B::/96 
      ```
      ```
      [*HUAWEI-acl6-adv-3003] commit
      ```
      ```
      [~HUAWEI-acl6-adv-3003] quit
      ```
   2. Configure a traffic classifier.
      
      
      ```
      [~HUAWEI] traffic classifier c1
      ```
      ```
      [*HUAWEI-classifier-c1] if-match ipv6 acl 3003
      ```
      ```
      [*HUAWEI-classifier-c1] commit
      ```
      ```
      [~HUAWEI-classifier-c1] quit
      ```
   3. Configure a traffic behavior and bind it to the NAT64 instance.
      
      
      ```
      [~HUAWEI] traffic behavior b1 
      ```
      ```
      [*HUAWEI-behavior-b1] nat64 bind instance nat1
      ```
      ```
      [*HUAWEI-behavior-b1] commit
      ```
      ```
      [~HUAWEI-behavior-b1] quit
      ```
   4. Configure a NAT64 traffic policy and associate the ACL-based traffic classification rule with the traffic behavior.
      
      
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
   5. Configure an IPv6 address in the user-side interface view.
      
      
      ```
      [~HUAWEI] interface GigabitEthernet0/2/1
      ```
      ```
      [*HUAWEI-GigabitEthernet0/2/1] ipv6 enable
      ```
      ```
      [*HUAWEI-GigabitEthernet0/2/1] ipv6 address 2001:db8::1:110e 126
      ```
      ```
      [*HUAWEI-GigabitEthernet0/2/1] commit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/2/1] quit
      ```
   6. Apply the NAT64 traffic diversion policy in the user-side interface view.
      
      
      ```
      [~HUAWEI] interface GigabitEthernet0/2/1
      ```
      ```
      [*HUAWEI-GigabitEthernet0/2/1] traffic-policy p1 inbound
      ```
      ```
      [*HUAWEI-GigabitEthernet0/2/1] commit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/2/1] quit
      ```
7. Configure a NAT64 conversion policy so that the addresses of the packets that are diverted by an interface board to the service board are converted using the addresses in the NAT64 address pool.
   
   
   ```
   [~HUAWEI] nat64 instance nat1 id 1
   ```
   ```
   [*HUAWEI-nat64-instance-nat1] nat64 outbound any address-group address-group1
   ```
   ```
   [*HUAWEI-nat64-instance-nat1] commit
   ```
   ```
   [~HUAWEI-nat64-instance-nat1] quit
   ```
8. Configure a static route to forward return traffic.
   
   
   ```
   [~HUAWEI] ipv6 route-static 2001:DB8::1:1112 126 2001:DB8::1:110F
   ```
   ```
   [*HUAWEI] commit
   ```
9. Verify the configuration.
   
   
   
   # Verify NAT64 user information.
   
   ```
   <HUAWEI> display nat user-information slot 3 verbose
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break ...
     Slot: 3
   Total number:  1.
     ---------------------------------------------------------------------------
     User Type                             :  NAT64
     IPv6Address                           :  2001:db8::1:1112
     User ID                               :  -
     VPN Instance                          :  -
     Address Group                         :  address-group1
     NAT64   Instance                      :  nat1
     Public IP                             :  11.11.11.100
     NoPAT Public IP                       :  0.0.0.0
     Start Port                            :  0
     Port Range                            :  128
     Port Total                            :  0
     MTU                                   :  1500
     Extend Port Alloc Times               :  1
     Extend Port Alloc Number              :  128
     First/Second/Third Extend Port Start  :  0/0/0
     Total/TCP/UDP/ICMP Session Limit      :  0/0/0/0
     Total/TCP/UDP/ICMP Session Current    :  1/0/1/0
     Total/TCP/UDP/ICMP Rev Session Limit  :  0/0/0/0
     Total/TCP/UDP/ICMP Rev Session Current:  0/0/0/0
     Nat ALG Enable                        :  ALL
     Token/TB/TP                           :  0/0/0
     Port Forwarding Flag                  :  Non Port Forwarding
     Port Forwarding Ports                 :  0 0 0 0 0
     Aging Time(s)                         :  0
     Left Time(s)                          :  0
     Port Limit Discard Count              :  0
     Session Limit Discard Count           :  0
     Fib Miss Discard Count                :  0
     -->Transmit Packets                   :  3597637
     -->Transmit Bytes                     :  784284866
     -->Drop Packets                       :  0
     <--Transmit Packets                   :  0
     <--Transmit Bytes                     :  0
     <--Drop Packets                       :  0
     ---------------------------------------------------------------------------
   
   ```

#### Configuration Files

NAT64 device configuration file

```
#
sysname HUAWEI
#
#
vsm on-board-mode disable //Configuration in a dedicated board scenario
license //Configuration in a dedicated board scenario
 active nat session-table size 16 slot 1 //Configuration in a dedicated board scenario
 active nat bandwidth-enhance 40 slot 1 //Configuration in a dedicated board scenario
 active nat64 vsuf slot 1 //Configuration in a dedicated board scenario
#
service-location 1
 
 location slot 1//Configuration in a dedicated board scenario
#
service-instance-group instance-group1
 service-location 1
#
nat64 instance nat1 id 1
 service-instance-group instance-group1
 nat64 address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
 nat64 outbound any address-group address-group1
 nat64 prefix 64:FF9B:: prefix-length 96 1
#
acl ipv6 number 3003
 rule 5 permit ipv6 source 2001:db8::1:1112/126 destination 64:FF9B::/96 
#
traffic classifier c1 operator or
 if-match ipv6 acl 3003 precedence 1
#
traffic behavior b1
 nat64 bind instance nat1
#
traffic policy p1
 share-mode
 classifier c1 behavior b1 precedence 1
#
interface GigabitEthernet0/2/1
 undo shutdown
 ipv6 enable
 ipv6 address 2001:db8::1:110e 126
 traffic-policy p1 inbound
#
ipv6 route-static 2001:DB8::1:1112 126 2001:DB8::1:110F
#
return
```