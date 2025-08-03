Example for Configuring the EVC Model to Transmit DHCP Relay Services
=====================================================================

This section describes how to configure an EVC to transmit DHCP relay services in a typical Layer 2 accessing Layer 3 EVC networking scenario.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172363423__fig_dc_vrp_evc_cfg_004201), the DHCP clients belong to VLAN 100. The CE connects to the PE through a sub-interface. The PE communicates with the DHCP server through a Layer 3 network. To allow the DHCP clients to automatically apply for IP addresses from the DHCP server, create a VBDIF interface on the PE and configure the DHCP relay function on the VBDIF interface.

**Figure 1** Example for configuring an EVC to transmit DHCP relay services![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1, interface2, and subinterface1.1 in this example stand for GE 0/1/1, GE 0/1/2, and GE 0/1/1.1, respectively.


  
![](images/fig_dc_vrp_evc_cfg_004201.png)

#### Configuration Roadmap

1. Create a VLAN and configure Layer 2 forwarding on the CE, so that the CE sends single-tagged packets to the PE.
2. Create an EVC model on the PE:
   1. Create a BD.
   2. Configure an EVC Layer 2 sub-interface and specify a traffic encapsulation type and behavior, so that the EVC Layer 2 sub-interface removes the VLAN tag from its received packets.
   3. Add the EVC Layer 2 sub-interface to the BD and create a VBDIF interface for the BD, so that the Layer 2 traffic accesses Layer 3.
3. Configure an interface IP address for the PE and DHCP server and configure a routing protocol to allow them to communicate at Layer 3.
4. Configure the DHCP relay function on the PE's VBDIF interface and specify the DHCP server's IP address, so that the DHCP clients in the BD can automatically request IP addresses from the DHCP server.

#### Data Preparation

To complete the configuration, you need the following data:

1. VLAN ID to which the DHCP clients belong: 100
2. BD ID: 10
3. IP address of the VBDIF interface: 1.1.1.1
4. IP address of the DHCP server: 2.2.2.2


#### Procedure

1. Create a VLAN and configure Layer 2 forwarding on the CE.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE] vlan 100
   ```
   ```
   [*CE-vlan100] quit
   ```
   ```
   [*CE] interface GigabitEthernet0/1/1
   ```
   ```
   [*CE-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/1/1] port link-type access
   ```
   ```
   [*CE-GigabitEthernet0/1/1] port default vlan 100
   ```
   ```
   [*CE-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE] interface GigabitEthernet0/1/2
   ```
   ```
   [*CE-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*CE-GigabitEthernet0/1/2] port trunk allow-pass vlan 100
   ```
   ```
   [*CE-GigabitEthernet0/1/2] quit
   ```
   ```
   [*CE] commit
   ```
2. Create an EVC model on the PE.
   
   
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
   [~PE] vlan 100
   ```
   ```
   [*PE-vlan100] quit
   ```
   ```
   [*PE] bridge-domain 10
   ```
   ```
   [*PE-bd10] quit
   ```
   ```
   [*PE] interface GigabitEthernet0/1/1.1 mode l2
   ```
   ```
   [*PE-gigabitethernet0/1/1.1] undo shutdown
   ```
   ```
   [*PE-gigabitethernet0/1/1.1] encapsulation dot1q vid 100
   ```
   ```
   [*PE-gigabitethernet0/1/1.1] rewrite pop single
   ```
   ```
   [*PE-gigabitethernet0/1/1.1] bridge-domain 10
   ```
   ```
   [*PE-gigabitethernet0/1/1.1] quit
   ```
   ```
   [*PE] commit
   ```
   ```
   [~PE] interface vbdif10
   ```
   ```
   [*PE-vbdif10] ip address 1.1.1.1 255.255.255.0
   ```
   ```
   [*PE-vbdif10] commit
   ```
3. Configure an interface IP address for the PE and DHCP server and configure a routing protocol to allow them to communicate at Layer 3. The configuration details are omitted.
4. Configure the DHCP relay function on the PE's VBDIF interface and specify the DHCP server's IP address.
   
   
   ```
   [~PE-vbdif10] dhcp select relay
   ```
   ```
   [*PE-vbdif10] ip relay address 2.2.2.2
   ```
   ```
   [*PE-vbdif10] commit
   ```
5. Verify the configuration.
   
   
   
   Run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) command on the PE. The command output shows the BD to which the Layer 2 EVC sub-interface is added and the BD status.
   
   ```
   [~PE] display bridge-domain
   ```
   ```
   --------------------------------------------------------------------------------
   MAC_LRN: MAC learning;         STAT: Statistics;         SPLIT: Split-horizon;
   BC: Broadcast;                 MC: Unknown multicast;    UC: Unknown unicast;
   *down: Administratively down;  FWD: Forward;             DSD: Discard;
   U: Up;         D: Down;
   --------------------------------------------------------------------------------
   
   BDID         Ports                                                          
   --------------------------------------------------------------------------------
   10           Eth0/1/1.1(U)                                                      
   
   BDID  State MAC-LRN STAT    BC  MC  UC  SPLIT   Description
   --------------------------------------------------------------------------------
   10    up    enable  disable FWD FWD FWD disable 
   ```
   
   Run the [**display dhcp relay address**](cmdqueryname=display+dhcp+relay+address) command on the PE. The command output shows the IP addresses of the DHCP relay agent and DHCP server.
   
   ```
   [~PE] display dhcp relay address all
   ```
   ```
       **  Vbdif10 DHCP Relay Address  **
    Dhcp Option          Relay Agent IP       Server IP
    *                    -                    2.2.2.2  
   ```

#### Configuration Files

* PE configuration file
  
  ```
  #
  sysname PE
  #
  vlan batch 100
  #
  bridge-domain 10
  #
  interface Vbdif10
   ip address 1.1.1.1 255.255.255.0
   dhcp select relay
   ip relay address 2.2.2.2
  #
  interface GigabitEthernet0/1/1.1 mode l2
   encapsulation dot1q vid 100
   rewrite pop single
   bridge-domain 10
  #
  ```
* CE configuration file
  
  ```
  #
  sysname CE
  #
  vlan batch 100
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type access
   port default vlan 100
  #
  interface GigabitEthernet0/1/2
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 100
  #
  ```