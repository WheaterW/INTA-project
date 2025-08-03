Configuring Dynamic BFD for RIP
===============================

On a network that runs high-rate data services, dynamic BFD for RIP can be configured to quickly detect and respond to network faults.

#### Usage Scenario

RIP-capable devices detect neighbor status by exchanging Update packets periodically. The default value of the aging timer is 180s. If a link fault occurs, RIP can detect the fault only after 180s. During this period, carriers or users may lose a large number of packets.

BFD can detect a fault (if any) within milliseconds and notify the RIP module of the fault. BFD for RIP can speed up fault detection and route convergence, which improves network reliability.

In BFD for RIP, BFD session establishment is triggered by RIP. When establishing a neighbor relationship, RIP will send detection parameters of the neighbor to BFD. Then, a BFD session will be established based on these detection parameters. If a link fault occurs, the local RIP process will receive a neighbor unreachable message within milliseconds. Then, the local RIP device will delete routing entries in which the neighbor relationship is Down and use the backup path to transmit messages.

Either of the following methods can be used to configure BFD for RIP:

* [Enable BFD in a RIP process](#EN-US_TASK_0172365867__step_dc_vrp_rip_cfg_005501): This method is feasible when BFD for RIP needs to be enabled on most RIP interfaces.
* [Enable BFD on RIP interface](#EN-US_TASK_0172365867__step_dc_vrp_rip_cfg_005502): This method is recommended when BFD for RIP needs to be enabled only on a small number of RIP interfaces.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The interface can be a physical interface or a GRE tunnel interface. If BFD is enabled on a GRE tunnel interface, millisecond-level fault detection can be implemented for the GRE tunnel.


#### Pre-configuration Tasks

Before configuring BFD for RIP, complete the following tasks:

* Assign an IP address to each interface to ensure that neighboring nodes are reachable at the network layer.
* [Configuring Basic RIP Functions](dc_vrp_rip_cfg_0003.html)

#### Procedure

* Enable BFD in a RIP process.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**rip**](cmdqueryname=rip) *process-id*
     
     
     
     The RIP view is displayed.
  5. Run [**bfd all-interfaces enable**](cmdqueryname=bfd+all-interfaces+enable)
     
     
     
     BFD is enabled in the RIP process to establish BFD sessions.
     
     
     
     If BFD is enabled globally, RIP will use default BFD parameters to establish BFD sessions on all the interfaces where RIP neighbor relationships are up in the process.
  6. (Optional) Run [**bfd all-interfaces**](cmdqueryname=bfd+all-interfaces) { **min-rx-interval** *min-receive-value* | **min-tx-interval** *min-transmit-value* | **detect-multiplier** *detect-multiplier-value* } \*
     
     
     
     The values of BFD parameters used to establish the BFD session are set.
     
     Configure BFD parameter values based on the reliability requirements of the live network.
     + If the live network requires high reliability, reduce the interval at which BFD packets are sent.
     + If the live network requires low reliability, increase the interval at which BFD packets are sent.BFD detection intervals are calculated as follows:
     + Effective local interval at which BFD packets are sent = MAX { Configured local interval at which BFD packets are sent, Configured remote interval at which BFD packets are received }
     + Effective local interval at which BFD packets are received = MAX { Configured remote interval at which BFD packets are sent, Configured local interval at which BFD packets are received }
     + Effective local detection interval = Effective local interval at which BFD packets are received x Configured remote detection multiplier
     
     Running the [**bfd all-interfaces**](cmdqueryname=bfd+all-interfaces) command changes BFD session parameters on all RIP interfaces. The default detection multiplier and interval at which BFD packets are sent are recommended.
  7. (Optional) Perform the following operations to prevent an interface in the RIP process from establishing a BFD session:
     
     
     + Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     + Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of a specified interface.
     + Run the [**rip bfd block**](cmdqueryname=rip+bfd+block) command to prevent the interface from establishing a BFD session.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable BFD on a RIP interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the specified interface is displayed.
  5. Run [**rip bfd enable**](cmdqueryname=rip+bfd+enable)
     
     
     
     BFD is enabled on the interface to establish a BFD session.
  6. (Optional) Run [**rip bfd**](cmdqueryname=rip+bfd) { **min-rx-interval** *min-receive-value* | **min-tx-interval**  *min-transmit-value* | **detect-multiplier** *detect-multiplier-value* } \*
     
     
     
     The values of BFD parameters used to establish the BFD session are set.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Checking the Configurations

After enabling BFD for RIP at both ends of a link, run the [**display rip bfd session**](cmdqueryname=display+rip+bfd+session) { **interface** *interface-type* *interface-number* | *neighbor-id* | **all** } command. The following command output shows that the **BFDState** field on the local Router is Up.