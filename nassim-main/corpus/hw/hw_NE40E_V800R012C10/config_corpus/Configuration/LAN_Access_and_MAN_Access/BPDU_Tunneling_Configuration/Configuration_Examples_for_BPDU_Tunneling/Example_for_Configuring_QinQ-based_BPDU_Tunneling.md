Example for Configuring QinQ-based BPDU Tunneling
=================================================

In this example, provider edges (PEs) function as aggregation devices. When the PEs are connected to a large number of user networks, you can configure 802.1Q in 802.1Q (QinQ)-based bridge protocol data unit (BPDU) tunneling. QinQ-based BPDU tunneling enables the customer edges (CEs) to allocate different virtual local area network (VLAN) tags to BPDUs and enables the PEs to allocate different outer VLAN tags to the BPDUs based on the CE VLAN IDs. QinQ-based BPDU tunneling differentiates BPDUs from different user networks and saves VLAN ID resources for the carrier network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172363732__fig_dc_vrp_bpdu-tunnel_cfg_002601), the CEs are connected to the PEs, BPDUs sent by CE1 and CE2 to the PEs carry the VLAN ID 100, and BPDUs sent by CE3 and CE4 to the PEs carry the VLAN ID 200. In this situation, you can configure QinQ-based BPDU tunneling on the PEs to achieve the following:

* The devices in VLAN 100 can complete the spanning tree calculation together.
* The devices in VLAN 200 can complete the spanning tree calculation together.

To save public VLAN ID resources, configure VLAN stacking on the PEs. This configuration enables the PEs to add the outer VLAN ID 10 to BPDUs carrying VLAN ID 100 and VLAN ID 200 received from the CEs. Therefore, each BPDU transmitted over the carrier network carries two VLAN tags.

This example describes the configuration on devices with different roles.

* The CEs are configured as customers. The default well-known destination MAC address of BPDUs sent by the CEs is 0180-C200-0000.
* The PEs are configured as providers. The default well-known destination MAC address of BPDUs sent by the PEs is 0180-C200-0008.

**Figure 1** Networking for configuring QinQ-based BPDU tunneling![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example are GE 0/1/1, GE 0/1/2, GE 0/1/3, respectively.


  
![](images/fig_dc_vrp_bpdu-tunnel_cfg_002601.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the spanning tree calculation on the CEs and PEs.
2. Configure the CEs to add specified VLAN IDs to BPDUs before sending them to the PEs.
3. Disable the spanning tree calculation on the PE interfaces that are connected to the CEs, and configure the PEs as providers to transparently transmit BPDUs.
4. Enable VLAN stacking on the Layer 2 interfaces of the PEs so that the PEs add the outer VLAN ID 10 to BPDUs with the specified VLAN IDs received from the CEs before forwarding them over the carrier network.

#### Data Preparation

To complete the configuration, you need the following data:

* Inner VLAN IDs of BPDUs sent by the CEs to the PEs
* Outer VLAN ID that the PEs add to received BPDUs
* IDs of the VLANs to which the interfaces on the PEs and CEs belong

#### Procedure

1. Switch the interfaces on the PEs and CEs that transmit BPDUs to Layer 2 interfaces.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If an interface is a Layer 2 interface, skip this step.
   
   Run the [**portswitch**](cmdqueryname=portswitch) command to switch all the PE and CE interfaces in [Figure 1](#EN-US_TASK_0172363732__fig_dc_vrp_bpdu-tunnel_cfg_002601) to Layer 2 interfaces. For configuration details, see "Configuration Files" in this section.
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
3. Configure CE1 and CE2 to add the VLAN ID 100 to BPDUs before sending them to the PEs. Configure CE3 and CE4 to add the VLAN ID 200 to BPDUs before sending them to the PEs.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] vlan 100
   ```
   ```
   [*CE1-vlan100] commit
   ```
   ```
   [~CE1-vlan100] quit
   ```
   ```
   [~CE1] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE1-GigabitEthernet0/1/1] port trunk allow-pass vlan 100
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] stp bpdu vlan 100
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CE1-GigabitEthernet0/1/1] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] vlan 100
   ```
   ```
   [*CE2-vlan100] commit
   ```
   ```
   [~CE2-vlan100] quit
   ```
   ```
   [~CE2] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE2-GigabitEthernet0/1/1] port trunk allow-pass vlan 100
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] stp bpdu vlan 100
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CE2-GigabitEthernet0/1/1] quit
   ```
   
   # Configure CE3.
   
   ```
   [~CE3] vlan 200
   ```
   ```
   [*CE3-vlan200] commit
   ```
   ```
   [~CE3-vlan200] quit
   ```
   ```
   [~CE3] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE3-GigabitEthernet0/1/1] port trunk allow-pass vlan 200
   ```
   ```
   [*CE3-GigabitEthernet0/1/1] stp bpdu vlan 200
   ```
   ```
   [*CE3-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CE3-GigabitEthernet0/1/1] quit
   ```
   
   # Configure CE4.
   
   ```
   [~CE4] vlan 200
   ```
   ```
   [*CE4-vlan200] commit
   ```
   ```
   [~CE4-vlan200] quit
   ```
   ```
   [~CE4] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE4-GigabitEthernet0/1/1] port trunk allow-pass vlan 200
   ```
   ```
   [*CE4-GigabitEthernet0/1/1] stp bpdu vlan 200
   ```
   ```
   [*CE4-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CE4-GigabitEthernet0/1/1] quit
   ```
4. Configure the PEs as providers.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bpdu-tunnel stp bridge role provider
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bpdu-tunnel stp bridge role provider
   ```
   ```
   [*PE2] commit
   ```
5. Configure VLAN stacking on the PEs so that the PEs add the outer VLAN ID 10 to BPDUs with the VLAN IDs 100 and 200 received from the CEs before forwarding them over the carrier network.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] vlan 10
   ```
   ```
   [*PE1-Vlan10] commit
   ```
   ```
   [~PE1-Vlan10] quit
   ```
   ```
   [~PE1] interface gigabitethernet 0/1/3
   ```
   ```
   [~PE1-GigabitEthernet0/1/3] port trunk allow-pass vlan 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] port vlan-stacking vlan 100 stack-vlan 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] stp disable
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/2
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] port vlan-stacking vlan 200 stack-vlan 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] stp disable
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [*PE2] vlan 10
   ```
   ```
   [*PE2-Vlan10] commit
   ```
   ```
   [~PE2-Vlan10] quit
   ```
   ```
   [~PE2] interface gigabitethernet 0/1/3
   ```
   ```
   [~PE2-GigabitEthernet0/1/3] port trunk allow-pass vlan 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/3] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] port vlan-stacking vlan 100 stack-vlan 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] stp disable
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/2
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] port vlan-stacking vlan 200 stack-vlan 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] stp disable
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE2] commit
   ```
6. Verify the configuration.
   
   
   
   Run the [**display stp**](cmdqueryname=display+stp) command on CE1 and CE2 to view the root bridge selected by the Multiple Spanning Tree Protocol (MSTP). The command output shows that CE1 and CE2 have completed the spanning tree calculation and that GE0/1/1 on CE1 is the **Root** interface and GE0/1/1 on CE2 is the **Designated** interface.
   
   ```
   [~CE1] display stp
   ```
   ```
   -------[CIST Global Info] [Mode MSTP] -------
   CIST Bridge         :32768.00e0-fc9f-3257
   Bridge Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
   Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 19
   CIST Root/ERPC      :32768.00e0-fc12-3458 / 199999
   CIST RegRoot/IRPC   :32768.00e0-fc12-3456 / 0
   CIST RootPortId     :128.82
   BPDU-Protection     :disabled
   TC or TCN received  :6
   TC count per hello  :0
   STP Converge Mode   :Normal
   Time since last TC received :0 days 2h:24m:36s
   Number of TC        :2
   Last  TC  occurred  :GigabitEthernet0/1/1
   ----[Port1(GigabitEthernet0/1/1)] [FORWARDING] ----
   Port Protocol       :Enabled
    Port Role           :CIST Root Port
    Port Priority       :128
    Port Cost(Dot1T )   :Config=auto / Active=200000000
    Desg. Bridge/Port   :32768.00e0-fc9a-4315 / 128.82
    Port Edged          :Config=disabled / Active=disabled
    Point-to-point      :Config=auto / Active=true
    Transit Limit       :147 packets/hello-time
    Protection Type     :None
    Port STP Mode       :MSTP
     Port Protocol Type  :Config=auto / Active=dot1s
    BPDU Encapsulation  :Config=stp / Active=stp
    PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20
    TC or TCN send      :2
    TC or TCN received  :0
    BPDU Sent           :7
             TCN: 0, Config: 0, RST: 0, MST: 7
    BPDU Received       :105
             TCN: 0, Config: 0, RST: 0, MST: 105
   ```
   ```
   [~CE2] display stp
   ```
   ```
   -------[CIST Global Info] [Mode MSTP] -------
   CIST Bridge         :32768.00e0-fc9a-4315
   Bridge Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
   Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 19
   CIST Root/ERPC      :32768.00e0-fc12-3458 / 0
   CIST RegRoot/IRPC   :32768.00e0-fc12-3458 / 0
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
    Desg. Bridge/Port   :32768.00e0-fc9a-4315 / 128.82
    Port Edged          :Config=disabled / Active=disabled
    Point-to-point      :Config=auto / Active=true
    Transit Limit       :3 packets/hello-time
    Protection Type     :None
    Port STP Mode       :MSTP
    Port Protocol Type  :Config=auto / Active=dot1s
    BPDU Encapsulation  :Config=stp / Active=stp
    PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 19
    TC or TCN send      :0
    TC or TCN received  :0
    BPDU Sent           :82
             TCN: 0, Config: 0, RST: 0, MST: 82
    BPDU Received       :0
             TCN: 0, Config: 0, RST: 0, MST: 0
   ```
   
   Run the **display stp** command on CE3 and CE4 to view the root bridge selected by MSTP. The command output shows that CE3 and CE4 have completed the spanning tree calculation. GE0/1/1 on CE3 is the **Root** interface and GE0/1/1 on CE4 is the **Designated** interface.
   
   ```
   [~CE3] display stp
   ```
   ```
   -------[CIST Global Info][Mode MSTP]-------
   CIST Bridge         :32768.00e0-fc12-3459
   Bridge Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
   Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 19
   CIST Root/ERPC      :32768.00e0-fc12-3457 / 199999
   CIST RegRoot/IRPC   :32768.00e0-fc12-3459 / 0
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
    Transit Limit       :3 packets/hello-time
    Protection Type     :None
    Port STP Mode       :MSTP
    Port Protocol Type  :Config=auto / Active=dot1s
    BPDU Encapsulation  :Config=stp / Active=stp
    PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20
    TC or TCN send      :2
    TC or TCN received  :0
    BPDU Sent           :7
             TCN: 0, Config: 0, RST: 0, MST: 7
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
    Transit Limit       :3 packets/hello-time
    Protection Type     :None
    Port STP Mode       :MSTP
    Port Protocol Type  :Config=auto / Active=dot1s
    BPDU Encapsulation  :Config=stp / Active=stp
    PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20
    TC or TCN send      :2
    TC or TCN received  :0
    BPDU Sent           :7
             TCN: 0, Config: 0, RST: 0, MST: 7
    BPDU Received       :105
             TCN: 0, Config: 0, RST: 0, MST: 105
   ```
   
   Run the [**display vlan**](cmdqueryname=display+vlan) command on the PEs to view VLAN stacking information.
   
   The command output on PE1 is used as an example.
   
   ```
   [*PE1] display vlan 10 verbose
   ```
   ```
     VLAN ID      : 10
   ```
   ```
     VLAN Type    : Common
   ```
   ```
     Description  : VLAN 0010
   ```
   ```
     Status       : Enable
   ```
   ```
     Broadcast    : Enable
   ```
   ```
     MAC learning : Enable
   ```
   ```
     Statistics   : Disable
   ```
   ```
     ----------------
   ```
   ```
     Tagged     Port: GigabitEthernet0/1/3
   ```
   ```
     ----------------
   ```
   ```
     QinQ-stack Port: GigabitEthernet0/1/1       GigabitEthernet0/1/2
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
   vlan batch 100
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
   port trunk allow-pass vlan 100
  ```
  ```
   stp bpdu vlan 100
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
   vlan batch 100
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
   port trunk allow-pass vlan 100
  ```
  ```
   stp bpdu vlan 100
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
   vlan batch 200
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
   port trunk allow-pass vlan 200
  ```
  ```
   stp bpdu vlan 200
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
   vlan batch 200
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
   port trunk allow-pass vlan 200
  ```
  ```
   stp bpdu vlan 200
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
   vlan batch 100
  ```
  ```
  #
  ```
  ```
   bpdu-tunnel stp bridge role provider
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
   port vlan-stacking vlan 100 stack-vlan 10
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
   port vlan-stacking vlan 200 stack-vlan 10
  ```
  ```
   stp disable
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
   port trunk allow-pass vlan 10
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
   vlan batch 100
  ```
  ```
  #
  ```
  ```
   bpdu-tunnel stp bridge role provider
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
   port vlan-stacking vlan 100 stack-vlan 10
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
   port vlan-stacking vlan 200 stack-vlan 10
  ```
  ```
   stp disable
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
   port trunk allow-pass vlan 10
  ```
  ```
  #
  ```
  ```
  return
  ```