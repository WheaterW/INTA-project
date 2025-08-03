Example for Configuring Roaming User Access (Dual-Stack User Access)
====================================================================

Example for Configuring Roaming User Access (Dual-Stack User Access)

#### Networking Requirements

When a WLAN user roams between different APs, the user needs to be re-authenticated for login after being logged out, causing services to be interrupted. WLAN user roaming switching ensures service continuity when a user roams between different APs. On the network shown in [Figure 1](#EN-US_TASK_0000001504949597__fig_dc_ne_cfg_01360001), when a user roams from AP1 to AP2, the user is switched from interface1 to interface2 for login, ensuring service continuity.

**Figure 1** Configuring roaming user access![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/2.1 and GE0/1/1.1, respectively.


  
![](figure/en-us_image_0000001455589700.png)

#### Configuration Roadmap

1. Configure an AAA scheme and adopt RADIUS authentication and accounting.
2. Configure a local IPv4 address pool.
3. Configure a local IPv6 prefix pool.
4. Configure a local IPv6 address pool, and bind the local IPv6 prefix pool to this address pool.
5. Configure a domain.
6. Configure a DUID for the device.
7. Configure a BAS interface.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* Local prefix pool name
* IPv6 prefix to be assigned/Prefix length
* Local address pool names
* Domain name

#### Procedure

1. # Configure an AAA authentication scheme.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] aaa
   ```
   ```
   [*HUAWEI-aaa] authentication-scheme huawei
   ```
   ```
   [*HUAWEI-aaa-authen-huawei] authentication-mode radius
   ```
   ```
   [*HUAWEI-aaa-authen-huawei] commit
   ```
   ```
   [~HUAWEI-aaa-authen-huawei] quit
   ```
2. Configure an AAA accounting scheme.
   
   
   ```
   [~HUAWEI-aaa] accounting-scheme huawei
   ```
   ```
   [*HUAWEI-aaa-accounting-huawei] accounting-mode radius
   ```
   ```
   [*HUAWEI-aaa-accounting-huawei] commit
   ```
   ```
   [~HUAWEI-aaa-accounting-huawei] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
3. Configure a RADIUS server group.
   
   
   ```
   [~HUAWEI] radius-server group rd1
   ```
   ```
   [*HUAWEI-radius-rd1] radius-server authentication 192.168.7.249 1812
   ```
   ```
   [*HUAWEI-radius-rd1] radius-server accounting 192.168.7.249 1813
   ```
   ```
   [*HUAWEI-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
   ```
   ```
   [*HUAWEI-radius-rd1] quit
   ```
   ```
   [*HUAWEI] commit
   ```
4. Configure a username generation mode and password.
   
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] default-user-name include sysname
   ```
   ```
   [~HUAWEI-aaa] default-password cipher YsHsjx_202206
   ```
   ```
   [~HUAWEI-aaa] commit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
5. Configure an address pool.
   
   
   ```
   [~HUAWEI] ip pool pool1 bas local
   ```
   ```
   [*HUAWEI-ip-pool-pool1] gateway 10.0.0.1 255.255.255.0
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool1] section 0 10.0.0.2 10.0.0.100
   ```
   ```
   [~HUAWEI-ip-pool-pool1] quit
   ```
6. Configure a local IPv6 prefix pool.
   
   
   ```
   [~HUAWEI] ipv6 prefix pre1 local
   ```
   ```
   [*HUAWEI-ipv6-prefix-pre1] prefix 2001:DB8::/64
   ```
   ```
   [*HUAWEI-ipv6-prefix-pre1] commit
   ```
   ```
   [~HUAWEI-ipv6-prefix-pre1] quit
   ```
7. Configure a local IPv6 address pool, and bind the local IPv6 prefix pool to this address pool.
   
   
   ```
   [~HUAWEI] ipv6 pool pool2 bas local
   ```
   ```
   [*HUAWEI-ipv6-pool-pool2] prefix pre1
   ```
   ```
   [*HUAWEI-ipv6-pool-pool2] commit
   ```
   ```
   [~HUAWEI-ipv6-pool-pool2] quit
   ```
8. Configure a domain.
   
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain huawei
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] authentication-scheme huawei
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] accounting-scheme huawei
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] radius-server group rd1
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] commit
   ```
   ```
   [~HUAWEI-aaa-domain-huawei] ip-pool pool1
   ```
   ```
   [~HUAWEI-aaa-domain-huawei] ipv6-pool pool2
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] commit
   ```
   ```
   [~HUAWEI-aaa-domain-huawei] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
9. Configure a DUID for the device.
   
   
   ```
   [~HUAWEI] dhcpv6 duid llt
   ```
   ```
   [*HUAWEI] commit
   ```
10. Configure the same MAC addresses for main interfaces of the BAS interfaces before and after roaming.
    
    
    
    The main interfaces include GE and Eth-Trunk main interfaces. If the MAC addresses are different, IP/ARP packets for triggering roaming cannot reach the new BAS interface after the switchover. As a result, roaming cannot be triggered. You are advised to change the address to the MAC address of a roaming interface (GE**0/1/1** in this example).
    
    ```
    [~HUAWEI] interface GigabitEthernet 0/1/2
    ```
    ```
    [~HUAWEI]-GigabitEthernet0/1/2] mac-address 00e0-fc12-3456
    ```
11. Enable IPv6 and configure stateful address autoconfiguration on the interface.
    
    
    ```
    [~HUAWEI] interface GigabitEthernet 0/1/2.1
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2.1] ipv6 enable
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2.1] ipv6 address auto link-local
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2.1] ipv6 nd autoconfig managed-address-flag
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2.1] commit
    ```
    ```
    [~HUAWEI] interface GigabitEthernet 0/1/1.1
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1] ipv6 enable
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1] ipv6 address auto link-local
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1] ipv6 nd autoconfig managed-address-flag
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1] commit
    ```
12. Configure user VLANs.
    
    
    ```
    [~HUAWEI] interface GigabitEthernet 0/1/2.1
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2.1] user-vlan 100 200 qinq 300 400
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2.1-vlan-100-200-QinQ-300-400] commit
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/2.1-vlan-100-200-QinQ-300-400] quit
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/2.1] quit
    ```
    ```
    [~HUAWEI] interface GigabitEthernet 0/1/1.1
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1] user-vlan 500 600 qinq 700 800
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1-vlan-500-600-QinQ-700-800] commit
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/1.1-vlan-500-600-QinQ-700-800] quit
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/1.1] quit
    ```
13. Configure a BAS interface for IPoE user access.
    
    
    ```
    [~HUAWEI] interface GigabitEthernet 0/1/2.1
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2.1] bas
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2.1-bas] access-type layer2-subscriber default-domain authentication huawei
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2.1-bas] authentication-method bind
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2.1-bas] authentication-method-ipv6 bind
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2.1-bas] commit
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/2.1-bas] quit
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/2.1] quit
    ```
    ```
    [~HUAWEI] interface GigabitEthernet 0/1/1.1
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1] bas
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1-bas] access-type layer2-subscriber default-domain authentication huawei
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1-bas] authentication-method bind
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1-bas] authentication-method-ipv6 bind
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1-bas] commit
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/1.1-bas] quit
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/1.1] quit
    ```
14. Configure roaming. Three roaming modes are available. Select one as required.
    
    
    * Configure traffic-triggered roaming without logging out users.When receiving a packet sent by a user to trigger roaming procedures, the device updates the user's access information in a timely manner to keep the user online.
      ```
      [~HUAWEI] interface GigabitEthernet 0/1/2.1
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1] bas
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] ip-trigger 
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] arp-trigger
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] ipv6-trigger
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] nd-trigger
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] wlan-switch enable
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] quit
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~HUAWEI] interface GigabitEthernet 0/1/1.1
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1] bas
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1-bas] ip-trigger 
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1-bas] arp-trigger
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1-bas] ipv6-trigger
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1-bas] nd-trigger
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1-bas] wlan-switch enable
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1-bas] quit
      ```
      ```
      [*HUAWEI] commit
      ```
    
    
    * Configure protocol packet-triggered roaming without logging out users.Perform this step to trigger quick login of terminal users to a new AP when they send DHCPv4 Discover or Request messages, DHCPv6 Solicit messages, or ND RS messages for login.
      ```
      [~HUAWEI] interface GigabitEthernet 0/1/2.1
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1] bas
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] wlan-switch enable
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] commit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.1-bas] dhcp session-mismatch action roam ipv4 ipv6 nd
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.1-bas] quit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.1] quit
      ```
      ```
      [~HUAWEI] interface GigabitEthernet 0/1/1.1
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1] bas
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1-bas] wlan-switch enable
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1-bas] commit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/1.1-bas] dhcp session-mismatch action roam ipv4 ipv6 nd
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/1.1-bas] quit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/1.1] quit
      ```
    * Configure roaming with logging out users.Perform this step to configure the device to log out online users whose physical location information is changed but MAC addresses remain unchanged when they resend DHCP or ND login requests.
      ```
      [~HUAWEI] interface GigabitEthernet 0/1/2.1
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1] bas
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.1-bas] ip-trigger 
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] arp-trigger
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] ipv6-trigger
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] nd-trigger
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] wlan-switch enable
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] commit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.1-bas] dhcp session-mismatch action offline
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] quit
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1] quit
      ```
      ```
      [*HUAWEI] interface GigabitEthernet 0/1/1.1
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1] bas
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1-bas] ip-trigger 
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1-bas] arp-trigger
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1-bas] ipv6-trigger
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1-bas] nd-trigger
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1-bas] wlan-switch enable
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1-bas] commit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/1.1-bas] dhcp session-mismatch action offline
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1-bas] quit
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1] quit
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1.1] commit
      ```
15. Verify the configuration.
    
    
    
    The user goes online through GigabitEthernet0/1/2.1.
    
    ```
    [~HUAWEI] display access-user domain huawei
    ```
    ```
    --------------------------------------------------------------
    UserID     Username       Interface   IP address  MAC             
               Vlan    IPv6 address  Access type 
    --------------------------------------------------------------- 
    208896     HUAWEI@huawei  GE0/1/2.1   10.0.0.98  00e0-fc12-3456  
               300/100  -            IPOE                              
    ---------------------------------------------------------------- 
    Normal users                       : 1 
    RUI Local users                    : 0 
    RUI Remote users                   : 0 
    Total users                        : 1
    ```
    
    The user roams to GigabitEthernet0/1/1.1 successfully.
    
    ```
    [~HUAWEI] display access-user domain huawei
    ```
    ```
    -----------------------------------------------------------------
    UserID     Username       Interface   IP address  MAC             
               Vlan    IPv6 address  Access type 
    ------------------------------------------------------------------ 
    208896     HUAWEI@huawei  GE0/1/1.1   10.0.0.98  00e0-fc12-3456  
               700/500  -            IPOE                              
    -------------------------------------------------------------------
    Normal users                       : 1 
    RUI Local users                    : 0 
    RUI Remote users                   : 0 
    Total users                        : 1
    ```

#### Configuration Files

* HUAWEI configuration file (traffic-triggered roaming without logging out users)
  ```
  #
  sysname HUAWEI
  #
  radius-server group rad_group1
   radius-server shared-key-cipher %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#  
   radius-server authentication 192.168.7.249 1812 weight 0  
   radius-server accounting 192.168.7.249 1813 weight 0  
  #
  ip pool pool1 bas local
   gateway 10.0.0.1 255.255.255.0
   section 0 10.0.0.2 10.0.0.100
  #
  ipv6 prefix pre1 local
   prefix 2001:DB8::/64
  #
  ipv6 pool pool2 bas local
   prefix pre1
  #
  dhcpv6 duid llt
  #
  aaa
   default-password cipher %^%#4*RHO=w*}.d\>j09'Z:%=:co~p\w9'G-^|-zR'N4%^%# 
   default-user-name include sysname
   #
   authentication-scheme default0
   #
   authentication-scheme default1
   #
   authentication-scheme huawei
   #
   authentication-scheme default
   #
   accounting-scheme huawei
   #
   domain default0
   #
   domain default1
   #
   domain default_admin
   #
   domain huawei
    authentication-scheme huawei
    accounting-scheme huawei
    radius-server group rd1
    ip-pool pool1
    ipv6-pool pool2
  #
  interface GigabitEthernet0/1/2
   mac-address 00e0-fc12-3456
  #
  interface GigabitEthernet0/1/2.1
   ipv6 enable
   ipv6 address auto link-local
   user-vlan 100 200 qinq 300 400
   ipv6 nd autoconfig managed-address-flag
   bas
   #
    access-type layer2-subscriber default-domain authentication huawei
    authentication-method bind
    authentication-method-ipv6 bind
    ip-trigger
    arp-trigger
    wlan-switch enable
    ipv6-trigger
    nd-trigger
   #
  #
  interface GigabitEthernet0/1/1.1
   ipv6 enable
   ipv6 address auto link-local
   user-vlan 500 600 qinq 700 800
   ipv6 nd autoconfig managed-address-flag
   bas
   #
    access-type layer2-subscriber default-domain authentication huawei
    authentication-method bind
    authentication-method-ipv6 bind
    ip-trigger
    arp-trigger
    wlan-switch enable
    ipv6-trigger
    nd-trigger
   #
  #
  return
  ```
* HUAWEI configuration file (protocol packet-triggered roaming without logging out users)
  ```
  #
  sysname HUAWEI
  #
  radius-server group rad_group1
   radius-server shared-key-cipher %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#  
   radius-server authentication 192.168.7.249 1812 weight 0  
   radius-server accounting 192.168.7.249 1813 weight 0  
  #
  ip pool pool1 bas local
   gateway 10.0.0.1 255.255.255.0
   section 0 10.0.0.2 10.0.0.100
  #
  ipv6 prefix pre1 local
   prefix 2001:DB8::/64
  #
  ipv6 pool pool2 bas local
   prefix pre1
  #
  dhcpv6 duid llt
  #
  aaa
   default-password cipher %^%#4*RHO=w*}.d\>j09'Z:%=:co~p\w9'G-^|-zR'N4%^%# 
   default-user-name include sysname
   #
   authentication-scheme default0
   #
   authentication-scheme default1
   #
   authentication-scheme huawei
   #
   authentication-scheme default
   #
   accounting-scheme huawei
   #
   domain default0
   #
   domain default1
   #
   domain default_admin
   #
   domain huawei
    authentication-scheme huawei
    accounting-scheme huawei
    radius-server group rd1
    ip-pool pool1
    ipv6-pool pool2
  #
  interface GigabitEthernet0/1/2
   mac-address 00e0-fc12-3456
  #
  interface GigabitEthernet0/1/2.1
   ipv6 enable
   ipv6 address auto link-local
   ipv6 nd autoconfig managed-address-flag
   user-vlan 100 200 qinq 300 400
   bas
   #
    access-type layer2-subscriber default-domain authentication huawei
    dhcp session-mismatch action roam ipv4 ipv6 nd
    authentication-method bind
    authentication-method-ipv6 bind
    wlan-switch enable
   #
  #
  interface GigabitEthernet0/1/1.1
   ipv6 enable
   ipv6 address auto link-local
   user-vlan 500 600 qinq 700 800
   ipv6 nd autoconfig managed-address-flag
   bas
   #
    access-type layer2-subscriber default-domain authentication huawei
    dhcp session-mismatch action roam ipv4 ipv6 nd
    authentication-method bind
    authentication-method-ipv6 bind
    wlan-switch enable
   #
  #
  return
  ```
* HUAWEI configuration file (roaming with logging out users)
  ```
  #
  sysname HUAWEI
  #
  radius-server group rad_group1
   radius-server shared-key-cipher %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#  
   radius-server authentication 192.168.7.249 1812 weight 0  
   radius-server accounting 192.168.7.249 1813 weight 0  
  #
  ip pool pool1 bas local
   gateway 10.0.0.1 255.255.255.0
   section 0 10.0.0.2 10.0.0.100
  #
  ipv6 prefix pre1 local
   prefix 2001:DB8::/64
  #
  ipv6 pool pool2 bas local
   prefix pre1
  #
  dhcpv6 duid llt
  #
  aaa
   default-password cipher %^%#4*RHO=w*}.d\>j09'Z:%=:co~p\w9'G-^|-zR'N4%^%# 
   default-user-name include sysname
   #
   authentication-scheme default0
   #
   authentication-scheme default1
   #
   authentication-scheme huawei
   #
   authentication-scheme default
   #
   accounting-scheme huawei
   #
   domain default0
   #
   domain default1
   #
   domain default_admin
   #
   domain huawei
    authentication-scheme huawei
    accounting-scheme huawei
    radius-server group rd1
    ip-pool pool1
    ipv6-pool pool2
  #
  interface GigabitEthernet0/1/2.1
   ipv6 enable
   ipv6 address auto link-local
   user-vlan 100 200 qinq 300 400
   ipv6 nd autoconfig managed-address-flag
   bas
   #
    access-type layer2-subscriber default-domain authentication huawei
    dhcp session-mismatch action offline
    authentication-method bind
    authentication-method-ipv6 bind
    ip-trigger
    arp-trigger
    wlan-switch enable
    ipv6-trigger
    nd-trigger
   #
  #
  interface GigabitEthernet0/1/1.1
   ipv6 enable
   ipv6 address auto link-local
   user-vlan 500 600 qinq 700 800
   ipv6 nd autoconfig managed-address-flag
   bas
   #
    access-type layer2-subscriber default-domain authentication huawei
    dhcp session-mismatch action offline
    authentication-method bind
    authentication-method-ipv6 bind
    ip-trigger
    arp-trigger
    wlan-switch enable
    ipv6-trigger
    nd-trigger
   #
  #
  return
  ```