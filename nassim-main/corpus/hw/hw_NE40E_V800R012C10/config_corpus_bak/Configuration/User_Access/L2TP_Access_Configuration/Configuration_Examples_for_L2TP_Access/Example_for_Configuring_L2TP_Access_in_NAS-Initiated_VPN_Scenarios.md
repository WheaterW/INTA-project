Example for Configuring L2TP Access in NAS-Initiated VPN Scenarios
==================================================================

This section provides an example for configuring L2TP access in NAS-Initiated VPN scenarios. A networking diagram is provided to help you understand the configuration procedure. The configuration example includes the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374273__fig_dc_ne_l2tp_cfg_01350701), PC1 is connected to a PSTN through a modem and then connected to the LAC (DeviceA). The LAC and LNS reside on a WAN and communicate with each other through a tunnel. A user accesses the network with a username carrying a domain name. Both the LAC and LNS authenticate the username and password through RADIUS authentication. On the LNS, an address pool needs to be configured in the domain for address assignment to the user. The user needs to communicate with the headquarters. However, the headquarters network uses private addresses, and the user cannot directly access the internal server over the Internet. Therefore, a VPN must be established to allow user access to the internal network.

**Figure 1** Configuring L2TP access in NAS-Initiated VPN scenarios![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 in this example represents GE0/1/0.


  
![](images/fig_dc_ne_l2tp_cfg_01350701.png "Click to enlarge")  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a dial-up connection on the user side.
2. Configure the LAC.
   
   * Configure an interface address for the LAC.
   * Configure the PPPoE access service on the LAC, including configuring a VT and AAA schemes, binding an interface to the VT, and configuring a BAS interface.
   * Enable L2TP.
   * Configure an L2TP tunnel connection on the LAC.
   * Configure a tunnel authentication mode.
   * Configure L2TP attributes.
3. Configure the LNS.
   
   * Configure an interface address for the LNS.
   * Configure a VT.
   * Configure an L2TP tunnel connection on the LNS.
   * Configure a tunnel authentication mode and user authentication mode.
   * Configure LNS-side tunnel parameters.
   * Configure an address pool for address assignment to L2TP users.
   * Configure an L2TP user domain and specify an address pool in the domain.

#### Data Preparation

To complete the configuration, you need the following data:

* Identical usernames, domain names, and passwords on the LAC-side NE40E and LNS-side NE40E
* LNS-side tunnel authentication mode (CHAP is used in this example) and tunnel password; LNS-side local and remote tunnel names
* VT number
* L2TP group ID
* ID, address range, and address mask of a remote address pool

#### Procedure

1. Configure a dial-up connection on the user side.
   
   
   
   Establish a dial-up connection so that the user can receive an IP address assigned by the LNS.
   
   In the dial-up terminal window that is displayed, enter the username **vpdnuser@huawei.com** and password **YsHsjx\_202206**. (The username and password have been registered on the LNS.)
2. Configure DeviceA that functions as the LAC.
   
   
   
   In this example, the IP address of the interface (GE0/1/0) connecting the LAC to the tunnel is 10.38.160.1, and the IP address of the interface (GE0/1/0) connecting the LNS to the tunnel is 10.38.160.2.
   
   # Assign an IP address to GE0/1/0.
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] sysname DeviceA
   ```
   ```
   [*Device] commit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ip address 10.38.160.1 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Enable L2TP and configure an L2TP tunnel connection on the LAC.
   
   ```
   [~DeviceA] l2tp enable
   ```
   ```
   [*DeviceA] l2tp-group 1
   ```
   ```
   [*DeviceA-l2tp-1] tunnel name LAC
   ```
   ```
   [*DeviceA-l2tp-1] tunnel source gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-l2tp-1] commit
   ```
   ```
   [~DeviceA-l2tp-1] start l2tp ip 10.38.160.2
   ```
   ```
   [~DeviceA-l2tp-1] tunnel password cipher YsHsjx_202206
   ```
   ```
   [~DeviceA-l2tp-1] quit
   ```
   
   Configure the PPPoE access service.
   
   # Configure a RADIUS server.
   
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
   [*DeviceA-radius-radius1] radius-server shared-key YsHsjx_202206
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
   [~DeviceA-aaa] domain huawei.com
   ```
   ```
   [*DeviceA-aaa-domain-huawei.com] authentication-scheme default1 
   ```
   ```
   [*DeviceA-aaa-domain-huawei.com] accounting-scheme default1
   ```
   ```
   [*DeviceA-aaa-domain-huawei.com] idle-cut 60 500
   ```
   ```
   [*DeviceA-aaa-domain-huawei.com] radius-server group radius1
   ```
   ```
   [*DeviceA-aaa-domain-huawei.com] commit
   ```
   ```
   [~DeviceA-aaa-domain-huawei.com] l2tp-group 1
   ```
   ```
   [~DeviceA-aaa-domain-huawei.com] quit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
   # Configure a VT.
   ```
   [~DeviceA] interface virtual-template 1
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
   [~DeviceA-GigabitEthernet0/2/0.100-bas] access-type layer2-subscriber default-domain authentication huawei.com
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
3. Configure DeviceB that functions as the LNS.
   
   
   
   # Assign an IP address to the interface connecting the LNS to the tunnel.
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] sysname DeviceB
   ```
   ```
   [*Device] commit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-gigabitethernet0/1/0] ip address 10.38.160.2 255.255.255.0
   ```
   ```
   [*DeviceB-gigabitethernet0/1/0] commit
   ```
   ```
   [~DeviceB-gigabitethernet0/1/0] quit
   ```
   
   # Configure a VT and specify the tunnel authentication mode.
   
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
   
   # Enable L2TP.
   
   ```
   [~DeviceB] l2tp enable
   ```
   ```
   [*DeviceB] l2tp-group 1
   ```
   
   # Configure the local tunnel name and peer tunnel name on the LNS side.
   
   ```
   [*DeviceB-l2tp-1] tunnel name LNS
   ```
   ```
   [*DeviceB-l2tp-1] allow l2tp virtual-template 1 remote LAC
   ```
   
   # Enable tunnel authentication and configure a tunnel authentication password.
   
   ```
   [*DeviceB-l2tp-1] tunnel authentication
   ```
   ```
   [*DeviceB-l2tp-1] tunnel password cipher YsHsjx_202206
   ```
   
   # Configure the local end to perform mandatory CHAP authentication.
   
   ```
   [*DeviceB-l2tp-1] mandatory-chap
   ```
   ```
   [*DeviceB-l2tp-1] commit
   ```
   ```
   [~DeviceB-l2tp-1] quit
   ```
   # Create an LNS group named **group1**.
   ```
   [~DeviceB] lns-group group1
   ```
   
   # Bind the tunnel board in slot 1 to the LNS group.
   ```
   [*DeviceB-lns-group-group1] bind slot 1 
   ```
   
   # Specify an interface for the LNS group.
   ```
   [*DeviceB-lns-group-group1] bind source gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-lns-group-group1] commit
   ```
   ```
   [~DeviceB-lns-group-group1] quit
   ```
   
   # Configure an address pool for address assignment to dial-up users.
   ```
   [~DeviceB] ip pool 1 bas local
   ```
   ```
   [*DeviceB-ip-pool-1] gateway 192.168.0.2 255.255.255.0
   ```
   ```
   [*DeviceB-ip-pool-1] commit
   ```
   ```
   [~DeviceB-ip-pool-1] section 0 192.168.0.10 192.168.0.100
   ```
   ```
   [~DeviceB-ip-pool-1] quit
   ```
   
   # Configure a RADIUS server.
   
   ```
   [~DeviceB] radius-server group radius1
   ```
   ```
   [*DeviceB-radius-radius1] radius-server authentication 10.20.20.1 1812
   ```
   ```
   [*DeviceB-radius-radius1] radius-server accounting 10.20.20.1 1813
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
   [~DeviceB-aaa] domain huawei.com
   ```
   ```
   [*DeviceB-aaa-domain-huawei.com] authentication-scheme default1
   ```
   ```
   [*DeviceB-aaa-domain-huawei.com] accounting-scheme default1
   ```
   ```
   [*DeviceB-aaa-domain-huawei.com] radius-server group radius1
   ```
   ```
   [*DeviceB-aaa-domain-huawei.com] commit
   ```
   ```
   [~DeviceB-aaa-domain-huawei.com] ip-pool 1
   ```
   ```
   [~DeviceB-aaa-domain-huawei.com] quit
   ```
   ```
   [~DeviceB-aaa] quit
   ```
4. Verify the configuration.
   
   
   
   # After completing the configurations, have the VPN user go online. Then, run the **display l2tp tunnel** command on both the LAC and LNS to check whether an L2TP tunnel is set up successfully. The following example uses the command output on the LNS.
   
   ```
   [~DeviceB] display l2tp tunnel
   ```
   ```
    ---------------------------------------------------------                     
     -----------tunnel information in LAC----------------------                    
    Total 0,0 printed                                                              
   
     ---------------------------------------------------------                     
     -----------tunnel information in LNS----------------------                    
    The tunnel information of k board 1                                            
    LocalTID RemoteTID RemoteAddress    Port   Sessions RemoteName                 
     ---------------------------------------------------------                     
    13921   7958       10.38.160.1     57344   1          LAC                  
     ---------------------------------------------------------                     
     Total 1,1 printed from slot 1 
   ```
   
   # Run the **display l2tp session** command to check information about session establishment. The following example uses the command output on the LNS.
   
   ```
   [~DeviceB] display l2tp session lns slot 1
   ```
   ```
   LocalSID  RemoteSID  LocalTID   RemoteTID  UserID  UserName                                                                       
    ------------------------------------------------------------------------------                                                     
     2036       1469      13921      7958       62172    vpdnuser@huawei.com                       
    ------------------------------------------------------------------------------                                         
   ```
   ```
   Total 1, 1 printed from slot 1
   ```
   
   # Check that the VPN user can access the headquarters.

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
 radius-server shared-key %^%#[aPaM9I8k"Y^ukH,LmbY+807,~L0_:<bLVYGo@R;%^%
```
```
#
```
```
 radius-server authentication 10.20.20.1 1812 
```
```
 radius-server accounting 10.20.20.1 1813 
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
#
```
```
interface GigabitEthernet0/2/0.100
```
```
 statistic enable
```
```
 user-vlan 1 100
```
```
 pppoe-server bind Virtual-Template 1
```
```
 bas
```
```
 #
```
```
  access-type layer2-subscriber default-domain authentication huawei.com
```
```
authentication-method ppp
```
```
#
```
```
aaa
```
```
 domain huawei.com
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
  radius-server group radius1
```
```
  l2tp-group 1
```
```
#
```
```
interface gigabitethernet0/1/0
```
```
 undo shutdown
```
```
 ip address 10.38.160.1 255.255.255.0
```
```
#
```
```
l2tp-group 1
```
```
 tunnel password cipher %^%#%@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#%^%#
```
```
 tunnel name LAC
```
```
 start l2tp ip 10.38.160.2
```
```
 tunnel source gigabitethernet 0/1/0
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
#
```
```
 radius-server shared-key %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^% 
```
```
#
```
```
 radius-server authentication 10.20.20.1 1812 
```
```
 radius-server accounting 10.20.20.1 1813 
```
```
#
```
```
ip pool 1 bas local
```
```
 gateway 192.168.0.2 255.255.255.0
```
```
 section 0 192.168.0.10 192.168.0.100
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
interface gigabitethernet0/1/0
```
```
 undo shutdown
```
```
 ip address 10.38.160.2 255.255.255.0
```
```
#
```
```
interface LoopBack0
```
```
 ip address 192.168.10.1 255.255.255.255
```
```
#
```
```
l2tp-group 1
```
```
 mandatory-chap
```
```
 allow l2tp virtual-template 1 remote LAC
```
```
 tunnel password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#  1qaz#EDC
```
```
 tunnel name LNS
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
 bind source gigabitethernet0/1/0
```
```
#
```
```
aaa
```
```
 domain huawei.com
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
  ip-pool 1
```
```
#
```
```
return
```