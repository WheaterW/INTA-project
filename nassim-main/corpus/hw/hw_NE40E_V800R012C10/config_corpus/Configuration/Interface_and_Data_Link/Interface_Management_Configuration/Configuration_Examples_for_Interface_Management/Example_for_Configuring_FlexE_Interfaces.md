Example for Configuring FlexE Interfaces
========================================

This section provides an example for configuring interfaces on two devices that are connected using FlexE.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0300605036__fig12995340422), FlexE clients need to be created on DeviceA and DeviceB for communication. Different bandwidths are configured for the FlexE clients to meet requirements for diversified services and applications. The bandwidths of FlexE Client1, FlexE Client2, FlexE Client3, and FlexE Client4 need to be set to 4 Gbit/s, 5 Gbit/s, 15 Gbit/s, and 20 Gbit/s, respectively.

**Figure 1** Networking diagram for configuring FlexE interfaces![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 0, interface 1, interface 2, interface 3, and interface 4 represent FlexE-50G 0/1/1, FlexE 0/1/129, FlexE 0/1/130, FlexE 0/1/131, and FlexE 0/1/132, respectively.


  
![](figure/en-us_image_0300605043.png)

#### Precautions

When you configure FlexE interfaces, note the following:

* To ensure normal communication between interconnected devices, you need to configure the same PHY number for the FlexE physical interfaces on both of them.
* To ensure normal communication between interconnected devices, you need to configure the same group number for the FlexE groups to which the FlexE physical interfaces on both devices are added.
* To ensure that the FlexE clients on both ends can communicate with each other, you need to configure the same ID and bandwidth for them.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Activate the FlexE interface license on a board.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command is not supported on the NE40E-M2E and NE40E-M2F.
2. Configure a standard Ethernet interface to work in FlexE mode.
3. Configure a PHY number for a FlexE physical interface.
4. Create a FlexE group and bind the FlexE physical interface to it.
5. Configure a number for the FlexE group.
6. Configure a sub-timeslot granularity for a FlexE card.
7. Create a FlexE client and configure an ID and bandwidth for it.
8. Configure an IP address for each interface.


#### Data Preparation

To complete the configuration, you need the following data:

* PHY number of a FlexE physical interface: 5
* Index of a FlexE group: 1
* Number of a FlexE group: 2345
* Sub-timeslot granularity of a FlexE card: 1 Gbit/s
* IDs of four FlexE interfaces: port numbers of interface 1, interface 2, interface 3, and interface 4
* IDs of four FlexE clients: 1, 2, 3, and 4 (corresponding to 4 Gbit/s, 5 Gbit/s, 15 Gbit/s, and 20 Gbit/s bandwidths, respectively)

#### Procedure

1. Activate the FlexE interface license on a board.
   
   
   ```
   <DeviceA> license active XXXXX.dat
   <DeviceA> system-view
   [~DeviceA] license
   [~DeviceA-license] active port-basic slot 3 card       1      port 1
   [*DeviceA-license] active port-flexe slot 3 card       1      port 1
   [*DeviceA-license] commit
   [~DeviceA-license] quit
   ```
2. Configure a standard Ethernet interface to work in FlexE mode.
   
   
   ```
   [~DeviceA] flexe enable port 0/1/1
   Warning: This operation will delete interface 50GE0/1/1 and related services. Continue? [Y/N]:y
   [*DeviceA] commit
   ```
3. Configure a PHY number for a FlexE physical interface.
   
   
   ```
   [~DeviceA] interface FlexE-50G 0/1/1
   [~DeviceA-FlexE-50G0/1/1] phy-number 5
   Warning: The traffic on this interface may be interrupted if the operation is performed. Continue? [Y/N]:y
   [*DeviceA-FlexE-50G0/1/1] commit
   [~DeviceA-FlexE-50G0/1/1] quit
   ```
4. Create a FlexE group and bind the FlexE physical interface to it.
   
   
   ```
   [~DeviceA] flexe group 1
   [*DeviceA-flexe-group-1] binding interface FlexE-50G 0/1/1
   ```
5. Configure a number for the FlexE group.
   
   
   ```
   [*DeviceA-flexe-group-1] flexe-groupnum 2345
   Warning: The traffic on related clients may be interrupted if the operation is performed. Continue? [Y/N]:y
   [*DeviceA-flexe-group-1] commit
   [~DeviceA-flexe-group-1] quit
   ```
6. Configure a sub-timeslot granularity for a FlexE card.
   
   
   ```
   [~DeviceA] set flexe sub-time-slot granula slot 3 card       1      1g
   [*DeviceA] commit
   ```
7. Create a FlexE client and configure an ID and bandwidth for it.
   
   
   ```
   [~DeviceA] flexe client-instance 1 flexe-group 1 flexe-type full-function port-id 129
   [*DeviceA-flexe-client-1] flexe-clientid 1
   Warning: The traffic on this interface may be interrupted if the operation is performed. Continue? [Y/N]:y
   [*DeviceA-flexe-client-1] flexe-bandwidth 4
   [*DeviceA-flexe-client-1] commit
   [~DeviceA-flexe-client-1] quit
   [~DeviceA] flexe client-instance 2 flexe-group 1 flexe-type full-function port-id 130
   [*DeviceA-flexe-client-2] flexe-clientid 2
   Warning: The traffic on this interface may be interrupted if the operation is performed. Continue? [Y/N]:y
   [*DeviceA-flexe-client-2] flexe-bandwidth 5
   [*DeviceA-flexe-client-2] commit
   [~DeviceA-flexe-client-2] quit
   [~DeviceA] flexe client-instance 3 flexe-group 1 flexe-type full-function port-id 131
   [*DeviceA-flexe-client-3] flexe-clientid 3
   Warning: The traffic on this interface may be interrupted if the operation is performed. Continue? [Y/N]:y
   [*DeviceA-flexe-client-3] flexe-bandwidth 15
   [*DeviceA-flexe-client-3] commit
   [~DeviceA-flexe-client-3] quit
   [~DeviceA] flexe client-instance 4 flexe-group 1 flexe-type full-function port-id 132
   [*DeviceA-flexe-client-4] flexe-clientid 4
   Warning: The traffic on this interface may be interrupted if the operation is performed. Continue? [Y/N]:y
   [*DeviceA-flexe-client-4] flexe-bandwidth 20
   [*DeviceA-flexe-client-4] commit
   [~DeviceA-flexe-client-4] quit
   ```
8. Configure an IP address for each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0300605036__postreq1260003530214026) in this section.
9. Repeat the preceding steps on DeviceB. For configuration details, see [Configuration Files](#EN-US_TASK_0300605036__postreq1260003530214026) in this section.
10. Verify the configuration.
    
    
    
    After completing the preceding configuration, run the [**display flexe group information**](cmdqueryname=display+flexe+group+information) command on DeviceA and DeviceB to check group information of FlexE cards. The command output on DeviceA is used as an example.
    
    ```
    [~DeviceA] display flexe group information slot 3 card       1     
    FlexE Card Info:
    =============================================================
    FlexE Config Mode                : Bandwidth
    =============================================================
    
    FlexE Group Info:
    =============================================================
    GroupID    Total Bandwidth(M)    Valid Bandwidth(M)
    ------------------------------------------------------
    1                50000                50000  
    =============================================================
    
    FlexE Group Binding Interfaces Capability:
    =============================================================
    -------------------------------------------------------------
    GroupID   Interfaces already bound  Interfaces can be bound  
    -------------------------------------------------------------
    1         FlexE-50G0/1/1                                                       
    -------------------------------------------------------------
    =============================================================
    
    FlexE Phy Info:
    =============================================================
    Port No             : FlexE-50G0/1/1
    Active Status       : 1
    Cfg Group ID        : 1
    Cfg Group No        : 2345
    Real TX Group No    : 2345
    Real RX Group No    : 2345
    Remote Group No     : 2345
    Cfg Phy No          : 5
    Real TX Phy No      : 5
    Real RX Phy No      : 5
    Remote Phy No       : 5
    =============================================================
    
    FlexE Time Slot Info:
    =============================================================
    
    ------------------------------------------------------
    port-no             : FlexE-50G0/1/1
    ts-num              : 10
    sub-ts-num          : 5
    -------------------------------------------------------
      time-slot-id      ts-port-map
    -------------------------------------------------------
       0:               [129][129][129][129][-]
       1:               [130][130][130][130][130]
       2:               [131][131][131][131][131]
       3:               [131][131][131][131][131]
       4:               [131][131][131][131][131]
       5:               [132][132][132][132][132]
       6:               [132][132][132][132][132]
       7:               [132][132][132][132][132]
       8:               [132][132][132][132][132]
       9:               [-][-][-][-][-]
    
    =============================================================
    
    FlexE Client Info:
    =============================================================
    ---------------------------------------------------
    Instance Index            Port Name                
    ---------------------------------------------------
    129                        FlexE0/1/129  
    130                        FlexE0/1/130 
    131                        FlexE0/1/131
    132                        FlexE0/1/132
    ---------------------------------------------------
    =============================================================
    ```
    Run the [**display interface ethernet brief**](cmdqueryname=display+interface+ethernet+brief) command on DeviceA and DeviceB to check brief information about FlexE interfaces. The command output on DeviceA is used as an example.
    ```
    [~DeviceA] display interface ethernet brief
    PHY: Physical
    *down: administratively down
    ^down: standby
    (l): loopback
    (b): BFD down
    (d): Dampening Suppressed
    (p): port alarm down
    InUti/OutUti: input utility/output utility
    Interface                   PHY   Auto-Neg Duplex Bandwidth  InUti OutUti Trunk
    FlexE0/1/129                up    -        full          4G  0.01%  0.01%    --
    FlexE0/1/130                up    -        full          5G  0.01%  0.01%    --
    FlexE0/1/131                up    -        full         15G  0.01%  0.01%    --
    FlexE0/1/132                up    -        full         20G  0.01%  0.01%    --
    FlexE-50G0/1/1            up    -        full         50G     --     --    --
    ```
    
    Run the [**display lldp neighbor brief**](cmdqueryname=display+lldp+neighbor+brief) command on DeviceA and DeviceB to check brief information about LLDP neighbors of FlexE interfaces. The command output on DeviceA is used as an example.
    ```
    [~DeviceA] display lldp neighbor brief
    Local Intf                     Neighbor Dev         Neighbor Intf        Exptime (sec)
    --------------------------------------------------------------------------------------
    FlexE0/1/129                   DeviceB              FlexE0/1/129                   114
    FlexE0/1/130                   DeviceB              FlexE0/1/130                   114
    FlexE0/1/131                   DeviceB              FlexE0/1/131                   114
    FlexE0/1/132                   DeviceB              FlexE0/1/132                   114
    FlexE-50G0/1/1               DeviceB              FlexE-50G0/1/1                 95
    ```
    
    Run the [**display interface flexe**](cmdqueryname=display+interface+flexe) *interface-number* command on DeviceA and DeviceB to check the running status and statistics of a FlexE interface. The following example uses the command output on FlexE 0/1/129 of DeviceA.
    ```
    [~DeviceA] display interface flexe 0/1/129
    FlexE0/1/129 current state : UP (ifindex: 285)
    Line protocol current state : UP 
    Last line protocol up time : 2024-11-11 09:11:24
    Link quality grade : GOOD
    Description: 
    Route Port,The Maximum Transmit Unit is 1500 
    Internet protocol processing : disabled
    IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc12-3456
    Port BW: 4G
    Pause Flowcontrol: Receive Enable and Send Enable
    Client-id Match State: Match
    Last physical up time   : 2024-11-10 15:11:46
    Last physical down time : 2024-11-10 15:11:29
    Current system time: 2024-11-11 11:36:52
    Statistics last cleared:never
        Last 300 seconds input rate: 10031 bits/sec, 1 packets/sec
        Last 300 seconds output rate: 10041 bits/sec, 1 packets/sec
        Input peak rate 125150137 bits/sec, Record time: 2024-11-10 09:25:57
        Output peak rate 125757954 bits/sec, Record time: 2024-11-10 09:25:57
        Input: 7006191780 bytes, 52343200 packets
        Output: 7024402448 bytes, 52482810 packets
        Input:
          Unicast: 52334185 packets, Multicast: 9010 packets
          Broadcast: 5 packets, JumboOctets: 0 packets
          CRC: 0 packets, Symbol: 0 packets
          Overrun: 0 packets, InRangeLength: 0 packets
          LongPacket: 0 packets, Jabber: 0 packets, Alignment: 0 packets
          Fragment: 0 packets, Undersized Frame: 0 packets
          RxPause: 0 packets
        Output:
          Unicast: 52473465 packets, Multicast: 9334 packets
          Broadcast: 11 packets, JumboOctets: 0 packets
          Lost: 0 packets, Overflow: 0 packets, Underrun: 0 packets
          System: 0 packets, Overruns: 0 packets
          TxPause: 0 packets
        Last 300 seconds input utility rate:  0.01%
        Last 300 seconds output utility rate: 0.01%
    ```

#### Configuration Files

* DeviceA configuration file
  ```
  #
  sysname DeviceA
  #
  set flexe sub-time-slot granula slot 3 card       1      1g
  flexe enable port 0/1/1
  #
  flexe group 1
   flexe-groupnum 2345
   binding interface FlexE-50G0/1/1
  #
  flexe client-instance 1 flexe-group 1 flexe-type full-function port-id 129
   flexe-clientid 1
   flexe-bandwidth 4
  #
  flexe client-instance 2 flexe-group 1 flexe-type full-function port-id 130
   flexe-clientid 2
   flexe-bandwidth 5
  #
  flexe client-instance 3 flexe-group 1 flexe-type full-function port-id 131
   flexe-clientid 3
   flexe-bandwidth 15
  #
  flexe client-instance 4 flexe-group 1 flexe-type full-function port-id 132
   flexe-clientid 4
   flexe-bandwidth 20
  #
  license
   active port-basic slot 3 card       1      port 1
   active port-flexe slot 3 card       1      port 1
  #
  interface FlexE-50G0/1/1
   undo shutdown
   undo dcn
   phy-number 5
  #
  return
  ```
* DeviceB configuration file
  ```
  #
  sysname DeviceB
  #
  set flexe sub-time-slot granula slot 3 card       1      1g
  flexe enable port 0/1/1
  #
  flexe group 1
   flexe-groupnum 2345
   binding interface FlexE-50G0/1/1
  #
  flexe client-instance 1 flexe-group 1 flexe-type full-function port-id 129
   flexe-clientid 1
   flexe-bandwidth 4
  #
  flexe client-instance 2 flexe-group 1 flexe-type full-function port-id 130
   flexe-clientid 2
   flexe-bandwidth 5
  #
  flexe client-instance 3 flexe-group 1 flexe-type full-function port-id 131
   flexe-clientid 3
   flexe-bandwidth 15
  #
  flexe client-instance 4 flexe-group 1 flexe-type full-function port-id 132
   flexe-clientid 4
   flexe-bandwidth 20
  #
  license
   active port-basic slot 3 card       1      port 1
   active port-flexe slot 3 card       1      port 1
  #
  interface FlexE-50G0/1/1
   undo shutdown
   undo dcn
   phy-number 5
  #
  return
  ```