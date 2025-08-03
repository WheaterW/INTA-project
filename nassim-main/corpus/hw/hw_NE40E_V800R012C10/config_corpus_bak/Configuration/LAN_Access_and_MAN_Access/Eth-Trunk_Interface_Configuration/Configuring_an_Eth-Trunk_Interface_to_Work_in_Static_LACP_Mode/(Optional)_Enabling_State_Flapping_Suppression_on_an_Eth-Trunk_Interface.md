(Optional) Enabling State Flapping Suppression on an Eth-Trunk Interface
========================================================================

You can enable state flapping suppression on an Eth-Trunk interface to prevent the Eth-Trunk interface from alternating between up and down due to member interface state flapping or received incorrect packets.

#### Context

* If the state of an Eth-Trunk interface frequently flaps, the LACP protocol status of the Eth-Trunk interface also flaps, affecting the Eth-Trunk interface operations. To resolve this problem, enable state flapping suppression on the Eth-Trunk interface working in LACP mode.
* By default, an Eth-Trunk interface in LACP mode is enabled to suppress invalid MAC addresses in Ethernet headers of received LACPDUs from flapping, in which case the source MAC addresses of the LACPDUs and system ID are checked. To disable the check, run the **lacp dampening unexpected-mac disable** command to disable MAC address flapping suppression in Ethernet headers of LACPDUs.

#### Procedure

* Enable state flapping suppression on an Eth-Trunk interface.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
     
     The Eth-Trunk interface view is displayed.
  3. Run [**lacp dampening state-flapping disable**](cmdqueryname=lacp+dampening+state-flapping+disable)
     
     State flapping suppression is enabled on the Eth-Trunk interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Disable invalid-MAC-packet-based state flapping suppression on an Eth-Trunk interface.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
     
     The Eth-Trunk interface view is displayed.
  3. Run [**lacp dampening unexpected-mac**](cmdqueryname=lacp+dampening+unexpected-mac)
     
     Invalid-MAC-packet-based state flapping suppression is disabled on the Eth-Trunk interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.