Example for Configuring L2TP Tunnel Access for PPPoE Dual-Stack Users
=====================================================================

This section provides an example for configuring L2TP tunnel access for PPPoE dual-stack users. A networking diagram is provided to help you understand the configuration procedure. The configuration example includes the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure1 Configuring L2TP tunnel access for PPPoE dual-stack users](#EN-US_TASK_0204897238__p21951554195113), a point-to-point L2TP tunnel is established on a public network. PPP data frames are encapsulated as L2TP packets, which are then transmitted over the L2TP tunnel. The LAC and LNS reside on a WAN and communicate with each other through the L2TP tunnel. Both the LAC and LNS implement RADIUS authentication on the username and password of a user. An IPv6 address, ND prefix, PD prefix, and the DNS server's IPv6 address must be configured on the LNS. After remote users access the public network, they can access internal network resources over the L2TP tunnel. This provides a secure and cost-effective way for remote users to access a private enterprise network.

**Figure 1** Configuring L2TP tunnel access for PPPoE dual-stack users![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 connecting the LAC to the tunnel represents GE0/1/0, and its IP address is 10.38.160.1. Interface1 connecting the LNS to the tunnel represents GE0/1/0, and its IP address is 10.38.160.2. Interface2 connecting the LAC to the remote user's private enterprise network is GE0/2/0.

![](figure/en-us_image_0206300925.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the LAC.
   
   * Configure an interface address for the LAC.
   * Enable L2TP.
   * Configure an L2TP tunnel connection on the LAC.
   * Configure a tunnel authentication mode.
   * Configure the PPPoE access service for the LAC.
2. Configure the LNS.
   
   * Configure an interface address for the LNS and enable IPv6 on the interface.
   * Configure a VT.
   * Enable L2TP.
   * Configure an L2TP tunnel connection on the LNS.
   * Configure a tunnel authentication mode and user authentication mode.
   * Configure LNS-side tunnel parameters.
   * Configure the DHCPv6 device to generate DUIDs in DUID-LLT mode.
   * Configure address pools, including a local IPv4 address pool and an IPv6 delegation prefix pool.
   * Configure an L2TP user domain and specify address pools in the domain.
   * Configure a RADIUS server.

#### Data Preparation

To complete the configuration, you need the following data:

* Identical domain names, usernames, and passwords on the LAC and LNS
* LNS-side tunnel authentication mode (CHAP is used in this example) and tunnel password
* LNS-side local and remote tunnel names
* VT number
* L2TP group ID
* Names and address ranges of address pools
* AAA domain name
* User authentication mode on DeviceA (RADIUS authentication)
* User authentication mode on DeviceB (RADIUS authentication)

#### Procedure

1. Configure DeviceA that functions as the LAC.
   
   
   
   # Assign an IP address to GE 0/1/0.
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] sysname DeviceA
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip address 10.38.160.1 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Enable basic L2TP functions and configure an L2TP connection on the LAC.
   
   ```
   [~DeviceA] l2tp enable
   ```
   ```
   [*DeviceA] l2tp-group group1
   ```
   ```
   [*DeviceA-l2tp-group1] tunnel name LAC
   ```
   ```
   [*DeviceA-l2tp-group1] start l2tp ip 10.38.160.2
   ```
   ```
   [*DeviceA-l2tp-group1] tunnel source gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-l2tp-group1] commit
   ```
   ```
   [~DeviceA-l2tp-group1] quit
   ```
   
   # Configure a tunnel authentication mode.
   
   ```
   [~DeviceA-l2tp-group1] tunnel authentication
   ```
   ```
   [*DeviceA-l2tp-group1] tunnel password cipher YsHsjx_202206
   ```
   ```
   [*DeviceA-l2tp-group1] commit
   ```
   ```
   [~DeviceA-l2tp-group1] quit
   ```
   
   # Configure the PPPoE access service.
   
   1. Configure AAA schemes.
      ```
      [~DeviceA] aaa
      ```
      ```
      [~DeviceA-aaa] accounting-scheme radius1
      ```
      ```
      [*DeviceA-aaa-accounting-radius1] authentication-mode radius
      ```
      ```
      [*DeviceA-aaa-accounting-radius1] commit
      ```
      ```
      [~DeviceA-aaa-accounting-radius1] quit
      ```
      ```
      [~DeviceA-aaa] authentication-scheme radius1
      ```
      ```
      [*DeviceA-aaa-authen-radius1] authentication-mode radius
      ```
      ```
      [*DeviceA-aaa-authen-radius1] commit
      ```
      ```
      [~DeviceA-aaa-authen-radius] quit
      ```
      ```
      [~DeviceA-aaa] quit
      ```
   2. Configure a RADIUS server group.
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
   3. Configure a user access domain.
      ```
      [~DeviceA] aaa
      ```
      ```
      [~DeviceA-aaa] domain huawei.com
      ```
      ```
      [*DeviceA-aaa-domain-huawei.com] authentication-scheme radius1 
      ```
      ```
      [*DeviceA-aaa-domain-huawei.com] accounting-scheme radius1
      ```
      ```
      [*DeviceA-aaa-domain-huawei.com] radius-server group radius1
      ```
      ```
      [*DeviceA-aaa-domain-huawei.com] commit
      ```
      ```
      [*DeviceA-aaa-domain-huawei.com] idle-cut 50 600
      ```
      ```
      [~DeviceA-aaa-domain-huawei.com] l2tp-group group1
      ```
      ```
      [*DeviceA-aaa-domain-huawei.com] commit
      ```
      ```
      [~DeviceA-aaa-domain-huawei.com] quit
      ```
      ```
      [~DeviceA-aaa] quit
      ```
   4. Configure a VT.
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
   5. Bind the VT1 to GE0/2/0.100.
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
   6. Configure a BAS interface.
      ```
      [~DeviceA-GigabitEthernet0/2/0.100] bas
      ```
      ```
      [~DeviceA-GigabitEthernet0/2/0.100-bas] access-type layer2-subscriber default-domain authentication huawei.com
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
2. Configure DeviceB that functions as the LNS.
   
   
   
   # Assign an IP address to the interface connecting the LNS to the tunnel and enable IPv6 on the interface.
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] sysname DeviceB
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-gigabitethernet0/1/0] ip address 10.38.160.2 255.255.255.0
   ```
   ```
   [*DeviceB-gigabitethernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceB-gigabitethernet0/1/0] ipv6 address auto link-local
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
   [*DeviceB] l2tp-group group1
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure the local tunnel name and peer tunnel name on the LNS side.
   
   ```
   [~DeviceB-l2tp-group1] tunnel name LNS
   ```
   ```
   [*DeviceB-l2tp-group1] allow l2tp virtual-template 1 remote LAC
   ```
   
   # Enable tunnel authentication and configure a tunnel authentication password.
   
   ```
   [*DeviceB-l2tp-group1] tunnel authentication
   ```
   ```
   [*DeviceB-l2tp-group1] tunnel password cipher YsHsjx_202206
   ```
   
   # Configure the LNS to perform mandatory CHAP authentication.
   
   ```
   [*DeviceB-l2tp-group1] mandatory-chap
   ```
   ```
   [*DeviceB-l2tp-group1] commit
   ```
   ```
   [~DeviceB-l2tp-group1] quit
   ```
   # Configure an LNS group named **group1**.
   ```
   [~DeviceB] lns-group group1
   ```
   ```
   [*DeviceB-lns-group-group1] bind slot 1 
   ```
   ```
   [*DeviceB-lns-group-group1] commit
   ```
   ```
   [~DeviceB-lns-group-group1] bind source gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-lns-group-group1] commit
   ```
   ```
   [~DeviceB-lns-group-group1] quit
   ```
   
   # Configure the DHCPv6 device to generate DUIDs in DUID-LLT mode.
   ```
   [~DeviceB] dhcpv6 duid llt
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure address pools.
   
   1. Configure an IPv6 delegation prefix pool named **pre1** for ND users.
      ```
      [~DeviceB] ipv6 prefix pre1 delegation
      ```
      ```
      [*DeviceB-ipv6-prefix-pre1] prefix 2001:db8:1::/48
      ```
      ```
      [*DeviceB-ipv6-prefix-pre1] slaac-unshare-only  
      ```
      ```
      [*DeviceB-ipv6-prefix-pre1] commit
      ```
      ```
      [~DeviceB-ipv6-prefix-pre1] quit
      ```
   2. Configure an IPv6 delegation prefix pool named **pre2** for PD users.
      ```
      [~DeviceB] ipv6 prefix pre2 delegation
      ```
      ```
      [*DeviceB-ipv6-prefix-pre2] prefix 2001:db8:10::/44
      ```
      ```
      [*DeviceB-ipv6-prefix-pre2] pd-unshare-only  
      ```
      ```
      [*DeviceB-ipv6-prefix-pre2] commit
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
      [*DeviceB-ipv6-pool-pool1] dns-server 2001:db8::1 2001:db8::2
      ```
      ```
      [*DeviceB-ipv6-pool-pool1] commit
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
      [*DeviceB-ipv6-pool-pool2] dns-server 2001:db8::1 2001:db8::2
      ```
      ```
      [*DeviceB-ipv6-pool-pool2] commit
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
   
   # Configure a RADIUS server group.
   
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
   [~DeviceB-aaa] accounting-scheme radius1
   ```
   ```
   [*DeviceB-aaa-accounting-radius1] authentication-mode radius
   ```
   ```
   [*DeviceB-aaa-accounting-radius1] commit
   ```
   ```
   [~DeviceB-aaa-accounting-radius1] quit
   ```
   ```
   [~DeviceB-aaa] authentication-scheme radius1
   ```
   ```
   [*DeviceB-aaa-authen-local1] authentication-mode radius
   ```
   ```
   [*DeviceB-aaa-authen-local1] quit
   ```
   ```
   [*DeviceB-aaa]  domain huawei.com
   ```
   ```
   [*DeviceB-aaa-domain-huawei.com] authentication-scheme radius1
   ```
   ```
   [*DeviceB-aaa-domain-huawei.com] accounting-scheme radius1
   ```
   ```
   [*DeviceB-aaa-domain-huawei.com] radius-server group radius1
   ```
   ```
   [*DeviceB-aaa-domain-huawei.com] commit
   ```
   ```
   [~DeviceB-aaa-domain-huawei.com] ip-pool pppoe-pool
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
 undo shutdown
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
l2tp-group group1
```
```
 tunnel password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
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
local-aaa-server
```
```
 user vpdnuser@huawei.com password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81wtNj:ej5XU>Jf_<1a"!)dspWPNxp5I!!!!!!!!!!1!!!!*M%{F9=pQ/,YelLM6Ad;%@%# authentication-type p
```
```
#
```
```
aaa
```
```
 #
```
```
  accounting-scheme radius1
```
```
 #
```
```
  accounting-scheme radius1  
```
```
 #
```
```
  radius-server group radius
```
```
 #
```
```
  domain huawei.com
```
```
   authentication-scheme radius1
```
```
   accounting-scheme radius1
```
```
   radius-server group radius1
```
```
   idle-cut 50 600
```
```
   l2tp-group group1
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
dhcpv6 duid 0001000124fbc193dc99141ea1e9
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
ipv6 enable
```
```
ipv6 address auto link-local
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
interface LoopBack0
```
```
 ip address 192.168.10.1 255.255.255.255
```
```
#
```
```
l2tp-group group1
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
ipv6 prefix pre1 delegation
```
```
 prefix 2001:db8:1::/48
```
```
 slaac-unshare-only
```
```
#
```
```
ipv6 prefix pre2 delegation
```
```
 prefix 2001:db8:10::/44
```
```
 pd-unshare-only  
```
```
#
```
```
ipv6 pool pool1 bas delegation
```
```
 prefix pre1
```
```
 dns-server 2001:db8::1 2001:db8::2
```
```
#
```
```
ipv6 pool pool2 bas delegation
```
```
 prefix pre2
```
```
 dns-server 2001:db8::1 2001:db8::2
```
```
#
```
```
aaa
```
```
#
```
```
 #
```
```
  authentication-scheme radius1
```
```
 #
```
```
  accounting-scheme radius1
```
```
 #
```
```
  domain huawei.com
```
```
   authentication-scheme radius1
```
```
   accounting-scheme radius1
```
```
   radius-server group radius1
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