Configuring BPDU Protection
===========================

Configuring BPDU Protection

#### Context

In most cases, edge ports are connected directly to user terminals and do not receive BPDUs. If edge ports on a device receive forged BPDUs, the device will change the edge ports to non-edge ports and recalculate the spanning tree, causing network flapping. To prevent this problem, BPDU protection can be enabled on the device to prevent malicious forged BPDU attacks. For details about edge port configuration, see [Configuring Edge Ports and BPDU Filtering Ports](galaxy_vbst_cfg_0012.html).

![](public_sys-resources/note_3.0-en-us.png) 

BPDU protection only takes effect on edge ports that are configured using the [**stp edged-port**](cmdqueryname=stp+edged-port) or [**stp edged-port default**](cmdqueryname=stp+edged-port+default) command, and not for those configured through automatic edge port detection.

The following procedure applies only to devices with edge ports.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BPDU protection.
   
   
   ```
   [stp bpdu-protection](cmdqueryname=stp+bpdu-protection)
   ```
   
   By default, BPDU protection is disabled.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If an edge port for which BPDU protection is enabled receives BPDUs, the edge port will enter the error-down state with its attributes unchanged. To restore an error-down edge port to the up state, use one of the following methods:
   
   * In the interface view, run the [**restart**](cmdqueryname=restart) command.
   * In the interface view, run the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands in sequence.
   * In the system view, run the [**error-down auto-recovery**](cmdqueryname=error-down+auto-recovery) **cause** **bpdu-protection** **interval** *interval-value* command to enable the port to recover to the up state and set a recovery delay. *interval-value* specifies a recovery delay after which the error-down port will go up automatically.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display stp vlan**](cmdqueryname=display+stp+vlan) [ *vlan-id* ] **information** [ **global** ] command and check the BPDU-Protection field to verify the BPDU protection configuration.