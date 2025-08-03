Example for Configuring a Local VPLS Connection
===============================================

A local VPLS connection enables two CEs that connect to the same PE to communicate.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172370257__fig_dc_vrp_vpls_cfg_603501), two CEs connect to the same PE. To enable the two CEs to communicate, establish a local VPLS connection between them. In this situation, the PE functions similar to a Layer 2 switch to directly swap labels without the need to configure any public network tunnel.

**Figure 1** Configuring a local VPLS connection![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface1 and interface2 represent GE0/1/0 and GE0/2/0, respectively.

  
![](images/fig_dc_vrp_vpls_cfg_603501.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic MPLS functions and enable MPLS L2VPN on the PE.
2. Establish a local VPLS connection between CE1 and CE2 on the PE.

#### Data Preparation

To complete the configuration, you need the following data:

* VSI names and IDs
* Interfaces bound to VSIs

#### Procedure

1. Configure IP addresses for CEs.
   
   
   
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
   [~CE1-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CE1] commit
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
   [~CE2-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CE2] commit
   ```
2. Configure a local VPLS connection on the PE.
   
   
   
   # Enable MPLS and MPLS L2VPN.
   
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
   [~PE] mpls
   ```
   ```
   [*PE-mpls] quit
   ```
   ```
   [*PE] mpls l2vpn
   ```
   ```
   [*PE-l2vpn] quit
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
   [*PE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE] commit
   ```
   
   # Configure a VSI.
   
   ```
   [~PE] vsi abc
   ```
   ```
   [*PE-vsi-abc] pwsignal ldp
   ```
   ```
   [*PE-vsi-abc-ldp] vsi-id 2
   ```
   ```
   [*PE-vsi-abc-ldp] quit
   ```
   ```
   [*PE-vsi-abc] mac-learning disable
   ```
   ```
   [*PE-vsi-abc] p2p-vsi enable
   ```
   ```
   [*PE-vsi-abc] quit
   ```
   ```
   [*PE] commit
   ```
   
   # Bind AC interfaces to the VSI.
   
   ```
   [~PE] interface gigabitethernet0/1/0.1
   ```
   ```
   [*PE-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*PE-GigabitEthernet0/1/0.1] l2 binding vsi abc
   ```
   ```
   [*PE-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [~PE] interface gigabitethernet0/2/0.1
   ```
   ```
   [*PE-GigabitEthernet0/2/0.1] l2 binding vsi abc
   ```
   ```
   [*PE-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*PE] commit
   ```
3. Verify the configuration.
   
   
   
   After the configurations are complete, run the [**display vsi verbose**](cmdqueryname=display+vsi+verbose) command on the PE. The command output shows that the local VPLS connection is up.
   
   ```
   [~HUAWEI] display vsi verbose
   ```
   ```
    ***VSI Name               : abc
       Work Mode              : normal
       Administrator VSI      : no
       Isolate Spoken         : disable
       VSI Index              : 6
       PW Signaling           : ldp
       Member Discovery Style : --
       Bridge-domain Mode     : disable
       PW MAC Learn Style     : unqualify
       Encapsulation Type     : vlan
       MTU                    : 1500
       Diffserv Mode          : uniform
       Service Class          : --
       Color                  : --
       DomainId               : 255
       Domain Name            :
       Ignore AcState         : disable
       P2P VSI               : disable
   
       Multicast Fast Switch  : disable
       Create Time            : 0 days, 0 hours, 2 minutes, 38 seconds
       VSI State             : up
       Resource Status        : --
   
       VSI ID                 : 2
   
       Interface Name         : GigabitEthernet0/1/0
       State                  : up
       Access Port            : false
       Last Up Time           : 2015/06/17 09:20:24
       Total Up Time          : 0 days, 0 hours, 0 minutes, 16 seconds
       Interface Name         : GigabitEthernet0/2/0
       State                  : up
       Access Port            : false
       Last Up Time           : 2015/06/17 09:20:24
       Total Up Time          : 0 days, 0 hours, 0 minutes, 16 seconds
    
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
* PE configuration file
  
  ```
  #
  sysname PE
  #
  mpls
  #
  mpls l2vpn
  #
  vsi abc
    pwsignal ldp
     vsi-id 2
    mac-learning disable
    p2p-vsi enable
  #
  interface GigabitEthernet0/1/0.1
   undo shutdown
   vlan-type dot1q 10
   l2 binding vsi abc
  #
  interface GigabitEthernet0/2/0.1
   undo shutdown
   l2 binding vsi abc
  #
  return
  ```