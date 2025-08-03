Example for Configuring User Access in L2TP over GRE Scenarios
==============================================================

This section provides an example for configuring user access in L2TP over GRE scenarios. A networking diagram is provided to help you understand the configuration procedure. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374300__fig_dc_ne_l2tp_cfg_01441501), PC1 is connected to a PSTN through a modem and then connected to the LAC (DeviceA). The LAC and LNS reside on a WAN and communicate with each other through an L2TP tunnel which runs over a GRE tunnel.

**Figure 1** Configuring user access in L2TP over GRE scenarios  
![](images/fig_dc_ne_l2tp_cfg_01441501.png "Click to enlarge")  


#### Configuration Roadmap

The headquarters network uses private addresses, and users cannot directly access the internal server over the Internet. Therefore, a VPN must be established to allow user access to the internal network. The configuration roadmap is as follows:

1. Configure a dial-up connection on the user side.
2. Configure the LAC.
   
   * Configure an interface address for the LAC.
   * Configure the PPPoE access service, including configuring a VT and AAA schemes, binding the VT to a sub-interface, and configuring a BAS interface.
   * Enable L2TP.
   * Configure an L2TP tunnel connection.
   * Configure a tunnel authentication mode.
   * Configure L2TP attributes.
   * Configure OSPF.
   * Configure loopback interfaces.
   * Configure a GRE tunnel interface.
3. Configure the LNS.
   
   * Configure an interface address for the LNS.
   * Configure a VT.
   * Configure an L2TP tunnel connection on the LNS.
   * Configure a tunnel authentication mode and user authentication mode.
   * Configure LNS-side tunnel parameters.
   * Configure an address pool for IP address assignment to L2TP users.
   * Configure an L2TP user domain and specify address pools in the domain.
   * Configure OSPF.
   * Configure loopback interfaces.
   * Configure a GRE tunnel interface.

#### Data Preparation

To complete the configuration, you need the following data:

* Identical domain names, usernames, and passwords on the LAC and LNS
* Protocol, tunnel authentication mode (CHAP is used in this example), and tunnel password used by the LNS; local name and remote name of the LNS
* VT number
* L2TP group ID
* IDs, address ranges, and address masks of remote address pools
* Loopback addresses
* Users authentication mode (local authentication)

#### Procedure

1. Perform configuration on the user side.
   
   
   
   # Establish a dial-up connection for the user to receive an IP address assigned by the LNS. In the dial-up terminal window that is displayed, enter the username **vpdnuser@huawei.com** and password **YsHsjx\_202206**. (The username and password have been registered on the LNS.)
2. Configure DeviceA that functions as the LAC.
   
   
   
   # Assign an IP address to GE 0/1/0.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In this example, the IP addresses of interface 1 (GE 0/1/0) on the LAC and interface 2 (GE 0/1/0) on the LNS are 10.38.160.1 and 10.38.160.2, respectively.
   
   ```
   <Device> system-view
   ```
   ```
   [Device] sysname DeviceA
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-Gigabitethernet0/1/0] ip address 10.38.160.1 255.255.255.0
   ```
   ```
   [*DeviceA-Gigabitethernet0/1/0] ospf enable 4 area 0.0.0.1
   ```
   ```
   [*DeviceA-Gigabitethernet0/1/0] commit
   ```
   ```
   [~DeviceA-Gigabitethernet0/1/0] quit
   ```
   
   # Configure OSPF.
   
   ```
   [~DeviceA] ospf 4
   ```
   ```
   [*DeviceA-ospf-4] area 0.0.0.1
   ```
   ```
   [*DeviceA-ospf-4-area-0.0.0.1] commit
   ```
   ```
   [~DeviceA-ospf-4-area-0.0.0.1] quit
   ```
   
   # Configure loopback1 and bind it to a GRE tunnel interface.
   
   ```
   [~DeviceA] interface LoopBack1
   ```
   ```
   [~DeviceA-LoopBack1] ip address 10.1.2.1 255.255.255.255
   ```
   ```
   [~DeviceA-LoopBack1] ospf enable 4 area 0.0.0.1
   ```
   ```
   [~DeviceA-LoopBack1] binding tunnel gre
   ```
   
   # Configure loopback2.
   
   ```
   [~DeviceA] interface LoopBack2
   ```
   ```
   [~DeviceA-LoopBack2] ip address 10.1.1.1 255.255.255.255
   ```
   
   # Configure a GRE tunnel interface.
   
   ```
   [*DeviceA] interface Tunnel1
   ```
   ```
   [*DeviceA-Tunnel] ip address 10.1.1.2 255.255.255.255
   ```
   ```
   [*DeviceA-Tunnel] tunnel-protocol gre
   ```
   ```
   [*DeviceA-Tunnel] source LoopBack1
   ```
   ```
   [*DeviceA-Tunnel] destination 10.10.10.10
   ```
   ```
   [*DeviceA-Tunnel] commit
   ```
   ```
   [~DeviceA-Tunnel] quit
   ```
   # Configure a static route.
   ```
   [~DeviceA] ip route-static 10.5.1.1 255.255.255.255 Tunnel1
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
   [*DeviceA-l2tp-1] tunnel source LoopBack1
   ```
   ```
   [*DeviceA-l2tp-1] tunnel authentication
   ```
   ```
   [~DeviceA-l2tp-1] commit
   ```
   
   # Configure a tunnel authentication mode.
   
   ```
   [~DeviceA-l2tp-1] start l2tp ip 10.5.1.1
   ```
   ```
   [~DeviceA-l2tp-1] tunnel password cipher YsHsjx_202206
   ```
   ```
   [~DeviceA-l2tp-1] quit
   ```
   
   # Configure a user access domain.
   
   ```
   [~DeviceA] aaa
   ```
   ```
   [~DeviceA-aaa] authentication-scheme auth1
   ```
   ```
   [*DeviceA-aaa-authen-auth1] authentication-mode local
   ```
   ```
   [*DeviceA-aaa-authen-auth1] commit
   ```
   ```
   [~DeviceA-aaa-authen-auth1] quit
   ```
   ```
   [~DeviceA-aaa] accounting-scheme default0
   ```
   ```
   [*DeviceA-aaa-accounting-default0] accounting-mode none
   ```
   ```
   [*DeviceA-aaa-accounting-default0] commit
   ```
   ```
   [~DeviceA-aaa-accounting-default0] quit
   ```
   ```
   [~DeviceA-aaa] domain huawei.com
   ```
   ```
   [*DeviceA-aaa-domain-huawei.com] authentication-scheme auth1 
   ```
   ```
   [*DeviceA-aaa-domain-huawei.com] accounting-scheme default0
   ```
   ```
   [*DeviceA-aaa-domain-huawei.com] commit
   ```
   ```
   [*DeviceA-aaa-domain-huawei.com] idle-cut 60 500
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
   
   
   
   # Set a username and password, which must be the same as those on the LNS.
   
   ```
   [~DeviceA] local-aaa-server
   ```
   ```
   [~DeviceA-local-aaa-server] user vpdnuser@huawei.com password cipher YsHsjx_202206 authentication-type p
   ```
   
   # Configure the PPPoE access service.
   
   1. Configure a VT.
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
   2. Bind VT1 to GE0/2/0.100.
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
   3. Configure a BAS interface.
      ```
      [~DeviceA-GigabitEthernet0/2/0.100] bas
      ```
      ```
      [*DeviceA-GigabitEthernet0/2/0.100-bas] access-type layer2-subscriber default-domain authentication huawei.com
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
   [*DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-Gigabitethernet0/1/0] ip address 10.38.160.2 255.255.255.0
   ```
   ```
   [*DeviceB-Gigabitethernet0/1/0] ospf enable 4 area 0.0.0.1
   ```
   ```
   [*DeviceB-Gigabitethernet0/1/0] ipv6 enable
   ```
   ```
   [~DeviceB-Gigabitethernet0/1/0] ipv6 address auto link-local
   ```
   ```
   [*DeviceB-Gigabitethernet0/1/0] commit
   ```
   ```
   [~DeviceB-Gigabitethernet0/1/0] quit
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
   
   # Set the LNS-side and LAC-side tunnel names.
   
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
   
   # Configure the LNS to perform mandatory CHAP authentication.
   
   ```
   [*DeviceB-l2tp-1] mandatory-chap
   ```
   ```
   [*DeviceB-l2tp-1] commit
   ```
   ```
   [~DeviceB-l2tp-1] quit
   ```
   
   # Configure OSPF.
   
   ```
   [~DeviceB] ospf 4
   ```
   ```
   [~DeviceB-ospf-4] default-route-advertise
   ```
   ```
   [~DeviceB-ospf-4] area 0.0.0.1
   ```
   ```
   [*DeviceB-ospf-4-area-0.0.0.1] commit
   ```
   ```
   [~DeviceB-ospf-4-area-0.0.0.1] quit
   ```
   
   # Configure loopback1 and loopback2, and bind loopback1 to a GRE tunnel interface.
   
   ```
   [~DeviceB] interface LoopBack1
   ```
   ```
   [*DeviceB-LoopBack1] ip address 10.10.10.10 255.255.255.255
   ```
   ```
   [*DeviceB-LoopBack1] ospf enable 4 area 0.0.0.1
   ```
   ```
   [*DeviceB-LoopBack1] binding tunnel gre
   ```
   ```
   [*DeviceB-LoopBack1] quit
   ```
   ```
   [*DeviceB] interface LoopBack2
   ```
   ```
   [*DeviceB-LoopBack2] ip address 10.5.1.1 255.255.255.255
   ```
   ```
   [*DeviceB-LoopBack2] quit
   ```
   ```
   [*DeviceB] interface Tunnel1
   ```
   ```
   [*DeviceB-Tunnel] ip address 192.168.1.1 255.255.255.255
   ```
   ```
   [*DeviceB-Tunnel] tunnel-protocol gre
   ```
   ```
   [*DeviceB-Tunnel] source LoopBack1
   ```
   ```
   [*DeviceB-Tunnel] destination 10.1.2.1
   ```
   ```
   [*DeviceB-Tunnel] commit
   ```
   ```
   [~DeviceB-Tunnel] quit
   ```
   
   # Configure a static route.
   
   ```
   [~DeviceB] ip route-static 10.1.1.1 255.255.255.255 Tunnel1
   ```
   
   # Create an LNS group named **group1**.
   
   ```
   [~DeviceB] lns-group group1
   ```
   ```
   [*DeviceB-lns-group-group1] bind slot 1
   ```
   ```
   [*DeviceB-lns-group-group1] bind source Loopback2
   ```
   ```
   [*DeviceB-lns-group-group1] commit
   ```
   ```
   [~DeviceB-lns-group-group1] quit
   ```
   
   # Set a username and password, which must be the same as those on the LAC.
   
   ```
   [~DeviceB] local-aaa-server
   ```
   ```
   [~DeviceB-local-aaa-server] user vpdnuser@huawei.com password cipher YsHsjx_202206 authentication-type p
   ```
   ```
   [~DeviceB-local-aaa-server] quit
   ```
   
   # Configure address pools.
   
   1. Configure an IPv6 delegation prefix pool named **pre1** for ND users.
      ```
      [~DeviceB] ipv6 prefix pre1 delegation
      ```
      ```
      [*DeviceB-ipv6-prefix-pre1] prefix 2001:db8:2001::2421/48
      ```
      ```
      [*DeviceB-ipv6-prefix-pre1] slaac-unshare-only  
      ```
      ```
      [~DeviceB-ipv6-prefix-pre1] commit
      ```
      ```
      [~DeviceB-ipv6-prefix-pre1] quit
      ```
   2. Configure an IPv6 delegation prefix pool named **pre2** for PD users.
      ```
      [~DeviceB] ipv6 prefix pre2 delegation
      ```
      ```
      [*DeviceB-ipv6-prefix-pre2] prefix 2001:db8:2001::/44
      ```
      ```
      [*DeviceB-ipv6-prefix-pre2] pd-unshare-only  
      ```
      ```
      [~DeviceB-ipv6-prefix-pre2] commit
      ```
      ```
      [~DeviceB-ipv6-prefix-pre2] quit
      ```
   3. Configure an IPv6 delegation address pool named **pool1** and bind it to the IPv6 delegation prefix pool **pre1**.
      ```
      [~DeviceB] ipv6 pool pool1 bas delegation
      ```
      ```
      [*DeviceB-ipv6-pool-pool1] prefix pre1
      ```
      ```
      [*DeviceB-ipv6-pool-pool1] dns-server 2001:db8:2400::1 2001:db8:2400::2
      ```
      ```
      [~DeviceB-ipv6-pool-pool1] commit
      ```
      ```
      [~DeviceB-ipv6-pool-pool1] quit
      ```
   4. Configure an IPv6 delegation address pool named **pool2** and bind it to the IPv6 delegation prefix pool **pre2**.
      ```
      [~DeviceB] ipv6 pool pool2 bas delegation
      ```
      ```
      [*DeviceB-ipv6-pool-pool2] prefix pre2
      ```
      ```
      [*DeviceB-ipv6-pool-pool2] dns-server 2001:db8:2400::1 2001:db8:2400::2
      ```
      ```
      [~DeviceB-ipv6-pool-pool2] commit
      ```
      ```
      [~DeviceB-ipv6-pool-pool2] quit
      ```
   5. Configure a local IPv4 address pool named **pppoe-pool**.
      ```
      [~DeviceB] ip pool pppoe-pool bas local
      ```
      ```
      [*DeviceB-ip-pool-pppoe-pool] gateway 10.179.180.1 255.255.255.0
      ```
      ```
      [*DeviceB-ip-pool-pppoe-pool] commit
      ```
      ```
      [~DeviceB-ip-pool-pppoe-pool] section 0 10.179.180.2 10.179.180.254
      ```
      ```
      [*DeviceB-ip-pool-pppoe-pool] commit
      ```
      ```
      [~DeviceB-ip-pool-pppoe-pool] quit
      ```
   
   # Configure a user access domain.
   
   ```
   [~DeviceB] aaa
   ```
   ```
   [~DeviceB-aaa] authentication-scheme auth1
   ```
   ```
   [*DeviceB-aaa-authen-auth1] authentication-mode local
   ```
   ```
   [*DeviceB-aaa-authen-auth1] commit
   ```
   ```
   [~DeviceB-aaa-authen-auth1] quit
   ```
   ```
   [~DeviceB-aaa] accounting-scheme default0
   ```
   ```
   [*DeviceB-aaa-accounting-default0] accounting-mode none
   ```
   ```
   [*DeviceB-aaa-accounting-default0] commit
   ```
   ```
   [~DeviceB-aaa-accounting-default0] quit
   ```
   ```
   [~DeviceB-aaa] domain huawei.com
   ```
   ```
   [~DeviceB-aaa-domain-huawei.com] authentication-scheme auth1
   ```
   ```
   [*DeviceB-aaa-domain-huawei.com] accounting-scheme default0
   ```
   ```
   [*DeviceB-aaa-domain-huawei.com] ip-pool pppoe-pool
   ```
   ```
   [*DeviceB-aaa-domain-huawei.com] ipv6-pool pool1
   ```
   ```
   [*DeviceB-aaa-domain-huawei.com] ipv6-pool pool2
   ```
   ```
   [*DeviceB-aaa-domain-huawei.com] commit
   ```
   ```
   [~DeviceB-aaa-domain-huawei.com] quit
   ```
   ```
   [~DeviceB-aaa] quit
   ```
4. Verify the configuration.
   
   
   
   # After completing the configurations, have the user go online. Then, run the **display l2tp tunnel** command on both the LAC and LNS to check whether an L2TP tunnel is set up successfully. The following example uses the command output on the LNS.
   
   ```
   [~Device] display l2tp tunnel
   ```
   ```
   ---------------------------------------------------------
   ```
   ```
   -----------tunnel information in LAC---------------------  
   ```
   ```
    Total 0,0 printed  
   ```
   ```
   ---------------------------------------------------------       
   ```
   ```
   -----------tunnel information in LNS---------------------       
   ```
   ```
   The tunnel information of k board 1
   ```
   ```
    LocalTID RemoteTID RemoteAddress    Port   Sessions RemoteName   
   ```
   ```
   ---------------------------------------------------------    
   ```
   ```
    13921    7958      10.38.160.1    57344     1       LAC      
   ```
   ```
   ---------------------------------------------------------     
   ```
   ```
   Total 1,1 printed from slot 1 
   ```

#### Configuration Files

DeviceA configuration file

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
 ip address 10.38.160.1 255.255.255.0
```
```
#
```
```
interface GigabitEthernet0/2/0.100
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
  access-type layer2-subscriber default-domain authentication huawei.com
```
```
  authentication-method ppp
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
 ip address 192.168.10.1 255.255.255.255
```
```
#
```
```
ospf 4
```
```
 area 0.0.0.1
```
```
#
```
```
interface LoopBack1
```
```
 ip address 10.1.2.1 255.255.255.255
```
```
 ospf enable 4 area 0.0.0.1
```
```
 binding tunnel gre
```
```
#
```
```
interface LoopBack2
```
```
 ip address 10.1.1.1 255.255.255.255 
```
```
interface Tunnel1
```
```
 ip address 10.1.1.2 255.255.255.255
```
```
 tunnel-protocol gre
```
```
 source LoopBack1
```
```
 destination 10.10.10.10
```
```
#
```
```
ip route-static 10.5.1.1 255.255.255.255 Tunnel1
```
```
#
```
```
l2tp-group 1
```
```
 tunnel password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
```
```
 tunnel name LAC
```
```
 start l2tp ip 10.5.1.1
```
```
 tunnel source LoopBack2
```
```
#
```
```
local-aaa-server
```
```
user vpdnuser@huawei.com password cipher 
%@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81wtNj:ej5XU>Jf_<1a"!)dspWPNxp5I!!!!!!!!!!1!!!!*M%{F9=pQ/,YelLM6Ad;%@%# authentication-type p
```
```
#
```
```
aaa
```
```
 authentication-scheme auth1
```
```
  authentication-mode local
```
```
 accounting-scheme default0
```
```
   accounting-mode none
```
```
 domain huawei.com
```
```
  authentication-scheme auth1
```
```
  accounting-scheme default0
```
```
  idle-cut 60 500
```
```
l2tp-group 1
```
```
#
```
```
return
```

DeviceB configuration file

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
interface gigabitethernet0/1/0
```
```
 undo shutdown
```
```
 ipv6 enable
```
```
 ip address 10.38.160.2 255.255.255.0
```
```
 ipv6 address auto link-local
```
```
 ospf enable 4 area 0.0.0.1
```
```
 undo dcn
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
ospf 4
```
```
 default-route-advertise
```
```
 area 0.0.0.1
```
```
#
```
```
interface LoopBack1
```
```
 ip address 10.10.10.10 255.255.255.255
```
```
 ospf enable 4 area 0.0.0.1
```
```
 binding tunnel gre
```
```
#
```
```
interface LoopBack2
```
```
 ip address 10.5.1.1 255.255.255.255
```
```
#
```
```
interface Tunnel1
```
```
 ip address 192.168.1.1 255.255.255.255
```
```
 tunnel-protocol gre
```
```
 source LoopBack1
```
```
 destination 10.1.2.1
```
```
#
```
```
ip route-static 10.1.1.1 255.255.255.255 Tunnel1
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
tunnel password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
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
bind source LoopBack2
```
```
#
```
```
ipv6 prefix pre2 delegation
```
```
 prefix 2001:db8:2001::/44  
```
```
 pd-unshare-only 
```
```
#
```
```
ipv6 prefix pre1 delegation
```
```
  prefix 2001:db8:2001::2421/48
```
```
  slaac-unshare-only
```
```
#
```
```
ip pool pppoe-pool bas local
```
```
 gateway 10.179.180.1 255.255.255.0
```
```
 section 0 10.179.180.2 10.179.180.254
```
```
#
```
```
ipv6 pool pool1 bas delegation
```
```
 dns-server 2001:db8:2400::1 2001:db8:2400::2
```
```
 prefix pre1
```
```
#
```
```
ipv6 pool pool2 bas delegation
```
```
 dns-server 2001:db8:2400::1 2001:db8:2400::2
```
```
 prefix pre2
```
```
#
```
```
local-aaa-server
```
```
 user vpdnuser@huawei.com password cipher %@%##!!!!!!!!!"!!!!#!!!!(!!!!JMi&5#;qTW7C9)&16~.M{sv*SzKjgN>0b[,G:tb%!!!!!!!!!!1!!!!E'QA>XV7kJ+tIm3UL=c=%@%# authentication-type p
```
```
#
```
```
aaa
```
```
 authentication-scheme auth1
```
```
   authentication-mode local
```
```
  domain huawei.com
```
```
   authentication-scheme auth1
```
```
   accounting-scheme default0
```
```
   ip-pool pppoe-pool
```
```
   ipv6-pool pool1
```
```
   ipv6-pool pool2
```
```
#
```
```
return
```