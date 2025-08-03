Configuring Flapping Suppression on an Eth-Trunk Interface
==========================================================

Configuring Flapping Suppression on an Eth-Trunk Interface

#### Context

Flapping suppression functions on an Eth-Trunk interface include state flapping suppression and invalid-MAC-based state flapping suppression.

* If the state of an Eth-Trunk interface frequently flaps, the LACP protocol status of the Eth-Trunk interface also flaps, affecting the Eth-Trunk interface operations. To resolve this problem, enable state flapping suppression on Eth-Trunk interfaces working in LACP mode.
* After LACP negotiation succeeds on an Eth-Trunk interface, the Eth-Trunk interface will save and check the source MAC address of the most recently received packets. If the Eth-Trunk interface receives a packet with a different source MAC address from that saved one, the Eth-Trunk interface may alternate between up and down due to renegotiation. To prevent this problem, the invalid-MAC-based state flapping suppression function is enabled on devices by default. When receiving a packet with an invalid source MAC address (different source MAC address from the saved one), an Eth-Trunk drops the packet and records the packet information. This function can be disabled if there is no need to check source MAC addresses of packets.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of an Eth-Trunk interface.
   
   
   ```
   [interface](cmdqueryname=interface) eth-trunk trunk-id
   ```
3. Perform the following configurations as required.
   
   
   * Enable the state flapping suppression function on an Eth-Trunk interface.
     ```
     [lacp dampening state-flapping](cmdqueryname=lacp+dampening+state-flapping)
     ```
     
     By default, state flapping suppression is disabled on an Eth-Trunk interface.
   * Enable the invalid-MAC-based state flapping suppression function on an Eth-Trunk interface.
     ```
     [undo lacp dampening unexpected-mac disable](cmdqueryname=undo+lacp+dampening+unexpected-mac+disable)
     ```
     
     By default, the invalid-MAC-based state flapping suppression function is enabled on an Eth-Trunk interface.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```