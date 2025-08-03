Configuring Dynamic BFD for SR-MPLS TE LSP
==========================================

Dynamic BFD for SR-MPLS TE LSP rapidly detects faults of SR-MPLS TE LSPs, which protects traffic transmitted on SR-MPLS TE LSPs.

#### Usage Scenario

BFD detects the connectivity of SR-MPLS TE LSPs. Dynamic BFD for SR-MPLS TE LSP is configured to rapidly switch traffic from a primary LSP to a backup LSP if the primary LSP fails. Unlike static BFD for SR-MPLS TE LSP, dynamic BFD for SR-MPLS TE LSP simplifies the configuration and minimizes manual configuration errors.

Dynamic BFD can only monitor a part of an SR-MPLS TE tunnel.


#### Pre-configuration Tasks

Before configuring dynamic BFD for SR-MPLS TE LSP, complete the following task:

* Configure an SR-MPLS TE tunnel.

#### Procedure

1. Enable BFD globally.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bfd**](cmdqueryname=bfd)
      
      
      
      BFD is enabled globally, and the BFD view is displayed.
      
      You can set BFD parameters only after running the [**bfd**](cmdqueryname=bfd) command to enable BFD globally.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Enable the ingress to dynamically create a BFD session to monitor SR-MPLS TE LSPs.
   
   
   
   Perform either of the following operations to enable the ingress to dynamically create a BFD session to monitor SR-MPLS TE LSPs:
   
   * Globally enable the capability if BFD sessions need to be automatically created for most SR-MPLS TE tunnels on the ingress.
   * Enable the capability on a specific tunnel interface if a BFD session needs to be automatically created for a specific or some SR-MPLS TE tunnels on the ingress.
   
   Perform the following operations as required:
   
   
   
   * **Globally enable the capability.**
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**mpls**](cmdqueryname=mpls)
        
        The MPLS view is displayed.
     3. Run [**mpls te bfd enable**](cmdqueryname=mpls+te+bfd+enable) [ **one-arm-echo** ]
        
        The ingress is configured to automatically create a BFD session for each SR-MPLS TE tunnel.
        
        After this command is run in the MPLS view, BFD for SR-MPLS TE LSP is enabled on all tunnel interfaces, except the tunnel interfaces on which BFD for SR-MPLS TE LSP is blocked.
        
        If **one-arm-echo** is configured, a one-arm BFD echo session is established to monitor an SR-MPLS TE LSP.
        
        If the egress does not support BFD for SR-MPLS TE, BFD sessions cannot be created. To address this issue, configure one-arm BFD.
     4. (Optional) If some SR-MPLS TE tunnels do not need to be monitored using BFD for SR-MPLS TE LSP, block BFD for SR-MPLS TE LSP on each tunnel interface:
        1. Run [**quit**](cmdqueryname=quit)
           
           Return to the system view.
        2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
           
           The SR-MPLS TE tunnel interface view is displayed.
        3. Run [**mpls te bfd block**](cmdqueryname=mpls+te+bfd+block)
           
           The tunnel interface is disabled from automatically creating a BFD session to monitor an SR-MPLS TE tunnel.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * **Enable the capability on a tunnel interface.**
     + Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
     + Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
       
       The view of the SR-MPLS TE tunnel interface is displayed.
     + Run [**mpls te bfd enable**](cmdqueryname=mpls+te+bfd+enable) [ **one-arm-echo** ]
       
       The ingress is configured to automatically create a BFD session for the tunnel.
       
       This command run in the tunnel interface view takes effect only on the tunnel interface.
       
       If **one-arm-echo** is configured, a one-arm BFD echo session is established to monitor an SR-MPLS TE LSP. A Huawei device at the ingress cannot use BFD for SR-MPLS TE LSP to communicate with a non-Huawei device at the egress. In this situation, no BFD session can be established. To address this issue, configure one-arm BFD.
     + Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
3. Enable the egress to passively create a BFD session.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bfd**](cmdqueryname=bfd)
      
      
      
      The BFD view is displayed.
   3. Run [**mpls-passive**](cmdqueryname=mpls-passive)
      
      
      
      The egress is enabled to create a BFD session passively.
      
      The egress has to receive an LSP ping request carrying a BFD TLV before creating a BFD session.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
4. (Optional) Adjust BFD parameters on the ingress.
   
   
   
   Adjust BFD parameters on the ingress in either of the following modes:
   
   * Adjust BFD parameters globally. This method is used when BFD parameters for most SR-MPLS TE tunnels need to be adjusted on the ingress.
   * Adjust BFD parameters on a specific tunnel interface. If an SR-MPLS TE tunnel interface needs BFD parameters different from the globally configured ones, adjust BFD parameters on the specific tunnel interface.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Effective local interval at which BFD packets are sent = MAX { Locally configured interval at which BFD packets are sent, Remotely configured interval at which BFD packets are received }
   * Effective local interval at which BFD packets are received = MAX { Remotely configured interval at which BFD packets are sent, Locally configured interval at which BFD packets are received }
   * Effective local BFD detection period = Effective local interval at which BFD packets are received x Remotely configured BFD detection multiplier
   
   On the egress that passively creates a BFD session, the BFD parameters cannot be adjusted, because the default values are the smallest values that can be set on the ingress. Therefore, if BFD for TE is used, the effective BFD detection period on both ends of an SR-MPLS TE tunnel is as follows:
   
   * Effective detection period on the ingress = Configured interval at which BFD packets are received on the ingress x 3
   * Effective detection period on the egress = Configured interval at which BFD packets are sent on the ingress x Configured detection multiplier on the ingress
   
   Perform the following operations as required:
   
   
   
   * **Adjust BFD parameters globally.**
     + Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
     + Run [**mpls**](cmdqueryname=mpls)
       
       The MPLS view is displayed.
     + Run [**mpls te bfd**](cmdqueryname=mpls+te+bfd) { **min-tx-interval** *tx-interval* | **min-rx-interval** *rx-interval* | **detect-multiplier** *multiplier* }\*
       
       The BFD parameters are set.
     + Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
   * **Adjust BFD parameters on a specific tunnel interface.**
     + Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
     + Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
       
       The tunnel interface view is displayed.
     + Run [**mpls te bfd**](cmdqueryname=mpls+te+bfd) { **min-tx-interval** *tx-interval* | **min-rx-interval** *rx-interval* | **detect-multiplier** *multiplier* }\*
       
       The BFD parameters are set.
     + Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.

#### Verifying the Configuration

After the configuration of dynamic BFD for SR-MPLS TE LSP is complete, verify the configurations.

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) **dynamic** [ **verbose** ] command to check information about BFD sessions on the ingress.
* Run the [**display bfd session**](cmdqueryname=display+bfd+session) **passive-dynamic** [ **peer-ip** *peer-ip* **remote-discriminator** *discriminator* ] [ **verbose** ] command to check information about BFD sessions that are passively created on the egress.
* Run the following commands to check BFD statistics:
  + Run the [**display bfd statistics**](cmdqueryname=display+bfd+statistics) command to check all BFD statistics.
  + Run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) **dynamic** command to check statistics about dynamic BFD sessions.
* Run the [**display mpls bfd session**](cmdqueryname=display+mpls+bfd+session) { **protocol** **rsvp-te** | **outgoing-interface** *interface-type* *interface-number* } [ **verbose** ] command to check information about BFD sessions for MPLS.