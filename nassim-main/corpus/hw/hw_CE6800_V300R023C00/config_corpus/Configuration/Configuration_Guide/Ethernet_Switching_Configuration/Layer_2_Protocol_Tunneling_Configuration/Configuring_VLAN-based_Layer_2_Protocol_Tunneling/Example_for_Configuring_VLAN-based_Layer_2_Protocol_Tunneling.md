Example for Configuring VLAN-based Layer 2 Protocol Tunneling
=============================================================

Example for Configuring VLAN-based Layer 2 Protocol Tunneling

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001159483960__fig_dc_cfg_l2pt_001901), CEs are edge devices on user networks in different locations of enterprises, and PE1 and PE2 are edge devices on an ISP network. VLAN 100 and VLAN 200 belong to Layer 2 networks of different users and are connected through the ISP network. STP is run on the Layer 2 networks to prevent loops. The enterprises require that STP be run only on their respective user networks to generate correct spanning trees.

* Devices in VLAN 100 can complete the spanning tree calculation together.
* Devices in VLAN 200 can complete the spanning tree calculation together.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.

**Figure 1** Network diagram of configuring VLAN-based Layer 2 protocol tunneling  
![](figure/en-us_image_0000001204643947.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure STP on CEs to prevent loops on Layer 2 networks.
2. Configure CEs to send STP BPDUs with specified VLAN IDs to PEs so that STP calculation is performed independently in VLAN 100 and VLAN 200.
3. Configure VLAN-based Layer 2 protocol tunneling on PEs so that STP BPDUs are not sent to the CPUs of PEs for processing.

#### Procedure

1. Enable STP on CEs.
   
   
   
   # Configure CE1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname CE1
   [*HUAWEI] commit
   [~CE1] stp enable
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname CE2
   [*HUAWEI] commit
   [~CE2] stp enable
   [*CE2] commit
   ```
   
   # Configure CE3.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname CE3
   [*HUAWEI] commit
   [~CE3] stp enable
   [*CE3] commit
   ```
   
   # Configure CE4.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname CE4
   [*HUAWEI] commit
   [~CE4] stp enable
   [*CE4] commit
   ```
2. Configure CE1 and CE2 to send STP BPDUs with VLAN ID 100 to PEs. Configure CE3 and CE4 to send STP BPDUs with VLAN ID 200 to PEs.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] vlan 100
   [*CE1-vlan100] quit
   [*CE1] interface 100ge 1/0/1
   [*CE1-100GE1/0/1] portswitch
   [*CE1-100GE1/0/1] port link-type trunk
   [*CE1-100GE1/0/1] port trunk allow-pass vlan 100
   [*CE1-100GE1/0/1] stp bpdu vlan 100
   [*CE1-100GE1/0/1] quit
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] vlan 100
   [*CE2-vlan100] quit
   [*CE2] interface 100ge 1/0/1
   [*CE2-100GE1/0/1] portswitch
   [*CE2-100GE1/0/1] port link-type trunk
   [*CE2-100GE1/0/1] port trunk allow-pass vlan 100
   [*CE2-100GE1/0/1] stp bpdu vlan 100
   [*CE2-100GE1/0/1] quit
   [*CE2] commit
   ```
   
   # Configure CE3.
   
   ```
   [~CE3] vlan 200
   [*CE3-vlan200] quit
   [*CE3] interface 100ge 1/0/1
   [*CE3-100GE1/0/1] portswitch
   [*CE3-100GE1/0/1] port link-type trunk
   [*CE3-100GE1/0/1] port trunk allow-pass vlan 200
   [*CE3-100GE1/0/1] stp bpdu vlan 200
   [*CE3-100GE1/0/1] quit
   [*CE3] commit
   ```
   
   # Configure CE4.
   
   ```
   [~CE4] vlan 200
   [*CE4-vlan200] quit
   [*CE4] interface 100ge 1/0/1
   [*CE4-100GE1/0/1] portswitch
   [*CE4-100GE1/0/1] port link-type trunk
   [*CE4-100GE1/0/1] port trunk allow-pass vlan 200
   [*CE4-100GE1/0/1] stp bpdu vlan 200
   [*CE4-100GE1/0/1] quit
   [*CE4] commit
   ```
3. Configure interfaces on PEs to transparently transmit STP BPDUs from CEs to the remote device.
   
   
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [~PE1] vlan 100
   [*PE1-vlan100] quit
   [*PE1] vlan 200
   [*PE1-vlan200] quit
   [*PE1] interface 100ge 1/0/2
   [*PE1-100GE1/0/2] portswitch
   [*PE1-100GE1/0/2] port link-type trunk
   [*PE1-100GE1/0/2] port trunk allow-pass vlan 100
   [*PE1-100GE1/0/2] l2protocol-tunnel stp vlan 100
   [*PE1-100GE1/0/2] quit
   [*PE1] interface 100ge 1/0/3
   [*PE1-100GE1/0/3] portswitch
   [*PE1-100GE1/0/3] port link-type trunk
   [*PE1-100GE1/0/3] port trunk allow-pass vlan 200
   [*PE1-100GE1/0/3] l2protocol-tunnel stp vlan 200
   [*PE1-100GE1/0/3] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE2
   [~PE2] vlan 100
   [*PE2-vlan100] quit
   [*PE2] vlan 200
   [*PE2-vlan200] quit
   [*PE2] interface 100ge 1/0/2
   [*PE2-100GE1/0/2] portswitch
   [*PE2-100GE1/0/2] port link-type trunk
   [*PE2-100GE1/0/2] port trunk allow-pass vlan 100
   [*PE2-100GE1/0/2] l2protocol-tunnel stp vlan 100
   [*PE2-100GE1/0/2] quit
   [*PE2] interface 100ge 1/0/3
   [*PE2-100GE1/0/3] portswitch
   [*PE2-100GE1/0/3] port link-type trunk
   [*PE2-100GE1/0/3] port trunk allow-pass vlan 200
   [*PE2-100GE1/0/3] l2protocol-tunnel stp vlan 200
   [*PE2-100GE1/0/3] quit
   [*PE2] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the peer device sends non-standard protocol packets, first run the [**l2protocol-tunnel user-defined-protocol**](cmdqueryname=l2protocol-tunnel+user-defined-protocol) *protocol-name* **protocol-mac** *protocol-mac* [ **encap-type** { { **ethernetii** | **snap** } **protocol-type** *protocol-type-value* | **llc dsap** *dsap-value* **ssap** *ssap-value* } ] **group-mac** { *group-mac* | **default-group-mac** } command to define the characteristics of the Layer 2 protocol for transparent transmission and then run the [**l2protocol-tunnel user-defined-protocol**](cmdqueryname=l2protocol-tunnel+user-defined-protocol) *protocol-name* **vlan** { *low-id* [ **to** *high-id* ] } &<1-10> command to enable VLAN-based Layer 2 protocol tunneling on the interface.
4. Configure PEs to replace the MAC addresses of STP BPDUs received from CEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] l2protocol-tunnel stp group-mac 0100-5e00-0011
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] l2protocol-tunnel stp group-mac 0100-5e00-0011
   [*PE2] commit
   ```
5. Set the priority of CE2 and CE4 to 4096.
   
   
   
   # Configure CE2.
   
   ```
   [~CE2] stp priority 4096
   [*CE2] commit
   ```
   
   # Configure CE4.
   
   ```
   [~CE4] stp priority 4096
   [*CE4] commit
   ```
6. Verify the configuration.
   
   
   
   # After the configuration is complete, run the [**display l2protocol-tunnel group-mac**](cmdqueryname=display+l2protocol-tunnel+group-mac) command on PEs to view the protocol name, protocol type, destination multicast MAC address, group MAC address, and priority of Layer 2 protocol packets that are transparently transmitted.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display l2protocol-tunnel group-mac stp
   Protocol         EncapeType ProtocolType Protocol-MAC   Group-MAC      Pri      
   -----------------------------------------------------------------------------   
   stp              llc        dsap 0x42    0180-c200-0000 0100-5e00-0011 0        
                               ssap 0x42                                           
   ```
   
   # Wait for 30s and run the [**display stp brief**](cmdqueryname=display+stp+brief) command on CE1 and CE2 to check the root in the MST region. The command output shows that CE1 and CE2 complete spanning tree calculation. 100GE 1/0/1 is the root port on CE1, and 100GE 1/0/1 is a designated port on CE2.
   
   ```
   [~CE1] display stp brief
   MSTID  Port                        Role  STP State     Protection  Cost       Edged
       0  100GE1/0/1                   ROOT  forwarding    none        2000       disable
   
   ```
   ```
   [~CE2] display stp brief
   MSTID  Port                        Role  STP State     Protection  Cost       Edged
       0  100GE1/0/1                   DESI  forwarding    none        2000       disable
   
   ```
   
   # Wait for 30s and run the [**display stp brief**](cmdqueryname=display+stp+brief) command on CE3 and CE4 to check the root in the MST region. The command output shows that CE3 and CE4 complete spanning tree calculation. 100GE 1/0/1 is the root port on CE3, and 100GE 1/0/1 is a designated port on CE4.
   
   ```
   [~CE3] display stp brief
   MSTID  Port                        Role  STP State     Protection  Cost       Edged
       0  100GE1/0/1                   ROOT  forwarding    none        2000       disable
   
   ```
   ```
   [~CE4] display stp brief
   MSTID  Port                        Role  STP State     Protection  Cost       Edged
       0  100GE1/0/1                   DESI  forwarding    none        2000       disable
   
   ```

#### Configuration Scripts

* CE1
  
  ```
  #
  sysname CE1
  #
  vlan batch 100
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 100
   stp bpdu vlan 100
  #
  return
  ```
* CE2
  
  ```
  #
  sysname CE2
  #
  vlan batch 100
  #
  stp instance 0 priority 4096
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 100
   stp bpdu vlan 100
  #
  return
  ```
* CE3
  
  ```
  #
  sysname CE3
  #
  vlan batch 200
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 200
   stp bpdu vlan 200
  #
  return
  ```
* CE4
  
  ```
  #
  sysname CE4
  #
  vlan batch 200
  #
  stp instance 0 priority 4096
  #
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 200
   stp bpdu vlan 200
  #
  return
  ```
* PE1
  
  ```
  #
  sysname PE1
  #
  vlan batch 100 200
  #
  l2protocol-tunnel stp group-mac 0100-5e00-0011
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 100
   l2protocol-tunnel stp vlan 100
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 200
   l2protocol-tunnel stp vlan 200
  #
  return
  ```
* PE2
  
  ```
  #
  sysname PE2
  #
  vlan batch 100 200
  #
  l2protocol-tunnel stp group-mac 0100-5e00-0011
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 100
   l2protocol-tunnel stp vlan 100
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 200
   l2protocol-tunnel stp vlan 200
  #
  return
  ```