Example for Configuring RSVP Authentication
===========================================

Example_for_Configuring_RSVP_Authentication

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172368321__fig_dc_vrp_te-p2p_cfg_009901), GE 0/1/0, GE 0/2/0, and GE 0/3/0 on LSRA and LSRB join Eth-Trunk1. An MPLS TE tunnel between LSRA and LSRC is established through RSVP.

The handshake function, RSVP key authentication, and message window are configured for LSRA and LSRB. The handshake function allows LSRA and LSRB to perform RSVP key authentication. RSVP key authentication prevents forged packets from requesting network resource usage. The message window function prevents RSVP message mis-sequence.

**Figure 1** Networking diagram for RSVP authentication![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 4 in this example represent GE 0/1/1, GE 0/1/2, GE 0/1/3, and GE 0/1/4, respectively.


  
![](images/fig_dc_vrp_te-p2p_cfg_009901.png)

#### Configuration Notes

None.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure MPLS and establish an MPLS TE tunnel.
2. Configure RSVP authentication on interfaces.
3. Configure the handshake function on interfaces.
4. Set the size for the message window to allow interfaces to store 32 sequence numbers.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The window size to 32 is recommended. If the window size is too small, received RSVP messages outside the window are discarded, which terminates RSVP neighbor relationships.



#### Data Preparation

To complete the configuration, you need the following data:

* OSPF process ID and area ID for every LSR
* Password and key for RSVP authentication
* RSVP message window size

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Assign an IP address and its mask to every interface as shown in [Figure 1](#EN-US_TASK_0172368321__fig_dc_vrp_te-p2p_cfg_009901). For configuration details, see [Configuration Files](#EN-US_TASK_0172368321__section_dc_vrp_te-p2p_cfg_009905) in this section.
2. Configure OSPF.
   
   
   
   Configure OSPF to advertise every network segment route and host route. For configuration details, see [Configuration Files](#EN-US_TASK_0172368321__section_dc_vrp_te-p2p_cfg_009905) in this section.
   
   After completing the configurations, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on every node. All nodes have learned routes from each other.
3. Configure basic MPLS functions and enable MPLS TE, RSVP-TE, and CSPF.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] mpls lsr-id 1.1.1.1
   ```
   ```
   [*LSRA] mpls
   ```
   ```
   [*LSRA-mpls] mpls te
   ```
   ```
   [*LSRA-mpls] mpls rsvp-te
   ```
   ```
   [*LSRA-mpls] mpls te cspf
   ```
   ```
   [*LSRA-mpls] quit
   ```
   ```
   [*LSRA] interface eth-trunk 1
   ```
   ```
   [*LSRA-Eth-Trunk1] mpls
   ```
   ```
   [*LSRA-Eth-Trunk1] mpls te
   ```
   ```
   [*LSRA-Eth-Trunk1] mpls rsvp-te
   ```
   ```
   [*LSRA-Eth-Trunk1] commit
   ```
   ```
   [~LSRA-Eth-Trunk1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Repeat this step for LSRB and LSRC. For configuration details, see [Configuration Files](#EN-US_TASK_0172368321__section_dc_vrp_te-p2p_cfg_009905) in this section.
4. Configure OSPF TE.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] ospf 1
   ```
   ```
   [~LSRA-ospf-1] opaque-capability enable
   ```
   ```
   [*LSRA-ospf-1] area 0
   ```
   ```
   [*LSRA-ospf-1-area-0.0.0.0] mpls-te enable
   ```
   ```
   [*LSRA-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~LSRA-ospf-1-area-0.0.0.0] quit
   ```
   
   # Configure LSRB.
   
   ```
   [~LSRB] ospf 1
   ```
   ```
   [~LSRB-ospf-1] opaque-capability enable
   ```
   ```
   [*LSRB-ospf-1] area 0
   ```
   ```
   [*LSRB-ospf-1-area-0.0.0.0] mpls-te enable 
   ```
   ```
   [*LSRB-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~LSRB-ospf-1-area-0.0.0.0] quit
   ```
   
   # Configure LSRC.
   
   ```
   [~LSRC] ospf 1
   ```
   ```
   [~LSRC-ospf-1] opaque-capability enable
   ```
   ```
   [*LSRC-ospf-1] area 0
   ```
   ```
   [*LSRC-ospf-1-area-0.0.0.0] mpls-te enable 
   ```
   ```
   [*LSRC-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~LSRC-ospf-1-area-0.0.0.0] quit
   ```
5. Configure an MPLS TE tunnel.
   
   
   
   # Configure the MPLS TE tunnel on LSRA.
   
   ```
   [~LSRA] interface tunnel1
   ```
   ```
   [*LSRA-Tunnel1] ip address unnumbered interface loopback 1
   ```
   ```
   [*LSRA-Tunnel1] tunnel-protocol mpls te
   ```
   ```
   [*LSRA-Tunnel1] destination 3.3.3.3
   ```
   ```
   [*LSRA-Tunnel1] mpls te tunnel-id 1
   ```
   ```
   [*LSRA-Tunnel1] commit
   ```
   ```
   [~LSRA-Tunnel1] quit
   ```
   
   After completing the configuration, run the [**display interface tunnel**](cmdqueryname=display+interface+tunnel) command on LSRA. The tunnel interface is **Up**.
   
   ```
   [~LSRA] display interface tunnel1
   ```
   ```
   Tunnel1 current state : UP (ifindex: 18)
   Line protocol current state : UP 
   Last line protocol up time : 2012-02-23 10:00:00
   Description:
   Route Port,The Maximum Transmit Unit is 1500, Current BW: 0Mbps 
   Internet Address is unnumbered, using address of LoopBack1(1.1.1.1/32)
   Encapsulation is TUNNEL, loopback not set
   Tunnel destination 3.3.3.3
   Tunnel up/down statistics 1
   Tunnel protocol/transport MPLS/MPLS, ILM is available,
   primary tunnel id is 0x161, secondary tunnel id is 0x0
   Current system time: 2012-02-24 03:33:48
       300 seconds output rate 0 bits/sec, 0 packets/sec
       0 seconds output rate 0 bits/sec, 0 packets/sec
       126 packets output,  34204 bytes
       0 output error
       18 output drop
       Last 300 seconds input utility rate:  0.00%
       Last 300 seconds output utility rate: 0.00%
   ```
6. Configure RSVP authentication on MPLS TE interfaces of LSRA and LSRB.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] interface eth-trunk 1
   ```
   ```
   [~LSRA-Eth-Trunk1] mpls rsvp-te authentication cipher YsHsjx_202206
   ```
   ```
   [*LSRA-Eth-Trunk1] mpls rsvp-te authentication handshake
   ```
   ```
   [*LSRA-Eth-Trunk1] mpls rsvp-te authentication window-size 32
   ```
   ```
   [*LSRA-Eth-Trunk1] commit
   ```
   
   # Configure LSRB.
   
   ```
   [~LSRB] interface eth-trunk 1
   ```
   ```
   [~LSRB-Eth-Trunk1] mpls rsvp-te authentication cipher YsHsjx_202206
   ```
   ```
   [*LSRB-Eth-Trunk1] mpls rsvp-te authentication handshake
   ```
   ```
   [*LSRB-Eth-Trunk1] mpls rsvp-te authentication window-size 32
   ```
   ```
   [*LSRB-Eth-Trunk1] commit
   ```
7. Verify the configuration.
   
   
   
   Run the [**reset mpls rsvp-te**](cmdqueryname=reset+mpls+rsvp-te) and [**display interface tunnel**](cmdqueryname=display+interface+tunnel) commands in sequence on LSRA. The tunnel interface is **Up**.
   
   Run the [**display mpls rsvp-te interface**](cmdqueryname=display+mpls+rsvp-te+interface) command on LSRA or LSRB. RSVP authentication information is displayed.
   
   ```
   [~LSRA] display mpls rsvp-te interface eth-trunk 1
   ```
   ```
   Interface: Eth-Trunk1
    Interface Address: 10.1.1.1
    Interface state: UP                          Interface Index: 0x15
    Total-BW: 0                                  Used-BW: 0
    Hello configured: NO                         Num of Neighbors: 1
    SRefresh feature: DISABLE                    SRefresh Interval: 30 sec
    Mpls Mtu: 1500                               Retransmit Interval: 500 msec
    Increment Value: 1
    Authentication: ENABLE
    Challenge: ENABLE                            WindowSize: 32
    Next Seq # to be sent: 486866945 12          Key ID: 0x0101051d0101
    Bfd Enabled: --                              Bfd Min-Tx: --
    Bfd Min-Rx: --                               Bfd Detect-Multi: --
    RSVP instance name: RSVP0
   ```

#### Configuration Files

* LSRA configuration file
  
  ```
  #
  ```
  ```
  sysname LSRA
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 1.1.1.1
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls te cspf
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface Eth-Trunk1
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls rsvp-te
  ```
  ```
   mpls rsvp-te authentication cipher O'W3[_\M"`!./a!1$H@GYA!!
  ```
  ```
   mpls rsvp-te authentication handshake
  ```
  ```
   mpls rsvp-te authentication window-size 32
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
   eth-trunk 1
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
   eth-trunk 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/3
  ```
  ```
   undo shutdown
  ```
  ```
   eth-trunk 1
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 1.1.1.1 255.255.255.255
  ```
  ```
  #
  ```
  ```
  interface Tunnel1
  ```
  ```
   ip address unnumbered interface LoopBack1
  ```
  ```
   tunnel-protocol mpls te
  ```
  ```
   destination 3.3.3.3
  ```
  ```
   mpls te tunnel-id 1
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   opaque-capability enable
  ```
  ```
   area 0.0.0.0
  ```
  ```
    mpls-te enable
  ```
  ```
    network 1.1.1.1 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* LSRB configuration file
  
  ```
  #
  ```
  ```
  sysname LSRB
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 2.2.2.2
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface Eth-Trunk1
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls rsvp-te
  ```
  ```
   mpls rsvp-te authentication cipher O'W3[_\M"`!./a!1$H@GYA!!
  ```
  ```
   mpls rsvp-te authentication handshake
  ```
  ```
   mpls rsvp-te authentication window-size 32
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
   eth-trunk 1
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
   eth-trunk 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/3
  ```
  ```
   undo shutdown
  ```
  ```
   eth-trunk 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/4
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 2.2.2.2 255.255.255.255
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   opaque-capability enable
  ```
  ```
   area 0.0.0.0
  ```
  ```
    mpls-te enable
  ```
  ```
    network 2.2.2.2 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 10.2.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* LSRC configuration file
  
  ```
  #
  ```
  ```
  sysname LSRC
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 3.3.3.3
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface GigabiEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 3.3.3.3 255.255.255.255
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   opaque-capability enable
  ```
  ```
   area 0.0.0.0
  ```
  ```
    mpls-te enable
  ```
  ```
    network 3.3.3.3 0.0.0.0
  ```
  ```
    network 10.2.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```