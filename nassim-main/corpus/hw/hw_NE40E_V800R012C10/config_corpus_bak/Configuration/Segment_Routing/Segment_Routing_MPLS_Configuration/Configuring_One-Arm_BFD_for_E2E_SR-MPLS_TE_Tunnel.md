Configuring One-Arm BFD for E2E SR-MPLS TE Tunnel
=================================================

One-arm BFD for E2E SR-MPLS TE tunnel quickly detects faults on inter-AS E2E SR-MPLS TE tunnels and protects traffic on the E2E SR-MPLS TE tunnels.

#### Usage Scenario

If one-arm BFD for inter-AS E2E SR-MPLS TE tunnel detects a fault on the primary tunnel, a protection application, for example, VPN FRR, rapidly switches traffic, which minimizes the impact on traffic.

With one-arm BFD for E2E SR-MPLS TE tunnel enabled, if the reflector can successfully recurse packets to the E2E SR-MPLS TE tunnel using the IP address of the initiator, the reflector forwards the packets through the E2E SR-MPLS TE tunnel. Otherwise, the reflector forwards the packets over IP routes.


#### Pre-configuration Tasks

Before configuring one-arm BFD for E2E SR-MPLS TE tunnel, configure an inter-AS E2E SR-MPLS TE tunnel.


#### Procedure

1. Enable BFD globally.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bfd**](cmdqueryname=bfd)
      
      
      
      BFD is enabled.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Enable the ingress to dynamically create a BFD session to monitor E2E SR-MPLS TE tunnels.
   
   
   
   Perform either of the following operations:
   
   * Globally enable the capability if BFD sessions need to be automatically created for most E2E SR-MPLS TE tunnels on the ingress.
   * Enable the capability on a specific tunnel interface if a BFD session needs to be automatically created for some E2E SR-MPLS TE tunnels on the ingress.
   
   Perform the following operations as required:
   
   
   
   * **Enable the capability globally.**
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**mpls**](cmdqueryname=mpls)
        
        The MPLS view is displayed.
     3. Run [**mpls te bfd tunnel enable one-arm-echo**](cmdqueryname=mpls+te+bfd+tunnel+enable+one-arm-echo)
        
        One-arm BFD for E2E SR-MPLS TE tunnel is enabled.
     4. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     5. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
        
        The view of the E2E SR-MPLS TE tunnel interface is displayed.
     6. Run [**mpls te reverse-lsp binding-sid**](cmdqueryname=mpls+te+reverse-lsp+binding-sid) **label** *label-value*
        
        A binding SID is set for a reverse LSP in the E2E SR-MPLS TE tunnel.
        
        Ensure that the [**mpls te binding-sid**](cmdqueryname=mpls+te+binding-sid) **label** *label-value* command has been run on the ingress of the reverse LSP.
     7. (Optional) Run [**mpls te bfd block**](cmdqueryname=mpls+te+bfd+block)
        
        The capability of automatically creating BFD sessions for the E2E SR-MPLS TE tunnel is blocked.
        
        If some SR-MPLS TE tunnels do not need to be monitored using BFD for E2E SR-MPLS TE tunnel, block this capability on each tunnel interface:
     8. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * **Enable the capability on a tunnel interface.**
     + Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
     + Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
       
       The view of the E2E SR-MPLS TE tunnel interface is displayed.
     + Run [**mpls te bfd tunnel enable one-arm-echo**](cmdqueryname=mpls+te+bfd+tunnel+enable+one-arm-echo)
       
       One-arm BFD for E2E SR-MPLS TE tunnel is enabled.
       
       This command run in the tunnel interface view takes effect only on the tunnel interface.
     + Run [**mpls te reverse-lsp binding-sid**](cmdqueryname=mpls+te+reverse-lsp+binding-sid) **label** *label-value*
       
       A binding SID is set for a reverse LSP in the E2E SR-MPLS TE tunnel.
       
       Ensure that the [**mpls te binding-sid**](cmdqueryname=mpls+te+binding-sid) **label** *label-value* command has been run on the ingress of the reverse LSP.
     + Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
3. (Optional) Adjust BFD parameters on the ingress.
   
   
   
   Adjust BFD parameters on the ingress in either of the following modes:
   
   * Adjust BFD parameters globally. This method is used when BFD parameters for most E2E SR-MPLS TE tunnels need to be adjusted on the ingress.
   * Adjust BFD parameters on a specific tunnel interface. If an E2E SR-MPLS TE tunnel interface needs BFD parameters different from the globally configured ones, adjust BFD parameters on the specific tunnel interface.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In one-arm BFD for E2E SR-MPLS TE mode, BFD does not need to be enabled on the peer, and the **min-tx-interval** *tx-interval* parameter of the local end does not take effect. Therefore, the actual detection period of the ingress equals the configured interval at which BFD packets are received on the ingress multiplied by the detection multiplier configured on the ingress.
   
   Perform the following operations as required:
   
   
   
   * **Adjust BFD parameters globally.**
     + Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
     + Run [**mpls**](cmdqueryname=mpls)
       
       The MPLS view is displayed.
     + Run [**mpls te bfd tunnel**](cmdqueryname=mpls+te+bfd+tunnel) { **min-rx-interval** *rx-interval* | **detect-multiplier** *multiplier* } \*
       
       BFD parameters are set.
     + Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
   * **Adjust BFD parameters on a specific tunnel interface.**
     + Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
     + Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
       
       The tunnel interface view is displayed.
     + Run [**mpls te bfd tunnel**](cmdqueryname=mpls+te+bfd+tunnel) { **min-rx-interval** *rx-interval* | **detect-multiplier** *multiplier* } \*
       
       BFD parameters are set.
     + Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.

#### Verifying the Configuration

After successfully configuring one-arm BFD for E2E SR-MPLS TE tunnel, verify the configurations.

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) **dynamic** [ **verbose** ] command to check information about BFD sessions on the ingress.
* Run the following commands to check BFD statistics:
  + Run the [**display bfd statistics**](cmdqueryname=display+bfd+statistics) command to check all BFD statistics.
  + Run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) **dynamic** command to check statistics about dynamic BFD sessions.