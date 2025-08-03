Example for Configuring IGMP over L2TP
======================================

The upgrade from the OTT mode to the IPTV mode requires the IGMP over L2TP function.

#### Networking Requirements

IPTV services are deployed on the network shown in [Figure 1](#EN-US_TASK_0257894242__fig_dc_vrp_multicast_cfg_206801). An L2TP tunnel is established between the LAC and LNS. The home gateway obtains an IP address from the LNS through PPPoE dialup. Users can order multicast programs.

**Figure 1** Configuring IGMP over L2TP![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1.1 and GE 0/1/2.1, respectively.


  
![](figure/en-us_image_0258098985.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

* On the LAC
  1. Configure an IP address for LAC's interface that is to establish an L2TP tunnel with the LNS.
  2. Enable L2TP and the L2TP connection initiation capability, and configure tunnel authentication.
  3. Configure a user access domain.
  4. Configure a VT (VT 1).
  5. Bind interface 1 to VT 1 and configure interface 1 as a BRAS interface.
  6. Set the user name and password, which must be the same as those on the LNS.
* On the LNS
  1. Configure an IP address for LNS's interface that is to establish an L2TP tunnel with the LAC.
  2. Enable multicast and L2TP.
  3. Configure a VT (VT 1).
  4. Configure an LNS-side tunnel name, specify the name of the LAC-side tunnel name, and configure L2TP tunnel authentication.
  5. Configure the LNS's network-side interface and enable PIM-SM.
  6. Configure a C-RP and C-BSR.
  7. Enable IGMP, PIM-SM, and controllable multicast for VT 1.
  8. Create an LNS group (**group1**), and bind a tunnel board and an interface to the LNS group.
  9. Set the user name and password, which must be the same as those on the LAC.
  10. Configure an address pool for IP address assignment to the dial-up user.
  11. Configure a user access domain.
  12. Configure a multicast program list, bind it to a multicast profile, and apply the multicast profile to the domain.

#### Data Preparation

To complete the configuration, you need the following data:

* Identical domain names, user names, and passwords on the LAC and LNS
* Protocol and tunnel authentication mode and password (ciphertext) on the LNS; local and remote names on the LNS
* VT number, IP address, and mask
* L2TP group ID
* ID, address range, and mask of the remote address pool
* User VLAN
* VLAN ID of the sub-interfaces connecting the LAC and LNS

#### Procedure

1. Configure the LAC.
   
   
   
   # Configure an IP address for GE 0/1/2.1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname LAC
   [*HUAWEI] commit
   [~LAC] interface gigabitEthernet0/1/2.1
   [*LAC-gigabitEthernet0/1/2.1] vlan-type dot1q 1
   [*LAC-gigabitEthernet0/1/2.1] ip address 10.0.0.2 255.255.255.0 
   [*LAC-gigabitEthernet0/1/2.1] quit
   [*LAC] commit
   ```
   
   # Enable L2TP and the L2TP connection initiation capability, and configure tunnel authentication.
   
   ```
   [~LAC] l2tp enable
   [*LAC] l2tp-group 1
   [*LAC-l2tp-1] tunnel name LAC 
   [*LAC-l2tp-1] start l2tp ip 10.0.0.1
   [*LAC-l2tp-1] tunnel authentication
   [*LAC-l2tp-1] tunnel password cipher YsHsjx_202206
   [*LAC-l2tp-1] tunnel source gigabitEthernet0/1/2.1
   [*LAC-l2tp-1] quit
   [*LAC] commit
   ```
   
   # Configure a user access domain.
   
   ```
   [~LAC] aaa
   [*LAC-aaa] authentication-scheme w1
   [*LAC-aaa-authen-w1] authentication-mode local
   [*LAC-aaa-authen-w1] quit
   [*LAC-aaa] accounting-scheme w1
   [*LAC-aaa-accounting-w1] accounting-mode none
   [*LAC-aaa-accounting-w1] quit
   [*LAC-aaa] domain test.com
   [*LAC-aaa-domain-test.com] authentication-scheme w1
   [*LAC-aaa-domain-test.com] accounting-scheme w1
   [*LAC-aaa-domain-test.com] l2tp-group 1
   [*LAC-aaa-domain-test.com] quit
   [*LAC-aaa] quit
   [*LAC] commit
   ```
   
   # Configure a VT (VT 1).
   
   ```
   [~LAC] interface Virtual-Template 1
   [*LAC-Virtual-Template1] ppp authentication-mode auto
   [*LAC-Virtual-Template1] quit
   [*LAC] commit
   ```
   
   # Bind VT 1 to GE 0/1/1.1 and configure GE 0/1/1.1 as a BRAS interface.
   
   ```
   [~LAC] interface gigabitEthernet0/1/1.1
   [*LAC-gigabitEthernet0/1/1.1] pppoe-server bind Virtual-Template 1
   [*LAC-gigabitEthernet0/1/1.1] user-vlan 400
   [*LAC-gigabitEthernet0/1/1.1-vlan-400] quit
   [*LAC-gigabitEthernet0/1/1.1] bas
   [~LAC-gigabitEthernet0/1/1.1-bas] access-type layer2-subscriber default-domain authentication test.com
   [*LAC-gigabitEthernet0/1/1.1-bas] quit
   [*LAC-gigabitEthernet0/1/1.1] quit
   [*LAC] commit
   ```
   
   # Set the user name and password, which must be the same as those on the LNS.
   
   ```
   [~LAC] local-aaa-server
   [*LAC-local-aaa-server] user vpdnuser@test.com password cipher YsHsjx_202206 authentication-type p block fail-times 3 interval 5
   [*LAC-local-aaa-server] quit
   [*LAC] commit
   ```
2. Configure the LNS.
   
   
   
   # Configure an IP address for LNS's interface that is to establish an L2TP tunnel with the LAC.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname LNS
   [*HUAWEI] commit
   [~LNS] interface gigabitEthernet0/1/1.1
   [*LNS-gigabitEthernet0/1/1.1] vlan-type dot1q 1
   [*LNS-gigabitEthernet0/1/1.1] ip address 10.0.0.1 255.255.255.0 
   [*LNS-gigabitEthernet0/1/1.1] quit
   [*LNS] commit
   ```
   
   # Enable multicast and L2TP.
   
   ```
   [~LNS] multicast routing-enable
   [*LNS] l2tp enable
   [*LNS] commit
   ```
   
   # Configure a VT (VT 1).
   
   ```
   [~LNS] interface Virtual-Template 1
   [*LNS-Virtual-Template1] ppp authentication-mode auto
   [*LNS-Virtual-Template1] quit
   [*LNS] commit
   ```
   
   # Configure an LNS-side tunnel name, specify the name of the LAC-side tunnel name, and configure L2TP tunnel authentication.
   
   ```
   [~LNS] l2tp-group 1
   [*LNS-l2tp-1] tunnel name LNS
   [*LNS-l2tp-1] allow l2tp Virtual-Template 1 remote LAC
   [*LNS-l2tp-1] tunnel authentication
   [*LNS-l2tp-1] tunnel password cipher YsHsjx_202206
   [*LNS-l2tp-1] quit
   [*LNS] commit
   ```
   
   # Configure the LNS's network-side interface and enable PIM-SM.
   
   ```
   [~LNS] interface gigabitEthernet0/1/2.1
   [*LNS-gigabitEthernet0/1/2.1] vlan-type dot1q 1
   [*LNS-gigabitEthernet0/1/2.1] ip address 10.3.0.1 255.255.255.0
   [*LNS-gigabitEthernet0/1/2.1] pim sm
   [*LNS-gigabitEthernet0/1/2.1] quit
   [*LNS] commit
   ```
   
   # Configure a C-RP and C-BSR.
   
   ```
   [~LNS] pim
   [*LNS-pim] c-bsr gigabitEthernet0/1/2.1
   [*LNS-pim] c-rp gigabitEthernet0/1/2.1
   [*LNS-pim] quit
   [*LNS] commit
   ```
   
   # Enable IGMP, PIM-SM, and controllable multicast for VT 1.
   
   ```
   [~LNS] interface Virtual-Template 1
   [*LNS-Virtual-Template1] igmp enable
   [*LNS-Virtual-Template1] pim sm
   [*LNS-Virtual-Template1] multicast authorization-enable
   [*LNS-Virtual-Template1] quit
   [*LNS] commit
   ```
   
   # Create an LNS group (**group1**), and bind a tunnel board in slot 1 and an interface to the LNS group.
   
   ```
   [~LNS] lns-group group1
   [*LNS-lns-group-group1] bind slot 1 
   [*LNS-lns-group-group1] bind source gigabitEthernet0/1/1.1
   [*LNS-lns-group-group1] quit
   [*LNS] commit
   ```
   
   # Set the user name and password, which must be the same as those on the LAC.
   
   ```
   [~LNS] local-aaa-server
   [*LNS-local-aaa-server] user vpdnuser@test.com password cipher YsHsjx_202207 authentication-type p block fail-times 3 interval 5
   [*LNS-local-aaa-server] quit
   [*LNS] commit
   ```
   
   # Configure an address pool for IP address assignment to the dial-up user.
   
   ```
   [~LNS] ip pool 1 bas local
   [*LNS-ip-pool-1] gateway 192.168.1.1 255.255.255.0
   [*LNS-ip-pool-1] commit
   [~LNS-ip-pool-1] section 0 192.168.1.2 192.168.1.100
   [*LNS-ip-pool-1] quit
   [*LNS] commit
   ```
   
   # Configure a user access domain.
   
   ```
   [~LNS] aaa
   [*LNS-aaa] authentication-scheme w1
   [*LNS-aaa-authen-w1] authentication-mode local
   [*LNS-aaa-authen-w1] quit
   [*LNS-aaa] accounting-scheme w1
   [*LNS-aaa-accounting-w1] accounting-mode none
   [*LNS-aaa-accounting-w1] quit
   [*LNS-aaa] domain test.com
   [*LNS-aaa-domain-test.com] authentication-scheme w1
   [*LNS-aaa-domain-test.com] accounting-scheme w1
   [*LNS-aaa-domain-test.com] ip-pool 1
   [*LNS-aaa-domain-test.com] quit
   [*LNS-aaa] quit
   [*LNS] commit
   ```
   
   # Configure a multicast program list, bind it to a multicast profile, and apply the multicast profile to the domain.
   
   ```
   [~LNS] aaa
   [*LNS-aaa] multicast-list list2 group-address 225.1.1.1
   [*LNS-aaa] multicast-profile profile2
   [*LNS-aaa-mprofile-profile2] multicast-list name list2
   [*LNS-aaa-mprofile-profile2] quit
   [*LNS-aaa] domain test.com
   [*LNS-aaa-domain-test.com] multicast-profile profile2
   [*LNS-aaa-domain-test.com] quit
   [*LNS-aaa] quit
   [*LNS] commit
   ```
3. Verify the configuration.
   
   
   
   # Check the multicast forwarding table of the public network instance on the LNS.
   
   ```
   <LNS> display pim routing-table
   VPN-Instance: public net
    Total 1 (*, G) entry; 1 (S, G) entry
   
    (*, 225.1.1.1)
        RP: NULL
        Protocol: pim-sm, Flag: WC NIIF 
        UpTime: 00:07:10     
        Upstream interface: NULL, Refresh time: 00:07:10
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: Virtual-Template1(bas)
                Protocol: igmp, UpTime: 00:07:10, Expires: - 
   
    (10.3.0.2, 225.1.1.1)
        RP: NULL
        Protocol: pim-sm, Flag: SPT LOC ACT 
        UpTime: 00:00:03     
        Upstream interface: gigabitEthernet0/1/2.1, Refresh time: 00:00:03
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: Virtual-Template1(bas)
                Protocol: pim-sm, UpTime: 00:00:03, Expires: - 
   ```

#### Configuration Files

* LAC configuration file
  
  ```
  #
   sysname LAC
  #
  interface gigabitEthernet0/1/2.1
   vlan-type dot1q 1 
   ip address 10.0.0.2 255.255.255.0
  #
  l2tp enable
  l2tp-group 1
   tunnel password cipher %^%#F`'0X6\)->M"l83`dW(K<lKE&1PT-%Y>i|YSvR@P%^%# 
   tunnel name LAC
   start l2tp ip 10.0.0.1
   tunnel source gigabitEthernet0/1/2.1
   tunnel authentication
  #
  interface Virtual-Template 1
  ppp authentication-mode auto
  #
  interface gigabitEthernet0/1/1.1
   pppoe-server bind Virtual-Template 1
   user-vlan 400
   bas
    access-type layer2-subscriber default-domain authentication test.com
  #
  local-aaa-server
   user vpdnuser@test.com password cipher %^%#&K_>:lR[r~<z\R~hytY5b01K21v1C9N]oyOJR]G@%^%# authentication-type P block fail-times 3 interval 5
   #
  aaa
   authentication-scheme w1
    authentication-mode local
  #
   accounting-scheme w1
    accounting-mode none
  #
   domain test.com
    authentication-scheme w1
    accounting-scheme w1
    l2tp-group 1
  #
  return
  ```
* LNS configuration file
  
  ```
  #
  sysname LNS
  #
  interface gigabitEthernet0/1/1.1
   vlan-type dot1q 1
   ip address 10.0.0.1 255.255.255.0
  #
   l2tp enable
  #
   multicast routing-enable
  #
  interface Virtual-Template 1
   ppp authentication-mode auto
   igmp enable
   pim sm
   multicast authorization-enable
  #
  interface gigabitEthernet0/1/2.1
   vlan-type dot1q 1
   ip address 10.3.0.1 255.255.255.0
   pim sm
  #
  l2tp-group 1
   allow l2tp virtual-template 1 remote LAC
   tunnel password cipher  %^%#bG-/,h7b-.BS5mJu(V+1{DiH(W&UJ-mXOKYPkHX+%^%#
   tunnel name LNS
   tunnel authentication
  #
  lns-group group1
   bind slot 1
   bind source gigabitEthernet0/1/1.1
  #
  ip pool 1 bas local
   gateway 192.168.1.1 255.255.255.0
   section 0 192.168.1.2 192.168.1.100
  #
  local-aaa-server
   user vpdnuser@test.com password cipher %^%#t:S^-wfw*+peAOU&7}"PeE2""l\lAGooewIcY,G&%^%# authentication-type P block fail-times 3 interval 5
   #
  pim
   c-bsr gigabitEthernet0/1/2.1
   c-rp  gigabitEthernet0/1/2.1
  #
  aaa
  multicast-list list2 group-address 225.1.1.1
   multicast-profile profile2
    multicast-list name list2
  # 
   authentication-scheme w1
    authentication-mode local
  #
   accounting-scheme w1
    accounting-mode none
  #
   domain test.com
    authentication-scheme w1
    accounting-scheme w1
    ip-pool 1
    multicast-profile profile2
  #
  return
  ```