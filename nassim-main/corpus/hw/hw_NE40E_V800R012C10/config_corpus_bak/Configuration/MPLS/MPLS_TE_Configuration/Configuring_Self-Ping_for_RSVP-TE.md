Configuring Self-Ping for RSVP-TE
=================================

Self-ping is a connectivity check method for RSVP-TE LSPs.

#### Prerequisites

Before configuring self-ping for RSVP-TE, complete the following task:

* [Configure RSVP-TE tunnels.](dc_vrp_te-p2p_cfg_0003.html)

#### Context

After an RSVP-TE LSP is established, the system sets the LSP status to up, without waiting for forwarding relationships to be completely established between nodes on the forwarding path. If service traffic is imported to the LSP before all forwarding relationships are established, some early traffic may be lost.

Self-ping can address this issue by checking whether the LSP can forward traffic.

Self-ping can be configured globally or for a specified tunnel. If both are configured, the tunnel-specific configuration takes effect.


#### Procedure

1. Configure self-ping globally.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**mpls**](cmdqueryname=mpls)
      
      
      
      The MPLS view is displayed.
   3. Run [**mpls te**](cmdqueryname=mpls+te)
      
      
      
      MPLS TE is enabled for the device.
   4. Run [**mpls te self-ping enable**](cmdqueryname=mpls+te+self-ping+enable)
      
      
      
      Self-ping is enabled globally.
   5. (Optional) Run [**mpls te self-ping duration**](cmdqueryname=mpls+te+self-ping+duration) *self-ping-duration*
      
      
      
      The self-ping duration is set globally.
      
      
      
      Value 65535 indicates an infinite detection duration.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure self-ping for a specified tunnel.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
      
      
      
      A tunnel interface is created, and its view is displayed.
   3. Run [**tunnel-protocol mpls te**](cmdqueryname=tunnel-protocol+mpls+te)
      
      
      
      MPLS TE is enabled.
   4. Run [**mpls te self-ping enable**](cmdqueryname=mpls+te+self-ping+enable)
      
      
      
      Self-ping is enabled for the specified tunnel.
   5. (Optional) Run [**mpls te self-ping duration**](cmdqueryname=mpls+te+self-ping+duration) *self-ping-duration*
      
      
      
      The self-ping duration is set for the specified tunnel.
      
      
      
      Value 65535 indicates an infinite detection duration.
      
      If self-ping is enabled globally but not for a specific tunnel, the global self-ping duration is effective for the tunnel. However, if self-ping is also enabled for the tunnel, the tunnel-specific self-ping duration is effective.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. (Optional) Block self-ping for a specified tunnel.
   
   
   
   If self-ping is enabled globally but this function should not be enabled for a tunnel, you can perform the following steps to block self-ping for the tunnel:
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
      
      
      
      A tunnel interface is created, and its view is displayed.
   3. Run [**tunnel-protocol mpls te**](cmdqueryname=tunnel-protocol+mpls+te)
      
      
      
      MPLS TE is enabled.
   4. Run [**mpls te self-ping block**](cmdqueryname=mpls+te+self-ping+block)
      
      
      
      Self-ping is blocked for the specified tunnel.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
4. (Optional) Configure whitelist session-CAR for self-ping.
   
   
   
   When the self-ping service suffers a traffic burst, bandwidth may be preempted among self-ping sessions. To resolve this problem, you can configure whitelist session-CAR for self-ping to isolate bandwidth resources by session. If the default parameters of whitelist session-CAR for self-ping do not meet service requirements, you can adjust them as required.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**whitelist session-car ospf disable**](cmdqueryname=whitelist+session-car+ospf+disable)
      
      
      
      Whitelist session-CAR for self-ping is disabled.
   3. (Optional) Run [**whitelist session-car self-ping**](cmdqueryname=whitelist+session-car+self-ping) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
      
      
      
      Parameters of whitelist session-CAR for self-ping are configured.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After configuring self-ping for RSVP-TE, verify the configuration.

* Run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) command to check the self-ping configuration. In the command output, the **Self-Ping** field indicates whether self-ping is enabled, and the **Self-Ping Duration** field indicates the self-ping duration.
* Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **self-ping** **statistics** **slot** *slot-id* command to check whitelist session-CAR statistics about self-ping packets on a specified interface board.
  
  To check the statistics in a coming period of time, you can run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car) **self-ping** **statistics** **slot** *slot-id* command to clear the existing whitelist session-CAR statistics about self-ping packets first. Then, after the period elapses, run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **self-ping** **statistics** **slot** *slot-id* command. In this case, all the statistics are newly generally, facilitating statistics query.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Cleared whitelist session-CAR statistics cannot be restored. Exercise caution when running the reset command.