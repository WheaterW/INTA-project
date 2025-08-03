Example for Configuring Syslog Source Tracing for NAT Flexible Flows
====================================================================

This section provides an example for configuring syslog source tracing for flexible NAT flows. The log function can be used to record information about intranet users' access to external networks in real time, improving network maintainability. A networking diagram is provided to help you understand the configuration procedure.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0219369081__fig323195820314), the NAT device (NAT1) performs the NAT function to help PCs within an enterprise network access the Internet. The NAT device is connected to the enterprise network through GE 0/2/0 and to the Internet through GE 0/2/1. The enterprise is assigned public IP addresses of 11.11.11.11/32 through 11.11.11.15/32. The router DeviceA is connected to the log server through GE 0/2/0 and to the external network through GE 0/2/1. An IPsec tunnel is established between NAT1 and DeviceA to transfer syslogs for NAT flexible flows to the log server.

The configuration requirements are as follows:

* Only PCs on the network segment of 192.168.10.0/24 can perform NAT and access the external network.
* The syslog server can record the actions of users when they access Internet applications.
* NAT1 and DeviceA support IPsec services.

**Figure 1** Networking of syslog source tracing for NAT flexible flows![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/2/0 and GE 0/2/1, respectively.


  
![](figure/en-us_image_0000001340590342.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic NAT functions.
2. Configure a NAT traffic diversion policy.
3. Configure the syslog function for NAT flexible flows.
4. Configure an IPsec tunnel between NAT1 and DeviceA. Configure NAT1 and DeviceA to encrypt packets using the HMAC-SHA256 and AES-256 algorithms for authentication.
5. Configure a routing policy to ensure that the syslog server is reachable.

#### Data Preparation

To complete the configuration, you need the following data:

* Service-location group index: 1 and 2.
* Service-instance group name: group1 and group2.
* NAT instance name (nat1) and index (1)
* NAT1's NAT address pool name (address-group1), address pool number (1), a range of public IP addresses (11.11.11.11 through 11.11.11.15)
* ACL number: 3000 and 3001.
* Name (GE 0/2/1) and IP address (192.0.2.1/24) of an interface to which a NAT traffic diversion policy is applied
* NAT syslog host address (198.51.100.1) and port number (514), and NAT device's source IP address (192.0.2.1) and source port number (514)


#### Procedure

1. Configure basic NAT functions.
   1. Create a NAT instance named **nat1** and bind it to the service board.
      
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname NAT1
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~NAT1] service-location 1
      ```
      ```
      [*NAT1-service-location-1] location slot 3
      ```
      ```
      [*NAT1-service-location-1] commit
      ```
      ```
      [~NAT1-service-location-1] quit
      ```
      ```
      [~NAT1] service-instance-group group1
      ```
      ```
      [*NAT1-service-instance-group-group1] service-location 1
      ```
      ```
      [*NAT1-service-instance-group-group1] commit
      ```
      ```
      [~NAT1-service-instance-group-group1] quit
      ```
      ```
      [~NAT1] nat instance nat1 id 1
      ```
      ```
      [*NAT1-nat-instance-nat1] service-instance-group group1
      ```
      ```
      [*NAT1-nat-instance-nat1] commit
      ```
      ```
      [~NAT1-nat-instance-nat1] quit
      ```
   2. Configure a NAT address pool with addresses ranging from 11.11.11.11 to 11.11.11.15.
      
      
      ```
      [~NAT1] nat instance nat1
      ```
      ```
      [~NAT1-nat-instance-nat1] nat address-group address-group1 group-id 1
      ```
      ```
      [*NAT1-nat-instance-nat1-nat-address-group-address-group1] section 1 11.11.11.11 11.11.11.15
      ```
      ```
      [*NAT1-nat-instance-nat1-nat-address-group-address-group1] commit
      ```
      ```
      [~NAT1-nat-instance-nat1-nat-address-group-address-group1] quit
      ```
      ```
      [~NAT1-nat-instance-nat1] quit
      ```
2. Configure a NAT traffic diversion policy on an outbound interface.
   
   
   1. Configure an ACL numbered **3001** and an ACL rule numbered **1** to allow hosts only within the network segment 192.168.10.0/24 to access the Internet.
      ```
      [~NAT1] acl 3001
      ```
      ```
      [*NAT1-acl4-advance-3001] rule 1 permit ip source 192.168.10.0 0.0.0.255
      ```
      ```
      [*NAT1-acl4-advance-3001] commit
      ```
      ```
      [~NAT1-acl4-advance-3001] quit
      ```
   2. Apply the ACL-based traffic classification policy in the view of GE 0/2/1.
      ```
      [~NAT1] interface gigabitEthernet 0/2/1
      ```
      ```
      [~NAT1-GigabitEthernet0/2/1] ip address 192.0.2.1 24
      ```
      ```
      [*NAT1-GigabitEthernet0/2/1] nat bind acl 3001 instance nat1
      ```
      ```
      [*NAT1-GigabitEthernet0/2/1] commit
      ```
      ```
      [~NAT1-GigabitEthernet0/2/1] quit
      ```
   3. Configure an IP address for GE 0/2/0.
      ```
      [~NAT1] interface gigabitEthernet 0/2/0
      ```
      ```
      [~NAT1-GigabitEthernet0/2/0] ip address 192.168.10.1 24
      ```
      ```
      [*NAT1-GigabitEthernet0/2/0] commit
      ```
      ```
      [~NAT1-GigabitEthernet0/2/0] quit
      ```
3. Configure the syslog function for NAT flexible flows.
   1. Enable the syslog function for NAT flexible flows in the NAT instance **nat1**.
      
      
      ```
      [~NAT1] nat instance nat1
      ```
      ```
      [~NAT1-nat-instance-nat1] nat log session enable syslog
      ```
      ```
      [*NAT1-nat-instance-nat1] nat log host 198.51.100.1 514 source 192.0.2.1 514 name NAT1 
      ```
      ```
      [*NAT1-nat-instance-nat1] commit
      ```
      ```
      [~NAT1-nat-instance-nat1] quit
      ```
   2. Create a syslog template for NAT flexible flows, configure the template, and specify a flexible log template type.
      
      
      ```
      [~NAT1] nat syslog flexible template session
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 0 fixed-string  "<134> 1 "
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 1 timestamp-year " "
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 2 timestamp-month-en " "
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 3 timestamp-date " "
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 4 timestamp-hour ":"
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 5 timestamp-minute  ":"
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 6 timestamp-second " "
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 7 host-ip " "
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 8 app-name " - "
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 9 scene ":"
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 10 fixed-string  "SessionbasedA [" create
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 10 fixed-string  "SessionbasedW [" free
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 11 protocol " "
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 12 source-ip " - "
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 13 destination-ip " "
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 14 source-port " "
      ```
      ```
      [*NAT1-nat-syslog-template-session] nat position 15 destination-port " -]"
      ```
      ```
      [*NAT1-nat-syslog-template-session] commit
      ```
      ```
      [~NAT1] quit
      ```
      ```
      [~NAT1] nat syslog descriptive format flexible template session
      ```
4. Configure an IPsec tunnel on NAT1.
   
   
   1. Enable IPsec and configure the service board in slot 1 to support IPsec.
      ```
      [~NAT1] license
      ```
      ```
      [~NAT1-license] active ipsec slot 1
      ```
      ```
      [*NAT1-license] commit
      ```
      ```
      [~NAT1-license] quit
      ```
   2. Create and configure a tunnel interface.
      ```
      [~NAT1] interface Tunnel 10
      ```
      ```
      [*NAT1-Tunnel10] tunnel-protocol ipsec
      ```
      ```
      [*NAT1-Tunnel10] ip address 192.168.1.1 32
      ```
      ```
      [*NAT1-Tunnel10] commit
      ```
      ```
      [~NAT1-Tunnel10] quit
      ```
   3. Configure ACL 3000.
      ```
      [~NAT1] acl 3000
      ```
      ```
      [*NAT1-acl-adv-3000] rule permit ip source 192.0.2.1 0 destination 198.51.100.1 0
      ```
      ```
      [*NAT1-acl-adv-3000] commit
      ```
      ```
      [~NAT1-acl-adv-3000] quit
      ```
   4. Configure an IPsec proposal named **tran1**.
      ```
      [~NAT1] ipsec proposal tran1
      ```
      ```
      [*NAT1-ipsec-proposal-tran1] encapsulation-mode tunnel
      ```
      ```
      [*NAT1-ipsec-proposal-tran1] transform esp
      ```
      ```
      [*NAT1-ipsec-proposal-tran1] esp authentication-algorithm sha2-256
      ```
      ```
      [*NAT1-ipsec-proposal-tran1] esp encryption-algorithm aes 256
      ```
      ```
      [*NAT1-ipsec-proposal-tran1] commit
      ```
      ```
      [~NAT1-ipsec-proposal-tran1] quit
      ```
   5. Configure an IKE proposal numbered **10**.
      ```
      [~NAT1] ike proposal 10
      ```
      ```
      [*NAT1-ike-proposal-10] authentication-method pre-share
      ```
      ```
      [*NAT1-ike-proposal-10] authentication-algorithm sha2-256
      ```
      ```
      [*NAT1-ike-proposal-10] dh group14
      ```
      ```
      [*NAT1-ike-proposal-10] commit
      ```
      ```
      [~NAT1-ike-proposal-10] quit
      ```
   6. Configure an IKE peer.
      ```
      [~NAT1] ike peer b
      ```
      ```
      [*NAT1-ike-peer-b] ike-proposal 10
      ```
      ```
      [*NAT1-ike-peer-b] remote-address 192.168.1.2
      ```
      ```
      [*NAT1-ike-peer-b] pre-shared-key abcde
      ```
      ```
      [*NAT1-ike-peer-b] commit
      ```
      ```
      [~NAT1-ike-peer-b] quit
      ```
   7. Configure dead peer detection (DPD).
      ```
      [~NAT1] ike dpd 100
      ```
      ```
      [*NAT1] commit
      ```
   8. Configure IPsec policy **map1**.
      ```
      [~NAT1] ipsec policy map1 10 isakmp
      ```
      ```
      [*NAT1-ipsec-policy-isakmp-map1-10] security acl 3000
      ```
      ```
      [*NAT1-ipsec-policy-isakmp-map1-10] proposal tran1
      ```
      ```
      [*NAT1-ipsec-policy-isakmp-map1-10] ike-peer a
      ```
      ```
      [*NAT1-ipsec-policy-isakmp-map1-10] commit
      ```
      ```
      [~NAT1-ipsec-policy-isakmp-map1-10] quit
      ```
   9. Configure an IPsec service-instance group.
      ```
      [~NAT1] service-location 2
      ```
      ```
      [*NAT1-service-location-2] location slot 1
      ```
      ```
      [*NAT1-service-location-2] commit
      ```
      ```
      [~NAT1-service-location-2] quit
      ```
      ```
      [~NAT1] service-instance-group group2
      ```
      ```
      [*NAT1-service-instance-group-group2] service-location 2
      ```
      ```
      [*NAT1-service-instance-group-group2] commit
      ```
      ```
      [~NAT1-service-instance-group-group2] quit
      ```
   10. Apply the IPsec policy to the tunnel interface.
       ```
       [~NAT1] interface Tunnel 10
       ```
       ```
       [*NAT1-Tunnel10] ipsec policy map1 service-instance-group group2
       ```
       ```
       [*NAT1-Tunnel10] commit
       ```
       ```
       [~NAT1-Tunnel10] quit
       ```
5. Configure an IPsec tunnel on Device A.
   
   
   1. Configure IP addresses for interfaces.
      ```
      <DeviceA> system-view
      ```
      ```
      [~DeviceA] interface gigabitethernet 0/2/0
      ```
      ```
      [~DeviceA-GigabitEthernet0/2/0] ip address 198.51.100.2 24
      ```
      ```
      [*DeviceA-GigabitEthernet0/2/0] commit
      ```
      ```
      [~DeviceA-GigabitEthernet0/2/0] quit
      ```
      ```
      [~DeviceA] interface gigabitethernet 0/2/1
      ```
      ```
      [~DeviceA-GigabitEthernet0/2/1] ip address 10.0.1.1 24
      ```
      ```
      [*DeviceA-GigabitEthernet0/2/1] commit
      ```
      ```
      [~DeviceA-GigabitEthernet0/2/1] quit
      ```
   2. Enable IPsec and configure the service board in slot 1 to support IPsec.
      ```
      [~DeviceA] license
      ```
      ```
      [~DeviceA-license] active ipsec slot 1
      ```
      ```
      [*DeviceA-license] commit
      ```
      ```
      [~DeviceA-license] quit
      ```
   3. Create and configure a tunnel interface.
      ```
      [~DeviceA] interface Tunnel 10
      ```
      ```
      [*DeviceA-Tunnel10] tunnel-protocol ipsec
      ```
      ```
      [*DeviceA-Tunnel10] ip address 192.168.1.2 32
      ```
      ```
      [*DeviceA-Tunnel10] commit
      ```
      ```
      [~DeviceA-Tunnel10] quit
      ```
   4. Configure ACL 3000.
      ```
      [~DeviceA] acl 3000
      ```
      ```
      [*DeviceA-acl-adv-3000] rule permit ip source 198.51.100.1 0 destination 192.0.2.1 0
      ```
      ```
      [*DeviceA-acl-adv-3000] commit
      ```
      ```
      [~DeviceA-acl-adv-3000] quit
      ```
   5. Configure an IPsec proposal named **tran1**.
      ```
      [~DeviceA] ipsec proposal tran1
      ```
      ```
      [*DeviceA-ipsec-proposal-tran1] encapsulation-mode tunnel
      ```
      ```
      [*DeviceA-ipsec-proposal-tran1] transform esp
      ```
      ```
      [*DeviceA-ipsec-proposal-tran1] esp authentication-algorithm sha2-256
      ```
      ```
      [*DeviceA-ipsec-proposal-tran1] esp encryption-algorithm aes 256
      ```
      ```
      [*DeviceA-ipsec-proposal-tran1] commit
      ```
      ```
      [~DeviceA-ipsec-proposal-tran1] quit
      ```
   6. Configure an IKE proposal numbered **10**.
      ```
      [~DeviceA] ike proposal 10
      ```
      ```
      [*DeviceA-ike-proposal-10] authentication-method pre-share
      ```
      ```
      [*DeviceA-ike-proposal-10] authentication-algorithm sha2-256
      ```
      ```
      [*DeviceA-ike-proposal-10] dh group14
      ```
      ```
      [*DeviceA-ike-proposal-10] commit
      ```
      ```
      [~DeviceA-ike-proposal-10] quit
      ```
   7. Configure an IKE peer.
      ```
      [~DeviceA] ike peer a
      ```
      ```
      [*DeviceA-ike-peer-a] ike-proposal 10
      ```
      ```
      [*DeviceA-ike-peer-a] remote-address 192.168.1.1
      ```
      ```
      [*DeviceA-ike-peer-a] pre-shared-key abcde
      ```
      ```
      [*DeviceA-ike-peer-a] commit
      ```
      ```
      [~DeviceA-ike-peer-a] quit
      ```
   8. Configure DPD.
      ```
      [~DeviceA] ike dpd 100
      ```
      ```
      [*DeviceA] commit
      ```
   9. Configure IPsec policy **map1**.
      ```
      [~DeviceA] ipsec policy map1 10 isakmp
      ```
      ```
      [*DeviceA-ipsec-policy-isakmp-map1-10] security acl 3000
      ```
      ```
      [*DeviceA-ipsec-policy-isakmp-map1-10] proposal tran1
      ```
      ```
      [*DeviceA-ipsec-policy-isakmp-map1-10] ike-peer a
      ```
      ```
      [*DeviceA-ipsec-policy-isakmp-map1-10] commit
      ```
      ```
      [~DeviceA-ipsec-policy-isakmp-map1-10] quit
      ```
   10. Configure an IPsec service-instance group.
       ```
       [~DeviceA] service-location 2
       ```
       ```
       [*DeviceA-service-location-2] location slot 1
       ```
       ```
       [*DeviceA-service-location-2] commit
       ```
       ```
       [~DeviceA-service-location-2] quit
       ```
       ```
       [~DeviceA] service-instance-group group2
       ```
       ```
       [*DeviceA-service-instance-group-group2] service-location 2
       ```
       ```
       [*DeviceA-service-instance-group-group2] commit
       ```
       ```
       [~DeviceA-service-instance-group-group2] quit
       ```
   11. Apply the IPsec policy to the tunnel interface.
       ```
       [~DeviceA] interface Tunnel 10
       ```
       ```
       [*DeviceA-Tunnel10] ipsec policy map1 service-instance-group group2
       ```
       ```
       [*DeviceA1-Tunnel10] commit
       ```
       ```
       [~DeviceA-Tunnel10] quit
       ```
6. Configure a static route to ensure that the log server is reachable. Set the next hop address of the route from the NAT device to the external network to 192.0.2.2/24 and the next hop address of the route from Device A to the external network to 10.0.1.1/24. (The routing policy needs to be configured based on the actual networking.)
   
   
   
   # Configure NAT1.
   
   
   
   ```
   [~NAT1] ip route-static 198.51.100.1 0.0.0.0 tunnel 10 192.168.1.2
   ```
   ```
   [*NAT1] ip route-static 192.168.1.2 255.255.255.255 192.0.2.2
   ```
   ```
   [*NAT1] commit
   ```
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ip route-static 192.0.2.1 0.0.0.0 tunnel 10 192.168.1.1
   ```
   ```
   [*DeviceA] ip route-static 192.168.1.1 255.255.255.255 10.0.1.1
   ```
   ```
   [*DeviceA] commit
   ```
7. Verify the configuration.
   
   # View the log format of the syslog template for NAT flexible flows.
   ```
   [~NAT1] display nat syslog flexible session template
   ```
   ```
   Create Log:
     fixed_string<134> 1 timestamp_year timestamp_month_en timestamp_date timestamp_hour:timestamp_minute:timestamp_second host_ip app_name - scene:fixed_stringSessionbasedA [protocol source_ip - destination_ip source_port destination_port -]  
     Example: 
     <134> 1 2019 January 18 14:09:22 X.X.X.X cnelog - NAT444:SessionbasedA [17 X.X.X.X - X.X.X.X 1052 2000 -]
   Free Log: 
     fixed_string<134> 1 timestamp_year timestamp_month_en timestamp_date timestamp_hour:timestamp_minute:timestamp_second host_ip app_name - scene:fixed_stringSessionbasedW [protocol source_ip - destination_ip source_port destination_port -]
     Example: 
     <134> 1 2019 January 18 14:09:22 X.X.X.X cnelog - NAT444:SessionbasedW [17 X.X.X.X - X.X.X.X 1052 2000 -]
   ```
   
   
   
   # Display the IPsec tunnel negotiation status.
   
   ```
   [~DeviceA] display ike sa
   ```
   ```
   current sa Num :2
      Single-homing :2          Multi-homing M and M|B :0        Multi-homing S and S|B :0
      None-backup sa :2         Backup sa :0
   Spu board slot 1 , IKE SA Information:
   Current IKE SA number: 2
   ------------------------------------------------------------------------------------
   conn-id    peer                    flag                phase   bfd   ext    vpn
   ------------------------------------------------------------------------------------
   2        192.168.1.2                 RD|ST               v2:2    -     -      -
   1        192.168.1.2                 RD|ST               v2:1    -     -      -
   ```

#### Configuration Files

* NAT1 configuration file
  
  ```
  #
  sysname NAT1
  #
   active ipsec slot 1
  #
  ike dpd 100
  service-location 1
   location slot 3
  # 
  service-location 2
   location slot 1
  #
  service-instance-group group1      
   service-location 1    
  #
  service-instance-group group2      
   service-location 2
  #
  nat instance nat1 id 1      
   service-instance-group group1      
   nat address-group address-group1 group-id 1 
    section 1 11.11.11.11 11.11.11.15  
   nat log host 198.51.100.1 514 source 192.0.2.1 514 name NAT1
   nat log session enable syslog
  # 
  acl number 3000 
   rule 5 permit ip source 192.0.2.1 0 destination 198.51.100.1 0
  #
  acl number 3001
   rule 1 permit ip source 192.168.10.0 0.0.0.255
  #
  ike proposal 10 
   encryption-algorithm des-cbc
   dh group14
   authentication-algorithm sha2-256
   integrity-algorithm hmac-sha2-256
  # 
  ike peer b 
   pre-shared-key cipher %^%#aRY4K;`"G=G{$z:d)#X;Y0Q,%@K|FF1/D=6k<G>;%^%#
   ike-proposal 10
   remote-address 192.168.1.2
  # 
  ipsec proposal tran1 
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  # 
  ipsec policy map1 10 isakmp 
   security acl 3000
   ike-peer b
   proposal tran1
  #
  interface GigabitEthernet 0/2/0
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
  #
  interface GigabitEthernet 0/2/1
   undo shutdown
   ip address 192.0.2.1 255.255.255.0
   nat bind acl 3001 instance nat1
  # 
  interface Tunnel10 
   ip address 192.168.1.1 255.255.255.255 
   tunnel-protocol ipsec 
   ipsec policy map1 service-instance-group 2
  #
  nat syslog flexible template session
   nat position 0 fixed-string  "<134> 1 "
   nat position 1 timestamp-year " "
   nat position 2 timestamp-month-en " "
   nat position 3 timestamp-date " "
   nat position 4 timestamp-hour ":"
   nat position 5 timestamp-minute  ":"
   nat position 6 timestamp-second " "
   nat position 7 host-ip " "
   nat position 8 app-name " - "
   nat position 9 scene ":"
   nat position 10 fixed-string  "SessionbasedA [" create
   nat position 10 fixed-string  "SessionbasedW [" free
   nat position 11 protocol " "
   nat position 12 source-ip " - "
   nat position 13 destination-ip " "
   nat position 14 source-port " "
   nat position 15 destination-port " -]"
  #
  nat syslog descriptive format flexible template session
  #
  ip route-static 198.51.100.1 0.0.0.0 Tunnel10 192.168.1.2
  ip route-static 192.168.1.2 255.255.255.255 192.0.2.2
  #
  return
  ```
* DeviceA configuration file
  ```
  # 
  sysname DeviceA 
  # 
  license  
   active ipsec slot 1   
  # 
  ike dpd 100
  # 
  service-location 2
   location slot 1
  # 
  service-instance-group group2       
   service-location 2
  # 
  acl number 3000 
   rule 5 permit ip source 198.51.100.1 0 destination 192.0.2.1 0 
  #
  ike proposal 10 
   encryption-algorithm des-cbc
   dh group14
   authentication-algorithm sha2-256
   integrity-algorithm hmac-sha2-256
  # 
  ike peer a 
   pre-shared-key cipher %^%#aRY4K;`"G=G{$z:d)#X;Y0Q,%@K|FF1/D=6k<G>;%^%#
   ike-proposal 10
   remote-address 192.168.1.1
  # 
  ipsec proposal tran1 
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  # 
  ipsec policy map1 10 isakmp 
   security acl 3000
   ike-peer a
   proposal tran1
  #
  interface GigabitEthernet 0/2/0 
   undo shutdown 
   ip address 192.51.100.2 255.255.255.0 
  # 
  interface GigabitEthernet 0/2/1 
   undo shutdown 
   ip address 10.0.1.1 255.255.255.0 
  # 
  interface Tunnel10 
   ip address 192.168.1.2 255.255.255.255 
   tunnel-protocol ipsec 
   ipsec policy map1 service-instance-group 2 
  # 
  ip route-static 192.0.2.1 0.0.0.0 Tunnel10 192.168.1.1 
  ip route-static 192.168.1.1 255.255.255.255 172.0.2.2 
  # 
  return
  ```