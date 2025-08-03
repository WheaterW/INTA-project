Configuring the Port Link Type (for RSTP/MSTP)
==============================================

Configuring the Port Link Type (for RSTP/MSTP)

#### Context

P2P links facilitate fast convergence. If a P2P link connects two root or designated ports, the ports can send Proposal and Agreement packets to change to the Forwarding state quickly. This reduces the forwarding delay.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure the port link type.
   
   
   ```
   [stp point-to-point](cmdqueryname=stp+point-to-point) { auto | force-false | force-true }
   ```
   
   The default link type for a port is auto, where RSTP or MSTP automatically detects whether the port is connected to a P2P link.
   
   * If the Ethernet port works in full-duplex mode, it is connected to a P2P link, and the [**stp point-to-point**](cmdqueryname=stp+point-to-point) **force-true** command can be used for fast convergence.
   * If the Ethernet port works in half-duplex mode, the [**stp point-to-point**](cmdqueryname=stp+point-to-point) **force-true** command can be used to set the port link type to P2P for fast convergence.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] [ **instance** *instance-id* ] [ **interface** *interface-type* *interface-number* | **slot** *slot-id* ] command and check the Point-to-point field to verify the port link type configuration.