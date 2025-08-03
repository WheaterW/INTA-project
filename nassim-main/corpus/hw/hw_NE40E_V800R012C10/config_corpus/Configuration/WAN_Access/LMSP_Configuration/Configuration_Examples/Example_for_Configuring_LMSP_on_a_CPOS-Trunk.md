Example for Configuring LMSP on a CPOS-Trunk
============================================

In this example, a CPOS-Trunk is configured on the Router to aggregate multiple E1 links connected to mid-range-and-low-end devices and identify devices with different timeslots. In addition, LMSP is configured on the CPOS interfaces of the Router to implement protection switching.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172364416__fig_dc_ne_lmsp_cfg_002101), mid-range-and-low-end devices are connected to the transport network through E1 links. These E1 links are aggregated into a CPOS-Trunk interface configured on Device A. Device A uses timeslots to identify these devices. The CPOS-Trunk interface on Device A consists of two CPOS interfaces. Single-chassis LMSP needs to be configured on the CPOS interfaces to improve data transfer reliability.

In real-world situations, mid-range-and-low-end devices are usually connected to CPOS interfaces over a multi-layer transport network. Therefore, relay devices and other transport means are probably involved.

**Figure 1** Networking diagram for configuring LMSP on a CPOS-Trunk![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configurations in this example are performed on Device-A. HUAWEI NE40E-M2 series can function as Device-A.


  
![](images/fig_dc_ne_lmsp_cfg_002101.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure single-chassis LMSP on the two CPOS interfaces and add the CPOS interfaces to a CPOS-Trunk interface.
2. Bundle timeslots of E1 channels in the CPOS-Trunk interface to create Trunk-Serial interfaces and add the Trunk-Serial interfaces into a Global-MP-Group interface.

#### Data Preparation

To complete the configuration, you need the following data:

* LMSP parameters
* CPOS-Trunk interface parameters
* Global-MP-Group interface number

#### Procedure

1. Configure single-chassis LMSP.
   1. Configure single-chassis LMSP on Device A.
      
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname DeviceA
      ```
      ```
      [~HUAWEI] commit
      ```
      ```
      [~DeviceA] controller cpos 0/1/0
      ```
      ```
      [*DeviceA-Cpos0/1/0] undo shutdown
      ```
      ```
      [*DeviceA-Cpos0/1/0] aps group 1
      ```
      ```
      [*DeviceA-Cpos0/1/0] aps working
      ```
      ```
      [*DeviceA-Cpos0/1/0] commit
      ```
      ```
      [~DeviceA-Cpos0/1/0] quit
      ```
      ```
      [~DeviceA] controller cpos 0/2/0
      ```
      ```
      [*DeviceA-Cpos0/2/0] undo shutdown
      ```
      ```
      [*DeviceA-Cpos0/2/0] aps group 1
      ```
      ```
      [*DeviceA-Cpos0/2/0] aps protect
      ```
      ```
      [*DeviceA-Cpos0/2/0] aps mode one-plus-one unidirection
      ```
      ```
      [*DeviceA-Cpos0/2/0] aps revert 6
      ```
      ```
      [*DeviceA-Cpos0/2/0] commit
      ```
      ```
      [~DeviceA-Cpos0/2/0] quit
      ```
   2. Create a CPOS-Trunk interface on Device A and add CPOS interfaces to the CPOS-Trunk interface.
      
      
      ```
      [~DeviceA] interface cpos-trunk 0
      ```
      ```
      [*DeviceA-Cpos-Trunk0] commit
      ```
      ```
      [~DeviceA-Cpos-Trunk0] quit
      ```
      ```
      [~DeviceA] controller cpos 0/1/0
      ```
      ```
      [~DeviceA-Cpos0/1/0] cpos-trunk 0
      ```
      ```
      [*DeviceA-Cpos0/1/0] commit
      ```
      ```
      [~DeviceA-Cpos0/1/0] quit
      ```
      ```
      [~DeviceA] controller cpos 0/2/0
      ```
      ```
      [~DeviceA-Cpos0/2/0] cpos-trunk 0
      ```
      ```
      [*DeviceA-Cpos0/2/0] commit
      ```
      ```
      [~DeviceA-Cpos0/2/0] quit
      ```
2. Configure the CPOS-Trunk interface.
   1. Bundle timeslots of E1 channels in the CPOS-Trunk interface.
      
      
      ```
      [~DeviceA] interface cpos-trunk 0
      ```
      ```
      [~DeviceA-Cpos-Trunk0] e1 1 channel-set 1 timeslot-list 1-15
      ```
      ```
      [*DeviceA-Cpos-Trunk0] e1 2 channel-set 2 timeslot-list 17-31
      ```
      ```
      [*DeviceA-Cpos-Trunk0] commit
      ```
      ```
      [~DeviceA-Cpos-Trunk0] quit
      ```
   2. Create a Global-MP-Group interface.
      
      
      ```
      [~DeviceA] interface global-mp-group 0
      ```
      ```
      [*DeviceA-Global-Mp-Group0] shutdown
      ```
      ```
      [*DeviceA-Global-Mp-Group0] commit
      ```
      ```
      [~DeviceA-Global-Mp-Group0] quit
      ```
   3. Add Trunk-Serial interfaces to the Global-MP-Group interface.
      
      
      ```
      [~DeviceA] interface Trunk-Serial0/1:1
      ```
      ```
      [~DeviceA-Trunk-Serial0/1:1] shutdown
      ```
      ```
      [*DeviceA-Trunk-Serial0/1:1] link-protocol ppp
      ```
      ```
      [*DeviceA-Trunk-Serial0/1:1] ppp mp-global global-mp-group 0
      ```
      ```
      [*DeviceA-Trunk-Serial0/1:1] commit
      ```
      ```
      [~DeviceA-Trunk-Serial0/1:1] quit
      ```
      ```
      [~DeviceA] interface Trunk-Serial0/2:2
      ```
      ```
      [~DeviceA-Trunk-Serial0/2:2] shutdown
      ```
      ```
      [*DeviceA-Trunk-Serial0/2:2] link-protocol ppp
      ```
      ```
      [*DeviceA-Trunk-Serial0/2:2] ppp mp-global global-mp-group 0
      ```
      ```
      [*DeviceA-Trunk-Serial0/2:2] commit
      ```
      ```
      [~DeviceA-Trunk-Serial0/2:2] quit
      ```
   4. Restart Trunk-Serial interfaces and the Global-MP-Group interface.
      
      
      ```
      [~DeviceA] interface global-mp-group 0
      ```
      ```
      [~DeviceA-Global-Mp-Group0] undo shutdown
      ```
      ```
      [*DeviceA-Global-Mp-Group0] commit
      ```
      ```
      [~DeviceA-Global-Mp-Group0] quit
      ```
      ```
      [~DeviceA] interface Trunk-Serial0/1:1
      ```
      ```
      [~DeviceA-Trunk-Serial0/1:1] undo shutdown
      ```
      ```
      [*DeviceA-Trunk-Serial0/1:1] commit
      ```
      ```
      [~DeviceA-Trunk-Serial0/1:1] quit
      ```
      ```
      [~DeviceA] interface Trunk-Serial0/2:2
      ```
      ```
      [~DeviceA-Trunk-Serial0/2:2] undo shutdown
      ```
      ```
      [*DeviceA-Trunk-Serial0/2:2] commit
      ```
      ```
      [~DeviceA-Trunk-Serial0/2:2] quit
      ```
3. Verify the configuration.
   
   
   
   # Run the **display aps group** command on Device A to view the LMSP configuration. The command output shows the working interface, protection interface, and switchback WTR time.
   
   ```
   [~DeviceA] display aps group 1
   ```
   ```
   APS Group  1: Cpos0/1/0 working channel 1(Active)
                  Cpos0/2/0 protection channel 0(Inactive)
                  Unidirectional, 1+1 mode, Revert time(6 minutes)
                  No Request on Both Working and Protection Side
   
   ------------------------------------------------------------------------
   Group Work-Channel Protect-Channel Wtr W-State P-State Switch-Cmd Switch-Result
   ------------------------------------------------------------------------
   1        Cpos0/1/0 Cpos0/2/0 6    ok         ok         NA          idle
   ------------------------------------------------------------------------
   total entry: 1
   ```
   
   # Run the **display cpos-trunk** command to view the CPOS-Trunk interface configuration. The command output shows the status of CPOS-Trunk member interfaces.
   
   ```
   [~DeviceA] display cpos-trunk 0
   ```
   ```
   Interface Cpos-Trunk0's state information is:
   Operate status: up          Number Of Up Port In Trunk: 1
   --------------------------------------------------------------------------------
   PortName                Status      Active Status
   Cpos0/1/0               Up          Active
   Cpos0/2/0               Up          Inactive
   
   ```
   
   # Run the **display ppp mp-global** command to view the Global-MP-Group interface configuration. The command output shows the status of Trunk-Serial interfaces in the Global-MP-Group interface.
   
   ```
   [~DeviceA] display ppp mp-global
   ```
   ```
    Global-Mp-Group is Global-Mp-Group0
    ===========Sublinks status begin======
    Trunk-Serial0/1:1 physical UP,protocol UP
    Trunk-Serial0/2:2 physical UP,protocol UP
    ===========Sublinks status end========
   ```

#### Configuration Files

* Device A configuration file
  
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
  controller Cpos0/1/0
  ```
  ```
   undo shutdown 
  ```
  ```
   aps group 1
  ```
  ```
   aps working
  ```
  ```
   cpos-trunk 0 
  ```
  ```
  #
  ```
  ```
  controller Cpos0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   aps group 1
  ```
  ```
   aps protect
  ```
  ```
   aps mode one-plus-one unidirection
  ```
  ```
   aps revert 6
  ```
  ```
   cpos-trunk 0 
  ```
  ```
  #
  ```
  ```
  interface Cpos-Trunk0
  ```
  ```
   undo shutdown
  ```
  ```
   e1 1 channel-set 1 timeslot-list 1-15
  ```
  ```
   e1 2 channel-set 2 timeslot-list 17-31
  ```
  ```
  #
  ```
  ```
  interface Global-Mp-Group0
  ```
  ```
   undo shutdown
  ```
  ```
  #
  ```
  ```
  interface Trunk-Serial0/1:1
  ```
  ```
   undo shutdown
  ```
  ```
   link-protocol ppp
  ```
  ```
   ppp mp-global global-mp-group 0
  ```
  ```
  #
  ```
  ```
  interface Trunk-Serial0/2:2
  ```
  ```
   undo shutdown
  ```
  ```
   link-protocol ppp
  ```
  ```
   ppp mp-global global-mp-group 0
  ```
  ```
  #
  ```
  ```
  return 
  ```