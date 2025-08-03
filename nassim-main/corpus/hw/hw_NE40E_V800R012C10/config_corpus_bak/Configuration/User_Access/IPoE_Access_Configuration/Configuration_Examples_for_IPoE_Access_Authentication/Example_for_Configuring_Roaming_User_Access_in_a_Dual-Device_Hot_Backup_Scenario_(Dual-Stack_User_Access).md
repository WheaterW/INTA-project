Example for Configuring Roaming User Access in a Dual-Device Hot Backup Scenario (Dual-Stack User Access)
=========================================================================================================

Example_for_Configuring_Roaming_User_Access_in_a_Dual-Device_Hot_Backup_Scenario_(Dual-Stack_User_Access)

#### Networking Requirements

WLAN roaming allows a STA to move between different APs in the same ESS without interrupting existing services. When a WLAN user roams between different APs, the user needs to be re-authenticated for login after being logged out, causing services to be interrupted. WLAN user roaming switching ensures service continuity when a user roams between different APs. On the network shown in [Figure 1](#EN-US_TASK_0000001509875365__fig624412481872), when a user roams from AP1 to AP2, the user is switched from Device1's interface1 to interface2 for login, ensuring service continuity. To ensure network reliability, dual-device hot backup is deployed. If a device fault occurs, the user can switch from Device2's interface4 to interface3 for login, without affecting roaming services.

**Figure 1** Configuring roaming user access in a dual-device hot backup scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 5 represent GE0/1/0.1, GE0/1/0.2, GE0/2/0.1, GE0/2/0.2, and GE0/3/0, respectively.


  
![](figure/en-us_image_0000002132210158.png)
#### Configuration Roadmap

1. Configure IP addresses for interfaces.
2. Configure routing protocols.
3. Configure an AAA scheme and adopt RADIUS authentication and accounting.
4. Configure a RADIUS server.
5. Configure a username generation mode and a password.
6. Configure a local IPv4 address pool, a local IPv6 prefix pool, and a local IPv6 address pool, and bind the prefix pool to the address pool.
7. Configure a DUID for the device.
8. Configure a domain.
9. Configure the IPv6 function on the user-side interface of the device.
10. Configure user VLANs.
11. Configure a BAS interface.
12. Deploy VRRP.
13. Configure a remote backup service (RBS) and a remote backup profile (RBP).
14. Configure roaming with logging out users.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configuration of Device2 is similar to the configuration of Device1. The configuration procedure on Device1 is used as an example. For details about the configuration on Device2, see Configuration Files.




#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* Local prefix pool name
* IPv6 prefix to be assigned/Prefix length
* Local address pool names
* Domain name

#### Procedure

1. Configure IP addresses for the protection tunnel.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device1
   [*HUAWEI] commit
   [~Device1] interface loopback2
   [*Device1-Loopback2] ipv6 enable
   [*Device1-Loopback2] ip address 10.3.3.3 32
   [*Device1-Loopback2] ipv6 address 2001:db8:9::7 128
   [*Device1-Loopback2] quit
   [*Device1] commit
   ```
2. Configure IP addresses for the network-side interface.
   
   
   ```
   [~Device1] interface gigabitEthernet0/3/0
   [*Device1-GigabitEthernet0/3/0] ipv6 enable 
   [*Device1-GigabitEthernet0/3/0] ipv6 address 2001:db8:8::7 64
   [*Device1-GigabitEthernet0/3/0] ipv6 address auto link-local
   [*Device1-GigabitEthernet0/3/0] ip address 10.2.1.1 24
   [*Device1-GigabitEthernet0/3/0] quit
   [*Device1] commit
   ```
3. Configure routing protocols.
   
   
   
   # Enable the function to automatically control a route's cost preference.
   
   ```
   [~Device1] peer-backup route-cost auto-advertising
   [*Device1] commit
   ```
   
   # Configure OSPF to import UNRs.
   
   ```
   [~Device1] ospf 1
   [*Device1-ospf-1] default cost inherit-metric
   [*Device1-ospf-1] import-route unr
   [*Device1-ospf-1] area 0
   [*Device1-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   [*Device1-ospf-1-area-0.0.0.0] network 10.3.3.3 0.0.0.0
   [*Device1-ospf-1-area-0.0.0.0] quit
   [*Device1-ospf-1] quit
   [*Device1] commit
   ```
   
   # Configure basic OSPFv3 functions to implement intra-AS IPv6 route reachability.
   
   ```
   [*Device1] ospfv3
   [*Device1-ospfv3-1] router-id 1.1.1.1
   [*Device1-ospfv3-1] area 0.0.0.0
   [*Device1-ospfv3-1-area-0.0.0.0] quit
   [*Device1-ospfv3-1] quit
   [*Device1] interface gigabitEthernet0/3/0
   [*Device1-GigabitEthernet0/3/0] ospfv3 1 area 0.0.0.0
   [*Device1-GigabitEthernet0/3/0] quit
   [*Device1] interface Loopback2
   [*Device1-Loopback2] ospfv3 1 area 0.0.0.0
   [*Device1] commit 
   ```
4. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme and set the authentication mode to RADIUS.
   
   ```
   [~Device1] aaa
   [~Device1-aaa] authentication-scheme auth1
   [*Device1-aaa-authen-auth1] authentication-mode radius
   [*Device1-aaa-authen-auth1] quit
   [*Device1-aaa] commit
   ```
   
   # Configure an accounting scheme and set the accounting mode to RADIUS.
   
   ```
   [~Device1-aaa] accounting-scheme acct1
   [*Device1-aaa-accounting-acct1] accounting-mode radius
   [*Device1-aaa-accounting-acct1] quit
   [*Device1-aaa] commit
   [*Device1-aaa] quit
   ```
5. Configure RADIUS.
   
   
   
   # Configure a RADIUS server group.
   
   
   
   ```
   [~Device1] radius-server group rd1
   [*Device1-radius-rd1] radius-server authentication 192.168.7.249 1812 weight 0
   [*Device1-radius-rd1] radius-server accounting 192.168.7.249 1813 weight 0
   [*Device1-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
   [*Device1-radius-rd1] quit
   [*Device1] commit
   ```
6. Configure a username generation mode and password.
   
   
   ```
   [~Device1] aaa
   [~Device1-aaa] default-user-name include sysname
   [~Device1-aaa] default-password cipher YsHsjx_202206
   [~Device1-aaa] commit
   [~Device1-aaa] quit
   ```
7. Configure address pools.
   
   
   
   # Configure a user-side local IPv4 address pool.
   
   ```
   [~Device1] ip pool pool2 bas local
   [*Device1-ip-pool-pool_v4] gateway 10.0.0.1 255.255.255.0
   [*Device1-ip-pool-pool_v4] commit
   [~Device1-ip-pool-pool_v4] section 0 10.0.0.2 10.0.0.100 
   [*Device1-ip-pool-pool_v4] quit
   [*Device1] commit
   ```
   
   # Configure a user-side local IPv6 address pool.
   
   ```
   [~Device1] ipv6 prefix pre1 local
   [*Device1-ipv6-prefix-pre_nd] prefix 2001:db8:1::/48
   [*Device1-ipv6-prefix-pre_nd] quit
   [*Device1] commit
   [~Device1] ipv6 pool pool1 bas local
   [*Device1-ipv6-pool-pool_nd] prefix pre1
   [*Device1-ipv6-pool-pool_nd] quit
   [*Device1] commit
   ```
8. Configure the DHCPv6 device to generate a DUID in DUID-LLT mode. (This step is not required if a DUID has been configured on Device1.)
   
   
   ```
   [~Device1] dhcpv6 duid llt
   [*Device1] commit
   ```
9. Configure a domain.
   
   
   ```
   [~Device1] aaa
   [~Device1-aaa] domain huawei
   [*Device1-aaa-domain-huawei] authentication-scheme auth1
   [*Device1-aaa-domain-huawei] accounting-scheme acct1
   [*Device1-aaa-domain-huawei] radius-server group rd1
   [*Device1-aaa-domain-huawei] commit 
   [~Device1-aaa-domain-huawei] ip-pool pool2
   [~Device1-aaa-domain-huawei] ipv6-pool pool1
   [*Device1-aaa-domain-huawei] commit
   [~Device1-aaa-domain-huawei] quit
   [~Device1-aaa] quit
   ```
10. Enable IPv6 and configure stateful address autoconfiguration on the interface.
    
    
    ```
    [~Device1] interface gigabitethernet 0/1/0.1
    [*Device1-GigabitEthernet0/1/0.1] ipv6 enable
    [*Device1-GigabitEthernet0/1/0.1] ipv6 address auto link-local
    [*Device1-GigabitEthernet0/1/0.1] quit
    [*Device1] commit
    [~Device1] interface gigabitethernet 0/1/0.2
    [*Device1-GigabitEthernet0/1/0.2] ipv6 enable
    [*Device1-GigabitEthernet0/1/0.2] ipv6 address auto link-local
    [*Device1-GigabitEthernet0/1/0.2] quit
    [*Device1] commit
    ```
11. Configure user VLANs.
    
    
    ```
    [~Device1] interface gigabitethernet 0/1/0.1 
    [*Device1-GigabitEthernet0/1/0.1] user-vlan 100 200 qinq 300 400
    [*Device1-GigabitEthernet0/1/0.1-vlan-100-200-QinQ-300-400] quit
    [*Device1-GigabitEthernet0/1/0.1] quit
    [*Device1] commit
    [~Device1] interface gigabitethernet 0/1/0.2
    [*Device1-GigabitEthernet0/1/0.2] user-vlan 500 600 qinq 700 800
    [*Device1-GigabitEthernet0/1/0.2-vlan-500-600-QinQ-700-800] quit
    [*Device1-GigabitEthernet0/1/0.2] quit
    [*Device1] commit
    ```
12. Configure a BAS interface for IPoE user access.
    
    
    ```
    [~Device1] interface gigabitethernet 0/1/0.1
    [~Device1-GigabitEthernet0/1/0.1] bas
    [~Device1-GigabitEthernet0/1/0.1-bas] access-type layer2-subscriber default-domain authentication huawei
    [*Device1-GigabitEthernet0/1/0.1-bas] authentication-method bind
    [*Device1-GigabitEthernet0/1/0.1-bas] authentication-method-ipv6 bind
    [*Device1-GigabitEthernet0/1/0.1-bas] quit
    [*Device1-GigabitEthernet0/1/0.1] quit
    [*Device1] commit
    [~Device1] interface gigabitethernet 0/1/0.2
    [*Device1-GigabitEthernet0/1/0.2] bas
    [*Device1-GigabitEthernet0/1/0.2-bas] access-type layer2-subscriber default-domain authentication huawei
    [*Device1-GigabitEthernet0/1/0.2-bas] authentication-method bind
    [*Device1-GigabitEthernet0/1/0.2-bas] authentication-method-ipv6 bind
    [*Device1-GigabitEthernet0/1/0.2-bas] quit
    [*Device1-GigabitEthernet0/1/0.2] quit
    [*Device1] commit
    ```
13. Deploy VRRP on the master and backup devices. Device1 is the master, and Device2 is the backup.
    
    
    
    # Configure a VRRP group on an interface (Gigabitethernet 0/1/0.100 is used as an example).
    
    ```
    [~Device1] interface gigabitethernet 0/1/0.100 
    [*Device1-Eth-trunk100.1] vlan-type dot1q 1001
    [*Device1-Eth-trunk100.1] ip address 10.1.10.1 255.255.255.0
    [*Device1-Eth-trunk100.1] vrrp vrid 1 virtual-ip 10.1.10.10
    [*Device1-Eth-trunk100.1] vrrp vrid 1 priority 150 
    [~Device1-Eth-trunk100.1] quit
    [*Device1] commit
    ```
14. Configure an RBS and an RBP.
    
    
    
    # Configure an RBS.
    
    ```
    [~Device1] peer-backup route-cost auto-advertising
    [~Device1] remote-backup-service s1
    [*Device1-rm-backup-srv-s1] peer 10.13.13.13 source 10.3.3.3 port 6001
    [*Device1-rm-backup-srv-s1] protect lsp-tunnel for-all-instance peer-ip 10.13.13.13
    [*Device1-rm-backup-srv-s1] ip-pool pool2 metric 20
    [*Device1-rm-backup-srv-s1] ipv6-pool pool1 metric 20
    [*Device1-rm-backup-srv-s1] quit
    [*Device1] commit
    ```
    
    # Configure an RBP.
    
    ```
    [~Device1] remote-backup-profile p1
    [*Device1-rm-backup-prf-p1] service-type bras
    [*Device1-rm-backup-prf-p1] peer-backup hot
    [*Device1-rm-backup-prf-p1] backup-id 1 remote-backup-service s1
    [*Device1-rm-backup-prf-p1] vrrp-id 1 interface gigabitethernet 0/1/0.100
    [*Device1-rm-backup-prf-p1] quit
    [*Device1] commit
    ```
    
    # Bind the RBP to the interface through which the user goes online.
    
    ```
    [~Device1] interface gigabitethernet 0/1/0.1
    [*Device1-GigabitEthernet0/1/0.1] remote-backup-profile p1
    [*Device1-GigabitEthernet0/1/0.1] quit
    [*Device1] interface gigabitethernet 0/1/0.2
    [*Device1-GigabitEthernet0/1/0.2] remote-backup-profile p1
    [*Device1-GigabitEthernet0/1/0.2] quit
    [*Device1] commit
    ```
15. Configure roaming with logging out users.
    
    
    ```
    [~Device1] interface gigabitethernet 0/1/0.1
    [*Device1-GigabitEthernet0/1/0.1] bas
    [*Device1-GigabitEthernet0/1/0.1-bas] ip-trigger
    [*Device1-GigabitEthernet0/1/0.1-bas] arp-trigger
    [*Device1-GigabitEthernet0/1/0.1-bas] ipv6-trigger
    [*Device1-GigabitEthernet0/1/0.1-bas] nd-trigger
    [*Device1-GigabitEthernet0/1/0.1-bas] commit
    [~Device1-GigabitEthernet0/1/0.1-bas] dhcp session-mismatch action offline
    [*Device1-GigabitEthernet0/1/0.1-bas] quit
    [*Device1-GigabitEthernet0/1/0.1] quit
    [~Device1] interface gigabitethernet 0/1/0.2
    [*Device1-GigabitEthernet0/1/0.2] bas
    [*Device1-GigabitEthernet0/1/0.2-bas] ip-trigger
    [*Device1-GigabitEthernet0/1/0.2-bas] arp-trigger
    [*Device1-GigabitEthernet0/1/0.2-bas] ipv6-trigger
    [*Device1-GigabitEthernet0/1/0.2-bas] nd-trigger
    [*Device1-GigabitEthernet0/1/0.2-bas] commit
    [~Device1-GigabitEthernet0/1/0.2-bas] dhcp session-mismatch action offline
    [*Device1-GigabitEthernet0/1/0.2-bas] quit
    [*Device1-GigabitEthernet0/1/0.2] quit
    [*Device1] commit
    ```
16. Verify the configuration.
    
    
    
    The user goes online through GE0/1/0.1.
    
    ```
    [~Device1] display access-user domain huawei
    ```
    ```
    ------------------------------------------------------------------------------ 
    UserID     Username                Interface      IP address       MAC             
               Vlan          IPv6 address             Access type 
    ------------------------------------------------------------------------------ 
    508928     Device1@huawei           GE0/1/0.1      10.0.0.98       00-e0-fc-12-34-56  
               300/100       2001:DB8:1:2                  IPOE                             
    ------------------------------------------------------------------------------ 
    Normal users                       : 0 
    RUI Local users                    : 1 
    RUI Remote users                   : 0 
    Total users                        : 1
    ```
    
    The terminal user successfully roams to GE0/1/0.2 by resending DHCPv4 Discover or Request messages and DHCPv6 Solicit messages.
    
    ```
    [~Device1] display access-user domain huawei
    ```
    ```
     ------------------------------------------------------------------------------ 
    UserID     Username                Interface      IP address     MAC            
               Vlan          IPv6 address             Access type 
    ------------------------------------------------------------------------------ 
    510976      Device1@huawei           GE0/1/0.2      10.0.0.97     00-e0-fc-12-34-56  
               700/500      2001:DB8:1:3                  IPOE                              
    ------------------------------------------------------------------------------ 
    Normal users                       : 0 
    RUI Local users                    : 1 
    RUI Remote users                   : 0 
    Total users                        : 1
    ```

#### Configuration Files

The configurations of Device1 and Device2 are as follows:

| Item | Device1 | Device2 |
| --- | --- | --- |
| Configure a device name. | ``` # sysname Device1 # ``` | ``` # sysname Device2 # ``` |
| Configure a RADIUS server group. | ``` radius-server group rd1   radius-server shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^%   radius-server authentication 192.168.7.249 1812 weight 0  radius-server accounting 192.168.7.249 1813 weight 0 # ``` | ``` radius-server group rd1                                                         radius-server shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^%  radius-server authentication 192.168.7.249 1812 weight 0  radius-server accounting 192.168.7.249 1813 weight 0 #  ``` |
| Configure address pools. | ``` ip pool pool2 bas local  gateway 10.0.0.1 255.255.255.0  section 0 10.0.0.2 10.0.0.100 # ipv6 prefix pre1 local  prefix 2001:DB8:1::/48 # ipv6 pool pool1 bas local  prefix pre1 # ``` | ``` ip pool pool2 bas local rui-slave  gateway 10.0.0.1 255.255.255.0  section 0 10.0.0.2 10.0.0.100 # ipv6 prefix pre1 local  prefix 2001:DB8:1::/48 # ipv6 pool pool1 bas local rui-slave  prefix pre1 # ``` |
| Configure dual-device backup. | ``` peer-backup route-cost auto-advertising remote-backup-service s1  peer 10.13.13.13 source 10.3.3.3 port 6001  protect lsp-tunnel for-all-instance peer-ip 10.13.13.13  ip-pool pool2 metric 20  ipv6-pool pool1 metric 20 # remote-backup-profile p1  service-type bras  backup-id 1 remote-backup-service s1  peer-backup hot  vrrp-id 1 interface GigabitEthernet0/1/0.100 # ``` | ``` peer-backup route-cost auto-advertising remote-backup-service s1  peer 10.3.3.3 source 10.13.13.13 port 6001  protect lsp-tunnel for-all-instance peer-ip 10.3.3.3  ip-pool pool2 metric 10  ipv6-pool pool1 metric 10 # remote-backup-profile p1  service-type bras  backup-id 1 remote-backup-service s1  peer-backup hot  vrrp-id 1 interface GigabitEthernet0/2/0.100 # ``` |
| Configure a DUID. | ``` dhcpv6 duid llt # ``` | ``` dhcpv6 duid llt # ``` |
| Configure an authentication mode and an accounting scheme, and bind them to a domain. | ``` aaa  default-password cipher %^%#4*RHO=w*}.d\>j09'Z:%=:co~p\w9'G-^|-zR'N4%^%#   default-user-name include sysname  #  authentication-scheme default0  #  authentication-scheme default1  #  authentication-scheme auth1  #  authentication-scheme default  #  accounting-scheme acct1  #  domain default0  #  domain default1  #  domain default_admin  #  domain huawei   authentication-scheme auth1   accounting-scheme acct1   radius-server group rd1   ip-pool pool2   ipv6-pool pool1                  #   ``` | ``` aaa  default-password cipher %^%#4*RHO=w*}.d\>j09'Z:%=:co~p\w9'G-^|-zR'N4%^%#   default-user-name include sysname  #  authentication-scheme default0  #  authentication-scheme default1  #  authentication-scheme auth1  #  authentication-scheme default  #  accounting-scheme acct1  #  domain default0  #  domain default1  #  domain default_admin  #  domain huawei   authentication-scheme auth1   accounting-scheme acct1   radius-server group rd1   ip-pool pool2   ipv6-pool pool1 #  ``` |
| Configure interface information and roaming | ``` interface LoopBack2  ipv6 enable  ip address 10.3.3.3 255.255.255.255  ipv6 address 2001:DB8:9::7 128  ospfv3 area 0.0.0.0 # interface GigabitEthernet0/1/0.100   vlan-type dot1q 1001  ip address 10.1.10.1 255.255.255.0  vrrp vrid 1 virtual-ip 10.1.10.10  vrrp vrid 1 priority 150  #  interface GigabitEthernet0/1/0.1  undo shutdown   ipv6 enable  ipv6 address auto link-local  user-vlan 100 200 qinq 300 400  ipv6 nd autoconfig managed-address-flag   ipv6 address auto link-local  remote-backup-profile p1  bas   #   access-type layer2-subscriber default-domain authentication huawei   dhcp session-mismatch action offline   authentication-method bind   authentication-method-ipv6 bind   ip-trigger   arp-trigger   ipv6-trigger   nd-trigger   # # interface GigabitEthernet0/1/1.2  undo shutdown   ipv6 enable  ipv6 address auto link-local  user-vlan 500 600 qinq 700 800  ipv6 nd autoconfig managed-address-flag   ipv6 address auto link-local  remote-backup-profile p1  bas   #   access-type layer2-subscriber default-domain authentication huawei   dhcp session-mismatch action offline   authentication-method bind   authentication-method-ipv6 bind   ip-trigger   arp-trigger   ipv6-trigger   nd-trigger   # # interface GigabitEthernet0/3/0  undo shutdown   ipv6 enable  ip address 10.2.1.1 255.255.255.0  ipv6 address 2001:DB8:8::7 64  ipv6 address auto link-local   ospfv3 area 0.0.0.0 ``` | ``` interface LoopBack2  ipv6 enable  ip address 10.13.13.13 255.255.255.255  ipv6 address 2001:DB8:19::7 128  ospfv3 area 0.0.0.0 # interface GigabitEthernet0/2/0.100   vlan-type dot1q 1001  ip address 10.1.10.2 255.255.255.0  vrrp vrid 1 virtual-ip 10.1.10.10 #  interface GigabitEthernet0/2/0.1  undo shutdown   ipv6 enable  ipv6 address auto link-local  user-vlan 100 200 qinq 300 400  ipv6 nd autoconfig managed-address-flag  ipv6 address auto link-local  remote-backup-profile p1  bas   #   access-type layer2-subscriber default-domain authentication huawei   dhcp session-mismatch action offline   authentication-method bind   authentication-method-ipv6 bind   ip-trigger   arp-trigger   ipv6-trigger   nd-trigger   # # interface GigabitEthernet0/2/0.2  undo shutdown   ipv6 enable  ipv6 address auto link-local  user-vlan 500 600 qinq 700 800  ipv6 nd autoconfig managed-address-flag   ipv6 address auto link-local  remote-backup-profile p1  bas   #   access-type layer2-subscriber default-domain authentication huawei   dhcp session-mismatch action offline   authentication-method bind   authentication-method-ipv6 bind   ip-trigger   arp-trigger   ipv6-trigger   nd-trigger   # # interface GigabitEthernet0/3/0  undo shutdown   ipv6 enable  ip address 10.4.1.1 255.255.255.0  ipv6 address 2001:DB8:18::7 64  ipv6 address auto link-local  ospfv3 area 0.0.0.0 ``` |
| Import UNRs. | ``` # ospf  default cost inherit-metric  import-route unr  area 0.0.0.0  network 10.2.1.0 0.0.0.255  network 10.3.3.3 0.0.0.0 # ``` | ``` # ospf  default cost inherit-metric  import-route unr  area 0.0.0.0  network 10.4.1.0 0.0.0.255  network 10.13.13.13 0.0.0.0 # ``` |
| Configure OSPFv3 routes. | ``` # ospfv3 1  router-id 1.1.1.1  area 0.0.0.0 # return ``` | ``` # ospfv3 1  router-id 2.2.2.2  area 0.0.0.0 # return ``` |