(Optional) Configuring Port-Level Load Balancing
================================================

In an EVPN VPWS dual-homing single-active scenario, after port-level load balancing is configured, EVPN VPWS services can use LACP signaling to notify CEs of DF election results for port-level load balancing.

#### Procedure

* Perform the following steps on the PEs at both ends of an EVPN instance.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**evpn redundancy-mode single-active**](cmdqueryname=evpn+redundancy-mode+single-active) command to set the redundancy mode of the device to single-active.
  3. Run the [**interface**](cmdqueryname=interface) **eth-trunk** *trunk-id* command to enter the Eth-Trunk interface view.
  4. Run the [**mode**](cmdqueryname=mode) **lacp-static** command to set the working mode of the Eth-Trunk interface to static LACP.
     
     
     
     After this command is run in the Eth-Trunk interface view, a dynamic ESI is automatically generated.
  5. Run the [**lacp system-id**](cmdqueryname=lacp+system-id) *mac-address* command to configure an LACP system ID for the Eth-Trunk interface.
  6. (Optional) Run the [**lacp unique-port-number enable**](cmdqueryname=lacp+unique-port-number+enable) command to enable LACP port number uniqueness.
  7. (Optional) Run the [**lacp trunk-down-delay enable**](cmdqueryname=lacp+trunk-down-delay+enable) command to enable LACP-driven Eth-Trunk down delay.
  8. Run the [**evpn port-active**](cmdqueryname=evpn+port-active) command to configure port-level load balancing.
     
     
     
     In this scenario, DF election delay is not supported.
  9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.