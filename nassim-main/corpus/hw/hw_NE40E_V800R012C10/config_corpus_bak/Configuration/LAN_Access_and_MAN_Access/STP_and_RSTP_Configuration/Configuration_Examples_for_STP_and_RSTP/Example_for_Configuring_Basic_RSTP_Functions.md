Example for Configuring Basic RSTP Functions
============================================

This example shows how to configure basic Rapid Spanning Tree Protocol (RSTP) functions.

#### Networking Requirements

On a complex network, loops are inevitable. With the requirement for network redundancy backup, network designers tend to deploy multiple physical links between two devices, one of which is the master and the others are the backup. In such a situation, loops are prone to happen, potentially leading to broadcast storms and flapping MAC address entries on network devices.

RSTP can be deployed on a network to eliminate loops by blocking some ports, and it is developed to implement the rapid convergence based on STP but outperforms STP. On the network shown in [Figure 1](#EN-US_TASK_0172363571__fig_dc_vrp_stp_cfg_0034_01), after DeviceA, DeviceB, DeviceC, and DeviceD running RSTP discover loops on the network by exchanging information with each other, they trim the ring topology into a loop-free tree topology by blocking a certain port. In this manner, replication and circular propagation of packets are prevented on the network and the devices are released from processing duplicated packets, thereby improving their processing performance.

**Figure 1** Configuring basic RSTP functions![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/1, GE0/1/2, and GE0/1/3, respectively.


  
![](images/fig_dc_vrp_stp_cfg_0034_01.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic RSTP functions, including:
   1. Configure the RSTP mode for the ring network.
   2. Configure primary and secondary root bridges.
   3. Set path costs for ports in each MSTI to block certain ports.
   4. Enable RSTP to eliminate loops, including:
      * Enable RSTP globally.
      * Enable RSTP on all the interfaces except the interfaces connected to terminals.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      RSTP is not required on the interfaces connected to terminals because these interfaces do not need to participate in RSTP calculation.
      
      By default, RSTP is enabled on a Layer 2 interface.
2. Configure RSTP protection functions, for example, root protection on a designated port of a root bridge in each MSTI.


#### Data Preparation

To complete the configuration, you need the following data.

* GE interface numbers, as shown in [Figure 1](#EN-US_TASK_0172363571__fig_dc_vrp_stp_cfg_0034_01)
* Primary root bridge DeviceA and secondary root bridge DeviceD
* Path cost of a port to be blocked (20000 is used in this example)


#### Procedure

1. Configure basic RSTP functions.
   
   
   1. Configure the RSTP mode for the devices on the ring network.
      
      # Configure the RSTP mode on DeviceA.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname DeviceA
      ```
      ```
      [*DeviceA] stp mode rstp
      ```
      ```
      [*DeviceA] commit
      ```
      
      # Configure the RSTP mode on DeviceB.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname DeviceB
      ```
      ```
      [*DeviceB] stp mode rstp
      ```
      ```
      [*DeviceB] commit
      ```
      
      # Configure the RSTP mode on DeviceC.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname DeviceC
      ```
      ```
      [*DeviceC] stp mode rstp
      ```
      ```
      [*DeviceC] commit
      ```
      
      # Configure the RSTP mode on DeviceD.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname DeviceD
      ```
      ```
      [*DeviceD] stp mode rstp
      ```
      ```
      [*DeviceD] commit
      ```
   2. Configure primary and secondary root bridges.
      
      # Configure DeviceA as a primary root bridge.
      
      ```
      [~DeviceA] stp root primary
      ```
      ```
      [*DeviceA] commit
      ```
      
      # Configure DeviceD as a secondary root bridge.
      
      ```
      [~DeviceD] stp root secondary
      ```
      ```
      [*DeviceD] commit
      ```
   3. Set path costs for ports in each spanning tree to block certain ports.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * The values of path costs depend on path cost calculation methods. Use the Huawei proprietary calculation method as an example to set the path costs of the ports to be blocked to 20000.
      * All devices on a network must use the same path cost calculation method.
      
      # On DeviceA, configure the path cost calculation method as the Huawei proprietary method.
      
      ```
      [~DeviceA] stp pathcost-standard legacy
      ```
      ```
      [*DeviceA] commit
      ```
      
      # On DeviceB, configure the path cost calculation method as the Huawei proprietary method.
      
      ```
      [~DeviceB] stp pathcost-standard legacy
      ```
      ```
      [*DeviceB] commit
      ```
      
      # On DeviceC, configure the path cost calculation method as the Huawei proprietary method and set the path cost of GE 0/1/1 to 20000.
      
      ```
      [~DeviceC] stp pathcost-standard legacy
      ```
      ```
      [*DeviceC] interface gigabitethernet 0/1/1
      ```
      ```
      [*DeviceC-GigabitEthernet0/1/1] stp cost 20000
      ```
      ```
      [*DeviceC-GigabitEthernet0/1/1] commit
      ```
      ```
      [~DeviceC-GigabitEthernet0/1/1] quit
      ```
      
      # On DeviceD, configure the path cost calculation method as the Huawei proprietary method.
      
      ```
      [~DeviceD] stp pathcost-standard legacy
      ```
      ```
      [*DeviceD] commit
      ```
   4. Enable RSTP to eliminate loops.
      
      * Disable RSTP on interfaces connected to PCs.
        
        # Disable RSTP on GE 0/1/2 on DeviceB.
        
        ```
        [~DeviceB] interface gigabitethernet 0/1/2
        ```
        ```
        [~DeviceB-GigabitEthernet0/1/2] stp disable
        ```
        ```
        [*DeviceB-GigabitEthernet0/1/2] commit
        ```
        ```
        [~DeviceB-GigabitEthernet0/1/2] quit
        ```
        
        # Disable RSTP on GE 0/1/2 on DeviceC.
        
        ```
        [~DeviceC] interface gigabitethernet 0/1/2
        ```
        ```
        [~DeviceC-GigabitEthernet0/1/2] stp disable
        ```
        ```
        [*DeviceC-GigabitEthernet0/1/2] commit
        ```
        ```
        [~DeviceC-GigabitEthernet0/1/2] quit
        ```
      * Enable RSTP globally.
        
        # Enable RSTP globally on DeviceA.
        
        ```
        [~DeviceA] stp enable
        ```
        ```
        [*DeviceA] commit
        ```
        
        # Enable RSTP globally on DeviceB.
        
        ```
        [~DeviceB] stp enable
        ```
        ```
        [*DeviceB] commit
        ```
        
        # Enable RSTP globally on DeviceC.
        
        ```
        [~DeviceC] stp enable
        ```
        ```
        [*DeviceC] commit
        ```
        
        # Enable RSTP globally on DeviceD.
        
        ```
        [~DeviceD] stp enable
        ```
        ```
        [*DeviceD] commit
        ```
      * Enable RSTP on all the interfaces except the interfaces connected to terminals.
        
        # Enable RSTP on GE 0/1/1 and GE 0/1/2 on DeviceA.
        
        ```
        [~DeviceA] interface gigabitethernet 0/1/1
        ```
        ```
        [~DeviceA-GigabitEthernet0/1/1] undo shutdown
        ```
        ```
        [*DeviceA-GigabitEthernet0/1/1] portswitch
        ```
        ```
        [*DeviceA-GigabitEthernet0/1/1] stp enable
        ```
        ```
        [*DeviceA-GigabitEthernet0/1/1] quit
        ```
        ```
        [*DeviceA] interface gigabitethernet 0/1/2
        ```
        ```
        [*DeviceA-GigabitEthernet0/1/2] undo shutdown
        ```
        ```
        [*DeviceA-GigabitEthernet0/1/2] portswitch
        ```
        ```
        [*DeviceA-GigabitEthernet0/1/2] stp enable
        ```
        ```
        [*DeviceA-GigabitEthernet0/1/2] commit
        ```
        ```
        [~DeviceA-GigabitEthernet0/1/2] quit
        ```
        
        # Enable RSTP on GE 0/1/1 and GE 0/1/3 on DeviceB.
        
        ```
        [~DeviceB] interface gigabitethernet 0/1/1
        ```
        ```
        [~DeviceB-GigabitEthernet0/1/1] undo shutdown
        ```
        ```
        [*DeviceB-GigabitEthernet0/1/1] portswitch
        ```
        ```
        [*DeviceB-GigabitEthernet0/1/1] stp enable
        ```
        ```
        [*DeviceB-GigabitEthernet0/1/1] quit
        ```
        ```
        [*DeviceB] interface gigabitethernet 0/1/3
        ```
        ```
        [*DeviceB-GigabitEthernet0/1/3] undo shutdown
        ```
        ```
        [*DeviceB-GigabitEthernet0/1/3] portswitch
        ```
        ```
        [*DeviceB-GigabitEthernet0/1/3] stp enable
        ```
        ```
        [*DeviceB-GigabitEthernet0/1/3] commit
        ```
        ```
        [~DeviceB-GigabitEthernet0/1/3] quit
        ```
        
        # Enable RSTP on GE 0/1/1 and GE 0/1/3 on DeviceC.
        
        ```
        [~DeviceC] interface gigabitethernet 0/1/1
        ```
        ```
        [~DeviceC-GigabitEthernet0/1/1] undo shutdown
        ```
        ```
        [*DeviceC-GigabitEthernet0/1/1] portswitch
        ```
        ```
        [*DeviceC-GigabitEthernet0/1/1] stp enable
        ```
        ```
        [*DeviceC-GigabitEthernet0/1/1] quit
        ```
        ```
        [*DeviceC] interface gigabitethernet 0/1/3
        ```
        ```
        [*DeviceC-GigabitEthernet0/1/3] undo shutdown
        ```
        ```
        [*DeviceC-GigabitEthernet0/1/3] portswitch
        ```
        ```
        [*DeviceC-GigabitEthernet0/1/3] stp enable
        ```
        ```
        [*DeviceC-GigabitEthernet0/1/3] commit
        ```
        ```
        [~DeviceC-GigabitEthernet0/1/3] quit
        ```
        
        # Enable RSTP on GE 0/1/1 and GE 0/1/2 on DeviceD.
        
        ```
        [~DeviceD] interface gigabitethernet 0/1/1
        ```
        ```
        [~DeviceD-GigabitEthernet0/1/1] undo shutdown
        ```
        ```
        [*DeviceD-GigabitEthernet0/1/1] portswitch
        ```
        ```
        [*DeviceD-GigabitEthernet0/1/1] stp enable
        ```
        ```
        [*DeviceD-GigabitEthernet0/1/1] quit
        ```
        ```
        [*DeviceD] interface gigabitethernet 0/1/2
        ```
        ```
        [*DeviceD-GigabitEthernet0/1/2] undo shutdown
        ```
        ```
        [*DeviceD-GigabitEthernet0/1/2] portswitch
        ```
        ```
        [*DeviceD-GigabitEthernet0/1/2] stp enable
        ```
        ```
        [*DeviceD-GigabitEthernet0/1/2] commit
        ```
        ```
        [~DeviceD-GigabitEthernet0/1/2] quit
        ```
2. Configure RSTP protection functions, for example, root protection on a designated port of a root bridge in each MSTI.
   
   
   
   # Enable root protection on GE 0/1/1 on DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] stp root-protection
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
   
   # Enable root protection on GE 0/1/2 on DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] stp root-protection
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] quit
   ```
3. Verify the configuration.
   
   
   
   After the previous configurations, run the following commands to verify the configuration when the network is stable:
   
   # Run the [**display stp brief**](cmdqueryname=display+stp+brief) command on DeviceA to view the interface status and protection type. The displayed information is as follows:
   
   ```
   [~DeviceA] display stp brief
    MSTID  Port                        Role  STP State     Protection
      0    GigabitEthernet0/1/1        DESI  FORWARDING    ROOT
      0    GigabitEthernet0/1/2        DESI  FORWARDING    ROOT
   ```
   
   After DeviceA is configured as a root bridge, GE 0/1/2 and GE 0/1/1 connected to DeviceB and DeviceD respectively are elected as designated ports in spanning tree calculation. The root protection function is enabled on the designated ports.
   
   # Run the **display stp interface gigabitethernet 0/1/1 brief** command on DeviceB to view status of GE 0/1/1. The displayed information is as follows:
   
   ```
   [~DeviceB] display stp interface gigabitethernet 0/1/1 brief
    MSTID  Port                        Role  STP State     Protection
      0    GigabitEthernet0/1/1        DESI  FORWARDING    NONE      
   ```
   
   GE 0/1/1 is elected as a designated port in spanning tree calculation and is in the Forwarding state.
   
   # Run the **display stp interface gigabitethernet 0/1/3 brief** command on DeviceC to view status of GE 0/1/3. The displayed information is as follows:
   
   ```
   [~DeviceC] display stp interface gigabitethernet 0/1/3 brief
    MSTID  Port                        Role  STP State     Protection
      0    GigabitEthernet0/1/3        ROOT  FORWARDING    NONE      
   ```
   
   GE 0/1/3 is elected as a designated port in spanning tree calculation and is in the Forwarding state.
   
   # Run the [**display stp**](cmdqueryname=display+stp) command on DeviceD to view detailed information about the interface status. The displayed information is as follows:
   
   ```
   [~DeviceD] display stp
   ```
   ```
   -------[CIST Global Info][Mode RSTP]-------
   CIST Bridge         :4096 .00e0-fc12-3456
   Bridge Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
   CIST Root/ERPC      :0    .00e0-fc12-3456 / 20000
   CIST RegRoot/IRPC   :4096 .00e0-fc12-3456 / 0
   CIST RootPortId     :128.1
   BPDU-Protection     :Disabled
   CIST Root Type      :SECONDARY root
   TC or TCN received  :4
   TC count per hello  :0
   STP Converge Mode   :Normal
   Time since last TC :0 days 0h:5m:44s
   ----[Port1(GigabitEthernet0/1/1)][FORWARDING]----
    Port Protocol       :enabled
    Port Role           :Root Port
    Port Priority       :128
    Port Cost(Dot1T )   :Config=auto / Active=20000
    Desg. Bridge/Port   :0.00e0-fc12-3456 / 128.1
    Port Edged          :Config=default / Active=disabled
    Point-to-point      :Config=auto / Active=true
    Transit Limit       :147 packets/hello-time
    Protection Type     :None
    Port Stp Mode       :RSTP
    Port Protocol Type  :Config=auto / Active=dot1s
    BPDU Encapsulation  :Config=stp / Active=stp
    PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 0
    TC or TCN send  :4
    TC or TCN received  :2
    BPDU Sent           :5
             TCN: 0, Config: 0, RST: 5, MST: 0
    BPDU Received       :177
             TCN: 0, Config: 0, RST: 177, MST: 0
   ----[Port2(GigabitEthernet0/1/2)][FORWARDING]----
    Port Protocol       :enabled
    Port Role           :Designated Port
    Port Priority       :128
    Port Cost(Dot1T )   :Config=auto / Active=20000
    Desg. Bridge/Port   :4096.00e0-fc12-3456 / 128.2
    Port Edged          :Config=default / Active=disabled
    Point-to-point      :Config=auto / Active=true
    Transit Limit       :147 packets/hello-time
    Protection Type     :None
    Port Stp Mode       :RSTP
    Port Protocol Type  :Config=auto / Active=dot1s
    BPDU Encapsulation  :Config=stp / Active=stp
    PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20
    TC or TCN send  :2
    TC or TCN received  :2
    BPDU Sent           :165
             TCN: 0, Config: 0, RST: 165, MST: 0
    BPDU Received       :2
             TCN: 0, Config: 0, RST: 2, MST: 0
   ```

#### Configuration Files

* Configuration file of DeviceA
  
  ```
  #
   sysname DeviceA                                                                
  #                                                                               
   stp mode rstp                                                                  
   stp instance 0 root primary                                                    
   stp pathcost-standard legacy                                                   
   stp enable                                                                     
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   portswitch
   undo shutdown
   stp root-protection                                                            
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   portswitch
   undo shutdown
   stp root-protection                                                            
  #
  return
  ```
* Configuration file of DeviceB
  
  ```
  #                                                                               
   sysname DeviceB                                                                
  #                                                                               
   stp mode rstp                                                                  
   stp pathcost-standard legacy                                                   
   stp enable                                                                     
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   portswitch
   undo shutdown
   stp enable                                                            
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   stp disable                                                                    
  #                                                                               
  interface GigabitEthernet0/1/3                                                  
   portswitch
   undo shutdown
   stp enable                                                            
  #                                                                               
  return                    
  ```
* Configuration file of DeviceC
  
  ```
  #                                                                               
   sysname DeviceC                                                                
  #                                                                               
   stp mode rstp                                                                  
   stp pathcost-standard legacy                                                   
   stp enable                                                                     
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   stp instance 0 cost 20000                                                      
   portswitch
   undo shutdown
   stp enable                                                            
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   stp disable                                                                    
  #                                                                               
  interface GigabitEthernet0/1/3                                                  
   portswitch
   undo shutdown
   stp enable                                                            
  #                                                                               
  return           
  
  ```
* Configuration file of DeviceD
  
  ```
  #                                                                               
   sysname DeviceD                                                                
  #                                                                               
   stp mode rstp                                                                  
   stp instance 0 root secondary                                                  
   stp pathcost-standard legacy                                                   
   stp enable                                                                     
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown
   portswitch
   stp enable                                                                     
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   undo shutdown
   portswitch
   stp enable                                                                     
  #                                                                               
  return                        
  
  ```