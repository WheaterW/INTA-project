Example for Configuring LDP Session Protection
==============================================

This session provides an example for configuring LDP session protection. The configuration involves configuring a local LDP session and the LDP session protection function.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172368595__fig_dc_vrp_ldp-p2p_cfg_008001), PE1 and PE2 are directly connected, and a redundancy link is deployed between them. The customer requires that the LDP session between PE1 and PE2 and and their peer relationship remain connected if the direct link between the PEs fails. To meet this requirement, you can configure LDP session protection.

**Figure 1** Networking diagram of LDP session protection![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/1/1, respectively.


  
![](figure/en-us_image_0279183714.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface and configure an IGP.
2. Configure a local LDP session.
3. Configure LDP session protection.

#### Data Preparation

To complete the configuration, you need the following data:

**Table 1** Data to be prepared
| Device Name | Parameter | Value |
| --- | --- | --- |
| **PE1** | Session hold time | Infinite |
| **PE2** | Session hold time | Infinite |



#### Procedure

1. Assign an IP address to each interface and configure an IGP. For configuration details, see [Configuration Files](#EN-US_TASK_0172368595__example_01) in this section.
2. Configure a local LDP session.
   
   
   
   # Configure PE1.
   
   ```
   <PE1> system-view
   ```
   ```
   [~PE1] mpls lsr-id 1.1.1.1
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] quit
   ```
   ```
   [*PE1] mpls ldp
   ```
   ```
   [*PE1-mpls-ldp] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] commit
   ```
   
   # Repeat this step for PE2. For configuration details, see [Configuration Files](#EN-US_TASK_0172368595__example_01) in this section.
3. Configure LDP session protection.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls ldp
   ```
   ```
   [*PE1-mpls-ldp] session protection duration infinite
   ```
   ```
   [*PE1-mpls-ldp] commit
   ```
   ```
   [~PE1-mpls-ldp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls ldp
   ```
   ```
   [*PE2-mpls-ldp] session protection duration infinite
   ```
   ```
   [*PE2-mpls-ldp] commit
   ```
   ```
   [~PE2-mpls-ldp] quit
   ```
4. Verify the configuration.
   
   # Shut down GE 0/1/1 on PE1 to simulate a link fault. Run the [**display mpls ldp remote-peer**](cmdqueryname=display+mpls+ldp+remote-peer) command. The command output shows that LDP session protection has taken effect.
   ```
   [~PE1] display mpls ldp remote-peer 
   ```
   ```
                            LDP Remote Entity Information
    ------------------------------------------------------------------------------
    Remote Peer Name  : pe2
    Description       : ----
    Remote Peer IP    : 3.3.3.3              LDP ID        : 1.1.1.1:0
    Transport Address : 1.1.1.1              Entity Status : Active
   
    Configured Keepalive Hold Timer : 45 Sec
    Configured Keepalive Send Timer : ----
    Configured Hello Hold Timer     : 45 Sec
    Negotiated Hello Hold Timer     : 45 Sec
    Configured Hello Send Timer     : ----
    Configured Delay Timer          : 10 Sec
    Hello Packet sent/received      : 91/86
    Label Advertisement Mode        : Downstream Unsolicited
    Auto-config                     : Session-Protect
    Manual-config                   : effective
    Session-Protect effect          : YES
    Session-Protect Duration        : infinite
    Session-Protect Remain          : ----
    ------------------------------------------------------------------------------
    TOTAL: 1 Remote-Peer(s) Found.
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
   session protection duration infinite
   #
   ipv4-family
  #
  isis 1
   is-level level-2
   network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.252
   isis enable 1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.252
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
   isis enable 1
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  isis 1
   is-level level-2
   network-entity 10.0000.0000.0003.00
  #               
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.252
   isis enable 1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.3.1 255.255.255.252
   isis enable 1
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls ldp
   session protection duration infinite
   #
   ipv4-family
  #
  isis 1
   is-level level-2
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.3.2 255.255.255.252
   isis enable 1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.2 255.255.255.252
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
  #
  return
  ```