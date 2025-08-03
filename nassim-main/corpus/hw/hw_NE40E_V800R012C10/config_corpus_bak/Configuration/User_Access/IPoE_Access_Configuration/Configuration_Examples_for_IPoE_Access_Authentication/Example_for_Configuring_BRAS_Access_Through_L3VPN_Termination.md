Example for Configuring BRAS Access Through L3VPN Termination
=============================================================

This section provides an example for configuring BRAS access through L3VPN termination.

#### Networking Requirements

DeviceB uses OSPF to exchange traffic with DeviceA through interfaces on multiple boards in load balancing mode. Traffic from the same user may be sent from different boards. DeviceB uses policy-based routing (PBR) to send traffic from the same user but different boards through the backplane to the same board for Layer 3 user authentication, as shown in [Figure 1](#EN-US_CONCEPT_0172374044__fig_dc_ne_cfg_01457801).

* DeviceA sends upstream traffic to different interfaces on DeviceB in load balancing mode.
* DeviceB adds all the inbound interfaces to an L3VPN and configures PBR. Then, DeviceB routes all traffic from the same user to the specified next hop based on the source IP address/VLAN ID/DSCP value. The outbound interface of the next hop directly connects to the BAS interface and resides on the same network segment as the BAS interface.
* After user traffic arrives at the BAS interface on DeviceB and the users go online, user forwarding entries are delivered. Subsequent user traffic will then be verified and forwarded based on these forwarding entries.
* Downstream user traffic is forwarded through the BAS interface on DeviceB to the L3VPN domain based on user forwarding entries.
* DeviceB then sends downstream traffic in the L3VPN domain to DeviceA based on routes (the traffic can be balanced). Then, DeviceA forwards the traffic to the users.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only Layer 3 static user access is supported in scenarios of BRAS access through L3VPN termination.

In this example, interfaces 1 and 2 represent VE0/1/1 and VE0/2/1, respectively.



**Figure 1** Configuring BRAS access through L3VPN termination  
![](figure/en-us_image_0000001401148414.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a local L3VPN.
2. Configure PBR on DeviceB to redirect user traffic to the primary/backup next hop. If the primary next hop fails, traffic is automatically switched to the backup next hop to trigger user login.
3. Configure user access interfaces. (User traffic enters these interfaces, not BAS interfaces.)
4. Configure an outbound interface for redirection to a next hop.
5. Configure an authentication domain on BAS interfaces.
6. Configure BAS interfaces through which users go online.
7. Configure Layer 3 static users.

#### Data Preparation

To complete the configuration, you need the following data:

* VE-group number
* Local L3VPN name
* OSPF parameters
* RADIUS authentication mode, RADIUS accounting mode, and authentication domain name used by Layer 3 users
* Interface IP addresses

#### Configuration Procedure

1. Configure a local L3VPN.
   
   Configure a local L3VPN on DeviceB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] ip vpn-instance access
   ```
   ```
   [*DeviceB-vpn-instance-access] ipv4-family
   ```
   ```
   [*DeviceB-vpn-instance-access-af-ipv4] route-distinguisher 200:1
   ```
   ```
   [*DeviceB-vpn-instance-access-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*DeviceB-vpn-instance-access-af-ipv4] commit
   ```
   ```
   [~DeviceB-vpn-instance-access-af-ipv4] quit
   ```
   ```
   [~DeviceB-vpn-instance-access] quit
   ```
2. Configure PBR on DeviceB.
   
   # Configure PBR to redirect user traffic to the primary/backup next hop based on the source IP address. If the primary next hop fails, traffic is automatically switched to the backup next hop to trigger user login through the BAS interface.
   
   ```
   [~DeviceB] acl 3000
   ```
   ```
   [*DeviceB-acl4-advance-3000] rule permit ip source 192.168.1.1 255.255.255.255
   ```
   ```
   [*DeviceB-acl4-advance-3000] quit
   ```
   ```
   [*DeviceB] traffic classifier class1
   ```
   ```
   [*DeviceB-classifier-class1] if-match acl 3000
   ```
   ```
   [*DeviceB-classifier-class1] quit
   ```
   ```
   [*DeviceB] traffic behavior behavior1
   ```
   ```
   [*DeviceB-behavior-behavior1] redirect ipv4-multinhp nhp 192.168.112.2 vpn access nhp 192.168.223.2 vpn access non-revertive
   ```
   ```
   [*DeviceB-behavior-behavior1] quit
   ```
   ```
   [*DeviceB] traffic policy loadbalance
   ```
   ```
   [*DeviceB-trafficpolicy-loadbalance] share-mode
   ```
   ```
   [*DeviceB-trafficpolicy-loadbalance] classifier class1 behavior behavior1
   ```
   ```
   [*DeviceB-trafficpolicy-loadbalance] quit
   ```
   ```
   [*DeviceB] commit
   ```
3. Configure user access interfaces. (User traffic enters these interfaces, not BAS interfaces.)
   
   ```
   [~DeviceB] interface GigabitEthernet0/1/3.100
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/3.100] vlan-type dot1q 100
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/3.100] ip binding vpn-instance access
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/3.100] ip address 192.168.111.1 255.255.255.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/3.100] traffic-policy loadbalance inbound
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/3.100] ospf enable 100 area 0.0.0.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/3.100] quit
   ```
   ```
   [*DeviceB] interface GigabitEthernet2/2/7.100
   ```
   ```
   [*DeviceB-GigabitEthernet2/2/7.100] vlan-type dot1q 100
   ```
   ```
   [*DeviceB-GigabitEthernet2/2/7.100] ip binding vpn-instance access
   ```
   ```
   [*DeviceB-GigabitEthernet2/2/7.100] ip address 192.168.222.1 255.255.255.0
   ```
   ```
   [*DeviceB-GigabitEthernet2/2/7.100] traffic-policy loadbalance inbound
   ```
   ```
   [*DeviceB-GigabitEthernet2/2/7.100] ospf enable 100 area 0.0.0.0
   ```
   ```
   [*DeviceB-GigabitEthernet2/2/7.100] quit
   ```
4. Configure an outbound interface for redirection to a next hop.
   
   ```
   [*DeviceB] interface Virtual-Ethernet0/1/0
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/1/0] ve-group 1 l3-terminate
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface Virtual-Ethernet0/1/0.100
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/1/0.100] vlan-type dot1q 100
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/1/0.100] ip address 192.168.112.1 255.255.255.0
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/1/0.100] quit
   ```
   
   # Configure a backup interface.
   
   ```
   [*DeviceB] interface Virtual-Ethernet0/2/0
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/2/0] ve-group 2 l3-terminate
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/2/0] quit
   ```
   ```
   [*DeviceB] interface Virtual-Ethernet0/2/0.100
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/2/0.100] vlan-type dot1q 100
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/2/0.100] ip address 192.168.223.1 255.255.255.0
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/2/0.100] quit
   ```
   ```
   [*DeviceB] commit
   ```
5. Configure an authentication domain on BAS interfaces.
   
   # Configure an authentication scheme.
   
   ```
   [~DeviceB] aaa
   ```
   ```
   [~DeviceB-aaa] authentication-scheme auth2
   ```
   ```
   [*DeviceB-aaa-authen-auth2] authentication-mode radius
   ```
   ```
   [*DeviceB-aaa-authen-auth2] commit
   ```
   ```
   [~DeviceB-aaa-authen-auth2] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~DeviceB-aaa] accounting-scheme acct2
   ```
   ```
   [*DeviceB-aaa-accounting-acct2] accounting-mode radius
   ```
   ```
   [*DeviceB-aaa-accounting-acct2] commit
   ```
   ```
   [~DeviceB-aaa-accounting-acct2] quit
   ```
   ```
   [~DeviceB-aaa] quit
   ```
   
   # Configure a RADIUS server group.
   
   ```
   [~DeviceB] radius-server group rd2
   ```
   ```
   [*DeviceB-radius-rd2] radius-server authentication 192.168.8.249 1812
   ```
   ```
   [*DeviceB-radius-rd2] radius-server accounting 192.168.8.249 1813
   ```
   ```
   [*DeviceB-radius-rd2] commit
   ```
   ```
   [~DeviceB-radius-rd2] radius-server type standard
   ```
   ```
   [~DeviceB-radius-rd2] radius-server shared-key-cipher it-is-my-secret1
   ```
   ```
   [*DeviceB-radius-rd2] commit
   ```
   ```
   [~DeviceB-radius-rd2] quit
   ```
   
   # Configure an address pool.
   
   ```
   [~DeviceB] ip pool pool2 bas local
   ```
   ```
   [*DeviceB-ip-pool-pool2] gateway 10.82.1.1 255.255.255.0
   ```
   ```
   [*DeviceB-ip-pool-pool2] commit
   ```
   ```
   [~DeviceB-ip-pool-pool2] section 0 10.82.1.2 10.82.1.200
   ```
   ```
   [~DeviceB-ip-pool-pool2] dns-server 192.168.8.252
   ```
   ```
   [*DeviceB-ip-pool-pool2] commit
   ```
   ```
   [~DeviceB-ip-pool-pool2] vpn-instance access
   ```
   ```
   [~DeviceB-ip-pool-pool2] quit
   ```
   
   # Configure a domain.
   
   ```
   [~DeviceB] aaa
   ```
   ```
   [~DeviceB-aaa] domain fastweb
   ```
   ```
   [*DeviceB-aaa-domain-fastweb] commit
   ```
   ```
   [~DeviceB-aaa-domain-fastweb] authentication-scheme auth2
   ```
   ```
   [*DeviceB-aaa-domain-fastweb] accounting-scheme acct2
   ```
   ```
   [*DeviceB-aaa-domain-fastweb] commit
   ```
   ```
   [~DeviceB-aaa-domain-fastweb] ip-pool pool2
   ```
   ```
   [~DeviceB-aaa-domain-fastweb] quit
   ```
6. Configure BAS interfaces through which users go online.
   
   # Configure a username generation mode and a user password.
   
   ```
   [~DeviceB-aaa] default-user-name template fastweb include ip-address .
   ```
   ```
   [*DeviceB-aaa] commit
   ```
   ```
   [~DeviceB-aaa] default-password template fastweb cipher YsHsjx_202206
   ```
   ```
   [~DeviceB-aaa] quit
   ```
   
   # Configure a BAS interface through which users go online.
   
   ```
   [~DeviceB] interface Virtual-Ethernet0/1/1
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/1/1] ve-group 1 l3-access
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/1/1] quit
   ```
   ```
   [*DeviceB] interface Virtual-Ethernet0/1/1.100
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/1/1.100] vlan-type dot1q 100
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/1/1.100] ip binding vpn-instance access
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/1/1.100] ip address 192.168.112.2 255.255.255.0
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/1/1.100] commit
   ```
   ```
   [~DeviceB-Virtual-Ethernet0/1/1.100] bas
   ```
   ```
   [~DeviceB-Virtual-Ethernet0/1/1.100-bas] access-type layer3-subscriber default-domain authentication fastweb
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/1/1.100-bas] default-user-name-template fastweb
   [*DeviceB-Virtual-Ethernet0/1/1.100-bas] commit
   [~DeviceB-Virtual-Ethernet0/1/1.100-bas] default-password-template fastweb
   [~DeviceB-Virtual-Ethernet0/1/1.100-bas] quit
   [~DeviceB-Virtual-Ethernet0/1/1.100] quit
   ```
   
   # Configure a backup BAS interface through which users go online.
   
   ```
   [~DeviceB] interface Virtual-Ethernet0/2/1
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/2/1] ve-group 2 l3-access
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/2/1] quit
   ```
   ```
   [*DeviceB] interface Virtual-Ethernet0/2/1.100
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/2/1.100] vlan-type dot1q 100
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/2/1.100] ip binding vpn-instance access
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/2/1.100] ip address 192.168.223.2 255.255.255.0
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/2/1.100] commit
   ```
   ```
   [~DeviceB-Virtual-Ethernet0/2/1.100] bas
   ```
   ```
   [~DeviceB-Virtual-Ethernet0/2/1.100-bas] access-type layer3-subscriber default-domain pre-authentication fastweb
   ```
   ```
   [*DeviceB-Virtual-Ethernet0/2/1.100-bas] default-user-name-template fastweb
   [*DeviceB-Virtual-Ethernet0/2/1.100-bas] commit
   [~DeviceB-Virtual-Ethernet0/2/1.100-bas] default-password-template fastweb
   [~DeviceB-Virtual-Ethernet0/2/1.100-bas] quit
   [~DeviceB-Virtual-Ethernet0/2/1.100] quit
   ```
7. Configure Layer 3 static users.
   
   ```
   [~DeviceB] layer3-subscriber 192.168.1.1 vpn-instance access domain-name fastweb
   ```

#### Configuration Files

DeviceB configuration file

```
#
sysname DeviceB
#
ip vpn-instance access
 ipv4-family
 route-distinguisher 200:1
 apply-label per-instance
 vpn-target 111:1 export-extcommunity
 vpn-target 111:1 import-extcommunity
#
radius-server group rd2 
 radius-server shared-key-cipher %^%#clY:%[]x='-RMNJus[s/VJ:3YBq3<..|.{'xgbp+%^%#
 radius-server authentication 192.168.8.249 1812 weight 0
 radius-server accounting 192.168.8.249 1813 weight 0
# 
ip pool pool2 bas local
 vpn-instance access
 gateway 10.82.1.1 255.255.255.0 
 section 0 10.82.1.2 10.82.1.200
 dns-server 192.168.8.252
#
acl number 3000
 rule permit source 192.168.1.1 255.255.255.255
#
traffic classifier class1 operator or
 if-match acl 3000 precedence 8
#
traffic behavior behavior1
 redirect ipv4-multinhp nhp 192.168.112.2 vpn access nhp 192.168.223.2 vpn access non-revertive
#
traffic policy loadbalance
 share-mode
 classifier class1 behavior behavior1 precedence 1
#
aaa
 default-password template fastweb cipher %^%#:d"1K5>aICqP6}.%)!#0IngT9sGU-B%6]>H7Ylj%%^%# 
 default-user-name template fastweb include ip-address . 
 #
 authentication-scheme auth2
 #
 accounting-scheme acct2
 #
 domain fastweb
  authentication-scheme auth2
  accounting-scheme acct2
  ip-pool pool2
#
interface GigabitEthernet0/1/3
 undo shutdown
#
interface GigabitEthernet0/1/3.100
 vlan-type dot1q 100
 ip binding vpn-instance access 
 ip address 192.168.111.1 255.255.255.0
 traffic-policy loadbalance inbound
 ospf enable 100 area 0.0.0.0
#
interface GigabitEthernet2/2/7
 undo shutdown
#
interface GigabitEthernet2/2/7.100 
 vlan-type dot1q 100
 ip binding vpn-instance access
 ip address 192.168.222.1 255.255.255.0
 traffic-policy loadbalance inbound
 ospf enable 100 area 0.0.0.0
#
interface Virtual-Ethernet0/1/0
 ve-group 1 l3-terminate
#
interface Virtual-Ethernet0/1/0.100
 vlan-type dot1q 100
 ip address 192.168.112.1 255.255.255.0
#
interface Virtual-Ethernet0/1/1 
 ve-group 1 l3-access
#
interface Virtual-Ethernet0/1/1.100
 vlan-type dot1q 100
 ip binding vpn-instance access
 ip address 192.168.112.2 255.255.255.0
 bas
  #
   access-type layer3-subscriber default-domain authentication fastweb
   default-user-name-template fastweb
   default-password-template fastweb
 #
#
interface Virtual-Ethernet0/2/0
 ve-group 2 l3-terminate
#
interface Virtual-Ethernet0/2/0.100
 vlan-type dot1q 100
 ip address 192.168.223.1 255.255.255.0
#
interface Virtual-Ethernet0/2/1
 ve-group 2 l3-access
#
interface Virtual-Ethernet0/2/1.100
 vlan-type dot1q 100
 ip binding vpn-instance access
 ip address 192.168.223.2 255.255.255.0
 bas
 #
  access-type layer3-subscriber default-domain pre-authentication fastweb
  default-user-name-template fastweb
  default-password-template fastweb
 #
#
ospf 100
 area 0.0.0.0
#
layer3-subscriber 192.168.1.1 192.168.1.1 vpn-instance access domain-name fastweb
#
return
```