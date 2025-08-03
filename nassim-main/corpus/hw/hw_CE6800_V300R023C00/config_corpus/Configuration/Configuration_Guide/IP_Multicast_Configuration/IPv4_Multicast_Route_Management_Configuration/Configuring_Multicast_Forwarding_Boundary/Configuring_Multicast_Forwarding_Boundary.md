Configuring Multicast Forwarding Boundary
=========================================

Configuring Multicast Forwarding Boundary

#### Context

Multicast forwarding boundary configured for a multicast group on a multicast device's interface specifies where multicast packets can be forwarded.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the multicast function.
   
   
   ```
   [multicast routing-enable](cmdqueryname=multicast+routing-enable)
   ```
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the working mode of the interface from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Configure multicast forwarding boundary.
   
   
   ```
   [multicast boundary](cmdqueryname=multicast+boundary) group-address { mask | mask-length }
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display multicast**](cmdqueryname=display+multicast) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **boundary** [ *group-address* [ *mask* | *mask-length* ] ] [ **interface** *interface-type interface-number* ] command to check information about multicast boundary configured on an interface.