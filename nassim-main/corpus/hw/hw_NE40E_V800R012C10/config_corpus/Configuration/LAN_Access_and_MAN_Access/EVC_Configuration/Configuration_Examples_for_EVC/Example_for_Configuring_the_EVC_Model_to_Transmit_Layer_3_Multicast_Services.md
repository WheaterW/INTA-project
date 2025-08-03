Example for Configuring the EVC Model to Transmit Layer 3 Multicast Services
============================================================================

This section provides an example for configuring the EVC model to transmit Layer 3 multicast services.

#### Networking Requirements

An EVC applies to Layer 2 interfaces and does not support IP address configuration. To enable an EVC-capable BD to communicate with Layer 3 interfaces, configure a logical VBDIF interface for the BD. Then, the EVC can be used to transmit Layer 3 multicast services, simplifying network planning and management.

On the Layer 3 network shown in [Figure 1](#EN-US_TASK_0172363417__fig_dc_vrp_evc_cfg_004101), configure Subinterface1.1 as a VBDIF interface.

**Figure 1** Network diagram of configuring the EVC model to transmit Layer 3 multicast services![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, subinterface1.1, interface1, and interface2 represent GE0/1/1.1, GE0/1/1, and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_evc_cfg_004101.png "Click to enlarge")  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an EVC model.
   
   1. Configure a BD to forward services.
   2. Create an EVC Layer 2 sub-interface and add the sub-interface to the BD.
   3. Create a VBDIF interface.
2. Assign IP addresses to interfaces and configure a unicast routing protocol.
3. Configure Layer 3 multicast.
   
   1. Enable multicast routing.
   2. Configure basic PIM-SM functions.
   3. Configure an IGMP static group and simulate user Join messages.
   4. Configure an RP.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast group address: 225.1.0.0
* Multicast source address: 10.0.0.1
* BD ID

#### Procedure

1. Create an EVC model.
   
   
   1. Create a BD on Device B.
      
      # Configure Device B.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname Device B
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~Device B] bridge-domain 10
      ```
      ```
      [*Device B-bd10] commit
      ```
      ```
      [~Device B-bd10] quit
      ```
   2. Create an EVC Layer 2 sub-interface, add the sub-interface to the BD, and specify the traffic encapsulation type and behavior on the sub-interface.
      
      # Configure Device B.
      
      ```
      [*Device B] interface gigabitethernet 0/1/1
      ```
      ```
      [*Device B-GigabitEthernet0/1/1] undo shutdown
      ```
      ```
      [*Device B-GigabitEthernet0/1/1] quit
      ```
      ```
      [*Device B] interface gigabitethernet 0/1/1.1 mode l2
      ```
      ```
      [*Device B-GigabitEthernet0/1/1.1] encapsulation dot1q vid 10
      ```
      ```
      [*Device B-GigabitEthernet0/1/1.1] rewrite pop single
      ```
      ```
      [*Device B-GigabitEthernet0/1/1.1] bridge-domain 10
      ```
      ```
      [*Device B-GigabitEthernet0/1/1.1] commit
      ```
      ```
      [~Device B-GigabitEthernet0/1/1] quit
      ```
   3. Create a VBDIF interface.
      
      # Configure Device B.
      
      ```
      [~Device B] interface vbdif 10
      ```
      ```
      [*Device B-Vbdif10] commit
      ```
      ```
      [~Device B-Vbdif10] quit
      ```
   4. Verify the configuration.
      
      After completing the configuration, run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) command. The command output shows the BD to which an EVC Layer 2 sub-interface belongs and the BD status.
      
      ```
      [~Device B] display bridge-domain
      ```
      ```
      The total number of bridge-domains is : 1
      --------------------------------------------------------------------------------
      MAC_LRN: MAC learning;         STAT: Statistics;         SPLIT: Split-horizon;
      BC: Broadcast;                 MC: Unknown multicast;    UC: Unknown unicast;
      *down: Administratively down;  FWD: Forward;             DSD: Discard;
      --------------------------------------------------------------------------------
      
      BDID  State MAC-LRN STAT    BC  MC  UC  SPLIT   Description
      --------------------------------------------------------------------------------
      10    up    enable  disable FWD FWD FWD disable
      ```
2. Assign IP addresses to interfaces and configure a unicast routing protocol.
   
   
   
   # Configure Device B.
   
   ```
   [~Device B] isis 1
   ```
   ```
   [*Device B-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*Device B-isis-1] commit
   ```
   ```
   [~Device B-isis-1] quit 
   ```
   ```
   [~Device B] interface gigabitEthernet 0/1/2
   ```
   ```
   [~Device B-GigabitEthernet0/1/2] ip address 192.168.1.2 24 
   ```
   ```
   [*Device B-GigabitEthernet0/1/2] isis enable 1 
   ```
   ```
   [*Device B-GigabitEthernet0/1/2] quit 
   ```
   ```
   [*Device B] interface vbdif 10
   ```
   ```
   [*Device B-Vbdif10] ip address 192.168.2.1 24
   ```
   ```
   [*Device B-Vbdif10] isis enable 1 
   ```
   ```
   [*Device B-Vbdif10] quit 
   ```
   ```
   [*Device B] commit
   ```
   
   The configuration of Device A is similar to the configuration of Device B. For configuration details, see [Configuration Files](#EN-US_TASK_0172363417__section_dc_vrp_evc_cfg_11111) in this section.
3. Configure Layer 3 multicast.
   
   
   1. Enable multicast routing on each Device A and Device B. Enable PIM-SM on each interface.
      
      ```
      [~Device B] multicast routing-enable
      ```
      ```
      [*Device B] interface gigabitEthernet 0/1/2
      ```
      ```
      [*Device B-GigabitEthernet0/1/2] pim sm
      ```
      ```
      [*Device B-GigabitEthernet0/1/2] quit
      ```
      ```
      [*Device B] interface vbdif 10
      ```
      ```
      [*Device B-Vbdif10] pim sm
      ```
      ```
      [*Device B-Vbdif10] igmp enable
      ```
      ```
      [*Device B-Vbdif10] igmp version 3
      ```
      ```
      [*Device B-Vbdif10] quit
      ```
      ```
      [*Device B] commit
      ```
      
      The configuration of Device A is similar to the configuration of Device B. For configuration details, see [Configuration Files](#EN-US_TASK_0172363417__section_dc_vrp_evc_cfg_11111) in this section.
   2. On Device B, configure a static IGMP group on GE 0/1/1.1 connected to user hosts. Simulate user Join messages.
      
      ```
      [~Device B] interface gigabitEthernet 0/1/1.1
      ```
      ```
      [~Device B-GigabitEthernet0/1/1.1] l2-multicast static-group source-address 10.0.0.1 group-address 225.0.0.1 dot1q vid 10
      ```
      ```
      [*Device B-GigabitEthernet0/1/1.1] quit
      ```
      ```
      [*Device B] commit
      ```
   3. Configure a C-BSR and C-RP on Device A.
      
      ```
      [~Device A] pim
      ```
      ```
      [*Device A-pim] c-bsr gigabitEthernet 0/1/2
      ```
      ```
      [*Device A-pim] c-rp gigabitEthernet 0/1/2
      ```
      ```
      [*Device A-pim] quit
      ```
      ```
      [*Device A] commit
      ```
4. Verify the configuration.
   
   
   
   # Run the **display pim interface** command on Device B to check whether PIM-SM is enabled.
   
   ```
   [~Device B] display pim interface 
   ```
   ```
    VPN-Instance: public net
    Interface           State NbrCnt HelloInt   DR-Pri     DR-Address
    GE0/1/2             up    0      30         1          192.168.1.2 (local)
    Vbdif10             up    1      30         1          192.168.2.1 (local)
   
   ```
   
   The command output shows that PIM-SM is enabled on VBDIF 10.
   
   # Run the **display pim routing-table** command on Device B to check the IPv4 routing table.
   
   ```
   [~Device B] display pim routing-table 
   ```
   ```
    (10.0.0.1, 225.0.0.1)
        RP: 192.168.1.1 
        Protocol: pim-sm, Flag: SPT SG_RCVR 
        UpTime: 00:25:11     
        Upstream interface: GigabitEthernet0/1/2
            Upstream neighbor: 192.168.1.1
            RPF prime neighbor: 192.168.1.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: Vbdif10
                Protocol: igmp, UpTime: 00:25:11, Expires: - 
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname Device A
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0001.00 
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.0.0.1 255.255.255.0
  interface GigabitEthernet0/1/2
   undo shutdown  
   ip address 192.168.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   c-bsr GigabitEthernet0/1/2
   c-rp GigabitEthernet0/1/2
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname Device B
  #
  multicast routing-enable
  #
  bridge-domain 10
  #
  isis 1
   network-entity 10.0000.0000.0002.00 
  #
  interface Vbdif10
   ip address 192.168.2.1 255.255.255.0
   pim sm
   igmp enable 
   igmp version 3
   isis enable 1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
   l2-multicast static-group source-address 10.0.0.1 group-address 225.0.0.1 dot1q vid 10
  #
  interface GigabitEthernet0/1/2
   undo shutdown  
   ip address 192.168.1.2 255.255.255.0
   pim sm         
   isis enable 1  
  #
  return
  ```