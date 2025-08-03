Example for Configuring the IP-Prefix Tunnel Function to Automatically Establish MPLS TE Tunnels in a Batch
===========================================================================================================

This section provides an example for configuring the IP-prefix tunnel function to automatically establish MPLS TE tunnels in a batch.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172368318__fig_dc_vrp_te-p2p_cfg_021001), a customer expects to establish MPLS TE tunnels to form a full-mesh network and configure Auto FRR for each tunnel. Establishing tunnels one by one is laborious and complex. In this case, the IP-prefix tunnel function can be configured to automatically establish MPLS tunnels in a batch.

**Figure 1** Configuring the IP-prefix tunnel function to automatically establish MPLS TE tunnels in a batch  
![](images/fig_dc_vrp_te-p2p_cfg_021001.png)

**Table 1** Interfaces and their IP addresses on each device
| Device Name | Interface Name | IP Address and Mask |
| --- | --- | --- |
| LSRA | Loopback0 | 1.1.1.9/32 |
| GE 0/1/0 | 10.1.1.1/24 |
| GE 0/1/1 | 10.1.2.1/24 |
| LSRB | Loopback0 | 2.2.2.9/32 |
| GE 0/1/0 | 10.1.1.2/24 |
| GE 0/1/1 | 10.1.3.1/24 |
| LSRC | Loopback0 | 3.3.3.9/32 |
| GE 0/1/1 | 10.1.2.2/24 |
| GE 0/1/2 | 10.1.3.2/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IS-IS and IS-IS TE.
2. Enable MPLS TE and BFD globally on each device.
3. Configure an IP prefix list.
4. Configure a P2P TE tunnel template.
5. Configure the automatic primary tunnel function.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface on each node: values shown in [Figure 1](#EN-US_TASK_0172368318__fig_dc_vrp_te-p2p_cfg_021001)
* LSR ID of each node: loopback addresses shown in [Figure 1](#EN-US_TASK_0172368318__fig_dc_vrp_te-p2p_cfg_021001)
* IS-IS process number (1), IS-IS level (level-2), and network entity name of each node:
  
  + LSRA: 10.0000.0000.0001.00
  + LSRC: 10.0000.0000.0002.00
  + LSRB: 10.0000.0000.0003.00
* IP prefix name on each node: te-tunnel
* P2P TE tunnel template name on each node: te-tunnel

#### Procedure

1. Assign an IP address to each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172368318__example_01) in this section.
2. Configure IS-IS and IS-IS TE. For configuration details, see [Configuration Files](#EN-US_TASK_0172368318__example_01) in this section.
3. Enable MPLS TE and Auto FRR globally on each device. For configuration details, see [Configuration Files](#EN-US_TASK_0172368318__example_01) in this section.
4. Configure an IP prefix list.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] ip ip-prefix te-tunnel permit 2.2.2.9 32
   ```
   ```
   [*LSRA] ip ip-prefix te-tunnel permit 3.3.3.9 32
   ```
   ```
   [*LSRA] commit
   ```
   
   The configurations on LSRB and LSRC are similar to the configuration on LSRA. For configuration details, see [Configuration Files](#EN-US_TASK_0172368318__example_01) in this section.
5. Configure a P2P TE tunnel template.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] mpls te p2p-template te-tunnel 
   ```
   ```
   [*LSRA-te-p2p-template-te-tunnel] bandwidth ct0 1000
   ```
   ```
   [*LSRA-te-p2p-template-te-tunnel] fast-reroute
   ```
   ```
   [*LSRA-te-p2p-template-te-tunnel] commit
   ```
   ```
   [~LSRA-te-p2p-template-te-tunnel] quit
   ```
   
   The configurations on LSRB and LSRC are similar to the configuration on LSRA. For configuration details, see [Configuration Files](#EN-US_TASK_0172368318__example_01) in this section.
6. Configure the automatic primary tunnel function.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] mpls te auto-primary-tunnel ip-prefix te-tunnel p2p-template te-tunnel 
   ```
   ```
   [*LSRA] commit
   ```
   
   The configurations on LSRB and LSRC are similar to the configuration on LSRA. For configuration details, see [Configuration Files](#EN-US_TASK_0172368318__example_01) in this section.
7. Verify the configuration.
   
   # After completing the preceding configuration, run the [**display mpls te tunnel**](cmdqueryname=display+mpls+te+tunnel) command on LSRA. The command output shows that MPLS TE tunnels have been established.
   ```
   [~LSRA] display mpls te tunnel
   * means the LSP is detour LSP
   -------------------------------------------------------------------------------
   Ingress LsrId   Destination     LSPID In/OutLabel     R Tunnel-name
   -------------------------------------------------------------------------------
   1.1.1.9         2.2.2.9         16    -/3             I AutoTunnel32769
   2.2.2.9         1.1.1.9         10    3/-             E AutoTunnel32769
   1.1.1.9         3.3.3.9         17    -/3             I AutoTunnel32770
   3.3.3.9         1.1.1.9         9     3/-             E AutoTunnel32770
   1.1.1.9         2.2.2.9         13    -/48060         I AutoBypassTunnel_1.1.1.9_2.2.2.9_32771
   2.2.2.9         3.3.3.9         8     48061/3         T AutoBypassTunnel_2.2.2.9_3.3.3.9_32771
   3.3.3.9         2.2.2.9         7     48060/3         T AutoBypassTunnel_3.3.3.9_2.2.2.9_32771
   1.1.1.9         3.3.3.9         15    -/48060         I AutoBypassTunnel_1.1.1.9_3.3.3.9_32772
   2.2.2.9         1.1.1.9         9     3/-             E AutoBypassTunnel_2.2.2.9_1.1.1.9_32772
   3.3.3.9         1.1.1.9         8     3/-             E AutoBypassTunnel_3.3.3.9_1.1.1.9_32772
   -------------------------------------------------------------------------------
   R: Role, I: Ingress, T: Transit, E: Egress
   ```
   
   Obtain a tunnel name, for example, **AutoTunnel32769**, displayed in the **Tunnel-name** column. Run the **display mpls te tunnel-interface auto-primary-tunnel AutoTunnel32769** command to view detailed information about the specified tunnel.

#### Configuration Files

* LSRA configuration file
  
  ```
  #
  sysname LSRA
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
   mpls te
   mpls te auto-frr
   mpls rsvp-te
   mpls te cspf
  #
  mpls te p2p-template te-tunnel
   record-route label
   bandwidth ct0 1000
   fast-reroute
  #
  mpls te auto-primary-tunnel ip-prefix te-tunnel p2p-template te-tunnel
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0001.00
   traffic-eng level-2
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #
  interface LoopBack0
   ip address 1.1.1.9 255.255.255.255
   isis enable 1
   #
  ip ip-prefix te-tunnel index 10 permit 2.2.2.9 32 
  ip ip-prefix te-tunnel index 20 permit 3.3.3.9 32 
  #
  return
  ```
* LSRB configuration file
  
  ```
  #
  sysname LSRB
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
   mpls te
   mpls te auto-frr
   mpls rsvp-te
   mpls te cspf
  #
  mpls te p2p-template te-tunnel
   record-route label
   bandwidth ct0 1000
   fast-reroute
  #
  mpls te auto-primary-tunnel ip-prefix te-tunnel p2p-template te-tunnel
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0002.00
   traffic-eng level-2
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #
  interface LoopBack0
   ip address 2.2.2.9 255.255.255.255
   isis enable 1
  #               
  ip ip-prefix te-tunnel index 10 permit 1.1.1.9 32 
  ip ip-prefix te-tunnel index 20 permit 3.3.3.9 32 
  #
  return
  ```
* LSRC configuration file
  
  ```
  #
  sysname LSRC
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
   mpls te
   mpls te auto-frr
   mpls rsvp-te
   mpls te cspf
  #
  mpls te p2p-template te-tunnel
   record-route label
   bandwidth ct0 1000
   fast-reroute
  #
  mpls te auto-primary-tunnel ip-prefix te-tunnel p2p-template te-tunnel
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0003.00
   traffic-eng level-2
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 10000
   mpls te bandwidth bc0 10000
   mpls rsvp-te
  #
  interface LoopBack0
   ip address 3.3.3.9 255.255.255.255
   isis enable 1
  #
  ip ip-prefix te-tunnel index 10 permit 1.1.1.9 32 
  ip ip-prefix te-tunnel index 20 permit 2.2.2.9 32 
  #
  return
  ```