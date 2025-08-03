Example for Configuring TDM on the CPOS-TRUNK Configured with LMSP
==================================================================

This section provides an example for configuring LMSP-based TDM on a CPOS interface.

#### Networking Requirements

TDMoPSN service can enable mobile operators to receive transparent transmission of 2G services between BTSs and BSCs in the same city through TDM links in a Metro Ethernet (ME) network. This simple and cost-reducing service can be essential, because usually, it requires one to three E1 interfaces on a BTS to connect to a BSC on a 2G RAN, and some mobile operators do not own fixed network infrastructure and have to rent E1 lines at high prices.

In [Figure 1](#EN-US_TASK_0172364412__fig_dc_ne_lmsp_cfg_002001), it is required that the BTS and PE1 be connected through two E1 links. The BSC and PE2 should be connected through two CPOS interfaces, which are configured with LMSP so as to increase reliability of data. The encapsulation protocol on the channelized serial interface of the E1 links needs to be configured as TDM. Finally, a PW needs to be set up between PE1 and PE2 to transparently transmit TDM cells.

**Figure 1** TDMoPSN networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configurations in this example are performed on PE-1 and PE-2. HUAWEI NE40E-M2 series can function as PE-1 and PE-2.

Interfaces 1 through 2 in this example are GE 0/1/0, GE 0/2/0 respectively.


  
![](images/fig_dc_ne_lmsp_cfg_002001.png)  

| **Device Name** | **Interface Name** | **IP Address and Mask** |
| --- | --- | --- |
| PE1 | GE 0/1/0  Loopback0 | 10.1.1.1/24  192.168.1.2/32 |
| P | GE 0/1/0  GE 0/2/0  Loopback0 | 10.1.1.2/24  10.2.1.1/24  192.168.1.4/32 |
| PE2 | GE 0/2/0  Loopback0 | 10.2.1.2/24  192.168.1.3/32 |




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Run an IGP protocol on the backbone network so that devices can communicate with each other.
2. Configure basic MPLS functions on the backbone network, as well as MPLS L2VPN functions on PEs. Establish a remote MPLS LDP peer relationship between PEs at both ends of a PW.
3. Configure LMSP on PE2.
4. Configure TDM interface parameters.
5. Configure a PW template.
6. Establish MPLS L2VC connections on PE1 and PE2.

#### Data Preparation

To complete the configuration, you need the following data:

* L2VC ID at both ends of the PW (must be the same)
* MPLS LSR IDs of the PEs and P device
* IP addresses of the remote peers of PEs

#### Procedure

1. Run an IGP protocol on the backbone network so that devices can communicate with each other. For detailed configurations, see the configuration file of this example.
2. Configure basic MPLS functions on the backbone network, as well as MPLS L2VPN functions on PEs. Then, establish the remote MPLS LDP peer relationship between PEs at both ends of the PW. For configuration details, see [Configuration Files](#EN-US_TASK_0172364412__section_dc_ne_lmsp_cfg_002005) in this section.
   
   
   
   The remote MPLS LDP peer relationship is only required for dynamic PWs.
3. Configure LMSP.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   The BSC device connected to PE2 must support LMSP.
   
   Configure PE2.
   
   ```
   [~PE2] interface cpos-trunk 1
   ```
   ```
   [*PE2-cpos-trunk1] commit
   ```
   ```
   [~PE2-cpos-trunk1] quit
   ```
   ```
   [~PE2] controller cpos 0/3/1
   [*PE2-Cpos0/3/1] aps group 1
   [*PE2-Cpos0/3/1] aps working 
   [*PE2-Cpos0/3/1] commit
   [~PE2-Cpos0/3/1] quit
   [~PE2] controller cpos 0/3/2
   [*PE2-Cpos0/3/2] aps group 1
   [*PE2-Cpos0/3/2] aps protect 
   [*PE2-Cpos0/3/2] aps mode one-plus-one unidirection
   [*PE2-Cpos0/3/2] commit
   [~PE2-Cpos0/3/2] quit
   [~PE2] controller cpos 0/3/1
   [~PE2-Cpos0/3/1] cpos-trunk 1
   [*PE2-Cpos0/3/1] commit
   [~PE2-Cpos0/3/1] quit
   [~PE2] controller cpos 0/3/2
   [~PE2-Cpos0/3/2] cpos-trunk 1
   [*PE2-Cpos0/3/2] commit
   [~PE2-Cpos0/3/2] quit
   ```
   
   # Run the [**display aps group**](cmdqueryname=display+aps+group) command on PE2 to view LMSP group configurations. Run the [**display cpos-trunk**](cmdqueryname=display+cpos-trunk) command on also on PE2 to view CPOS-Trunk interface configurations.
   
   ```
   <PE2> display aps group 1
   ```
   ```
   APS Group  1: Cpos 0/3/1 working channel 1(Active)
                  Cpos0/3/2 protection channel 0(Inactive)
                  Unidirection, 1+1 mode, No Revert mode
                  No Request on Both Working and Protection Side
   
   ------------------------------------------------------------------------
   Group Work-Channel Protect-Channel Wtr W-State P-State Switch-Cmd Switch-Result
   ------------------------------------------------------------------------
   1        Cpos 0/3/1   Cpos 0/3/2    NA    ok         ok         NA          idle
   ------------------------------------------------------------------------
   total entry: 1
   
   ```
   ```
   <PE2> display cpos-trunk 1
   ```
   ```
   Interface Cpos-Trunk1's state information is:,
   Operate status: up     Number Of Up Port In Trunk: 2
   --------------------------------------------------------------------------------
   PortName     Status     Active Status
   Cpos0/3/1    Up         Active
   Cpos0/3/2    Up         Inactive
   ```
4. Configure TDM interface parameters.
   
   
   1. Configure PE1.
      
      # Configure the clear channelized mode for CE1 0/2/1 and CE1 0/2/2 on PE1.
      
      ```
      [~PE1] controller e1 0/2/1
      [*PE1-E1 0/2/1] using e1
      [*PE1-E1 0/2/1] commit
      [~PE1-E1 0/2/1] quit
      [~PE1] controller e1 0/2/2
      [*PE1-E1 0/2/2] using e1
      [*PE1-E1 0/2/2] commit
      [~PE1-E1 0/2/2] quit
      ```
   2. Configure PE2.
      
      # Set CPOS-Trunk interface parameters on PE2.
      
      ```
      [~PE2] interface cpos-trunk 1
      [~PE2-Cpos-trunk1] e1 1 unframed
      [*PE2-Cpos-trunk1] e1 2 unframed
      [*PE2-Cpos-trunk1] commit
      [~PE2-Cpos-trunk1] quit
      ```
5. Configure TDM as an encapsulation protocol on the serial interface.
   
   
   1. Configure PE1.
      
      ```
      [~PE1] interface serial0/2/1:0
      [~PE1-Serial0/2/1:0] link-protocol tdm
      [*PE1-Serial0/2/1:0] commit
      [~PE1-Serial0/2/1:0] quit
      [~PE1] interface serial0/2/2:0
      [~PE1-Serial0/2/2:0] link-protocol tdm
      [*PE1-Serial0/2/2:0] commit
      [~PE1-Serial0/2/2:0] quit
      ```
   2. Configure PE2.
      
      ```
      [~PE2] interface trunk-serial1/1:0
      [~PE2-Trunk-Serial1/1:0] link-protocol tdm
      [*PE2-Trunk-Serial1/1:0] commit
      [~PE2-Trunk-Serial1/1:0] quit
      [~PE2] interface trunk-serial1/2:0
      [~PE2-Trunk-Serial1/2:0] link-protocol tdm
      [*PE2-Trunk-Serial1/2:0] commit
      [~PE2-Trunk-Serial1/2:0] quit
      ```
6. Configuring PWs.
   
   
   1. Configure PE1.
      
      ```
      [~PE1] pw-template 1to3
      [*PE1-pw-template-1to3] peer-address 192.168.1.3
      [*PE1-pw-template-1to3] jitter-buffer depth 20
      [*PE1-pw-template-1to3] tdm-encapsulation-number 40
      [*PE1-pw-template-1to3] commit
      [~PE1-pw-template-1to3] quit
      [~PE1] interface serial0/2/1:0
      [~PE1-Serial0/2/1:0] mpls l2vc pw-template 1to3 100
      [*PE1-Serial0/2/1:0] commit
      [~PE1-Serial0/2/1:0] quit
      [~PE1] interface serial0/2/2:0
      [~PE1-Serial0/2/2:0] mpls l2vc pw-template 1to3 200
      [*PE1-Serial0/2/2:0] commit
      [~PE1-Serial0/2/2:0] quit
      ```
   2. Configure PE2.
      
      ```
      [~PE2] pw-template 3to1
      [*PE2-pw-template-3to1] peer-address 192.168.1.2
      [*PE2-pw-template-3to1] jitter-buffer depth 20
      [*PE2-pw-template-3to1] tdm-encapsulation-number 40
      [*PE2-pw-template-3to1] commit
      [~PE2-pw-template-3to1] quit
      [~PE2] interface trunk-serial1/1:0
      [~PE2-Trunk-Serial1/1:0] mpls l2vc pw-template 3to1 100
      [*PE2-Trunk-Serial1/1:0] undo shutdown
      [*PE2-Trunk-Serial1/1:0] commit
      [~PE2-Trunk-Serial1/1:0] quit
      [~PE2] interface trunk-serial1/2:0
      [~PE2-Trunk-Serial1/2:0] mpls l2vc pw-template 3to1 200
      [*PE2-Trunk-Serial1/2:0] undo shutdown
      [*PE2-Trunk-Serial1/2:0] commit
      [~PE2-Trunk-Serial1/2:0] quit
      ```
      
      Run the **display mpls l2vc** command on PE1. The command output shows that the PW status is Up.
      
      ```
      <PE1> display mpls l2vc interface serial0/2/1:0
      *client interface       : Serial0/2/1:0 is up
        session state          : up
        AC state               : up
        VC state               : up
        VC ID                  : 100
        VC type                : SAT E1 over Packet
        destination            : 192.168.1.3
        local group ID         : 0 
        remote group ID        : 0
        local VC label         : 146432
        remote VC label        : 145287
        TDM encapsulation number : 40
        jitter-buffer            : 20
        idle-code                : FF
        rtp-header               : disable
        local AC OAM State     : up
        local PSN State        : up
        local forwarding state : forwarding
        local status code      : 0x0
        remote AC OAM state    : up
        remote PSN state       : up
        remote forwarding state: forwarding
        remote statuscode      : 0x0   
        BFD for PW             : unavailable
        manual fault           : not set
        active state           : active
        forwarding entry       : not exist
        link state             : up
        local VC MTU           : 1500         
        remote VC MTU          : 1500
        local VCCV             : alert lsp-ping bfd
        remote VCCV            : none
        local control word     : disable      
        remote control word    : disable
        tunnel policy name     : --
        traffic behavior name  : --
        PW template name       : --
        primary or secondary   : primary
        VC tunnel/token info   : 0 tunnels/tokens
        create time            : 0 days, 4 hours, 48 minutes, 51 seconds
        up time                : 0 days, 3 hours, 43 minutes, 49 seconds
        last change time       : 0 days, 0 hours, 39 minutes, 29 seconds
        VC last up time        : 2008/12/26 12:02:49
        VC total up time       : 0 days, 3 hours, 43 minutes, 49 seconds
        CKey                   : 11
        NKey                   : 10
      
      ```
7. Verify the configuration.
   
   
   
   Simulate a fault on the side of PE2 connecting to the BSC.
   
   # Run the [**shutdown**](cmdqueryname=shutdown) command on CPOS 0/3/1.
   
   ```
   [~PE2] controller cpos 0/3/1
   [~PE2-Cpos0/3/1] shutdown
   ```
   
   Run the [**display aps group 1**](cmdqueryname=display+aps+group+1) command on PE2. The LMSP status changes to Switch. Run the [**display cpos-trunk 1**](cmdqueryname=display+cpos-trunk+1) command to view the CPOS-Trunk member interface status. CPOS 0/3/2 becomes Active.
   
   ```
   [~PE2] display aps group 1
   ```
   ```
   APS Group  1: Cpos 0/3/1 working channel 1(Inactive)
                  Cpos0/3/2 protection channel 0(Active)
                  Unidirection, 1+1 mode, No Revert mode
                  No Request on Both Working and Protection Side
   
   ------------------------------------------------------------------------
   Group Work-Channel Protect-Channel Wtr W-State P-State Switch-Cmd Switch-Result
   ------------------------------------------------------------------------
   1       Cpos 0/3/1   Cpos 0/3/2    NA    sf     ok         NA          switch
   ------------------------------------------------------------------------
   total entry: 1
   
   ```
   ```
   <PE2> display cpos-trunk 1
   ```
   ```
   Interface Cpos-Trunk1's state information is:,
   Operate status: up     Number Of Up Port In Trunk: 2
   --------------------------------------------------------------------------------
   PortName     Status     Active Status
   Cpos0/3/1   Down         Inactive
   Cpos0/3/2    Up         Active
   ```
   
   Run the **display mpls l2vc** command on PE1. The command output shows that the PW status is Up and has not been affected by the fault in CPOS 0/3/1 on PE2.
   
   ```
   <PE1> display mpls l2vc interface serial0/2/1:0
   *client interface       : Serial0/2/1:0 is up
     session state          : up
     AC state               : up
     VC state               : up
     VC ID                  : 100
     VC type                : SAT E1 over Packet
     destination            : 192.168.1.3
     local group ID         : 0 
     remote group ID        : 0
     local VC label         : 146432
     remote VC label        : 145287
     TDM encapsulation number : 40
     jitter-buffer            : 20
     idle-code                : FF
     rtp-header               : disable
     local AC OAM State     : up
     local PSN State        : up
     local forwarding state : forwarding
     local status code      : 0x0
     remote AC OAM state    : up
     remote PSN state       : up
     remote forwarding state: forwarding
     remote statuscode      : 0x0   
     BFD for PW             : unavailable
     manual fault           : not set
     active state           : active
     forwarding entry       : not exist
     link state             : up
     local VC MTU           : 1500         
     remote VC MTU          : 1500
     local VCCV             : alert lsp-ping bfd
     remote VCCV            : none
     local control word     : disable      
     remote control word    : disable
     tunnel policy name     : --
     traffic behavior name  : --
     PW template name       : --
     primary or secondary   : primary
     VC tunnel/token info   : 0 tunnels/tokens
     create time            : 0 days, 4 hours, 48 minutes, 51 seconds
     up time                : 0 days, 4 hours, 02 minutes, 39 seconds
     last change time       : 0 days, 0 hours, 39 minutes, 29 seconds
     VC last up time        : 2008/12/26 12:02:49
     VC total up time       : 0 days, 4 hours, 02 minutes, 39 seconds
     CKey                   : 11
     NKey                   : 10
   
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
   sysname PE1
  #
   mpls lsr-id 192.168.1.2
   mpls
  #
   mpls l2vpn
  #
  pw-template 1to3
   peer-address 192.168.1.3
   jitter-buffer depth 20
   tdm-encapsulation-number 40
  #
  mpls ldp
  #
   mpls ldp remote-peer 192.168.1.3
   remote-ip 192.168.1.3 
  #
  controller e1 0/2/1
  using e1
  undo shutdown
  #
  controller e1 0/2/2
  using e1
  undo shutdown
  #
  interface serial0/2/1:0
  link-protocol tdm
  mpls l2vc pw-template 1to3 100
  undo shutdown
  #
  interface serial0/2/2:0
  link-protocol tdm
  mpls l2vc pw-template 1to3 200
  undo shutdown
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 192.168.1.2 255.255.255.255
  #
  ospf 1
  area 0.0.0.0
    network 192.168.1.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  
  ```
* PE2 configuration file
  
  ```
  #
   sysname PE2
  #
   mpls lsr-id 192.168.1.3
   mpls
  #
   mpls l2vpn
  #
  pw-template 3to1
   peer-address 192.168.1.2
   jitter-buffer depth 20
   tdm-encapsulation-number 40
  #
  mpls ldp
  #
   mpls ldp remote-peer 192.168.1.2
   remote-ip 192.168.1.2
  #
  controller Cpos0/3/1
   undo shutdown
   aps group 1
   aps working
  #
  controller Cpos0/3/2
   undo shutdown
   aps group 1
   aps protect
   aps mode one-plus-one unidirection
  #
  interface cpos-trunk1
  e1 1 unframed
  e1 2 unframed
   Cpos0/3/1
   Cpos0/3/2
  #
  interface trunk-serial1/1:0
  link-protocol tdm
  mpls l2vc pw-template 3to1 100
  undo shutdown
  #
  interface trunk-serial1/2:0
  link-protocol tdm
  mpls l2vc pw-template 3to1 200
  undo shutdown
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.2.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 192.168.1.3 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.3 0.0.0.0
    network 10.2.1.0 0.0.0.255
  #
  return
  
  ```
* P configuration file
  
  ```
  #
   sysname P
  #
   mpls lsr-id 192.168.1.4
   mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.2.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 192.168.1.4 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.4 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
  #
  return
  
  ```