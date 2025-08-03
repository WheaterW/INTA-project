Configuring TC/TCN BPDU Suppression
===================================

Configuring TC/TCN BPDU Suppression

#### Context

If you do not want an interface to update ARP and MAC entries when receiving TC/TCN BPDUs, configure the TC/TCN BPDU suppression function on this interface. This will cause the interface neither to update ARP and MAC entries nor flood TC or TCN BPDUs to other interfaces on the local device after receiving TC or TCN BPDUs.

Configuring the TC/TCN BPDU suppression function on an interface will result in packet loss for a long time after the topology changes. Exercise caution when configuring this function.


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
4. Configure the TC/TCN BPDU suppression function.
   
   
   ```
   [stp tc-restriction enable](cmdqueryname=stp+tc-restriction+enable)
   ```
   
   By default, the TC/TCN BPDU suppression function is disabled.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display stp**](cmdqueryname=display+stp) **interface** *interface-type* *interface-number* command to check whether the TC/TCN BPDU suppression function is enabled on an interface based on the TC Restriction field.