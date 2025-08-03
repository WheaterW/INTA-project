Example for Configuring L2TP Tunnel Load Balancing
==================================================

This section provides an example for configuring L2TP tunnel load balancing. A networking diagram is provided to help you understand the configuration procedure. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374291__fig_dc_ne_l2tp_cfg_01351301), a single LNS cannot carry all L2TP services due to performance issues. As such, LNS load balancing can be enabled to assign services to multiple LNSs based on weights.

**Figure 1** Configuring L2TP tunnel load balancing  
![](images/fig_dc_ne_l2tp_cfg_01351301.png "Click to enlarge")  


#### Configuration Roadmap

When configuring an L2TP connection on the LAC side, configure two LNSs in an L2TP group and specify the IP addresses and weights of the LNSs.

1. Configure a dial-up connection on the user side.
2. Configure the LAC. (When configuring an L2TP connection on the LAC side, configure two LNS addresses for weight-based load balancing.)
3. Configure the LNS.

#### Data Preparation

To complete the configuration, you need the following data:

* Username and password of PC1
* Tunnel password, and the local tunnel name and remote tunnel name on the LNS
* Numbers of the VT and L2TP group
* Number, range, and mask of the remote address pool

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section provides only the L2TP-related configuration procedure.



#### Procedure

1. Configure a dial-up connection on the user side.
   
   
   
   Create a dial-up connection, with the access number of DeviceA specified to receive addresses assigned by the LNS.
   
   For PC1, enter the username **user1@isp1** and password (which have been registered on the LNS) in the dial-up terminal window that is displayed.
2. Configure DeviceA that functions as the LAC.
   
   
   
   # Configure VT1.
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] sysname DeviceA
   ```
   ```
   [*DeviceA] interface virtual-template 1
   ```
   ```
   [*DeviceA-Virtual-Template1] ppp authentication-mode chap
   ```
   ```
   [*DeviceA-Virtual-Template1] commit
   ```
   ```
   [~DeviceA-Virtual-Template1] quit
   ```
   
   # Bind VT1 to GE0/2/0.100.
   
   ```
   [~DeviceA] interface gigabitethernet 0/2/0.100
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.100] pppoe-server bind virtual-template 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.100] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0.100] user-vlan 1 100
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0.100-vlan-1-100] quit
   ```
   
   # Configure a BAS interface.
   
   ```
   [~DeviceA-GigabitEthernet0/2/0.100] bas
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.100-bas] access-type layer2-subscriber
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.100-bas] authentication-method ppp
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.100-bas] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0.100-bas] quit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0.100] quit
   ```
   
   # Create a loopback interface.
   
   ```
   [~DeviceA] interface loopback0
   ```
   ```
   [*DeviceA-LoopBack0] ip address 1.1.1.1 255.255.255.255
   ```
   ```
   [*DeviceA-LoopBack0] commit
   ```
   ```
   [~DeviceA-LoopBack0] quit
   ```
   
   # Assign IP addresses to physical interfaces on the tunnel.
   
   ```
   [~DeviceA] interface gigabitethernet0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ip address 11.11.11.1 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] ip address 12.12.12.1 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] quit
   ```
   
   # Create an L2TP group and configure attributes for tunnel load balancing.
   
   ```
   [~DeviceA] l2tp enable
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] l2tp-group lac1
   ```
   ```
   [*DeviceA-l2tp-lac1] tunnel name lac1
   ```
   ```
   [*DeviceA-l2tp-lac1] start l2tp ip 3.3.3.3 
   ```
   ```
   [*DeviceA-l2tp-lac1] start l2tp ip 4.4.4.4
   ```
   ```
   [*DeviceA-l2tp-lac1] tunnel load-sharing
   ```
   ```
   [*DeviceA-l2tp-lac1] tunnel authentication
   ```
   ```
   [*DeviceA-l2tp-lac1] tunnel password cipher YsHsjx_202206
   ```
   ```
   [*DeviceA-l2tp-lac1] tunnel source loopback0
   ```
   ```
   [*DeviceA-l2tp-lac1] commit
   ```
   ```
   [~DeviceA-l2tp-lac1] quit
   ```
   
   # Configure a RADIUS server group.
   
   ```
   [~DeviceA] radius-server group radius1
   ```
   ```
   [*DeviceA-radius-radius1] radius-server authentication 10.20.20.1 1812
   ```
   ```
   [*DeviceA-radius-radius1] radius-server accounting 10.20.20.1 1813
   ```
   ```
   [*DeviceA-radius-radius1] radius-server shared-key itellin
   ```
   ```
   [*DeviceA-radius-radius1] commit
   ```
   ```
   [~DeviceA-radius-radius1] quit
   ```
   
   # Configure a user access domain.
   
   ```
   [~DeviceA] aaa
   ```
   ```
   [~DeviceA-aaa] domain isp1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] l2tp-group lac1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] radius-server group radius1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] authentication-scheme default1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] accounting-scheme default1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] idle-cut 60 500
   ```
   ```
   [*DeviceA-aaa-domain-isp1] commit
   ```
   ```
   [~DeviceA-aaa-domain-isp1] quit
   ```
   
   # Configure routes.
   
   ```
   [~DeviceA] ip route-static 3.3.3.3 255.255.255.255 11.11.11.2
   ```
   ```
   [*DeviceA] ip route-static 4.4.4.4 255.255.255.255 12.12.12.2
   ```
   ```
   [*DeviceA] commit
   ```
3. Configure DeviceB that functions as the LNS.
   
   
   
   # Create a loopback interface.
   
   ```
   [~DeviceB] interface loopback0
   ```
   ```
   [*DeviceB-LoopBack0] ip address 3.3.3.3 255.255.255.255
   ```
   ```
   [*DeviceB-LoopBack0] commit
   ```
   ```
   [~DeviceB-LoopBack0] quit 
   ```
   
   # Assign IP addresses to physical interfaces on the tunnel.
   
   ```
   [~DeviceB] interface gigabitethernet0/1/1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] ip address 11.11.11.2 255.255.255.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] quit
   ```
   
   # Create VT1.
   
   ```
   [~DeviceB] interface virtual-template 1
   ```
   ```
   [*DeviceB-Virtual-Template1] ppp authentication-mode chap
   ```
   ```
   [*DeviceB-Virtual-Template1] commit
   ```
   ```
   [~DeviceB-Virtual-Template1] quit
   ```
   
   # Enable the L2TP service and configure an L2TP group.
   
   ```
   [~DeviceB] l2tp enable
   ```
   ```
   [*DeviceB] commit
   ```
   ```
   [~DeviceB] l2tp-group lns1
   ```
   ```
   [*DeviceB-l2tp-lns1] tunnel name lns1
   ```
   ```
   [*DeviceB-l2tp-lns1] allow l2tp virtual-template 1 remote lac1
   ```
   ```
   [*DeviceB-l2tp-lns1] tunnel authentication
   ```
   ```
   [*DeviceB-l2tp-lns1] tunnel password cipher YsHsjx_202206
   ```
   ```
   [*DeviceB-l2tp-lns1] commit
   ```
   ```
   [~DeviceB-l2tp-lns1] quit
   ```
   
   # Create and configure an LNS group named **group1**.
   
   ```
   [~DeviceB] lns-group group1
   ```
   ```
   [*DeviceB-lns-group-group1] bind slot 1
   ```
   ```
   [*DeviceB-lns-group-group1] bind source loopback 0
   ```
   ```
   [*DeviceB-lns-group-group1] commit
   ```
   ```
   [~DeviceB-lns-group-group1] quit
   ```
   
   # Configure an address pool from which addresses are assigned to users.
   
   ```
   [~DeviceB] ip pool pool1 bas local
   ```
   ```
   [*DeviceB-ip-pool-pool1] gateway 10.10.0.1 255.255.255.0
   ```
   ```
   [*DeviceB-ip-pool-pool1] section 0 10.10.0.2 10.10.0.100
   ```
   ```
   [*DeviceB-ip-pool-pool1] commit
   ```
   ```
   [~DeviceB-ip-pool-pool1] quit
   ```
   
   # Configure a RADIUS server group.
   
   ```
   [~DeviceB] radius-server group radius1
   ```
   ```
   [*DeviceB-radius-radius1] radius-server authentication 10.10.0.249 1812
   ```
   ```
   [*DeviceB-radius-radius1] radius-server accounting 10.10.0.249 1813
   ```
   ```
   [*DeviceB-radius-radius1] radius-server shared-key itellin
   ```
   ```
   [*DeviceB-radius-radius1] commit
   ```
   ```
   [~DeviceB-radius-radius1] quit
   ```
   
   # Configure a user access domain.
   
   ```
   [~DeviceB] aaa
   ```
   ```
   [*DeviceB-aaa] domain isp1
   ```
   ```
   [*DeviceB-aaa-domain-isp1] authentication-scheme default1
   ```
   ```
   [*DeviceB-aaa-domain-isp1] accounting-scheme default1
   ```
   ```
   [*DeviceB-aaa-domain-isp1] radius-server group radius1
   ```
   ```
   [*DeviceB-aaa-domain-isp1] ip-pool pool1
   ```
   ```
   [*DeviceB-aaa-domain-isp1] commit
   ```
   ```
   [~DeviceB-aaa-domain-isp1] quit
   ```
   ```
   [~DeviceB-aaa] quit
   ```
   
   # Configure a route.
   
   ```
   [~DeviceB] ip route-static 1.1.1.1 255.255.255.255 11.11.11.1
   ```
4. Configure DeviceC that functions as the LNS.
   
   
   
   # Create a loopback interface.
   
   ```
   [~DeviceC] interface loopback1
   ```
   ```
   [*DeviceC-LoopBack1] ip address 4.4.4.4 255.255.255.255
   ```
   ```
   [*DeviceC-LoopBack1] commit
   ```
   ```
   [~DeviceC-LoopBack1] quit
   ```
   
   # Assign IP addresses to physical interfaces on the tunnel.
   
   ```
   [~DeviceC] interface gigabitethernet0/1/1
   ```
   ```
   [*DeviceC--GigabitEthernet0/1/1] ip address 12.12.12.2 255.255.255.0
   ```
   ```
   [*DeviceC--GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceC--GigabitEthernet0/1/1] quit
   ```
   
   # Create VT1.
   
   ```
   [~DeviceC] interface virtual-template 1
   ```
   ```
   [*DeviceC-Virtual-Template1] ppp authentication-mode chap
   ```
   ```
   [*DeviceC-Virtual-Template1] commit
   ```
   ```
   [~DeviceC-Virtual-Template1] quit
   ```
   
   # Enable the L2TP service and configure an L2TP group.
   
   ```
   [~DeviceC] l2tp enable
   ```
   ```
   [*DeviceC] commit
   ```
   ```
   [~DeviceC] l2tp-group lns1
   ```
   ```
   [*DeviceC-l2tp-lns1] tunnel name lns1
   ```
   ```
   [*DeviceC-l2tp-lns1] allow l2tp virtual-template 1 remote lac1
   ```
   ```
   [*DeviceC-l2tp-lns1] tunnel authentication
   ```
   ```
   [*DeviceC-l2tp-lns1] tunnel password cipher YsHsjx_202206
   ```
   ```
   [*DeviceC-l2tp-lns1] commit
   ```
   ```
   [~DeviceC-l2tp-lns1] quit
   ```
   
   # Create and configure an LNS group named **group1**.
   
   ```
   [~DeviceC] lns-group group1
   ```
   ```
   [*DeviceC-lns-group-group1] bind slot 1 
   ```
   ```
   [*DeviceC-lns-group-group1] bind source loopback 1
   ```
   ```
   [*DeviceC-lns-group-group1] commit
   ```
   ```
   [~DeviceC-lns-group-group1] quit
   ```
   
   # Configure an address pool from which addresses are assigned to users.
   
   ```
   [~DeviceC] ip pool pool1 bas local
   ```
   ```
   [*DeviceC-ip-pool-pool1] gateway 10.10.0.101 255.255.255.0
   ```
   ```
   [*DeviceC-ip-pool-pool1] section 0 10.10.0.102 10.10.0.200
   ```
   ```
   [*DeviceC-ip-pool-pool1] commit
   ```
   ```
   [~DeviceC-ip-pool-pool1] quit
   ```
   
   # Configure a RADIUS server group.
   
   ```
   [~DeviceC] radius-server group radius1
   ```
   ```
   [*DeviceC-radius-radius1] radius-server authentication 10.10.0.249 1812
   ```
   ```
   [*DeviceC-radius-radius1] radius-server accounting 10.10.0.249 1813
   ```
   ```
   [*DeviceC-radius-radius1] radius-server shared-key itellin
   ```
   ```
   [*DeviceC-radius-radius1] commit
   ```
   ```
   [~DeviceC-radius-radius1] quit
   ```
   
   # Configure a user access domain.
   
   ```
   [~DeviceC] aaa
   ```
   ```
   [*DeviceC-aaa] domain isp1
   ```
   ```
   [*DeviceC-aaa-domain-isp1] authentication-scheme default1
   ```
   ```
   [*DeviceC-aaa-domain-isp1] accounting-scheme default1
   ```
   ```
   [*DeviceC-aaa-domain-isp1] radius-server group radius1
   ```
   ```
   [*DeviceC-aaa-domain-isp1] ip-pool pool1
   ```
   ```
   [*DeviceC-aaa-domain-isp1] commit
   ```
   ```
   [~DeviceC-aaa-domain-isp1] quit
   ```
   ```
   [~DeviceC-aaa] quit
   ```
   
   # Configure a route.
   
   ```
   [~DeviceC] ip route-static 1.1.1.1 255.255.255.255 12.12.12.1
   ```
5. Verify the configuration.
   
   
   ```
   [~DeviceA] test l2tp-tunnel l2tp-group lac1 ip-address 3.3.3.3
   ```
   ```
   Testing L2TP tunnel connectivity now....... 
   ```
   ```
   Test L2TP tunnel connectivity success.
   ```
   ```
   [~DeviceA] test l2tp-tunnel l2tp-group lac1 ip-address 4.4.4.4
   ```
   ```
   Testing L2TP tunnel connectivity now....... 
   ```
   ```
   Test L2TP tunnel connectivity success.
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceA
  ```
  ```
  #
  ```
  ```
   l2tp enable
  ```
  ```
  #
  ```
  ```
  radius-server group radius1
  ```
  ```
   radius-server authentication 10.20.20.1 1812 
  ```
  ```
   radius-server accounting 10.20.20.1 1813 
  ```
  ```
   radius-server shared-key %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^% 
  ```
  ```
  #
  ```
  ```
  interface Virtual-Template1
  ```
  ```
  ppp authentication-mode chap
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   pppoe-server bind Virtual-Template 1
  ```
  ```
   user-vlan 1 100
  ```
  ```
   undo shutdown
  ```
  ```
   bas
  ```
  ```
    access-type layer2-subscriber
  ```
  ```
    authentication-method ppp
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 1.1.1.1 255.255.255.255
  ```
  ```
  #
  ```
  ```
  l2tp-group lac1
  ```
  ```
   tunnel password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
  ```
  ```
   tunnel name lac1
  ```
  ```
   start l2tp ip 3.3.3.3 
  ```
  ```
   start l2tp ip 4.4.4.4
  ```
  ```
   tunnel load-sharing
  ```
  ```
   tunnel source LoopBack0
  ```
  ```
  #
  ```
  ```
  aaa
  ```
  ```
  domain isp1
  ```
  ```
    authentication-scheme default1
  ```
  ```
    accounting-scheme default1
  ```
  ```
    radius-server group radius1
  ```
  ```
    idle-cut 60 500
  ```
  ```
    l2tp-group lac1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 11.11.11.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 12.12.12.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
   ip route-static 3.3.3.3 255.255.255.255 11.11.11.2
  ```
  ```
   ip route-static 4.4.4.4 255.255.255.255 12.12.12.2
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceB
  ```
  ```
  #
  ```
  ```
   l2tp enable
  ```
  ```
  #
  ```
  ```
  radius-server group radius1
   radius-server authentication 10.10.0.249 1812
   radius-server accounting 10.10.0.249 1813
   radius-server shared-key %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^% 
  #
  ```
  ```
  interface Virtual-Template1
  ```
  ```
  ppp authentication-mode chap
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 3.3.3.3 255.255.255.255
  ```
  ```
  #
  ```
  ```
  l2tp-group lns1
  ```
  ```
   allow l2tp virtual-template 1 remote lac1
  ```
  ```
   tunnel password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
  ```
  ```
   tunnel name lns1
  ```
  ```
  #
  ```
  ```
  lns-group group1
  ```
  ```
   bind slot 1 
  ```
  ```
   bind source LoopBack0
  ```
  ```
  #
  ```
  ```
  ip pool pool1 bas local
  ```
  ```
   gateway 10.10.0.1 255.255.255.0
  ```
  ```
   section 0 10.10.0.2 10.10.0.100
  ```
  ```
  #
  ```
  ```
  aaa
  ```
  ```
   domain isp1
  ```
  ```
    authentication-scheme default1
  ```
  ```
    accounting-scheme default1
  ```
  ```
    radius-server group radius1
  ```
  ```
    ip-pool pool1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 11.11.11.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
   ip route-static 1.1.1.1 255.255.255.255 11.11.11.1
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceC configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceC
  ```
  ```
  #
  ```
  ```
   l2tp enable
  ```
  ```
  #
  ```
  ```
  radius-server group radius1
   radius-server authentication 10.10.0.249 1812
   radius-server accounting 10.10.0.249 1813
   radius-server shared-key %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^% 
  #
  ```
  ```
  interface Virtual-Template1
  ```
  ```
  ppp authentication-mode chap
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 4.4.4.4 255.255.255.255
  ```
  ```
  #
  ```
  ```
  l2tp-group lns1
  ```
  ```
   allow l2tp virtual-template 1 remote lac1
  ```
  ```
   tunnel password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
  ```
  ```
   tunnel name lns1
  ```
  ```
  #
  ```
  ```
  lns-group group1
  ```
  ```
   bind slot 1 
  ```
  ```
   bind source LoopBack1
  ```
  ```
  #
  ```
  ```
  ip pool pool1 bas local
  ```
  ```
   gateway 10.10.0.101 255.255.255.0
  ```
  ```
   section 0 10.10.0.102 10.10.0.200
  ```
  ```
  #
  ```
  ```
  aaa
  ```
  ```
  domain  isp1
  ```
  ```
    authentication-scheme default1
  ```
  ```
    accounting-scheme default1
  ```
  ```
    radius-server group radius1
  ```
  ```
    ip-pool pool1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 12.12.12.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
   ip route-static  1.1.1.1 255.255.255.255 12.12.12.1
  ```
  ```
  #
  ```
  ```
  return
  ```