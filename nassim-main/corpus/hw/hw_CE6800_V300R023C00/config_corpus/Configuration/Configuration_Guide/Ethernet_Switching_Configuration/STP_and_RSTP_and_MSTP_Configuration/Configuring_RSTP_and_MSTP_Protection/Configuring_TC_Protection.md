Configuring TC Protection
=========================

Configuring TC Protection

#### Context

If an attacker forges TC BPDUs to attack a device, the device receives a large number of TC BPDUs within a short period of time, and frequently deletes MAC address entries or ARP entries, increasing the device load and affecting network stability.

After enabling TC protection on the device, you can configure the maximum number of TC BPDUs that the device processes within a specified period. If the number of TC BPDUs received by the device within the specified period exceeds the configured maximum number, the device processes only the specified number of TC BPDUs. After the specified period expires, the device processes all the excess TC BPDUs together. This prevents the device from frequently deleting MAC address entries and ARP entries, reducing the device load.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable TC protection.
   
   
   ```
   [stp tc-protection](cmdqueryname=stp+tc-protection)
   ```
   
   By default, TC protection is disabled on a device.
3. Set either or both of the following TC protection parameters:
   
   
   * Set the period during which the device processes the maximum number of TC BPDUs.
     
     ```
     [stp tc-protection interval](cmdqueryname=stp+tc-protection+interval) interval-value
     ```
     
     The default period is the Hello Time.
   * Set the maximum number of TC BPDUs that the device processes within the specified period.
     
     ```
     [stp tc-protection threshold](cmdqueryname=stp+tc-protection+threshold) threshold
     ```
     
     By default, a device processes one TC BPDU within the specified period.![](public_sys-resources/note_3.0-en-us.png) 
   * There are two TC protection parameters: the period during which a device processes the maximum number of TC BPDUs (**tc-protection interval**) and the maximum number of TC BPDUs processed within the period (**tc-protection threshold**). If **tc-protection interval** and **tc-protection threshold** are set to 10 seconds and 5 respectively on a device, the device processes only the first five TC BPDUs within 10 seconds and continues to process the others after the 10 second period expires. You are advised to set the period during which a device processes the maximum number of TC BPDUs to the number of ports in an STP instance divided by 10, and set the maximum number of TC BPDUs processed within the period to 1. For example, if the number of ports in an STP instance is 100, you are advised to configure the device to process one TC BPDU every 10 seconds.
   * Within the period specified by the [**stp tc-protection interval**](cmdqueryname=stp+tc-protection+interval) command, the device processes only the number of TC BPDUs specified by the [**stp tc-protection threshold**](cmdqueryname=stp+tc-protection+threshold) command and delays processing other packets. This may affect the spanning tree convergence speed.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display stp global**](cmdqueryname=display+stp+global) command and check the Tc-protection, Tc-protection threshold, and Tc-protection interval fields to verify the TC protection configuration.