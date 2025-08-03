Configuring the Ingress as a PCE Client
=======================================

A PCE client can be configured on the ingress so that the ingress establishes a PCEP session with a PCE server and sends a request to the server over the session to calculate a path.

#### Usage Scenario

Different from CSPF configured on the ingress, the PCE algorithm allows a PCE server to configure and manage network-wide TE information, including node, link, and tunnel attributes. Some steps are mandatory when CSPF is used, whereas are optional when PCE is used.

If the ingress has to delegate LSPs only in some TE tunnels to the PCE server, the ingress must report information about both delegated and undelegated LSPs to the PCE server, which helps the PCE server correctly calculate global bandwidth information. To implement partial LSP delegation, perform either of the following configurations:

* Configure the ingress to delegate LSPs in all TE tunnels to the PCE server. Then configure the ingress to report LSP information on a specified tunnel interface to the PCE server and withdraw the LSP delegation from the PCE server.
* Configure the ingress to report information about LSPs in all TE tunnels to the PCE server, without delegating the LSPs to the PCE server. Then configure the ingress to delegate the LSP on a specified TE tunnel interface to the PCE server.

Perform the following steps on the ingress:

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   The device is configured as a PCE client, and the PCE client view is displayed.
3. (Optional) Run [**stateless-bringup**](cmdqueryname=stateless-bringup)
   
   
   
   The PCE client is enabled to send PCReq messages to the PCE server to request path computation.
   
   
   
   With the [**stateless-bringup**](cmdqueryname=stateless-bringup) command configured, after synchronization between the PCE client and server is complete, the PCE client sends a PCReq message to request path computation for a newly configured LSP of a TE tunnel. After receiving the request, the PCE server returns a path computation result using a PCRep message. This function can be configured in PCE delegation scenarios. If the returned path computation result meets service requirements, delegation can be started. However, if a no-path message or an error is returned, rectify faults before starting delegation.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
6. (Optional) Run [**mpls te pce cleanup lsp-state**](cmdqueryname=mpls+te+pce+cleanup+lsp-state)
   
   
   
   The PCE client is enabled to automatically degrade to use the local path computation function if a PCEP session fails.
   
   If a PCE server fails or a PCEP connection is interrupted, to correctly establish an MPLS TE tunnel, the PCE client must be able to automatically degrade to use the local path computation function. The PCE client can use CSPF (if configured) or routes to establish an MPLS TE tunnel.
7. Select either of the following solutions:
   * Solution 1: applicable to scenarios where most LSPs need to be delegated
     
     1. Run [**mpls te pce**](cmdqueryname=mpls+te+pce) **delegate** (MPLS view)
        
        The ingress is configured to delegate LSPs of all local TE tunnels to the PCE server.
     2. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     3. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
        
        The specified TE tunnel interface view is displayed.
     4. Run [**mpls te pce passive-delegate report-only**](cmdqueryname=mpls+te+pce+passive-delegate+report-only) (Tunnel interface view)
        
        The ingress is configured to report LSP information of the specified tunnel to the PCE server, without delegating LSPs of the tunnel to the PCE server.
   * Solution 2: applicable to scenarios where only a few LSPs need to be delegated
     
     1. Run [**mpls te pce passive-delegate report-only**](cmdqueryname=mpls+te+pce+passive-delegate+report-only) (MPLS view)
        
        The ingress is configured to report LSP information of all local tunnels to the PCE server, without delegating LSPs of the tunnels to the PCE server.
     2. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     3. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
        
        The specified TE tunnel interface view is displayed.
     4. Run [**mpls te pce delegate**](cmdqueryname=mpls+te+pce+delegate) (Tunnel interface view)
        
        The ingress is configured to delegate LSPs of the specified tunnel to the PCE server.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.