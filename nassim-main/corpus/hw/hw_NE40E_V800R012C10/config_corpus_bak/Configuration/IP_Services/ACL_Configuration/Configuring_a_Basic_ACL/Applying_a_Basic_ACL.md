Applying a Basic ACL
====================

Basic ACLs can be used in device management, routing policies, multicast packet filtering, and QoS services.

#### Context

[Table 1](#EN-US_TASK_0172364583__tab_dc_vrp_acl4_cfg_005201) describes the typical applications of basic ACLs.

**Table 1** Typical applications of basic ACLs
| Typical Application | Usage Scenario | Operation |
| --- | --- | --- |
| Device management | When a device functions as an FTP or TFTP server, configure a basic ACL on the device to allow only the clients that match specific ACL rules to access the server. | For details on how to configure rights to access an FTP or TFTP server, see  * [Configuring FTP Access Control](dc_vrp_vfm_cfg_0011.html) * [Configuring TFTP Access Authority](dc_vrp_basic_cfg_0090.html) |
| Configure a basic ACL to restrict the incoming or outgoing calls on VTY user interfaces. | For details on how to configure the restriction on incoming and outgoing calls on VTY user interfaces, see [Setting Restrictions for Incoming and Outgoing Calls on VTY User Interfaces](dc_vrp_basic_cfg_0015.html). |
| Specify an NMS and manageable MIB objects for SNMP-based communication between the NMS and managed device to improve communication security. | For details on how to configure the NMS's right to access devices, see  * [Controlling the NM Station's Access to the Device (SNMPv1)](dc_vrp_snmp_cfg_0006.html) * [Controlling the NM Station's Access to the Device (SNMPv2)](dc_vrp_snmp_cfg_0011.html) * [Controlling the NM Station's Access to the Device (SNMPv3)](dc_vrp_snmp_cfg_0017.html) |
| Multicast packet filtering | To filter multicast packets, configure a basic ACL to receive or forward only the multicast packets that match the ACL rules. | For details on how to filter multicast packets, see  * [Setting a Multicast Source Address Range](dc_vrp_multicast_cfg_0011.html) * [Setting a Legal C-RP Address Range](dc_vrp_multicast_cfg_0017.html) * [Setting a Legal BSR Address Range](dc_vrp_multicast_cfg_0019.html) * [Setting an SSM Group Address Range](dc_vrp_multicast_cfg_0024.html) |
| Routing policies | To control the reception and advertisement of routing information on a device, configure a basic ACL on the device to allow the device to receive or advertise only the routes that match the ACL rules. | For details on how to control the reception and advertisement of routing information on a device, see  * [Applying Filters to the Received Routes](dc_vrp_route-policy_cfg_0012.html) * [Applying a Policy to BGP Route Acceptance](dc_vrp_bgp_cfg_3115.html) * [Applying Filters to the Advertised Routes](dc_vrp_route-policy_cfg_0017.html) * [Applying a Policy to BGP Route Advertisement](dc_vrp_bgp_cfg_3114.html) |
| QoS services | To process different types of traffic, configure a basic ACL to perform traffic policing, traffic shaping, or traffic classification on traffic that matches the ACL rules. | For details on how to process different types of traffic, see Configuring the Traffic Policing Policy, Configuring Traffic Shaping, and Configuring Traffic Behaviors. |



#### Typical Cases of Applying a Basic ACL

* **Cases of applying a basic ACL in device management**
  
  For example, a user configures a device as follows:
  + Configuring a basic ACL for FTP login
    ```
    acl number 2001 
     rule 5 deny source 192.168.2.100 0 
     rule 10 permit
    ftp acl 2001
    ```
    
    Matching result: Users with the IP address 192.168.2.100 are prohibited from logging in to the device using FTP.
  + Configuring a basic ACL for Telnet login
    ```
    acl number 2001 
     rule 5 permit source 192.168.2.100 0 
     rule 10 deny 
    user-interface vty 0 4 
     acl 2001 inbound
    ```
    
    Matching result: Only users with the IP address 192.168.2.100 are allowed to log in to the device using Telnet.
  + Configuring a basic ACL for SNMP login
    ```
    acl number 2001 
     rule 5 deny source 192.168.2.100 0 
     rule 10 permit
    snmp-agent community read cipher public acl 2001
    ```
    
    Matching result: Users with the IP address 192.168.2.100 are prohibited from logging in to the device using SNMP.
* **Case of applying a basic ACL in multicast packet filtering**
  
  For example, a user configures a device as follows:
  ```
  acl number 2001
   rule 5 permit source 10.10.1.2 0
   rule 10 deny source 10.10.1.1 0
  pim
   source-policy 2001
  ```
  
  Matching result: The device permits multicast packets containing the source address 10.10.1.2 whereas discarding those containing the source address 10.10.1.1.
* **Cases of applying a basic ACL in routing policies**
  
  For example, a user configures a device as follows:
  + A route-policy of a routing protocol is used to filter routes.
    
    ```
    ip route-static 1.1.1.10 255.255.255.0 NULL0
    ip route-static 192.168.2.0 255.255.255.0 NULL0
    ip route-static 192.168.2.100 255.255.255.255 NULL0
    bgp 1
     peer 10.1.1.1 as-number 1
     ipv4-family unicast
      undo synchronization
      import-route static route-policy test
    peer 10.1.1.1 enable
    
    ```
    ```
    route-policy test permit node 0
     if-match acl 2001
    acl number 2001
     rule 5 permit source 192.168.2.100 0
     rule 10 deny source 1.1.1.10 0.0.0.255
    
    ```
    
    Matching result: Routes from the network segments 1.1.1.10 and 192.168.2.0 are filtered out, whereas the route 192.168.2.100 is permitted.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    - Routes from the network segment 1.1.1.10 are filtered out, because the action defined in the ACL rule that the routes match is **deny**.
    - Routes from the network segment 192.168.2.0 do not match any specified ACL rules. By default, the device matches the routes with the last ACL rule. The action defined in the last ACL rule is **deny**, and therefore the routes are filtered out.
    - The route 192.168.2.100 is permitted, because the action defined in the ACL rule that the route matches is **permit** and the action defined in the route-policy is also **permit**.
    ```
    route-policy test permit node 0 
     if-match acl 2001 
     apply cost 100 
    route-policy test permit node 1 
     apply cost 200
    acl number 2001 
     rule 5 permit source 192.168.2.100 0 
    
    ```
    
    Matching result: The cost of the route 192.168.2.100 is changed to 100, whereas the costs of other routes are changed to 200.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    In the preceding route-policy, permit is specified for node 0, the route 192.168.2.100/32 passes the check by the if-match clause, and the device takes the action (**apply cost 100**) specified in the apply clause. As a result, the cost of the route is changed to 100. The other routes do not pass the check by the if-match clause, and the device takes the action (**apply cost 200**) specified in node 1 in the route-policy. As a result, the costs of these routes are changed to 200.
    
    ```
    route-policy test deny node 0 
     if-match acl 2001 
     apply cost 100 
    route-policy test permit node 1 
     apply cost 200
    acl number 2001 
     rule 5 permit source 192.168.2.100 0 
    
    ```
    Matching result: The cost of the route 192.168.2.100/32 is not changed to 100.![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    In the preceding route-policy, deny is specified for node 0, the route 192.168.2.100/32 passes the check by the if-match clause, and the device does not take the action (**apply cost 100**) specified in the apply clause. As a result, the cost of the route is not changed to 100. The other routes do not pass the check by the if-match clause, and the device takes the action (**apply cost 200**) specified in node 1 in the route-policy. As a result, the costs of these routes are changed to 200.
  + A filter-policy of a routing protocol is used to filter routes.
    
    ```
    ip route-static 1.1.1.10 255.255.255.0 NULL0
    ip route-static 192.168.2.0 255.255.255.0 NULL0  
    ip route-static 192.168.2.100 255.255.255.255 NULL0 
    bgp 1
     peer 10.1.1.2 as-number 1 
     ipv4-family unicast 
      undo synchronization 
      filter-policy 2001 export 
      import-route static  
    peer 10.1.1.2 enable 
    acl number 2001
     rule 5 permit source 192.168.2.100 0 
     rule 10 deny source 1.1.1.10 0.0.0.255 
    
    ```
    
    Matching result: Routes from the network segments 1.1.1.10 and 192.168.2.0 are filtered out, whereas the route 192.168.2.100 is permitted.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    - Routes from the network segment 1.1.1.10 are filtered out, because the action defined in the ACL rule that the routes match is **deny**.
    - Routes from the network segment 192.168.2.0 do not match any specified ACL rules. By default, the device matches the routes with the last ACL rule. The action defined in the last ACL rule is **deny**, and therefore the routes are filtered out.
    - The route 192.168.2.100 is permitted, because the action defined in the ACL rule that the route matches is **permit** and the action defined in the filter-policy is **export**.
* **Cases of applying a basic ACL in QoS services**
  
  For example, a user configures a device as follows:
  + Configuring a basic ACL in firewall traffic behavior (packet filtering)
    ```
    acl number 2001
     rule 5 permit source 192.168.0.0 0.255.255.255
     rule 10 deny source 10.0.0.0 0.255.255.255
    traffic classifier acl 
     if-match acl 2001
    traffic behavior test
     deny
    traffic policy test
     classifier acl behavior test
    interface GigabitEthernet0/1/1
     traffic-policy test inbound
    ```
    
    GE 0/1/1 receives the following packets:
    - Packet 1 with the source IP address 192.168.0.1/24
    - Packet 2 with the source IP address 10.0.0.1/24
    - Packet 3 with the source IP address 172.16.0.1/24
    
    Matching result: Packets 1 and 2 are discarded but packet 3 is permitted.
  + Configuring a basic ACL in common traffic behavior
    ```
    acl number 2001
     rule 5 permit source 192.168.0.0 0.255.255.255
     rule 10 deny source 10.0.0.0 0.255.255.255
    traffic classifier acl 
     if-match acl 2001
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