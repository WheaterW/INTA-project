Example for Configuring mLACP-based Dual-Homing Access Protection
=================================================================

This section provides an example for configuring mLACP-based dual-homing access protection. After mLACP is configured on PEs that a CE is dual-homed to, device-level protection rather than board-level protection is provided.

#### Networking Requirements

Configure mLACP on dual-homed PEs to implement device redundancy and improve network reliability.

On the network shown in Figure 1, a CE is dual-homed to two PEs through Eth-Trunk interfaces in static LACP mode. To improve reliability, deploy mLACP on PE1 and PE2 with PE1 as the master device and PE2 as the backup device. If the link between PE1 and the CE fails, the traffic from the CE to PE1 must be automatically switched to PE2. If the link between the CE and PE1 recovers, traffic must be switched back to PE1.

**Figure 1** Configuring CE dual-homing access protection based on mLACP![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent GE0/1/1 and GE0/2/1, respectively.


  
![](figure/en-us_image_0000001214370930.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an LDP session between PE1 and PE2.
   
   1. Configure a routing protocol on PE1 and PE2 to ensure Layer 3 network connectivity.
      
      OSPF is used in this example.
   2. Configure basic MPLS functions and MPLS LDP, and set up LDP LSPs on PE1 and PE2.
2. Create Eth-Trunk interfaces working in static LACP mode on the CE and PEs and add member interfaces to the Eth-Trunk interfaces to improve link reliability.
3. Create an ICCP redundancy group and ICCP session on PE1 and PE2.
   
   1. Configure an ICCP redundancy group on PE1 and PE2.
   2. Bind the ICCP redundancy group to the peer IP address of the LDP session, which is used by PE1 and PE2 to communicate with each other.
4. Configure mLACP on PE1 and PE2 to improve device-level reliability.
   1. Configure a system ID, system priority, and node ID for the ICCP redundancy group on PE1 and PE2 to enable mLACP.
   2. Bind the Eth-Trunk interface on PE1 and PE2 to the ICCP redundancy group, and the interface is then automatically added to mLACP.
   3. Set a higher priority for the Eth-Trunk interface on PE1 (A smaller value indicates a higher priority) so that this interface functions as the master.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR ID of each PE
* System priority of each Eth-Trunk interface
* mLACP system priority, system ID, and node ID
* mLACP port priority

![](../../../../public_sys-resources/note_3.0-en-us.png) 

On PE1 and PE2, the mLACP system priorities must be the same, so are the system IDs; however, the node IDs must be different. To ensure normal mLACP switching, it is recommended that PE1 and PE2 be the LACP Actors. This means that their mLACP system priority value must be smaller than that on the CE.

mLACP does not support protection against node faults. The convergence time upon a PE1 fault depends on the Keepalive time of the LDP session.

PE1 and PE2 must have the same Eth-Trunk ID for dual-homing protection.



#### Procedure

1. Enable MPLS and set up an LDP session between PE1 and PE2.
   
   
   
   Enable MPLS on PE1 and PE2, and set up an LDP session and LSPs between the PEs. For details on how to configure MPLS, see [MPLS LDP Configuration](dc_vrp_ldp-p2p_cfg_0000.html).
   
   After completing the configuration, run the [**display mpls ldp session**](cmdqueryname=display+mpls+ldp+session) command to check that an LDP session in the **Operational** state has been established between PE1 and PE2.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display mpls ldp session all
   ```
   ```
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode),  SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
   --------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge       KASent/Rcv
   --------------------------------------------------------------------------
    10.2.2.2:0          Operational DU   Passive  0000:00:00   3/3
   --------------------------------------------------------------------------
   TOTAL: 1 Session(s) Found.
   ```
2. Create an ICCP redundancy group on PE1 and PE2 and bind the group to the LDP session to establish an ICCP connection.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1]iccp redundancy group 1
   [*PE1-iccp-redundancy-group-1]peer-ip 10.2.2.2
   [*PE1-iccp-redundancy-group-1]commit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2]iccp redundancy group 1
   [*PE2-iccp-redundancy-group-1]peer-ip 10.1.1.1
   [*PE2-iccp-redundancy-group-1]commit
   ```
   
   
   
   After completing the configuration, run the [**display iccp group**](cmdqueryname=display+iccp+group) command on PE1 and PE2 to check that an ICCP session in the **OPERATIONAL** state has been established between the two PEs.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1]display iccp group 1
   ```
   ```
                            The ICCP Redundancy Group Information
   ICCP Redundancy Group:    1
   Peer IP:                  10.2.2.2
   Local Sender Name:        PE1
   Peer Sender Name:         PE2
   State Machine Status:     OPERATIONAL
   ICCP Capability:          Enable
   LDP Session State:        UP 
   ```
3. Add interfaces on the CE, PE1, and PE2 to the corresponding Eth-Trunk interfaces.
   
   # Configure the CE.
   ```
   [~CE]interface Eth-Trunk 10
   [*CE-Eth-Trunk10]mode lacp-static
   [*CE-Eth-Trunk10]trunkport gigabitethernet 0/1/1
   [*CE-Eth-Trunk10]trunkport gigabitethernet 0/2/1
   [*CE-Eth-Trunk10]commit
   ```
   
   
   # Configure PE1.
   ```
   [~PE1]interface Eth-Trunk 10
   [*PE1-Eth-Trunk10]mode lacp-static
   [*PE1-Eth-Trunk10]trunkport gigabitethernet 0/2/1
   [*PE1-Eth-Trunk10]commit
   ```
   
   
   # Configure PE2.
   ```
   [~PE2]interface Eth-Trunk 10
   [*PE2-Eth-Trunk10]mode lacp-static
   [*PE2-Eth-Trunk10]trunkport gigabitethernet 0/1/1
   [*PE2-Eth-Trunk10]commit
   ```
4. Enable mLACP in the ICCP redundancy group on PE1 and PE2.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1]iccp redundancy group 1
   [*PE1-iccp-redundancy-group-1]mlacp system-id 00e0-fc12-3458
   [*PE1-iccp-redundancy-group-1]mlacp system-priority 100
   [*PE1-iccp-redundancy-group-1]mlacp node-id 1
   [*PE1-iccp-redundancy-group-1]commit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2]iccp redundancy group 1
   [*PE2-iccp-redundancy-group-1]mlacp system-id 00e0-fc12-3458
   [*PE2-iccp-redundancy-group-1]mlacp system-priority 100
   [*PE2-iccp-redundancy-group-1]mlacp node-id 5
   [*PE2-iccp-redundancy-group-1]commit
   ```
   
   
   
   After completing the configuration, run the [**display mlacp iccp-status group**](cmdqueryname=display+mlacp+iccp-status+group) command to check that the mLACP session was successfully set up, the mLACP state machine is **OPERATIONAL**, and the mLACP local and peer information is correct.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1]display mlacp iccp-status group 1
   ```
   ```
                         The mLACP ICCP group information
   ICCP Redundancy Group: 1
   ICCP Status: Up                         mLACP Machine Status: OPERATIONAL
   Local:
   --------------------------------------------------------------------------------
   mLACP System ID: 00e0-fc12-3458         Work System ID: 00e0-fc12-3458
   mLACP System Priority: 100              Work System Priority: 100
   mLACP Node ID: 1
   mLACP Support Version: 1
   --------------------------------------------------------------------------------
   Peer:
   --------------------------------------------------------------------------------
   mLACP System ID : 00e0-fc12-3458
   mLACP System Priority : 100
   mLACP Node ID : 5
   mLACP Support Version: 1
   --------------------------------------------------------------------------------
   Member:
   --------------------------------------------------------------------------------
   AggName Role State PeerAggName State
   ```
5. Bind the Eth-Trunk interface to the ICCP redundancy group on PE1 and PE2, and configure a higher mLACP port priority on PE1.
   
   # Configure PE1.
   ```
   [~PE1]interface Eth-Trunk 10
   [~PE1-Eth-Trunk1]mlacp iccp-group 1
   [*PE1-Eth-Trunk1]mlacp port-priority 100
   [*PE1-Eth-Trunk1]commit
   ```
   
   
   # Configure PE2.
   ```
   [~PE2]interface Eth-Trunk 10
   [~PE2-Eth-Trunk1]mlacp iccp-group 1
   [*PE2-Eth-Trunk1]commit
   ```
6. Verify the configuration. 
   
   
   
   # Run the [**display eth-trunk**](cmdqueryname=display+eth-trunk) command on the CE to check the Eth-Trunk interface configuration.
   
   ```
   [~CE]display eth-trunk 10
   ```
   ```
   Eth-Trunk10's state information is:
   (h): high priority
   (r): reference port
   Local:
   LAG ID: 1                   WorkingMode: STATIC
   Preempt Delay: Disabled     Hash arithmetic: According to flow
   System Priority: 32768      System ID: 00e0-fc12-3469
   Least Active-linknumber: 1  Max Active-linknumber: 64
   Operate status: up          Number Of Up Port In Trunk: 1
   Timeout Period: Slow
   PortKeyMode: Auto
   --------------------------------------------------------------------------------
   ActorPortName                 Status   PortType PortPri PortNo PortKey PortState Weight
   GigabitEthernet0/1/1(r)       Selected  1G      32768   1      289     10111100  1
   GigabitEthernet0/2/1          Unselect  1G      32768   2      289     10110000  1
   
   Partner:
   --------------------------------------------------------------------------------
   ActorPortName              SysPri    SystemID       PortPri PortNo  PortKey   PortState
   GigabitEthernet0/1/1 (r)      1      00e0-fc12-3458  32768  36865     1       10111100
   GigabitEthernet0/2/1          1      00e0-fc12-3458  32768  53249     1       10100000
   ```
   
   The command output shows that the CE's Eth-Trunk member interfaces GigabitEthernet0/1/1 and GigabitEthernet0/2/1 are in the **Selected** and **Unselect** states, respectively.
   
   
   
   # Run the [**display mlacp eth-trunk**](cmdqueryname=display+mlacp+eth-trunk) command on PE1 to check information about the Eth-Trunk interface added to mLACP.
   
   ```
   [~PE1]display mlacp eth-trunk 10
   ```
   ```
                      The mLACP Trunk Information
   --------------------------------------------------------------------------------
   Eth-Trunk1's state information is:
   Trunk ID: 10                           mLACP Role: Master    
   ICCP Group: 1                       
   mLACP System ID: 00e0-fc12-3458        mLACP System Priority: 100       
   mLACP Port Priority: 100             ROID: 0000.0001.0000.0000 
   --------------------------------------------------------------------------------
   
   
                          The Local Port Information
   (P): Peer Request   (C): Local Configured   (L): Local Request
   -------------------------------------------------------------------------------
   PortName                   Status     PortPri   PortNo PortKey State     IsRef 
   -------------------------------------------------------------------------------
   GE0/2/1                   Select     100(C)    36865  0xa     10111100  1     
   -------------------------------------------------------------------------------
   
   Partner:
   --------------------------------------------------------------------------------
   PortName                   SysPri SystemID       PortPri PortNo PortKey State    
   --------------------------------------------------------------------------------
   GE0/2/1                   32768  00e0-fc12-3469 32768   1      0xa21   10111100 
   --------------------------------------------------------------------------------
   
                          The Peer Port Information
   --------------------------------------------------------------------------------
   PortName                   Status     PortPri   PortNo PortKey State            
   --------------------------------------------------------------------------------
   GE0/1/1                   Unselect   32768     53249  0xa     10100000         
   --------------------------------------------------------------------------------
   
   Partner:
   --------------------------------------------------------------------------------
   PortName                   SysPri SystemID       PortPri PortNo PortKey State    
   --------------------------------------------------------------------------------
   GE0/1/1                   32768  00e0-fc12-3469 32768   2      0xa21   10110000 
   --------------------------------------------------------------------------------   
   
   ```
   
   
   
   # Run the [**display mlacp eth-trunk**](cmdqueryname=display+mlacp+eth-trunk) command on PE2 to check information about the Eth-Trunk interface added to mLACP.
   
   ```
   [~PE2]display mlacp eth-trunk 10
   ```
   ```
                      The mLACP Trunk Information
   --------------------------------------------------------------------------------
   Eth-Trunk1's state information is:
   Trunk ID: 10                           mLACP Role: Backup    
   ICCP Group: 1                       
   mLACP System ID: 00e0-fc12-3458        mLACP System Priority: 100       
   mLACP Port Priority: 32768             ROID: 0000.0001.0000.0000 
   --------------------------------------------------------------------------------
   
   
                          The Local Port Information
   (P): Peer Request   (C): Local Configured   (L): Local Request
   --------------------------------------------------------------------------------
   PortName                   Status     PortPri   PortNo PortKey State      IsRef       
   --------------------------------------------------------------------------------
   GE0/1/1                   Unselect   32768(C)  53249  0xa     10100000   1      
   --------------------------------------------------------------------------------
   
   Partner:
   --------------------------------------------------------------------------------
   PortName                   SysPri SystemID       PortPri PortNo PortKey State    
   --------------------------------------------------------------------------------
   GE0/1/1                   32768  00e0-fc12-3469 32768   2      0xa21   10110000 
   --------------------------------------------------------------------------------   
   
                          The Peer Port Information
   -------------------------------------------------------------------------------
   PortName                   Status     PortPri   PortNo PortKey State     
   -------------------------------------------------------------------------------
   GE0/2/1                   Select     100       36865  0xa     10111100       
   -------------------------------------------------------------------------------
   
   Partner:
   --------------------------------------------------------------------------------
   PortName                   SysPri SystemID       PortPri PortNo PortKey State    
   --------------------------------------------------------------------------------
   GE0/2/1                   32768  00e0-fc12-3469 32768   1      0xa21   10111100 
   --------------------------------------------------------------------------------
   ```
   
   The command output on PE1 and PE2 shows that the Eth-Trunk interface on PE1 plays the master role and that on PE2 plays the backup role.

#### Configuration Files

* CE configuration file
  
  ```
  #
  sysname CE
  #
  interface Eth-Trunk10
   mode lacp-static
   #
  interface GigabitEthernet0/1/1
   undo shutdown
   eth-trunk 10
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   eth-trunk 10
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  mpls lsr-id 10.1.1.1
  #
  mpls
  #
  mpls ldp
  #
  mpls ldp remote-peer 10.2.2.2
  #
  mpls ldp remote-peer PE2
   remote-ip 10.2.2.2
  #
  iccp redundancy group 1
   peer-ip 10.2.2.2
   mlacp system-id 00e0-fc12-3458
   mlacp system-priority 100
   mlacp node-id 1
  #
  interface Eth-Trunk10
   mode lacp-static
   mlacp iccp-group 1
   mlacp port-priority 100
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   eth-trunk 10
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 10.2.2.2
  #
  mpls
  #
  mpls ldp
  #
  mpls ldp remote-peer 10.1.1.1
  #
  mpls ldp remote-peer PE1
   remote-ip 10.1.1.1
  #
  iccp redundancy group 1
   peer-ip 10.1.1.1
   mlacp system-id 00e0-fc12-3458
   mlacp system-priority 100
   mlacp node-id 5
  #
  interface Eth-Trunk10
   mode lacp-static
   mlacp iccp-group 1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   eth-trunk 10
  #
  return
  ```