Example for Configuring Interface-based Layer 2 Protocol Tunneling
==================================================================

Example for Configuring Interface-based Layer 2 Protocol Tunneling

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001204643937__fig_dc_cfg_l2pt_001801), CEs are edge devices on user networks in different locations of an enterprise, and PE1 and PE2 are edge devices on an ISP network. The two networks of the enterprise are Layer 2 networks and are connected through the ISP network. STP is run on the Layer 2 networks to prevent loops. The enterprise requires that STP be run only on the user networks to generate correct spanning trees.

![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


**Figure 1** Network diagram of configuring interface-based Layer 2 protocol tunneling  
![](figure/en-us_image_0000001204882485.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure STP on CEs to prevent loops on Layer 2 networks.
2. Add PE interfaces connected to CEs to specified VLANs so that the PEs can forward packets from the VLANs.
3. Configure interface-based Layer 2 protocol tunneling on PEs so that STP BPDUs are not sent to the CPUs of PEs for processing.

#### Procedure

1. Enable STP on CEs.
   
   
   
   # Configure CE1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname CE1
   [*HUAWEI] commit
   [~CE1] vlan 100
   [*CE1-vlan100] quit
   [*CE1] stp enable
   [*CE1] interface 100ge 1/0/1
   [*CE1-100GE1/0/1] portswitch
   [*CE1-100GE1/0/1] port link-type access
   [*CE1-100GE1/0/1] port default vlan 100
   [*CE1-100GE1/0/1] quit
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname CE2
   [*HUAWEI] commit
   [~CE2] vlan 100
   [*CE2-vlan100] quit
   [*CE2] stp enable
   [*CE2] interface 100ge 1/0/1
   [*CE2-100GE1/0/1] portswitch
   [*CE2-100GE1/0/1] port link-type access
   [*CE2-100GE1/0/1] port default vlan 100
   [*CE2-100GE1/0/1] quit
   [*CE2] commit
   ```
2. Add 100GE 1/0/1 on PE1 and PE2 to VLAN 100 and enable Layer 2 protocol tunneling on the PEs.
   
   
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] stp enable
   [*PE1] commit
   [~PE1] vlan 100
   [*PE1-vlan100] quit
   [*PE1] interface 100ge 1/0/1
   [*PE1-100GE1/0/1] portswitch
   [*PE1-100GE1/0/1] port link-type access
   [*PE1-100GE1/0/1] port default vlan 100
   [*PE1-100GE1/0/1] stp disable
   [*PE1-100GE1/0/1] l2protocol-tunnel stp enable
   [*PE1-100GE1/0/1] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE2
   [*HUAWEI] commit
   [~PE2] stp enable
   [*PE2] commit
   [~PE2] vlan 100
   [*PE2-vlan100] quit
   [*PE2] interface 100ge 1/0/1
   [*PE2-100GE1/0/1] portswitch
   [*PE2-100GE1/0/1] port link-type access
   [*PE2-100GE1/0/1] port default vlan 100
   [*PE2-100GE1/0/1] stp disable
   [*PE2-100GE1/0/1] l2protocol-tunnel stp enable
   [*PE2-100GE1/0/1] quit
   [*PE2] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the peer device sends non-standard protocol packets, first run the [**l2protocol-tunnel user-defined-protocol**](cmdqueryname=l2protocol-tunnel+user-defined-protocol) *protocol-name* **protocol-mac** *protocol-mac* [ **encap-type** { { **ethernetii** | **snap** } **protocol-type** *protocol-type-value* | **llc dsap** *dsap-value* **ssap** *ssap-value* } ] **group-mac** { *group-mac* | **default-group-mac** } command to define the characteristics of the Layer 2 protocol for transparent transmission and then run the [**l2protocol-tunnel user-defined-protocol**](cmdqueryname=l2protocol-tunnel+user-defined-protocol) *protocol-name* **enable** command to enable Layer 2 protocol tunneling on the interface.
3. Configure PEs to replace the destination MAC addresses of STP BPDUs received from CEs.
   
   
   
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
4. Set the priority of CE2 to 4096.
   
   
   ```
   [~CE2] stp priority 4096
   [*CE2] commit
   ```
5. Verify the configuration.
   
   
   
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

#### Configuration Scripts

* CE1
  
  ```
  #
  sysname CE1
  #
  vlan batch 100
  #
  interface 100GE1/0/1
   port default vlan 100
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
   port default vlan 100
  #
  return
  ```
* PE1
  
  ```
  #
  sysname PE1
  #
  vlan batch 100
  #
  l2protocol-tunnel stp group-mac 0100-5e00-0011
  #
  interface 100GE1/0/1
   port default vlan 100
   stp disable
   l2protocol-tunnel stp enable
  #
  return
  ```
* PE2
  
  ```
  #
  sysname PE2
  #
  vlan batch 100
  #
  l2protocol-tunnel stp group-mac 0100-5e00-0011
  #
  interface 100GE1/0/1
   port default vlan 100
   stp disable
   l2protocol-tunnel stp enable
  #
  return
  ```