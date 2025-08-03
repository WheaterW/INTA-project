Example for Configuring EVPN VPWS in CCC Mode
=============================================

A local CCC connection is a connection between two CEs connected to the same PE. The PE functions like a Layer 2 switch to directly transmit packets without BGP.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001403525232__fig_dc_vrp_vpws_cfg_301301), the CEs and PE are connected through GE interfaces.

A local CCC EVPN VPWS connection needs to be deployed between CE1 and CE2.

**Figure 1** Configuring EVPN VPWS in CCC mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1 and interface2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001453845241.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a local CCC connection between CE1 and CE2 on the PE. Because a local CCC connection is bidirectional, only one connection is required.

#### Data Preparation

No data is required except interface IP addresses.


#### Procedure

1. Configure CEs.
   
   
   
   # Configure CE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~CE1-GigabitEthernet0/1/0] quit
   ```
   
   # Configure CE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] commit
   ```
   ```
   [~CE2-GigabitEthernet0/1/0] quit
   ```
2. On the PE, configure an EVPL instance and create a local CCC connection between CE1 and CE2.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE] evpl instance 1
   ```
   ```
   [*PE-evpl1] ccc interface gigabitethernet 0/1/0 out-interface gigabitethernet 0/2/0
   ```
   ```
   [*PE-evpl1] quit
   ```
   ```
   [*PE] commit
   ```
   ```
   [*PE] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*PE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*PE-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE-GigabitEthernet0/2/0] quit
   ```
3. Verify the configuration.
   
   
   
   After the configurations are complete, run the **display bgp evpn evpl** command on the PE. The command output shows that the EVPL status is **Up**.
   
   ```
   <PE> display bgp evpn evpl
   ```
   ```
   Total EVPL CCCs: 1      1 Up     0 Down
   EVPL ID : 1
   State : up
   Evpl Type : none
   Local CCC Interface1 : GigabitEthernet0/1/0 (up)
   Local CCC Interface2 : GigabitEthernet0/2/0 (up)
   Last Interface1 UP Timestamp: 2022-11-14 16:31:21+00:00
   Last Interface2 UP Timestamp: 2022-11-14 16:31:21+00:00
   ```
   
   CE1 and CE2 can ping each other.
   
   ```
   <CE1> ping 10.1.1.2
   ```
   ```
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=4 ms
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=2 ms
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=1 ms
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=1 ms
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=1 ms
   
     --- 10.1.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 1/1/4 ms
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  return
  ```
* PE configuration file
  
  ```
  #
  sysname PE
  #
  evpl instance 1
   ccc interface GigabitEthernet0/1/0 out-interface GigabitEthernet0/2/0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  return
  ```