Configuring the STP/RSTP/MSTP Convergence Mode
==============================================

Configuring the STP/RSTP/MSTP Convergence Mode

#### Context

When the topology of a spanning tree instance changes, the forwarding paths of VLANs mapped to this instance also change. As a result, ARP entries related to these VLANs need to be updated. You can set the STP, RSTP, or MSTP convergence mode to **fast** or **normal** based on the method for processing ARP entries.

* **fast**: ARP entries are directly deleted for an update.
* **normal**: ARP entries are aged quickly for an update. To age ARP entries, a device sets the remaining lifetime of these entries to 0 and ages them. If the number of ARP aging probe attempts is greater than 0, the device checks whether these ARP entries have been aged.

The default **normal** convergence mode is recommended. If you select **fast** mode for a device, frequent ARP entry deletion may consume all CPU resources on the device. As a result, packet processing will time out, causing network flapping.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the STP, RSTP, or MSTP convergence mode.
   
   
   ```
   [stp converge](cmdqueryname=stp+converge) { fast | normal }
   ```
   
   The default STP, RSTP, or MSTP convergence mode is **normal**.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] [ **instance** *instance-id* ] [ **interface** *interface-type* *interface-number* | **slot** *slot-id* ] command and check the STP Converge Mode field for the STP, RSTP, or MSTP convergence mode setting.