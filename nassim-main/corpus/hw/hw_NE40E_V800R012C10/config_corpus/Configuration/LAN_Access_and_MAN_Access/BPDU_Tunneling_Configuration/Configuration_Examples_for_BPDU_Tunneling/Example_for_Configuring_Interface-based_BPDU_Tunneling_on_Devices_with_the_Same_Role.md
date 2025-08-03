Example for Configuring Interface-based BPDU Tunneling on Devices with the Same Role
====================================================================================

You can configure both customer edges (CEs) and provider edges (PEs) as customers and configure interface-based bridge protocol data unit (BPDU) tunneling on the CEs and PEs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172363726__fig_dc_vrp_bpdu-tunnel_cfg_002401), the CEs are connected to the PEs, and BPDUs exchanged between the CEs must be transparently transmitted by the PEs over the carrier network. Each PE interface is connected to only one CE, and BPDUs sent by the CEs to the PEs must be untagged. In this situation, you can configure interface-based BPDU tunneling.

This example describes the configuration on devices with the same role. In this scenario, the CEs and PEs are both customers, and the default well-known destination MAC address of BPDUs is 0180-C200-0000. The PEs cannot transparently transmit BPDUs sent by the CEs. In this case, you need to enable BPDU tunneling on the PE interfaces.

**Figure 1** Networking for configuring interface-based BPDU tunneling on devices with the same role![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE0/1/1, GE0/1/2, GE0/1/3, respectively.


  
![](images/fig_dc_vrp_bpdu-tunnel_cfg_002401.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the spanning tree calculation on the CEs and PEs.
2. Add the PE interfaces that are connected to the CEs to specified VLANs.
3. Disable the spanning tree calculation on the PE interfaces that are connected to the CEs, and enable BPDU tunneling on these interfaces.
4. Configure the PE interfaces that are connected to the carrier network to allow the passing of BPDUs with the VLAN IDs 100 and 200.

#### Data Preparation

To complete the configuration, you need the following data:

* IDs of the VLANs to which the PE interfaces connected to the CEs belong
* VLAN ID range that the PE interfaces connected to the carrier network allow to pass

#### Procedure

1. Switch the interfaces on the PEs and CEs that transmit BPDUs to Layer 2 interfaces.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If an interface is a Layer 2 interface, skip this step.
   
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
   [~CE1] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE1-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CE1-GigabitEthernet0/1/1] quit
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
   [~CE2] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE2-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CE2-GigabitEthernet0/1/1] quit
   ```
   
   # Configure CE3.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE3
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE3] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE3-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE3-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE3-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CE3-GigabitEthernet0/1/1] quit
   ```
   
   # Configure CE4.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE4
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE4] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE4-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE4-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE4-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CE4-GigabitEthernet0/1/1] quit
   ```
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE1] interface gigabitethernet 0/1/3
   ```
   ```
   [~PE1-GigabitEthernet0/1/3] portswitch
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/2
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE2] interface gigabitethernet 0/1/3
   ```
   ```
   [~PE2-GigabitEthernet0/1/3] portswitch
   ```
   ```
   [*PE2-GigabitEthernet0/1/3] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/3] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/2
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE2] commit
   ```
2. Enable the spanning tree calculation on the CEs and PEs.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] stp enable
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] stp enable
   ```
   ```
   [*CE2] commit
   ```
   
   # Configure CE3.
   
   ```
   [~CE3] stp enable
   ```
   ```
   [*CE3] commit
   ```
   
   # Configure CE4.
   
   ```
   [~CE4] stp enable
   ```
   ```
   [*CE4] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] stp enable
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] stp enable
   ```
   ```
   [*PE2] commit
   ```
3. Configure the PEs to replace the MAC addresses of BPDUs received from the CEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bpdu-tunnel stp group-mac 00e0-fc12-3456
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bpdu-tunnel stp group-mac 00e0-fc12-3456
   ```
   ```
   [*PE2] commit
   ```
4. Add GE0/1/3 of PE1 and PE2 to VLAN 100, add GE0/1/1 of PE1 and PE2 to VLAN 200, and enable BPDU tunneling on these interfaces.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] vlan 100
   ```
   ```
   [*PE1-vlan100] port gigabitethernet 0/1/3
   ```
   ```
   [*PE1-vlan100] commit
   ```
   ```
   [~PE1-vlan100] quit
   ```
   ```
   [~PE1] vlan 200
   ```
   ```
   [*PE1-vlan200] port gigabitethernet 0/1/1
   ```
   ```
   [*PE1-vlan200] commit
   ```
   ```
   [~PE1-vlan200] quit
   ```
   ```
   [~PE1] interface gigabitethernet 0/1/3
   ```
   ```
   [~PE1-GigabitEthernet0/1/3] bpdu-tunnel enable
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] stp disable
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] bpdu-tunnel enable
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] stp disable
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] vlan 100
   ```
   ```
   [*PE2-vlan100] port gigabitethernet 0/1/3
   ```
   ```
   [*PE2-vlan100] commit
   ```
   ```
   [~PE2-vlan100] quit
   ```
   ```
   [~PE2] vlan 200
   ```
   ```
   [*PE2-vlan200] port gigabitethernet 0/1/1
   ```
   ```
   [*PE2-vlan200] commit
   ```
   ```
   [~PE2-vlan200] quit
   ```
   ```
   [~PE2] interface gigabitethernet 0/1/3
   ```
   ```
   [~PE2-GigabitEthernet0/1/3] bpdu-tunnel enable
   ```
   ```
   [*PE2-GigabitEthernet0/1/3] stp disable
   ```
   ```
   [*PE2-GigabitEthernet0/1/3] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] bpdu-tunnel enable
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] stp disable
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE2] commit
   ```
5. Configure the PEs' GE0/1/2 connected to the carrier network to allow the passing of BPDUs with the VLAN IDs 100 and 200.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet 0/1/2
   ```
   ```
   [~PE1-GigabitEthernet0/1/2] port trunk allow-pass vlan 100 200
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/2] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface gigabitethernet 0/1/2
   ```
   ```
   [~PE2-GigabitEthernet0/1/2] port trunk allow-pass vlan 100 200
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] commit
   ```
   ```
   [~PE2-GigabitEthernet0/1/2] quit
   ```
6. Verify the configuration.
   
   
   
   Run the [**display stp**](cmdqueryname=display+stp) command on CE1 and CE2 to view the root bridge selected by the Multiple Spanning Tree Protocol (MSTP). The command output shows that CE1 and CE2 have completed the spanning tree calculation and that GE0/1/1 on CE1 is the **Root** interface and GE0/1/1 on CE2 is the **Designated** interface.
   
   ```
   [~CE1] display stp
   ```
   ```
   -------[CIST Global Info] [Mode MSTP] -------
   CIST Bridge         :32768.00e0-fc12-1213
   Bridge Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
   Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 19
   CIST Root/ERPC      :32768.00e0-fc12-1212 / 199999
   CIST RegRoot/IRPC   :32768.00e0-fc12-1213 / 0
   CIST RootPortId     :128.82
   BPDU-Protection     :disabled
   TC or TCN received  :6
   TC count per hello  :0
   STP Converge Mode   :Normal
   Time since last TC received :0 days 2h:24m:36s
   Number of TC        :1
   Last TC occurred    :GigabitEthernet0/1/1
   ----[Port1(GigabitEthernet0/1/1)] [FORWARDING] ----
    Port Protocol       :enabled
    Port Role           :CIST Root Port
    Port Priority       :128
    Port Cost(Dot1T )   :Config=auto / Active=199999
    Desg. Bridge/Port   :32768.00e0-fc12-1212 / 128.82
    Port Edged          :Config=disabled / Active=disabled
    Point-to-point      :Config=auto / Active=true
    Transit Limit       :3 packets/hello-time
    Protection Type     :None
    Port STP Mode       :MSTP
    Port Protocol Type  :Config=auto / Active=dot1s
    BPDU Encapsulation  :Config=stp / Active=stp
    PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20
    TC or TCN send      :2
    TC or TCN received  :0
    BPDU Sent           :13
             TCN: 0, Config: 0, RST: 0, MST: 13
    BPDU Received       :154
             TCN: 0, Config: 0, RST: 0, MST: 154
   ```
   ```
   [~CE2] display stp
   ```
   ```
   -------[CIST Global Info] [Mode MSTP] -------
   CIST Bridge         :32768.00e0-fc12-1212
   Bridge Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
   Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 19
   CIST Root/ERPC      :32768.00e0-fc12-1212 / 0
   CIST RegRoot/IRPC   :32768.00e0-fc12-1212 / 0
   CIST RootPortId     :0.0
   BPDU-Protection     :disabled
   TC or TCN received  :3
   TC count per hello  :0
   STP Converge Mode   :Normal
   Time since last TC received :0 days 2h:26m:42s
   Number of TC        :1
   Last TC occurred    :GigabitEthernet0/1/1
   ----[Port1(GigabitEthernet0/1/1)] [FORWARDING] ----
    Port Protocol       :enabled
    Port Role           :CIST Designated Port
    Port Priority       :128
    Port Cost(Dot1T )   :Config=auto / Active=199999
    Desg. Bridge/Port   :32768.00e0-fc12-1212 / 128.82
    Port Edged          :Config=disabled / Active=disabled
    Point-to-point      :Config=auto / Active=true
    Transit Limit       :3 packets/hello-time
    Protection Type     :None
    Port STP Mode       :MSTP
    Port Protocol Type  :Config=auto / Active=dot1s
    BPDU Encapsulation  :Config=stp / Active=stp
    PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20
    TC or TCN send      :2
    TC or TCN received  :0
    BPDU Sent           :11
             TCN: 0, Config: 0, RST: 0, MST: 11
    BPDU Received       :105
             TCN: 0, Config: 0, RST: 0, MST: 105
   ```
   
   Run the [**display stp**](cmdqueryname=display+stp) command on CE3 and CE4 to view the root bridge selected by MSTP. The command output shows that CE3 and CE4 have completed the spanning tree calculation. GE0/1/1 on CE3 is the **Root** interface and GE0/1/1 on CE4 is the **Designated** interface.
   
   ```
   [~CE3] display stp
   ```
   ```
   -------[CIST Global Info][Mode MSTP]-------
   CIST Bridge         :32768.00e0-fc12-3458
   Bridge Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
   Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 19
   CIST Root/ERPC      :32768.00e0-fc12-3457 / 199999
   CIST RegRoot/IRPC   :32768.00e0-fc12-3458 / 0
   CIST RootPortId     :128.82
   BPDU-Protection     :disabled
   TC or TCN received  :0
   TC count per hello  :0
   STP Converge Mode   :Normal
   Time since last TC received :0 days 10h:54m:37s   
   Number of TC        :1
   Last TC occurred    :GigabitEthernet0/1/1
   ----[Port1(GigabitEthernet0/1/1)][FORWARDING]----
    Port Protocol       :enabled
    Port Role           :CIST Root Port
    Port Priority       :128
    Port Cost(Dot1T )   :Config=auto / Active=199999
    Desg. Bridge/Port   :32768.00e0-fc12-3457 / 128.82
    Port Edged          :Config=disabled / Active=disabled
    Point-to-point      :Config=auto / Active=true
    Transit Limit       :3 packets/hello time
    Protection Type     :None
    Port STP Mode       :MSTP
    Port Protocol Type  :Config=auto / Active=dot1s
    BPDU Encapsulation  :Config=stp / Active=stp
    PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20
    TC or TCN send      :2
    TC or TCN received  :0
    BPDU Sent           :456
             TCN: 0, Config: 0, RST: 0, MST: 456
    BPDU Received       :105
             TCN: 0, Config: 0, RST: 0, MST: 105
   ```
   ```
   [~CE4] display stp
   ```
   ```
   -------[CIST Global Info][Mode MSTP]-------
   CIST Bridge         :32768.00e0-fc12-3457
   Bridge Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
   Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 19
   CIST Root/ERPC      :32768.00e0-fc12-3457 / 0
   CIST RegRoot/IRPC   :32768.00e0-fc12-3457 / 0
   CIST RootPortId     :0.0
   BPDU-Protection     :disabled
   TC or TCN received  :4
   TC count per hello  :0
   STP Converge Mode   :Normal
   Time since last TC received :0 days 8h:59m:18s
   Number of TC        :1
   Last TC occurred    :GigabitEthernet0/1/1
   ----[Port1(GigabitEthernet0/1/1)][FORWARDING]----
    Port Protocol       :enabled
    Port Role           :CIST Designated Port
    Port Priority       :128
    Port Cost(Dot1T )   :Config=auto / Active=199999
    Desg. Bridge/Port   :32768.00e0-fc12-3457 / 128.82
    Port Edged          :Config=disabled / Active=disabled
    Point-to-point      :Config=auto / Active=true
    Transit Limit       :3 packets/hello time
    Protection Type     :None
    Port STP Mode       :MSTP
    Port Protocol Type  :Config=auto / Active=dot1s
    BPDU Encapsulation  :Config=stp / Active=stp
    PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20
    TC or TCN send      :2
    TC or TCN received  :0
    BPDU Sent           :23
             TCN: 0, Config: 0, RST: 0, MST:23
    BPDU Received       :105
             TCN: 0, Config: 0, RST: 0, MST: 105
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  ```
  ```
   sysname CE1
  ```
  ```
  #
  ```
  ```
  stp enable
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
   portswitch
  ```
  ```
  #
  ```
  ```
  return
  ```
* CE2 configuration file
  
  ```
  #
  ```
  ```
   sysname CE2
  ```
  ```
  #
  ```
  ```
  stp enable
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
   portswitch
  ```
  ```
  #
  ```
  ```
  return
  ```
* CE3 configuration file
  
  ```
  #
  ```
  ```
   sysname CE3
  ```
  ```
  #
  ```
  ```
  stp enable
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
   portswitch
  ```
  ```
  #
  ```
  ```
  return
  ```
* CE4 configuration file
  
  ```
  #
  ```
  ```
   sysname CE4
  ```
  ```
  #
  ```
  ```
  stp enable
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
   portswitch
  ```
  ```
  #
  ```
  ```
  return
  ```
* PE1 configuration file
  
  ```
  #
  ```
  ```
   sysname PE1
  ```
  ```
  #
  ```
  ```
   vlan batch 100 200
  ```
  ```
  #
  ```
  ```
   bpdu-tunnel stp group-mac 00e0-fc12-3456
  ```
  ```
  #
  ```
  ```
   stp enable
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
   portswitch
  ```
  ```
   port default vlan 200
  ```
  ```
   bpdu-tunnel enable
  ```
  ```
   stp disable
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
   portswitch
  ```
  ```
   port trunk allow-pass vlan 100 200
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
   portswitch
  ```
  ```
   port default vlan 100
  ```
  ```
   bpdu-tunnel enable
  ```
  ```
   stp disable
  ```
  ```
  #
  ```
  ```
  return
  ```
* PE2 configuration file
  
  ```
  #
  ```
  ```
   sysname PE2
  ```
  ```
  #
  ```
  ```
   vlan batch 100 200
  ```
  ```
  #
  ```
  ```
   bpdu-tunnel stp group-mac 00e0-fc12-3456
  ```
  ```
  #
  ```
  ```
   stp enable
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
   portswitch
  ```
  ```
   port default vlan 200
  ```
  ```
   bpdu-tunnel enable
  ```
  ```
   stp disable
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
   portswitch
  ```
  ```
   port trunk allow-pass vlan 100 200
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
   portswitch
  ```
  ```
   port default vlan 100
  ```
  ```
   bpdu-tunnel enable
  ```
  ```
   stp disable
  ```
  ```
  #
  ```
  ```
  return
  ```