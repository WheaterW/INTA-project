Configuring the CFI as the Internal Drop Priority
=================================================

Configuring the CFI as the Internal Drop Priority

#### Context

The Canonical Format Indicator (CFI) field, also known as the Drop Eligible Indicator (DEI), in a VLAN tag identifies the drop priority of a packet. When the rate of packets on the device exceeds the CIR, the value of the DEI field is set to 1. In this case, the drop priority of the packets is high. When congestion occurs, the device first discards the packets with the DEI field value of 1.

To configure the device to discard packets whose rate exceeds the CIR, configure the CFI as the internal drop priority.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-type interface-number | interface-name }
   ```
3. Configure the CFI as the internal drop priority.
   
   
   ```
   [dei enable](cmdqueryname=dei+enable)
   ```
4. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```