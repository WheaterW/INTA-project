Example for Configuring L2TP Tunnel Switching
=============================================

This section provides an example for configuring L2TP tunnel switching. A networking diagram is provided to help you understand the configuration procedure. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374282__fig_dc_ne_l2tp_cfg_01351001), DeviceA, DeviceB, and DeviceC function as the LAC, LTS, and LNS, respectively.

* A user dials in through PPPoE using the username **user1@domain1** and password **YsHsjx\_202206**.
* DeviceA performs RADIUS authentication and accounting for the user.
* DeviceB and DeviceC do not need to perform authentication or accounting for the user.
* DeviceC uses the local address pool to assign an IP address to the user.

**Figure 1** Configuring L2TP tunnel switching![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 in this example represents GE0/1/0.1.


  
![](images/fig_dc_ne_l2tp_cfg_01351001.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a dial-up connection on the user side.
2. Configure the LAC.
3. Configure the LTS.
4. Configure the LNS.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of DeviceB's Loopback0
* IP address of DeviceC's Loopback0
* Name of a user access domain

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section provides only the L2TP-related configuration procedure.



#### Procedure

1. Perform configuration on the user side.
   
   
   
   In the PPPoE dial-up window, enter **user1@domain1** as the username and **YsHsjx\_202206** as the password for dial-up.
2. Configure DeviceA that functions as the LAC.
   
   
   
   # Configure VT1.
   
   ```
   <Device> system-view
   ```
   ```
   <~Device> sysname DeviceA
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
   
   # Bind VT1 to GE0/1/0.1 and configure user VLANs.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] pppoe-server bind virtual-template 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.1] user-vlan 1 100
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.1-vlan-1-100] quit
   ```
   
   # Configure a BAS interface.
   
   ```
   [~DeviceA-GigabitEthernet0/1/0.1] bas
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1-bas] access-type layer2-subscriber
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1-bas] authentication-method ppp
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1-bas] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.1-bas] quit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.1] bas
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1-bas] access-type layer2-subscriber
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1-bas] authentication-method ppp
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1-bas] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.1-bas] quit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.1] quit
   ```
   
   # Configure an L2TP group and specify related attributes.
   
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
   [*DeviceA] commit
   ```
   ```
   [~DeviceA-l2tp-lac1] start l2tp ip 1.1.1.1
   ```
   ```
   [*DeviceA-l2tp-lac1] tunnel authentication
   ```
   ```
   [*DeviceA-l2tp-lac1] tunnel password cipher YsHsjx_202206
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
   [*DeviceA-radius-radius1] radius-server authentication 10.0.0.249 1812
   ```
   ```
   [*DeviceA-radius-radius1] radius-server accounting 10.0.0.249 1813
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
   [~DeviceA-aaa] domain domain1
   ```
   ```
   [*DeviceA-aaa-domain-domain1] l2tp-group lac1
   ```
   ```
   [*DeviceA-aaa-domain-domain1] radius-server group radius1
   ```
   ```
   [*DeviceA-aaa-domain-domain1] authentication-scheme default1
   ```
   ```
   [*DeviceA-aaa-domain-domain1] accounting-scheme default1
   ```
   ```
   [*DeviceA-aaa-domain-domain1] idle-cut 60 500
   ```
   ```
   [*DeviceA-aaa-domain-domain1] commit
   ```
   ```
   [~DeviceA-aaa-domain-domain1] quit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The username **user1@domain1** and password **YsHsjx\_202206** must be configured on the RADIUS server.
3. Configure DeviceB that functions as the LTS.
   
   
   
   # Create VT1 and configure related information.
   
   ```
   <Device> system-view
   ```
   ```
   <~Device> sysname DeviceB
   ```
   ```
   [*DeviceB] interface virtual-template 1
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
   
   # Create loopback0.
   
   ```
   [~DeviceB] interface loopback 0
   ```
   ```
   [*DeviceB-LoopBack0] ip address 1.1.1.1 255.255.255.255
   ```
   ```
   [*DeviceB-LoopBack0] commit
   ```
   ```
   [~DeviceB-LoopBack0] quit
   ```
   
   # Enable the L2TP service and configure an L2TP group to function as the LNS.
   
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
   
   # Create and configure the LNS group named **group1**, and bind the tunnel source interface and tunnel board to the LNS group.
   
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
   
   # Configure an L2TP group to function as the LAC.
   
   ```
   [~DeviceB] l2tp-group lac1
   ```
   ```
   [*DeviceB-l2tp-lac1] tunnel name lac2
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceB-l2tp-lac1] start l2tp ip 2.2.2.2
   ```
   ```
   [*DeviceB-l2tp-lac1] tunnel authentication
   ```
   ```
   [*DeviceB-l2tp-lac1] tunnel password cipher YsHsjx_202206
   ```
   ```
   [*DeviceB-l2tp-lac1] commit
   ```
   ```
   [~DeviceB-l2tp-lac1] quit
   ```
   
   # Configure a RADIUS server group.
   
   ```
   [~DeviceB] radius-server group radius1
   ```
   ```
   [*DeviceB-radius-radius1] radius-server authentication 10.0.0.249 1812
   ```
   ```
   [*DeviceB-radius-radius1] radius-server accounting 10.0.0.249 1813
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
   [*DeviceB-aaa] domain domain1
   ```
   ```
   [*DeviceB-aaa-domain-domain1] l2tp-group lac1
   ```
   ```
   [*DeviceB-aaa-domain-domain1] radius-server group radius1
   ```
   ```
   [*DeviceB-aaa-domain-domain1] authentication-scheme default1
   ```
   ```
   [*DeviceB-aaa-domain-domain1] accounting-scheme default1
   ```
   ```
   [*DeviceB-aaa-domain-domain1] idle-cut 60 500
   ```
   ```
   [*DeviceB-aaa-domain-domain1] commit
   ```
   ```
   [~DeviceB-aaa-domain-domain1] quit
   ```
   ```
   [~DeviceB-aaa] quit
   ```
4. Configure DeviceC that functions as the LNS.
   
   
   
   # Create VT1.
   
   ```
   <Device> system-view
   ```
   ```
   <~Device> sysname DeviceC
   ```
   ```
   [*DeviceC] interface virtual-template 1
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
   
   # Create loopback0.
   
   ```
   [~DeviceC] interface loopback 0
   ```
   ```
   [*DeviceC-LoopBack0] ip address 2.2.2.2 255.255.255.255
   ```
   ```
   [*DeviceC-LoopBack0] commit
   ```
   ```
   [~DeviceC-LoopBack0] quit
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
   [*DeviceC-l2tp-lns1] tunnel name LNS2
   ```
   ```
   [*DeviceC-l2tp-lns1] allow l2tp virtual-template 1 remote lac2
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
   [*DeviceC-lns-group-group1] bind source loopback 0
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
   [*DeviceC-ip-pool-pool1] gateway 10.10.0.1 255.255.255.0
   ```
   ```
   [*DeviceC-ip-pool-pool1] commit
   ```
   ```
   [~DeviceC-ip-pool-pool1] section 0 10.10.0.2 10.10.0.100
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
   [*DeviceC-radius-radius1] radius-server authentication 10.0.0.249 1812
   ```
   ```
   [*DeviceC-radius-radius1] radius-server accounting 10.0.0.249 1813
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
   [*DeviceC-aaa] domain domain1
   ```
   ```
   [*DeviceC-aaa-domain-domain1] radius-server group radius1
   ```
   ```
   [*DeviceC-aaa-domain-domain1] authentication-scheme default1
   ```
   ```
   [*DeviceC-aaa-domain-domain1] accounting-scheme default1
   ```
   ```
   [*DeviceC-aaa-domain-domain1] ip-pool pool1
   ```
   ```
   [*DeviceC-aaa-domain-domain1] commit
   ```
   ```
   [~DeviceC-aaa-domain-domain1] quit
   ```
   ```
   [~DeviceC-aaa] quit
   ```
   
   # Verify the configuration.
   
   Check the status of the tunnel established for user login.
   
   ```
   <Device> display l2tp tunnel
   ```
   ```
     ---------------------------------------------------------
     -----------tunnel information in LAC----------------------
    Total 0,0 printed
   
     ---------------------------------------------------------
     -----------tunnel information in LNS----------------------
    The tunnel information of k board 1 
    LocalTID RemoteTID RemoteAddress    Port   Sessions RemoteName
    ------------------------------------------------------------------------------
    39       4         1.1.1.1    1701   1        user1@domain1
    ------------------------------------------------------------------------------
     Total 1, 1 printed from slot 1 
   
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
   radius-server authentication 10.0.0.249 1812 
  ```
  ```
   radius-server accounting 10.0.0.249 1813 
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0.1
  ```
  ```
   pppoe-server bind Virtual-Template 1
  ```
  ```
   undo shutdown
  ```
  ```
   user-vlan 1 100
  ```
  ```
   bas
  ```
  ```
    access-type layer2-subscriber
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
  undo shutdown
  ```
  ```
   ip address 10.100.100.1 255.255.255.0
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
   start l2tp ip 1.1.1.1
  ```
  ```
  #
  ```
  ```
  aaa
  ```
  ```
  domain  domain1
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
    l2tp-group  lac1
  ```
  ```
  #
  ```
  ```
   ip route-static 1.1.1.1 255.255.255.255 10.100.100.2
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
  ```
  ```
   radius-server authentication 10.0.0.249 1812 
  ```
  ```
   radius-server accounting 10.0.0.249 1813 
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
   undo shutdown
  ```
  ```
   ip address 10.100.100.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.200.200.1 255.255.255.0
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
   tunnel name lac2
  ```
  ```
   start l2tp ip 2.2.2.2
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
  aaa
  ```
  ```
  domain  domain1
  ```
  ```
   radius-server group radius1
  ```
  ```
   authentication-scheme default1
  ```
  ```
   accounting-scheme default1
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
   ip route-static 2.2.2.2 255.255.255.255 10.200.200.2
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
  ```
  ```
   radius-server authentication 10.0.0.249 1812 
  ```
  ```
   radius-server accounting 10.0.0.249 1813 
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
   undo shutdown
  ```
  ```
   ip address 10.200.200.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 2.2.2.2 255.255.255.255
  ```
  ```
  #
  ```
  ```
  l2tp-group lns1
  ```
  ```
   allow l2tp virtual-template 1 remote lac2
  ```
  ```
   tunnel password cipher %@%##!!!!!!!!!"!!!!#!!!!(!!!!JMi;5#;qTW7C9);16~.M{sv*SzKjgN>0b[,G:tb%!!!!!!!!!!1!!!!E'QA>XV7kJ+tIm3UL=c=%@%#
  ```
  ```
   tunnel name lns2
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
  domain  domain1
  ```
  ```
    radius-server group radius1
  ```
  ```
    authentication-scheme default1
  ```
  ```
    accounting-scheme default1
  ```
  ```
    ip-pool pool1
  ```
  ```
  #
  ```
  ```
   ip route-static 1.1.1.1 255.255.255.255 10.200.200.1
  ```
  ```
  #
  ```
  ```
  return
  ```