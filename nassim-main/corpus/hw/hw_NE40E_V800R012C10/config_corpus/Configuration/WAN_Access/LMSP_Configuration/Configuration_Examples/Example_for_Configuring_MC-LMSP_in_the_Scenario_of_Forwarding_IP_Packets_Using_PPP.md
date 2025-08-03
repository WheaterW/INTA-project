Example for Configuring MC-LMSP in the Scenario of Forwarding IP Packets Using PPP
==================================================================================

This section describes how to configure multi-chassis linear multiplex section protection (MC-LMSP) for CPOS interfaces on a Layer 3 IP forwarding network based on the Point-to-Point Protocol (PPP).

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172364419__fig_dc_ne_lmsp_cfg_002401), PE1 is dual-homed to PE2 and PE3 through two PWs. MC-LMSP is implemented on the AC side to prevent a network fault from causing data loss.![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the LMSP-enabled interface uses a dynamic routing protocol to advertise routes on the Layer 3 IP packet forwarding network using PPP, the dynamic routes must be learned again after an LMSP is performed. The route convergence takes dozens of seconds, causing a service interruption. To prevent the problem, static routes can be bound to the master device, backup device, and the LMSP-enabled interfaces of a radio network controller (RNC) and imported by a dynamic routing protocol. When an LMSP is performed, the routes do not have to be learned again, which accelerates the route convergence and prevents a long service interruption.



**Figure 1** Configuring MC-LMSP in the scenario of forwarding IP packets using PPP  
![](images/fig_dc_ne_lmsp_cfg_002401.png)  

| Device | Interface Name | Interface |
| --- | --- | --- |
| PE1 | interface1  interface2 | GE0/2/1  GE0/2/2 |
| P1 | interface1  interface6 | GE0/2/1  GE0/2/5 |
| P2 | interface1  interface2 | GE0/2/1  GE0/2/2 |
| PE2 | interface1  interface2  interface5 | GE0/2/1  GE0/2/2  CPOS0/2/3 |
| PE3 | interface1  interface2  interface5 | GE0/2/1  GE0/2/2  CPOS0/2/3 |
| CE2 | interface3  interface4 | CPOS0/2/1  CPOS0/2/2 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface.
2. Configure MC-LMSP on PE2 and PE3 and LMSP on CE2.
3. Bind static routes to the MC-LMSP-enabled interfaces of PE2 and PE3 and the LMSP-enabled interfaces of CE2.
4. Configure an IGP to import static routes.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* MC-LMSP parameters. The HMAC authentication algorithm is used.
* CPOS-Trunk interface parameters
* Global-MP-Group interface number

#### Procedure

1. Configure IP addresses.
   
   
   
   Assign the IP address and mask to each interface according to [Figure 1](#EN-US_TASK_0172364419__fig_dc_ne_lmsp_cfg_002401). For configuration details, see [Configuration Files](#EN-US_TASK_0172364419__section_dc_ne_cfg_aps_002605) in this section.
2. Configure MC-LMSP.
   1. Configure LMSP on PE2, PE3, and CE2.
      
      
      
      # Configure PE2.
      
      ```
      [~PE2] controller cpos 0/2/3
      ```
      ```
      [~PE2-Cpos0/2/3] undo shutdown
      ```
      ```
      [*PE2-Cpos0/2/3] aps group 24
      ```
      ```
      [*PE2-Cpos0/2/3] aps working 4.4.4.4 5.5.5.5
      [*PE2-Cpos0/2/3] aps authenticate cipher 333aa55bbf hmac
      ```
      ```
      [*PE2-Cpos0/2/3] commit
      ```
      ```
      [~PE2-Cpos0/2/3] quit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] controller cpos 0/2/3
      ```
      ```
      [~PE3-Cpos0/2/3] undo shutdown
      ```
      ```
      [*PE3-Cpos0/2/3] aps group 24
      ```
      ```
      [*PE3-Cpos0/2/3] aps protect 5.5.5.5 4.4.4.4
      [*PE3-Cpos0/2/3] aps authenticate cipher 333aa55bbf hmac
      ```
      ```
      [*PE3-Cpos0/2/3] aps mode one2one bidirection
      ```
      ```
      [*PE3-Cpos0/2/3] aps revert 1
      ```
      ```
      [*PE3-Cpos0/2/3] commit
      ```
      ```
      [~PE3-Cpos0/2/3] quit
      ```
      
      # Configure CE2.
      
      ```
      [~CE2] controller cpos0/2/1
      ```
      ```
      [~CE2-Cpos0/2/1] undo shutdown
      ```
      ```
      [*CE2-Cpos0/2/1] aps group 24
      ```
      ```
      [*CE2-Cpos0/2/1] aps working
      ```
      ```
      [*CE2-Cpos0/2/1] commit
      ```
      ```
      [~CE2-Cpos0/2/1] quit
      ```
      ```
      [~CE2] controller cpos0/2/2
      ```
      ```
      [~CE2-Cpos0/2/2] undo shutdown
      ```
      ```
      [*CE2-Cpos0/2/2] aps group 24
      ```
      ```
      [*CE2-Cpos0/2/2] aps protect
      ```
      ```
      [*CE2-Cpos0/2/2] aps mode one2one bidirection
      ```
      ```
      [*CE2-Cpos0/2/2] aps revert 1
      ```
      ```
      [*CE2-Cpos0/2/2] commit
      ```
      ```
      [~CE2-Cpos0/2/2] quit
      ```
   2. Create a CPOS-Trunk on PE2, PE3, and CE2 and add interfaces to the CPOS-Trunk.
      
      
      
      # Configure PE2.
      
      ```
      [~PE2] interface Cpos-Trunk 24
      ```
      ```
      [*PE2-Cpos-Trunk24] e1 24 unframed
      ```
      ```
      [*PE2-Cpos-Trunk24] commit
      ```
      ```
      [~PE2-Cpos-Trunk24] quit
      ```
      ```
      [~PE2] controller cpos0/2/3
      ```
      ```
      [~PE2-Cpos0/2/3] cpos-Trunk 24
      ```
      ```
      [*PE2-Cpos0/2/3] commit
      ```
      ```
      [~PE2-Cpos0/2/3] quit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] interface Cpos-Trunk 24
      ```
      ```
      [*PE3-Cpos-Trunk24] e1 24 unframed
      ```
      ```
      [*PE3-Cpos-Trunk24] commit
      ```
      ```
      [~PE3-Cpos-Trunk24] quit
      ```
      ```
      [~PE3] controller cpos0/2/3
      ```
      ```
      [~PE3-Cpos0/2/3] cpos-Trunk 24
      ```
      ```
      [*PE3-Cpos0/2/3] commit
      ```
      ```
      [~PE3-Cpos0/2/3] quit
      ```
      
      # Configure CE2.
      
      ```
      [~CE2] interface Cpos-Trunk 24
      ```
      ```
      [*CE2-Cpos-Trunk24] e1 24 unframed
      ```
      ```
      [*CE2-Cpos-Trunk24] commit
      ```
      ```
      [~CE2-Cpos-Trunk24] quit
      ```
      ```
      [~CE2] controller cpos0/2/1
      ```
      ```
      [~CE2-Cpos0/2/1] cpos-Trunk 24
      ```
      ```
      [*CE2-Cpos0/2/1] commit
      ```
      ```
      [~CE2-Cpos0/2/1] quit
      ```
      ```
      [~CE2] controller cpos0/2/2
      ```
      ```
      [~CE2-Cpos0/2/2] cpos-Trunk 24
      ```
      ```
      [*CE2-Cpos0/2/2] commit
      ```
      ```
      [~CE2-Cpos0/2/2] quit
      ```
3. Configure the CPOS-Trunk interface.
   1. Create Global-Mp-Group interfaces.
      
      
      
      # Configure PE2.
      
      ```
      [~PE2] interface Global-Mp-Group 24
      ```
      ```
      [*PE2-Global-Mp-Group24] ip address 172.16.1.2 255.255.255.0
      ```
      ```
      [*PE2-Global-Mp-Group24] commit
      ```
      ```
      [~PE2-Global-Mp-Group24] quit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] interface Global-Mp-Group 24
      ```
      ```
      [*PE3-Global-Mp-Group24] ip address 172.16.1.2 255.255.255.0
      ```
      ```
      [*PE3-Global-Mp-Group24] commit
      ```
      ```
      [~PE3-Global-Mp-Group24] quit
      ```
      
      # Configure CE2.
      
      ```
      [~CE2] interface Global-Mp-Group 24
      ```
      ```
      [*CE2-Global-Mp-Group24] ip address 172.16.1.1 255.255.255.0
      ```
      ```
      [*CE2-Global-Mp-Group24] commit
      ```
      ```
      [~CE2-Global-Mp-Group24] quit
      ```
   2. Add a Trunk-Serial interface to each Global-Mp-Group interface.
      
      
      
      # Configure PE2.
      
      ```
      [~PE2] interface Trunk-Serial 24/24:0
      ```
      ```
      [~PE2-Trunk-Serial24/24:0] link-protocol ppp
      ```
      ```
      [*PE2-Trunk-Serial24/24:0] ppp mp-global global-mp-group 24
      ```
      ```
      [*PE2-Trunk-Serial24/24:0] commit
      ```
      ```
      [~PE2-Trunk-Serial24/24:0] quit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] interface Trunk-Serial 24/24:0
      ```
      ```
      [~PE3-Trunk-Serial24/24:0] link-protocol ppp
      ```
      ```
      [*PE3-Trunk-Serial24/24:0] ppp mp-global global-mp-group 24
      ```
      ```
      [*PE3-Trunk-Serial24/24:0] commit
      ```
      ```
      [~PE3-Trunk-Serial24/24:0] quit
      ```
      
      # Configure CE2.
      
      ```
      [~CE2] interface Trunk-Serial 24/24:0
      ```
      ```
      [~CE2-Trunk-Serial24/24:0] link-protocol ppp
      ```
      ```
      [*CE2-Trunk-Serial24/24:0] ppp mp-global global-mp-group 24
      ```
      ```
      [*CE2-Trunk-Serial24/24:0] commit
      ```
      ```
      [~CE2-Trunk-Serial24/24:0] quit
      ```
4. Bind static routes to the LMSP-enabled interfaces of PE2, PE3, and CE2.
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] ip route-static 192.168.1.0 255.255.255.0 Global-Mp-Group24 172.16.1.1
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   192.168.1.0 is the destination IP address, and 255.255.255.0 is the IP address mask.
   
   # Configure PE3.
   
   ```
   [~PE3] ip route-static 192.168.1.0 255.255.255.0 Global-Mp-Group24 172.16.1.1
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   192.168.1.0 is the destination IP address, and 255.255.255.0 is the IP address mask.
   
   # Configure CE2.
   
   ```
   [~CE2] ip route-static 192.168.2.0 255.255.255.0 Global-Mp-Group24 172.16.1.2
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   192.168.2.0 is the destination IP address, and 255.255.255.0 is the IP address mask.
5. Configure an Interior Gateway Protocol (IGP) and import static routes on PE2, PE3, and CE2. Intermediate System to Intermediate System (IS-IS) is used in this example.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   ```
   ```
   [*PE1-isis-1] is-level level-1
   ```
   ```
   [*PE1-isis-1] network-entity 1111.1111.1111.1111.00
   ```
   ```
   [*PE1-isis-1] graceful-restart
   ```
   ```
   [*PE1-isis-1] cost-style wide-compatible
   ```
   ```
   [*PE1-isis-1] timer spf 1 1 50
   ```
   ```
   [*PE1-isis-1] traffic-eng level-1-2
   ```
   ```
   [*PE1-isis-1] commit
   ```
   ```
   [~PE1-isis-1] quit
   ```
   ```
   [~PE1] interface gigabitEthernet 0/2/1
   ```
   ```
   [~PE1-GigabitEthernet0/2/1] isis enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] commit
   ```
   ```
   [~PE1-GigabitEthernet0/2/1] quit
   ```
   ```
   [~PE1] interface gigabitEthernet 0/2/2
   ```
   ```
   [~PE1-GigabitEthernet0/2/2] isis enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/2/2] commit
   ```
   ```
   [~PE1-GigabitEthernet0/2/2] quit
   ```
   ```
   [~PE1] interface loopback 0
   ```
   ```
   [~PE1-LoopBack0] isis enable 1
   ```
   ```
   [~PE1-LoopBack0] commit
   ```
   ```
   [~PE1-LoopBack0] quit
   ```
   
   # Configure P1.
   
   ```
   [~P1] isis 1
   ```
   ```
   [*P1-isis-1] is-level level-1
   ```
   ```
   [*P1-isis-1] network-entity 2222.2222.2222.2222.00
   ```
   ```
   [*P1-isis-1] graceful-restart
   ```
   ```
   [*P1-isis-1] cost-style wide-compatible
   ```
   ```
   [*P1-isis-1] timer spf 1 1 50
   ```
   ```
   [*P1-isis-1] traffic-eng level-1-2
   ```
   ```
   [*P1-isis-1] commit
   ```
   ```
   [~P1-isis-1] quit
   ```
   ```
   [~P1] interface gigabitEthernet 0/2/1
   ```
   ```
   [~P1-GigabitEthernet0/2/1] isis enable 1
   ```
   ```
   [*P1-GigabitEthernet0/2/1] commit
   ```
   ```
   [~P1-GigabitEthernet0/2/1] quit
   ```
   ```
   [~P1] interface gigabitEthernet 0/2/5
   ```
   ```
   [~P1-GigabitEthernet0/2/5] isis enable 1
   ```
   ```
   [*P1-GigabitEthernet0/2/5] commit
   ```
   ```
   [~P1-GigabitEthernet0/2/5] quit
   ```
   ```
   [~P1] interface loopback 0
   ```
   ```
   [~P1-LoopBack0] isis enable 1
   ```
   ```
   [*P1-LoopBack0] commit
   ```
   ```
   [~P1-LoopBack0] quit
   ```
   
   # Configure P2.
   
   ```
   [~P2] isis 1
   ```
   ```
   [*P2-isis-1] is-level level-1
   ```
   ```
   [*P2-isis-1] network-entity 3333.3333.3333.3333.00
   ```
   ```
   [*P2-isis-1] graceful-restart
   ```
   ```
   [*P2-isis-1] cost-style wide-compatible
   ```
   ```
   [*P2-isis-1] timer spf 1 1 50
   ```
   ```
   [*P2-isis-1] traffic-eng level-1-2
   ```
   ```
   [*P2-isis-1] commit
   ```
   ```
   [~P2-isis-1] quit
   ```
   ```
   [~P2] interface gigabitEthernet 0/2/2
   ```
   ```
   [~P2-GigabitEthernet0/2/2] isis enable 1
   ```
   ```
   [*P2-GigabitEthernet0/2/2] commit
   ```
   ```
   [~P2-GigabitEthernet0/2/2] quit
   ```
   ```
   [~P2] interface gigabitEthernet 0/2/1
   ```
   ```
   [~P2-GigabitEthernet0/2/1] isis enable 1
   ```
   ```
   [*P2-GigabitEthernet0/2/1] commit
   ```
   ```
   [~P2-GigabitEthernet0/2/1] quit
   ```
   ```
   [~P2] interface loopback 0
   ```
   ```
   [~P2-LoopBack0] isis enable 1
   ```
   ```
   [*P2-LoopBack0] commit
   ```
   ```
   [~P2-LoopBack0] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   ```
   ```
   [*PE2-isis-1] import-route static
   ```
   ```
   [*PE2-isis-1] is-level level-1
   ```
   ```
   [*PE2-isis-1] network-entity 4444.4444.4444.4444.00
   ```
   ```
   [*PE2-isis-1] graceful-restart
   ```
   ```
   [*PE2-isis-1] cost-style wide-compatible
   ```
   ```
   [*PE2-isis-1] timer spf 1 1 50
   ```
   ```
   [*PE2-isis-1] traffic-eng level-1-2
   ```
   ```
   [*PE2-isis-1] commit
   ```
   ```
   [~PE2-isis-1] quit
   ```
   ```
   [~PE2] interface gigabitEthernet 0/2/1
   ```
   ```
   [~PE2-GigabitEthernet0/2/1] isis enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/2/1] commit
   ```
   ```
   [~PE2-GigabitEthernet0/2/1] quit
   ```
   ```
   [~PE2] interface gigabitEthernet 0/2/2
   ```
   ```
   [~PE2-GigabitEthernet0/2/2] isis enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/2/2] commit
   ```
   ```
   [~PE2-GigabitEthernet0/2/2] quit
   ```
   ```
   [~PE2] interface loopback 0
   ```
   ```
   [~PE2-LoopBack0] isis enable 1
   ```
   ```
   [*PE2-LoopBack0] commit
   ```
   ```
   [~PE2-LoopBack0] quit
   ```
   ```
   [~PE2] interface global-mp-group 24
   ```
   ```
   [*PE2-Global-Mp-Group24] isis enable 1
   ```
   ```
   [*PE2-Global-Mp-Group24] commit
   ```
   ```
   [~PE2-Global-Mp-Group24] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] isis 1
   ```
   ```
   [*PE3-isis-1] import-route static
   ```
   ```
   [*PE3-isis-1] is-level level-1
   ```
   ```
   [*PE3-isis-1] network-entity 5555.5555.5555.5555.00
   ```
   ```
   [*PE3-isis-1] graceful-restart
   ```
   ```
   [*PE3-isis-1] cost-style wide-compatible
   ```
   ```
   [*PE3-isis-1] timer spf 1 1 50
   ```
   ```
   [*PE3-isis-1] traffic-eng level-1-2
   ```
   ```
   [*PE3-isis-1] commit
   ```
   ```
   [~PE3-isis-1] quit
   ```
   ```
   [~PE3] interface gigabitEthernet 0/2/1
   ```
   ```
   [~PE3-GigabitEthernet0/2/1] isis enable 1
   ```
   ```
   [*PE3-GigabitEthernet0/2/1] commit
   ```
   ```
   [~PE3-GigabitEthernet0/2/1] quit
   ```
   ```
   [~PE3] interface gigabitEthernet 0/2/2
   ```
   ```
   [~PE3-GigabitEthernet0/2/2] isis enable 1
   ```
   ```
   [*PE3-GigabitEthernet0/2/2] commit
   ```
   ```
   [~PE3-GigabitEthernet0/2/2] quit
   ```
   ```
   [~PE3] interface loopback 0
   ```
   ```
   [~PE3-LoopBack0] isis enable 1
   ```
   ```
   [*PE3-LoopBack0] commit
   ```
   ```
   [~PE3-LoopBack0] quit
   ```
   ```
   [~PE3] interface global-mp-group 24
   ```
   ```
   [*PE3-Global-Mp-Group24] isis enable 1
   ```
   ```
   [*PE3-Global-Mp-Group24] commit
   ```
   ```
   [~PE3-Global-Mp-Group24] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] isis 1
   ```
   ```
   [*CE2-isis-1] import-route static
   ```
   ```
   [*CE2-isis-1] is-level level-1
   ```
   ```
   [*CE2-isis-1] network-entity 5555.5555.5555.5555.00
   ```
   ```
   [*CE2-isis-1] graceful-restart
   ```
   ```
   [*CE2-isis-1] cost-style wide-compatible
   ```
   ```
   [*CE2-isis-1] timer spf 1 1 50
   ```
   ```
   [*CE2-isis-1] traffic-eng level-1-2
   ```
   ```
   [*CE2-isis-1] commit
   ```
   ```
   [~CE2-isis-1] quit
   ```
   ```
   [~CE2] interface global-mp-group 24
   ```
   ```
   [*CE2-Global-Mp-Group24] isis enable 1
   ```
   ```
   [*CE2-Global-Mp-Group24] commit
   ```
   ```
   [~CE2-Global-Mp-Group24] quit
   ```
6. Verify the configuration.
   
   
   
   # Run the **display aps group** command on PE2, PE3, and CE2 to view the MC-LMSP configurations.
   
   ```
   [~PE2] display aps group 24
   ```
   ```
   APS Group 24: Cpos0/2/3 working channel 1(Active)
                        PGP authentication string: 1234
                        APS protection channel is 5.5.5.5
   --------------------------------------------------------------------------------
   Group Work-Channel Protect-Channel Wtr W-State P-State Switch-Cmd Switch-Result
   --------------------------------------------------------------------------------
   24      Cpos0/2/3     5.5.5.5       NA   ok      ok     NA          idle
   --------------------------------------------------------------------------------
   ```
   ```
   [~PE3] display aps group 24
   ```
   ```
   APS Group 24: APS working channel is 4.4.4.4
                        Cpos0/2/3 protection channel 0(Inactive)
                        PGP authentication string: 1234
                        Bidirection, 1:1 mode, Revert time(1 minutes)
                        KeepAlive Timer: 2(seconds), Hold Timer: 200(seconds)
                        No Request on Both Working and Protection Side
   --------------------------------------------------------------------------------
   Group Work-Channel Protect-Channel Wtr W-State P-State Switch-Cmd Switch-Result
   --------------------------------------------------------------------------------
   24     4.4.4.4       Cpos0/2/3      1    ok      ok     NA          idle
   --------------------------------------------------------------------------------
   
   ```
   ```
   [~CE2] display aps group 24
   ```
   ```
   APS Group 24: Cpos0/2/1 working channel 1(Active)                        
                        Cpos0/2/2 protection channel 0(Inactive)                      
                        Bidirection, 1:1 mode, Revert time(1 minutes)                                      
                        No Request on Both Working and Protection Side
   --------------------------------------------------------------------------------
   Group Work-Channel Protect-Channel Wtr W-State P-State Switch-Cmd Switch-Result
   --------------------------------------------------------------------------------
   24     Cpos0/2/1    Cpos0/2/2       1    ok      ok     NA          idle
   --------------------------------------------------------------------------------
   
   ```
   
   # Run the **display current-configuration | include route** command on PE2, PE3, and CE2 to view the configured parameters.
   
   ```
   [~PE2] display current-configuration | include route
   ```
   ```
   import-route static
   ip route-static 192.168.1.0 255.255.255.0 Global-Mp-Group24 172.16.1.1
   ```
   ```
   [~PE3] display current-configuration | include route
   ```
   ```
   import-route static                                                        
   ip route-static 192.168.1.0 255.255.255.0 Global-Mp-Group24 172.16.1.1 
   
   ```
   ```
   [~CE2] display current-configuration | include route
   ```
   ```
   import-route static         
   ip route-static 192.168.2.0 255.255.255.0 Global-Mp-Group24 172.16.1.2  
   
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #                                                                               
   sysname PE1                                                              
   isis 1 
    is-level level-1
    network-entity 1111.1111.1111.1111.00
    graceful-restart
    cost-style wide-compatible
    timer spf 1 1 50
    traffic-eng level-1-2
  
  #
   interface gigabitEthernet 0/2/1
    isis enable 1
  #
   interface gigabitEthernet 0/2/2
    isis enable 1
  #
   interface loopBack 0
    ip address 1.1.1.1 32
  
  #
  return 
  ```
* P1 configuration file
  
  ```
   isis 1
    is-level level-1
    network-entity 2222.2222.2222.2222.00
    graceful-restart
    cost-style wide-compatible
    timer spf 1 1 50
    traffic-eng level-1-2
  
  #
   interface gigabitEthernet 0/2/1
    isis enable 1
  
   interface gigabitEthernet 0/2/5
    isis enable 1
  #
   interface loopBack 0
    ip address 2.2.2.2 32
  
  #
  return
  ```
* P2 configuration file
  
  ```
   isis 1
    is-level level-1
    network-entity 3333.3333.3333.3333.00
    graceful-restart
    cost-style wide-compatible
    timer spf 1 1 50
    traffic-eng level-1-2
  
  #
   interface gigabitEthernet 0/2/2
    isis enable 1
  #
   interface gigabitEthernet 0/2/1
    isis enable 1
  #
   interface loopBack 0
    ip address 3.3.3.3 32
  
  #
  return
  ```
* PE2 configuration file
  
  ```
   isis 1
    import-route static
    is-level level-1
    network-entity 4444.4444.4444.4444.00
    graceful-restart
    cost-style wide-compatible
    timer spf 1 1 50
    traffic-eng level-1-2
  
  #
   ip route-static 192.168.1.0 255.255.255.0 Global-Mp-Group24 172.16.1.1
  #
   interface Cpos-Trunk24                                                          
    e1 24 unframed
  
  #
   interface gigabitEthernet 0/2/1
    isis enable 1
  #
   interface gigabitEthernet 0/2/2
    isis enable 1
  #
   interface global-mp-group 24
    isis enable 1
  #
   interface loopBack 0
    ip address 4.4.4.4 32
  
  #
   controller Cpos0/2/3
    undo shutdown
    aps group 24
    aps working 4.4.4.4 5.5.5.5
    aps authenticate cipher %^%#'d`;Ykv]v5U4q.%+'D`8m{YlN#D&uX:CS](*\.b$%^%# hmac
    cpos-trunk 24
  
  #
   interface Trunk-Serial24/24:0
    link-protocol ppp
    ppp mp-global global-mp-group 24
  
  #
   interface Global-Mp-Group24
    ip address 172.16.1.2 255.255.255.0
  
  #
  return
  
  ```
* PE3 configuration file
  
  ```
   isis 1
    import-route static
    is-level level-1
    network-entity 5555.5555.5555.5555.00
    graceful-restart
    cost-style wide-compatible
    timer spf 1 1 50
    traffic-eng level-1-2
  
  #
   interface gigabitEthernet 0/2/1
    isis enable 1
  #
   interface gigabitEthernet 0/2/2
    isis enable 1
  #
  interface global-mp-group 24
    isis enable 1
  #
   interface loopBack 0
    ip address 5.5.5.5 32
  
  #
   controller Cpos0/2/3                                                            
    undo shutdown                                                                  
    aps group 24                                                                   
    aps protect 4.4.4.4 5.5.5.5
    aps authenticate cipher %^%#'d`;Ykv]v5U4q.%+'D`8m{YlN#D&uX:CS](*\.b$%^%# hmac
    aps mode one2one bidirection                                                   
    aps revert 1                                                                   
    cpos-trunk 24 
  
  #
   interface Cpos-Trunk24                                                          
    e1 24 unframed
  
  #
   interface Trunk-Serial24/24:0                                                   
    link-protocol ppp                                                              
    ppp mp-global global-mp-group 24 
  
  #
   interface Global-Mp-Group24                                                     
    ip address 172.16.1.2 255.255.255.0
  
  #
  return
  
  ```
* CE2 configuration file
  ```
  #
   isis 1
    import-route static
    is-level level-1
    network-entity 5555.5555.5555.5555.00
    graceful-restart
    cost-style wide-compatible
    timer spf 1 1 50
    traffic-eng level-1-2
  #
   ip route-static 192.168.2.0 255.255.255.0 Global-Mp-Group24 172.16.1.2
  #
   interface Cpos-Trunk 24
    e1 24 unframed
  #
   controller cpos2/0/1
    undo shutdown
    aps group 24
    aps working
    cpos-Trunk 24
  #
   controller cpos2/0/2
    undo shutdown
    aps group 24
    aps protect
    aps mode one2one bidirection
    aps revert 1
    cpos-Trunk 24
  #
   interface Trunk-Serial 24/24:0
    link-protocol ppp
    ppp mp-global global-mp-group 24
  #
   interface global-mp-group 24
    ip address 172.16.1.1 255.255.255.0
    isis enable 1
  #
  ```