Example for Configuring LB for a PW
===================================

This section provides an example for configuring loopback (LB) for a pseudo wire (PW).

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172362436__fig_dc_vrp_mpls-tp_oam_cfg_002401), LSRA, LSRB, and LSRC are connected using a PW built over a bidirectional label switched path (LSP). The following deployment is made to ensure connectivity and correct packet forwarding between LSRA and LSRC:

* LSRA and LSRC serve as MEPs.
* LSRB serves as a MIP.

LB can be used on a MEP to check the following items:

* Reachability of the RMEP
* Round-trip delay in the communication between the MEP and RMEP
* Loss of ping packets between the MEP and RMEP
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  LB counts only the ping packets that are lost after being sent out, providing a rough packet loss rate of the link between MEPs. The LM function can be used to obtain the accurate packet loss rate of the link between MEPs.

**Figure 1** PW over a bidirectional LSP![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_mpls-tp_oam_cfg_002401.png)  

**Table 1** Interfaces and IP addresses
| Device | Interface | IP Address |
| --- | --- | --- |
| LSRA | Loopback1 | 10.1.1.1/32 |
| GigabitEthernet0/1/0 | 10.1.2.1/24 |
| LSRB | Loopback1 | 10.1.1.2/32 |
| GigabitEthernet0/1/0 | 10.1.2.2/24 |
| GigabitEthernet0/2/0 | 10.1.3.1/24 |
| LSRC | Loopback1 | 10.1.1.3/32 |
| GigabitEthernet0/2/0 | 10.1.3.2/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a maintenance entity (ME) instance and bind it to a PW.
2. Enable LB.

#### Data Preparation

To complete the configuration, you need the following data:

* MEG name
* ID of the virtual circuit (VC) bound to the ME instance

#### Procedure

1. Configure a PW over a bidirectional LSP.
   
   
   
   For configuration details, see "[Configuration Examples](dc_vrp_vpws_cfg_3012.html)" in *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - VPN* or "Configuration Files" in this section.
2. Create an ME instance and bind it to the PW.
   
   # Create an ME instance named **test** on LSRA and bind it to the PW.
   ```
   [~LSRA] mpls-tp meg test
   [*LSRA-mpls-tp-meg-test] me l2vc peer-ip 10.1.1.3 vc-id 30000 vc-type vlan mep-id 1 remote-mep-id 2
   ```
   
   # Create an ME instance named **test** on LSRC and bind it to the PW.
   ```
   [~LSRC] mpls-tp meg test
   [*LSRC-mpls-tp-meg-test] me l2vc peer-ip 10.1.1.1 vc-id 30000 vc-type vlan mep-id 2 remote-mep-id 1
   ```
3. Enable LB.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   LB can be used to monitor connectivity between a MEP and its RMEP or a MIP. In this example, LB is used to monitor connectivity between LSRA and LSRC.
   
   
   Enable LB on LSRA.
   ```
   <LSRA> ping meg test
     PING test: 9 data bytes, press CTRL_C to break
       Reply from test: bytes=9, Sequence=1 time=100 ms
       Reply from test: bytes=9, Sequence=2 time=90 ms
       Reply from test: bytes=9, Sequence=3 time=100 ms
       Reply from test: bytes=9, Sequence=4 time=90 ms
       Reply from test: bytes=9, Sequence=5 time=100 ms
     --- ping statistics ---
       5 packet (s) transmitted
       5 packet (s) received
       0.00% packet loss
       round-trip min/avg/max 90/96/100 ms
   ```

#### Configuration Files

* LSRA configuration file
  
  ```
  #
   sysname LSRA
  #
   mpls lsr-id 10.1.1.1
   mpls
    mpls te
  #
   mpls l2vpn
  #
   bidirectional static-cr-lsp ingress Tunnel10
    forward nexthop 10.1.2.2 out-label 20
    backward in-label 20
  #
  pw-template tpatoc
   peer-address 10.1.1.3
   control-word
   tnl-policy tpatoc
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 1
   mpls
   mpls static-l2vc pw-template tpatoc 30000 transmit-vpn-label 101 receive-vpn-label 101
  #
  interface LoopBack1
   ip address 10.1.1.1 255.255.255.255
  #
  interface Tunnel10
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 10.1.1.3
   mpls te signal-protocol cr-static
   mpls te tunnel-id 100
   mpls te bidirectional
   mpls te reserved-for-binding
  #
   ip route-static 10.1.1.2 255.255.255.255 10.1.2.2
   ip route-static 10.1.1.3 255.255.255.255 10.1.2.2
  #
  tunnel-policy tpatoc
   tunnel binding destination 10.1.1.3 te Tunnel10
  #
   mpls-tp meg test
    me l2vc peer-ip 10.1.1.3 vc-id 30000 vc-type vlan mep-id 1 remote-mep-id 2
  #
  return 
  ```
* LSRB configuration file
  
  ```
  #
   sysname LSRB
  #
   mpls lsr-id 10.1.1.2
   mpls
    mpls te
  #
   bidirectional static-cr-lsp transit lsp1
    forward in-label 20 nexthop 10.1.3.2 out-label 40
    backward in-label 16 nexthop 10.1.2.1 out-label 20
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   mpls
   mpls te
   ais enable
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   mpls
   mpls te
   ais enable
  #
  interface LoopBack1
   ip address 10.1.1.2 255.255.255.255
  #
   ip route-static 10.1.1.1 255.255.255.255 10.1.2.1
   ip route-static 10.1.1.3 255.255.255.255 10.1.3.2
  #
  return  
  ```
* LSRC configuration file
  
  ```
  #
   sysname LSRC
  #
   mpls lsr-id 10.1.1.3
   mpls
    mpls te
  #
   mpls l2vpn
  #
   bidirectional static-cr-lsp egress lsp1
    forward in-label 40 lsrid 10.1.1.1 tunnel-id 100
    backward nexthop 10.1.3.1 out-label 16
  #
  pw-template tpctoa
   peer-address 10.1.1.1
   control-word
   tnl-policy tpctoa
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 1
   mpls static-l2vc pw-template tpctoa 30000 transmit-vpn-label 101 receive-vpn-label 101
  #
  interface LoopBack1
   ip address 10.1.1.3 255.255.255.255
  #
  interface Tunnel20
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 10.1.1.1
   mpls te signal-protocol cr-static
   mpls te tunnel-id 200
   mpls te passive-tunnel
   mpls te binding bidirectional static-cr-lsp egress lsp1
   mpls te reserved-for-binding
  #
   ip route-static 10.1.1.1 255.255.255.255 10.1.3.1
   ip route-static 10.1.1.2 255.255.255.255 10.1.3.1
  #
  tunnel-policy tpctoa
   tunnel binding destination 10.1.1.1 te Tunnel20
  #
   mpls-tp meg test
    me l2vc peer-ip 10.1.1.1 vc-id 30000 vc-type vlan mep-id 2 remote-mep-id 1
  #
  return  
  ```