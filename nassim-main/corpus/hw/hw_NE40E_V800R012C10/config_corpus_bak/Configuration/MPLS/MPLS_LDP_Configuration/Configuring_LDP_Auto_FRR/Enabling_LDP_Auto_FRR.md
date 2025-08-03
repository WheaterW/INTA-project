Enabling LDP Auto FRR
=====================

If LDP auto FRR is needed, configure it on the ingress or a transit node of a tunnel.

#### Context

LDP auto FRR depends on IGP auto FRR. LDP auto FRR will be automatically enabled after IGP auto FRR is enabled. To change a policy for triggering LDP LSP establishment, you can run the [**auto-frr lsp-trigger**](cmdqueryname=auto-frr+lsp-trigger) command.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before you enable remote LFA FRR, configure the remote LFA algorithm when you configure IGP auto FRR.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. (Optional) Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The MPLS-LDP-IPv4 view is displayed.
4. (Optional) Run [**auto-frr lsp-trigger**](cmdqueryname=auto-frr+lsp-trigger+all+host+ip-prefix+none) { **all** | **host** | **ip-prefix** *ip-prefix-name* | **none** }
   
   
   
   A policy for triggering LDP to establish backup LSPs is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If both the [**auto-frr lsp-trigger**](cmdqueryname=auto-frr+lsp-trigger) and [**lsp-trigger**](cmdqueryname=lsp-trigger) commands are run, the established backup LSPs satisfy both the policy for triggering LDP LSP establishment and the policy for triggering backup LDP LSP establishment.
   
   This command can be run in both the MPLS-LDP and MPLS-LDP-IPv4 views. If it is run in both views, only the later configuration takes effect.
5. To enable remote LFA FRR, perform the following steps in the MPLS-LDP view of a PQ node:
   1. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the MPLS-LDP view.
   2. Run [**accept target-hello**](cmdqueryname=accept+target-hello+all+peer-group+ip-prefix) { **all** | **peer-group** **ip-prefix** *ip-prefix-name* }
      
      
      
      Automatic remote LDP session establishment upon the receiving of a Targeted Hello message is enabled.
      
      
      
      In a Remote LFA FRR scenario, after an ingress uses the Remote LFA algorithm to calculate a PQ node, LDP automatically establishes a remote LDP session between the ingress and the PQ node. To enable the PQ node to implement this function, run the [**accept target-hello**](cmdqueryname=accept+target-hello) command on the PQ node.
      
      In the preceding command:
      
      * **all**: enables a PQ node to establish remote LDP sessions based on all received Targeted Hello messages.
      * **peer-group** **ip-prefix** *ip-prefix-name*: enables a PQ node to establish remote LDP sessions based on Targeted Hello messages sent by LDP peers that meet a specified IP prefix list.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      After the [**accept target-hello**](cmdqueryname=accept+target-hello) command is run, the PQ node is prone to Targeted Hello packet-based attacks. If the PQ node receives a large number of Targeted Hello packets, it establishes many remote LDP sessions. To prevent such an issue, perform either of the following operations:
      
      * Specify the **peer-group** **ip-prefix** *ip-prefix-name* parameter to limit the LDP peers with which a PQ node can establish remote LDP sessions.
      * Configure LDP security authentication for LDP peers in batches. For details, see [Configuring LDP Security Features](dc_vrp_ldp-p2p_cfg_0055.html).
   3. Run [**send-message address all-loopback**](cmdqueryname=send-message+address+all-loopback)
      
      
      
      The PQ node is enabled to advertise all local loopback interface addresses to LDP peers.
      
      
      
      In a remote LFA FRR scenario, LDP uses the PQ node's address calculated using an IGP to establish a remote LDP session between a node and the PQ node. Then the two nodes establish a remote LFA FRR LSP over the session. The PQ node's IP address can be any loopback interface's IP address or an LSR ID. To advertise the loopback addresses to LDP peers, run this command on a PQ node so that a remote LFA FRR LSP can be established.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
7. (Optional) Enable poison reverse for LDP FRR/ECMP.
   1. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface or sub-interface view is displayed.
      
      
      
      You can enter the Eth-Trunk interface view, Eth-Trunk sub-interface view, POS interface view, IP-Trunk interface view, GE interface view, or GE sub-interface view.
   3. Run [**mpls poison-reverse enable**](cmdqueryname=mpls+poison-reverse+enable)
      
      
      
      Poison reverse is enabled for LDP FRR/ECMP.
      
      
      
      In an FRR or TI-LFA scenario on an LDP/SR-MPLS BE ring network, if the primary path fails, the ingress switches traffic from the primary path to the backup path. In this case, a transit node sends traffic back to the ingress before routes are converged. As a result, a traffic loop occurs. To address this issue, run this command on the inbound interface of the transit node. If the transit node finds that the outbound interface of traffic is the same as the inbound interface of the traffic, the transit node switches traffic from the primary path to the backup path in a timely manner, blocking looped traffic.
      
      This command also applies to the scenario where two ECMP paths are formed on an LDP/SR-MPLS BE ring network to resolve similar issues.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.