Example for Configuring Distributed VPN NAT
===========================================

This section provides an example for configuring distributed VPN NAT so that users on different VPNs can access one another through NAT.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.

On the distributed NAT network shown in [Figure 1](#EN-US_TASK_0000001140094141__en-us_task_0172374669_fig_dc_ne_cfg_nat_015601), a BRAS provides NAT functions. PC1 on VPN-A attempts to access PC2 on VPN-B through the BRAS. Upon receipt of user-side traffic, the BRAS performs NAT translation, in addition to user authentication, authorization, and accounting.

**Figure 1** Distributed VPN NAT![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/2/1 on the BRAS.


  
![](images/fig_dc_ne_cfg_nat_015601.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic NAT functions.
2. Configure VPN instances.
3. Configure a NAT address pool and a NAT traffic conversion policy.
4. Configure user information and RADIUS authentication on the BRAS.
5. Configure a NAT traffic diversion policy.
6. Configure user-side interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Name of a NAT instance
* Name, RD, and VPN target extended community attributes of a VPN instance
* NAT address pool's number and start and end IP addresses
* User group name
* ACL number and UCL number
* Information about the NAT traffic diversion policy


#### Procedure

1. Configure basic NAT functions.
   
   1. Set the maximum number of sessions that can be created on the CPU of the NAT service board to 16M.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname BRAS
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [*BRAS] vsm on-board-mode disable
      ```
      ```
      [~BRAS] commit
      ```
      ```
      [~BRAS] license
      ```
      ```
      [~BRAS-license] active nat session-table size 16 slot 1 
      ```
      ```
      [~BRAS-license] active nat bandwidth-enhance 40 slot 1
      ```
      ```
      [~BRAS-license] quit
      ```
   2. Create a service-instance group named **group1** and bind it to the service-location group.
      
      ```
      [~BRAS] service-location 1
      ```
      ```
      [*BRAS-service-location-1] location slot 1 
      ```
      ```
      [*BRAS-service-location-1] commit
      ```
      ```
      [~BRAS-service-location-1] quit
      ```
      ```
      [~BRAS] service-instance-group group1
      ```
      ```
      [*BRAS-service-instance-group-group1] service-location 1
      ```
      ```
      [*BRAS-service-instance-group-group1] commit
      ```
      ```
      [~BRAS-service-instance-group-group1] quit
      ```
   3. Bind the NAT instance named **nat1** to the service-instance-group instance group named **group1**.
      
      ```
      [~BRAS] nat instance nat1 id 1
      ```
      ```
      [*BRAS-nat-instance-nat1] service-instance-group group1
      ```
      ```
      [*BRAS-nat-instance-nat1] commit
      ```
      ```
      [~BRAS-nat-instance-nat1] quit
      ```
2. Configure VPN instances.
   
   ```
   [~BRAS] ip vpn-instance vpna
   ```
   ```
   [*BRAS-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*BRAS-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*BRAS-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*BRAS-vpn-instance-vpna-af-ipv4] commit
   ```
   ```
   [~BRAS-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [~BRAS] ip vpn-instance vpnb
   ```
   ```
   [*BRAS-vpn-instance-vpnb] ipv4-family
   ```
   ```
   [*BRAS-vpn-instance-vpnb-af-ipv4] route-distinguisher 200:1
   ```
   ```
   [*BRAS-vpn-instance-vpnb-af-ipv4] vpn-target 222:1 both
   ```
   ```
   [*BRAS-vpn-instance-vpnb-af-ipv4] commit
   ```
   ```
   [~BRAS-vpn-instance-vpnb-af-ipv4] quit
   ```
3. Configure a NAT address pool and a NAT traffic conversion policy so that NAT is performed using addresses in the NAT address pool. This applies to all packets that are diverted by an interface board to a NAT service board.
   
   ```
   [~BRAS] nat instance nat1 id 1
   ```
   ```
   [*BRAS-nat-instance-nat1] nat address-group address-group1 group-id 1 11.1.1.1 11.1.1.5 vpn-instance vpnb
   ```
   ```
   [*BRAS-nat-instance-nat1] nat outbound any address-group address-group1
   ```
   ```
   [*BRAS-nat-instance-nat1] commit
   ```
   ```
   [~BRAS-nat-instance-nat1] quit
   ```
4. Configure NAT user information.
   
   1. Configure the BRAS service on the device so that users can go online. For details, see [AAA and User Management Configuration (Access Users)](dc_ne_aaa_cfg_0035.html) in *HUAWEI NE40E Configuration Guide-User Access*.
      
      ```
      [~BRAS] ip pool baspool1 bas local
      ```
      ```
      [~BRAS-ip-pool-baspool1] vpn-instance vpna
      ```
      ```
      [~BRAS-ip-pool-baspool1] gateway 10.1.1.101 255.255.255.0
      ```
      ```
      [~BRAS-ip-pool-baspool1] section 1 10.1.1.1 10.1.1.100 
      ```
      ```
      [*BRAS-ip-pool-baspool1] dns-server 192.168.7.252
      ```
      ```
      [*BRAS-ip-pool-baspool1] commit
      ```
      ```
      [~BRAS-ip-pool-baspool1] quit
      ```
   2. Create a user group named **group1**.
      
      ```
      [~BRAS] user-group group1
      ```
   3. Specify the domain to which the users belong.
      
      ```
      [~BRAS] aaa
      ```
      ```
      [~BRAS-aaa] authentication-scheme default0
      ```
      ```
      [*BRAS-aaa-authen-default0] authentication-mode radius
      ```
      ```
      [*BRAS-aaa-authen-default0] commit
      ```
      ```
      [~BRAS-aaa-authen-default0] quit
      ```
      ```
      [~BRAS-aaa] accounting-scheme default0
      ```
      ```
      [*BRAS-aaa-accounting-default0] accounting-mode radius
      ```
      ```
      [~BRAS-aaa-accounting-default0] commit
      ```
      ```
      [~BRAS-aaa-accounting-default0] quit
      ```
      ```
      [~BRAS-aaa] domain natbras
      ```
      ```
      [*BRAS-aaa-domain-natbras] authentication-scheme default0
      ```
      ```
      [*BRAS-aaa-domain-natbras] accounting-scheme default0
      ```
      ```
      [*BRAS-aaa-domain-natbras] user-group group1 bind nat instance nat1
      ```
      ```
      [*BRAS-aaa-domain-natbras] vpn-instance vpna
      ```
      ```
      [*BRAS-aaa-domain-natbras] ip-pool baspool1
      ```
      ```
      [*BRAS-aaa-domain-natbras] commit
      ```
      ```
      [~BRAS-aaa-domain-natbras] quit
      ```
      ```
      [~BRAS-aaa] quit
      ```
5. Configure a NAT traffic diversion policy.
   
   1. Configure an ACL numbered **6001**.
      
      ```
      [~BRAS] acl 6001
      ```
      ```
      [*BRAS-acl-ucl-6001] rule 1 permit ip source user-group group1
      ```
      ```
      [*BRAS-acl-ucl-6001] commit
      ```
      ```
      [~BRAS-acl-ucl-6001] quit
      ```
   2. Configure a traffic classifier.
      
      ```
      [~BRAS] traffic classifier c1
      ```
      ```
      [*BRAS-classifier-c1] if-match acl 6001
      ```
      ```
      [*BRAS-classifier-c1] commit
      ```
      ```
      [~BRAS-classifier-c1] quit
      ```
   3. Configure a traffic behavior named **b1**, which binds traffic to the NAT instance named **nat1**.
      
      ```
      [~BRAS] traffic behavior b1
      ```
      ```
      [*BRAS-behavior-b1] nat bind instance nat1
      ```
      ```
      [*BRAS-behavior-b1] commit
      ```
      ```
      [~BRAS-behavior-b1] quit
      ```
   4. Define a NAT policy to associate the ACL rule with the traffic behavior.
      
      ```
      [~BRAS] traffic policy p1
      ```
      ```
      [*BRAS-trafficpolicy-p1] classifier c1 behavior b1
      ```
      ```
      [*BRAS-trafficpolicy-p1] commit
      ```
      ```
      [~BRAS-trafficpolicy-p1] quit
      ```
   5. Apply the NAT traffic diversion policy in the system view.
      
      ```
      [~BRAS] traffic-policy p1 inbound
      ```
      ```
      [*BRAS] commit
      ```
6. Configure a user-side interface.
   
   ```
   [~BRAS] interface gigabitEthernet 0/2/1
   ```
   ```
   [*BRAS-GigabitEthernet0/2/1] commit
   ```
   ```
   [~BRAS-GigabitEthernet0/2/1] bas
   ```
   ```
   [~BRAS-GigabitEthernet0/2/1-bas] access-type layer2-subscriber default-domain authentication natbras
   ```
   ```
   [*BRAS-GigabitEthernet0/2/1-bas] authentication-method bind
   ```
   ```
   [*BRAS-GigabitEthernet0/2/1-bas] commit
   ```
   ```
   [~BRAS-GigabitEthernet0/2/1-bas] quit
   ```

#### Configuration Files

BRAS configuration file

```
#
sysname BRAS
#
vsm on-board-mode disable
#
user-group group1
#
ip vpn-instance vpna
 ipv4-family
  route-distinguisher 100:1
  apply-label per-instance 
  vpn-target 111:1 export-extcommunity
  vpn-target 111:1 import-extcommunity
#
ip vpn-instance vpnb
 ipv4-family
  route-distinguisher 200:1
  apply-label per-instance 
  vpn-target 222:1 export-extcommunity
  vpn-target 222:1 import-extcommunity
#
service-location 1
 location slot 1 
#
service-instance-group group1
 service-location 1
#
nat instance nat1 id 1
 service-instance-group group1
 nat address-group address-group1 group-id 1 11.1.1.1 11.1.1.5 vpn-instance vpnb
 nat outbound any address-group address-group1
#
ip pool baspool1 bas local
 vpn-instance vpna
 gateway 10.1.1.101 255.255.255.0
 section 1 10.1.1.1 10.1.1.100 
#
acl 6001
 rule 1 permit ip source user-group group1
#
traffic classifier c1 operator or
 if-match acl 6001 precedence 1
#
traffic behavior b1
 nat bind instance nat1
#
traffic policy p1
 classifier c1 behavior b1 precedence 1
#
radius-server group rd1
 radius-server authentication 192.168.7.249 1645 weight 0
 radius-server accounting 192.168.7.249 1646 weight 0
#
aaa
 authentication-scheme default0 
  authentication-mode RADIUS 
# 
 accounting-scheme default0 
  accounting-mode RADIUS 
# 
 domain natbras
  authentication-scheme default0
  accounting-scheme default0
  radius-server group rd1
  ip-pool baspool1
  vpn-instance vpna
  user-group group1 bind nat instance nat1
#
license
 active nat session-table size 16 slot 1
 active nat bandwidth-enhance 40 slot 1
#
interface GigabitEthernet0/2/1
 undo shutdown
 bas
 #
  access-type layer2-subscriber default-domain authentication natbras
  authentication-method bind
 #
#
traffic-policy p1 inbound
#
return
```