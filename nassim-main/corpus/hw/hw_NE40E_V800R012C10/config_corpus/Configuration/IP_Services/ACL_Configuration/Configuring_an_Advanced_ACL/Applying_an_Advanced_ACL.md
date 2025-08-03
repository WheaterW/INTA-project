Applying an Advanced ACL
========================

Advanced ACLs can be used in device management, routing policies, multicast packet filtering, and QoS services.

#### Context

[Table 1](#EN-US_TASK_0172364595__tab_dc_vrp_acl4_cfg_005801) describes the typical applications of advanced ACLs.

**Table 1** Typical applications of advanced ACLs
| Typical Application | Usage Scenario | Operation |
| --- | --- | --- |
| Device management | Configure an advanced ACL to restrict the incoming or outgoing calls on VTY user interfaces. | For details on how to configure the restriction on incoming and outgoing calls on VTY user interfaces, see [Setting Restrictions for Incoming and Outgoing Calls on VTY User Interfaces](dc_vrp_basic_cfg_0015.html). |
| Multicast packet filtering | To filter multicast packets, configure an advanced ACL to receive or forward only the multicast packets that match the ACL rules. | For details on how to filter multicast packets, see  * [Setting a Multicast Source Address Range](dc_vrp_multicast_cfg_0011.html) * [Setting a Legal C-RP Address Range](dc_vrp_multicast_cfg_0017.html) * [Setting a Legal BSR Address Range](dc_vrp_multicast_cfg_0019.html) * [Setting an SSM Group Address Range](dc_vrp_multicast_cfg_0024.html) |
| QoS services | To process different types of traffic, configure an advanced ACL to perform traffic policing, traffic shaping, or traffic classification on traffic that matches the ACL rules. | For details on how to process different types of traffic, see Configuring the Traffic Policing Policy, Configuring Traffic Shaping, and Configuring Traffic Behaviors. |



#### Typical Cases of Applying an Advanced ACL

* **Cases of applying an advanced ACL in device management**
  
  For example, a user configures a device as follows:
  ```
  acl number 3001 
   rule 5 permit ip source 192.168.2.100 0 
   rule 10 deny ip source any
  user-interface vty 0 4 
   acl 3001 inbound
  ```
  Matching result: Only users with the IP address 192.168.2.100 are allowed to log in to the device using Telnet.
* **Case of applying an advanced ACL in multicast packet filtering**
  
  For example, a user configures a device as follows:
  ```
  acl number 3001
   rule 5 permit ip source 10.10.1.2 0
   rule 10 deny ip source 10.10.1.1 0
  pim
   source-policy 3001
  ```
  
  Matching result: The device permits multicast packets containing the source address 10.10.1.2 whereas discarding those containing the source address 10.10.1.1.
* **Cases of applying an advanced ACL in QoS services**
  
  For example, a user configures a device as follows:
  + Configuring an advanced ACL in firewall traffic behavior (packet filtering)
    ```
    acl number 3000 
     rule 5 permit tcp destination-port eq domain 
     rule 10 permit udp destination-port eq dns 
     rule 15 permit icmp icmp-type echo 
     rule 20 permit icmp icmp-type echo-reply
    traffic classifier acl 
     if-match acl 3000
    traffic behavior test
     permit
    traffic policy test
     classifier acl behavior test
    interface GigabitEthernet0/1/1
     traffic-policy test inbound
    ```
    
    Matching result: DNS Echo, DNS Echo Reply, ICMP Echo, and ICMP Echo Reply packets are permitted.
    
    ```
    acl number 3000 
     rule 5 permit ip source 10.108.0.0 0.0.0.255
     rule 10 deny ip source 10.108.0.0 0.0.255.255
    traffic classifier acl 
     if-match acl 3000
    traffic behavior test
     permit
    traffic policy test
     classifier acl behavior test
    interface GigabitEthernet0/1/1
     traffic-policy test inbound
    ```
    
    Matching result: IP packets from the network segment 10.108.0.0/24 are permitted, whereas those from the network segment 10.108.0.0/16 are denied.
    
    ```
    acl number 3000 
     rule permit tcp source 10.9.0.0 0.0.255.255 destination 10.8.160.0 0.0.0.255 destination-port eq www
    traffic classifier acl 
     if-match acl 3000
    traffic behavior test
     permit
    traffic policy test
     classifier acl behavior test
    interface GigabitEthernet0/1/1
     traffic-policy test inbound
    ```
    
    Matching result: Hosts in the 10.9.0.0 network segment are permitted to send WWW packets to hosts in the 10.8.160.0 network segment.
    
    ```
    time-range no-http 08:00 to 16:00 working-day 
    acl number 3000 
     rule 5 deny tcp source-port eq www time-range no-http 
     rule 10 deny tcp destination-port eq www time-range no-http
    traffic classifier acl 
     if-match acl 3000
    traffic behavior test
     permit
    traffic policy test
     classifier acl behavior test
    interface GigabitEthernet0/1/1
     traffic-policy test inbound
    ```
    
    Matching result: HTTP packets are denied from 8:00 am to 6:00 pm Monday through Friday.
    
    ```
    acl number 3000 
     rule 5 permit tcp
    traffic classifier acl 
     if-match acl 3000
    traffic behavior test
     permit
    traffic policy test
     classifier acl behavior test
    interface GigabitEthernet0/1/1
     traffic-policy test inbound
    ```
    
    Matching result: TCP packets are permitted.
  + Configuring an advanced ACL in common traffic behavior
    ```
    acl number 3001
     rule 5 permit ip source 192.168.0.0 0.255.255.255
     rule 10 deny ip source 10.0.0.0 0.255.255.255
    traffic classifier acl 
     if-match acl 3001
    traffic behavior test
     remark ip-precedence 7
    traffic policy test
     classifier acl behavior test
    interface GigabitEthernet0/1/1
     traffic-policy test inbound
    ```
    
    GE 0/1/1 receives the following packets:
    - Packet 1 with the source IP address 192.168.0.1/24 and IP precedence 0
    - Packet 2 with the source IP address 10.0.0.1/24 and IP precedence 0
    - Packet 3 with the source IP address 172.16.0.1/24 and IP precedence 0
    
    Matching result: Packet 1 is permitted, and its IP precedence is re-marked 7; packet 3 is permitted, and its IP precedence remains 0; packet 2 is discarded.