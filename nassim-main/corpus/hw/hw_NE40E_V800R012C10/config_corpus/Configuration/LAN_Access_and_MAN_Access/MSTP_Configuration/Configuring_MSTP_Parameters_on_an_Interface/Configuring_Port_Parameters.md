Configuring Port Parameters
===========================

Port parameters that may affect Multiple Spanning Tree Protocol (MSTP) topology convergence include the link type and maximum number of sent Bridge Protocol Data Units (BPDUs). Configure proper port parameters to implement rapid topology convergence.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the Ethernet interface participating in spanning tree protocol calculation is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following configuration can be configured both on a Layer 2 interface and a Layer 3 interface.
3. (Optional) Run [**stp point-to-point**](cmdqueryname=stp+point-to-point) { **auto** | **force-false** | **force-true** }
   
   
   
   The link type is configured for the interface.
   
   
   
   * If the Ethernet port works in full-duplex mode, the port is connected to a P2P link. In this case, **force-true** can be configured to implement rapid network convergence.
   * If the Ethernet port works in half-duplex mode, you can configure [**stp point-to-point**](cmdqueryname=stp+point-to-point) **force-true** to forcibly set the link type to P2P to implement rapid network convergence.
4. Run [**stp mcheck**](cmdqueryname=stp+mcheck)
   
   
   
   The MCheck operation is performed.
   
   
   
   On a device running MSTP, if an interface is connected to a device running STP, the interface automatically transitions to the STP mode.
   
   Performing MCheck on the interface is required to manually switch the interface to the MSTP mode because the interface fails to automatically transition to the MSTP mode in the following situations:
   
   * The device running STP is shut down or moved.
   * The device running STP transitions to the MSTP mode.
5. Run [**stp transmit-limit**](cmdqueryname=stp+transmit-limit) *packet-number*
   
   
   
   The maximum number of BPDUs that the interface sends per second is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the same maximum number of BPDUs need to be sent by each interface on a device, run the [**stp transmit-limit (system view)**](cmdqueryname=stp+transmit-limit+%28system+view%29) command. The [**stp transmit-limit (interface view)**](cmdqueryname=stp+transmit-limit+%28interface+view%29) command takes precedence over the [**stp transmit-limit (system view)**](cmdqueryname=stp+transmit-limit+%28system+view%29) command. If the [**stp transmit-limit (interface view)**](cmdqueryname=stp+transmit-limit+%28interface+view%29) command is run on an interface, the [**stp transmit-limit (system view)**](cmdqueryname=stp+transmit-limit+%28system+view%29) command does not take effect on the interface.
6. (Optional) Run [**stp edged-port**](cmdqueryname=stp+edged-port) **enable**
   
   
   
   The interface is configured as an edge port.
   
   If a device port is connected to a terminal, you can run this command to configure the port as an edge port.
   
   If the current port has been configured as an edge port, the port is still be able to send BPDUs. This may cause BPDUs to be sent to other networks, leading to network flapping. To prevent this problem, run the [**stp bpdu-filter**](cmdqueryname=stp+bpdu-filter) command to configure the edge port as a BPDU filter port that does not process or send BPDUs.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the [**stp bpdu-filter**](cmdqueryname=stp+bpdu-filter) command is run on a port, the port no longer processes or sends BPDUs and cannot negotiate STP status with the directly connected port. Therefore, exercise caution when running this command.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. Run [**error-down auto-recovery**](cmdqueryname=error-down+auto-recovery) **cause** *error-down-type* **interval** *interval-value*
   
   
   
   The edge port in the error-down state is enabled to automatically go up, and the delay for the transition from down to up is set.
   
   There is no default value for the delay. Therefore, you must specify a delay when using this command.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

When the topology of a spanning tree changes, the forwarding paths to associated VLANs are changed. The ARP entries corresponding to those VLANs on the device need to be updated. STP/RSTP processes ARP entries in either fast or normal mode.

* In fast mode, ARP entries to be updated are directly deleted.
* In normal mode, ARP entries to be updated are rapidly aged.
  
  The remaining lifetime of ARP entries to be updated is set to 0. The device rapidly processes these aged entries. If the number of ARP aging probe attempts is not set to 0, ARP implements aging probe for these ARP entries.
  
  In either fast or normal mode, MAC entries are directly deleted.

You can run the [**stp converge**](cmdqueryname=stp+converge) { **fast** | **normal** } command in the system view to configure the STP/RSTP convergence mode.