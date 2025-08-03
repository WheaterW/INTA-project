Example for Configuring User Address Assignment Through a Remote Address Pool
=============================================================================

This section provides an example for configuring a remote address pool to assign IPv4 addresses to access users.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172373815__fig_dc_ne_ipv4_address_cfg_006701), it is required that a remote address pool be configured to assign addresses to access users and the following requirements be met:

* A remote address pool is used to assign addresses to users in the domain **isp2**.
* The Router functions as a relay agent and is connected to the DHCPv4 server through GE 0/3/0. The IP address of GE0/3/0 is 10.1.1.2/24.
* The address of the DHCPv4 server bound to the remote address pool is 10.1.1.1, and no standby DHCPv4 server is deployed.

**Figure 1** Configuring user address assignment through a remote address pool  
![](figure/en-us_image_0000001193362342.png)![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0.1, GE0/2/0, and GE0/3/0, respectively.




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a DHCPv4 server group and a remote address pool, and bind the address pool to the DHCPv4 server group.
2. Configure a domain named **isp2** to which users belong, including the authentication and accounting modes.
3. Configure a BAS interface, including the user access mode.

#### Data Preparation

To complete the configuration, you need the following data:

* Address pool name
* Gateway address
* Name of the domain to which users belong
* IP address of the interface that connects the device to the server
* User access mode
* User authentication mode (RADIUS authentication)

#### Procedure

1. Perform the following steps on the Router.
   
   
   
   # Create a DHCPv4 server group.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] dhcp-server group group1
   ```
   ```
   [*HUAWEI-dhcp-server-group-group1] dhcp-server 10.1.1.1
   ```
   ```
   [*HUAWEI-dhcp-server-group-group1] commit
   ```
   ```
   [~HUAWEI-dhcp-server-group-group1] quit
   ```
   
   # Create a remote address pool, and bind the pool to the DHCPv4 server group.
   
   ```
   [~HUAWEI] ip pool pool2 bas remote
   ```
   ```
   [~HUAWEI-ip-pool-pool2] gateway 10.10.10.1 24
   ```
   ```
   [*HUAWEI-ip-pool-pool2] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool2] dhcp-server group group1
   ```
   ```
   [*HUAWEI-ip-pool-pool2] commit
   ```
   ```
   [~HUAWEI] quit
   ```
   
   # Configure a RADIUS server group.
   
   ```
   [~HUAWEI-aaa] radius-server group rd
   ```
   ```
   [*HUAWEI-radius-rd] radius-server authentication 10.7.66.66 1812
   ```
   ```
   [*HUAWEI-radius-rd] radius-server accounting 10.7.66.66 1813
   ```
   ```
   [*HUAWEI-radius-rd] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*HUAWEI-radius-rd] radius-server retransmit 2
   ```
   ```
   [*HUAWEI-radius-rd] commit
   ```
   ```
   [~HUAWEI-radius-rd] quit
   ```
   
   # Configure a domain named **isp2**.
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain isp2
   ```
   ```
   [*HUAWEI-aaa-domain-isp2] authentication-scheme default1
   ```
   ```
   [*HUAWEI-aaa-domain-isp2] accounting-scheme default0
   ```
   ```
   [*HUAWEI-aaa-domain-isp2] radius-server group rd
   ```
   ```
   [*HUAWEI-aaa-domain-isp2] commit
   ```
   ```
   [~HUAWEI-aaa-domain-isp2] ip-pool pool2
   ```
   ```
   [*HUAWEI-aaa-domain-isp2] commit
   ```
   ```
   [~HUAWEI-aaa-domain-isp2] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
   
   # Configure a user access interface.
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/0.1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1] user-vlan 1
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1-vlan-1-1] bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1-bas] access-type layer2-subscriber
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1-bas] authentication-method bind
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1-bas] default-domain authentication isp2
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.1-bas] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1-bas] quit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1] quit
   ```
   
   # Configure the interface connecting the device to the server.
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/3/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/3/0] ip address 10.1.1.2 255.255.255.0
   ```
   ```
   [*HUAWEI-GigabitEthernet0/3/0] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/3/0] quit
   ```
2. Verify the configuration.
   
   
   
   # Check the configurations of the DHCP server group **group1**.
   
   ```
   [~HUAWEI] display dhcp-server group group1
     Group-Name          : group1
     Release-Agent       : Support
     Primary-Server      : 10.1.1.1
       Vpn instance      : --
     Weight              : 0
     Status              : up
     Secondary-Server    : -
       Vpn instance      : --
     Weight              : 0
     Status              : -
     Algorithm           : master-backup
     Source              : --
     Giaddr              : --      
   
   ```
   
   # Check the configurations of the remote address pool **pool2**.
   
   ```
   [~HUAWEI] display ip pool name pool2
   ```
   ```
     Pool-Name      : pool2
     Pool-No        : 0 
     Pool-constant-index :- 
     DHCP-Group     : group1
     Position       : Remote          Status           : Unlocked
     Gateway        : 10.10.10.1      Mask             : 255.255.255.0
     Vpn instance   : --
     Profile-Name   : -               Server-Name      : -
     Codes: CFLCT (conflicted)
   
     ---------------------------------------------------------------------------------------
     ID           start             end total  used  idle CFLCT disable reserved static-bind
     ---------------------------------------------------------------------------------------
      0      10.10.10.0    10.10.10.255   256     0   256     0       0        0           0
     ---------------------------------------------------------------------------------------
   ```
   
   # Check the configurations of the domain **isp2**.
   
   ```
   [~HUAWEI] display domain isp2
    ------------------------------------------------------------------------------
     Domain-name                     : isp2
     Domain-state                    : Active
     Authentication-scheme-name      : default0
     Accounting-scheme-name          : default0
     Authorization-scheme-name       :
     Primary-DNS-IP-address          : -
     Second-DNS-IP-address           : -
     Primary-NBNS-IP-address         : -
     Second-NBNS-IP-address          : -
     User-group-name                 : -
     Idle-data-attribute (time,flow) : 0, 60
     Install-BOD-Count               : 0
     Report-VSM-User-Count           : 0
     Value-added-service             : default
     User-access-limit               : 279552
     Online-number                   : 0
     Web-IP-address                  : -
     Web-URL                         : -
     Portal-server-IP                : -
     Portal-URL                      : -
     Portal-force-times              : 2
     PPPoE-user-URL                  : Disable
     IPUser-ReAuth-Time(second)      : 300
     Ancp auto qos adapt             : Disable
     RADIUS-server-template          : -
     Two-acct-template               : -
     HWTACACS-server-template        : -
     Bill Flow                       : Disable
     Tunnel-acct-2867                : Disabled
   
     Flow Statistic:
     Flow-Statistic-Up               : Yes
     Flow-Statistic-Down             : Yes
     Source-IP-route                 : Disable
     IP-warning-threshold            : -
     Multicast Forwarding            : Yes
     Multicast Virtual               : No
     Max-multilist num               : 4
     Multicast-profile               : -
     IP-address-pool-name            : pool2
     Quota-out                     : Offline
     ------------------------------------------------------------------------------
   
   ```

#### Configuration Files

* Configuration files
  
  ```
  #
   sysname HUAWEI
  #
  ip pool pool2 bas remote
   gateway 10.10.10.1 255.255.255.0
   dhcp-server group group1
  #
  dhcp-server group group1
   dhcp-server 10.1.1.1
  #
  radius-server group rd                                                       
   radius-server authentication 10.7.66.66 1812 weight 0                                             
   radius-server accounting 10.7.66.66 1813 weight 0                                                        
   radius-server shared-key-cipher %^%#h{FXVBLZX9#`VI]EWUUaOSHGd5E!.1DGeVYEie=%^%                                       
   radius-server retransmit 2                                                    
  # 
  aaa
   authentication-scheme default1
   authorization-scheme default
   #
   accounting-scheme default0
   #
  domain isp2
   authentication-scheme default1
   accounting-scheme default0
   ip-pool pool2
   radius-server group rd  
   #
  interface GigabitEthernet0/1/0.1
   statistic enable
   user-vlan 1
   bas
   #
    access-type layer2-subscriber default-domain authentication isp2
    authentication-method bind
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  return
  ```