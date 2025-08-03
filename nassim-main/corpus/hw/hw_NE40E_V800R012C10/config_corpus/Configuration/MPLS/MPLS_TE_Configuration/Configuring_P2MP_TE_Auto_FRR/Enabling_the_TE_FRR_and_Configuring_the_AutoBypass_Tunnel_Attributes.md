Enabling the TE FRR and Configuring the AutoBypass Tunnel Attributes
====================================================================

After MPLS TE FRR is enabled on the ingress of a primary LSP, a bypass LSP is established automatically.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The tunnel interface view of the primary LSP is displayed.
3. Run [**mpls te fast-reroute**](cmdqueryname=mpls+te+fast-reroute) [ **bandwidth** ]
   
   
   
   TE FRR is enabled.
   
   
   
   If TE FRR bandwidth protection is needed, configure the **bandwidth** parameter in this command.
4. (Optional) Run [**mpls te frr-switch degrade**](cmdqueryname=mpls+te+frr-switch+degrade)
   
   
   
   The MPLS TE tunnel is enabled to mask the FRR function.
   
   
   
   After TE FRR takes effect, traffic is switched to the bypass LSP when the primary LSP fails. If the bypass LSP is not the optimal path, traffic congestion easily occurs. To prevent traffic congestion, you can configure LDP to protect TE tunnels. To have the LDP protection function take effect, you need to run the [**mpls te frr-switch degrade**](cmdqueryname=mpls+te+frr-switch+degrade) command to enable the MPLS TE tunnel to mask the FRR function. After the command is run:
   
   1. If the primary LSP is in the FRR-in-use state (that is, traffic has been switched to the bypass LSP), traffic cannot be switched to the primary LSP.
   2. If HSB is configured for the tunnel and an HSB LSP is available, traffic is switched to the HSB LSP.
   3. If no HSB LSP is available for the tunnel, the tunnel is unavailable, and traffic is switched to another tunnel like an LDP tunnel.
   4. If no tunnels are available, traffic is interrupted.
5. (Optional) Run [**mpls te bypass-attributes**](cmdqueryname=mpls+te+bypass-attributes) [ **bandwidth** *bandwidth* | **priority** *setup-priority* [ *hold-priority* ] ]
   
   
   
   Attributes are set for the automatic bypass LSP.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The bandwidth attribute can only be set for the bypass LSP after the [**mpls te fast-reroute**](cmdqueryname=mpls+te+fast-reroute) **bandwidth** command is run for the primary LSP.
   * The bypass LSP bandwidth cannot exceed the primary LSP bandwidth.
   * If no attributes are configured for an automatic bypass LSP, by default, the automatic bypass LSP uses the same bandwidth as that of the primary LSP.
   * The setup priority of a bypass LSP must be lower than or equal to the holding priority. These priorities cannot be higher than the corresponding priorities of the primary LSP.
   * If TE FRR is disabled, the bypass LSP attributes are automatically deleted.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. (Optional) Configure attributes for a bypass LSP.
   1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view of the link through which the bypass LSP passes is displayed.
   2. Run [**mpls te auto-frr attributes**](cmdqueryname=mpls+te+auto-frr+attributes) { **bandwidth** *bandwidth* | **priority** *setup-priority* [ *hold-priority* ] | **hop-limit** *hop-limit-value* }
      
      
      
      Attributes are configured for the bypass LSP.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
8. (Optional) Configure affinities for the automatic bypass tunnel.
   
   
   
   Affinities determine link attributes of an automatic bypass LSP. Affinities and a link administrative group attribute are used together to determine over which links the automatic bypass LSP can be established.
   
   Perform either of the following configurations:
   
   
   
   * Set a hexadecimal number.
     
     1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
        
        The interface view of the link through which the bypass LSP passes is displayed.
     2. Run [**mpls te link administrative group**](cmdqueryname=mpls+te+link+administrative+group) *value*
        
        An administrative group attribute is specified.
     3. (Optional) Run [**mpls te auto-frr attributes affinity**](cmdqueryname=mpls+te+auto-frr+attributes+affinity) **property** *properties* [ **mask** *mask-value* ] or [**mpls te auto-frr attributes affinity**](cmdqueryname=mpls+te+auto-frr+attributes+affinity) { **include-all** | **include-any** | **exclude** } *bit-name* &<1-32>
        
        An affinity is configured for the bypass LSP.
     4. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     5. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
        
        The tunnel interface view of the primary LSP is displayed.
     6. Run [**mpls te bypass-attributes affinity**](cmdqueryname=mpls+te+bypass-attributes+affinity) **property** *properties* [ **mask** *mask-value*]
        
        An affinity is configured for the bypass LSP.
   * Set an affinity name.
     
     Naming an affinity makes the affinity easy to understand and maintain. Setting an affinity name is recommended.
     
     1. Run [**path-constraint affinity-mapping**](cmdqueryname=path-constraint+affinity-mapping)
        
        An affinity name mapping template is configured, and the template view is displayed.
        
        Repeat this step on each node used to calculate the path over which an automatic bypass LSP is established. The affinity name configured on each node must match the mappings between affinity bits and names.
     2. Run [**attribute**](cmdqueryname=attribute) *affinity-name* **bit-sequence** *bit-number*
        
        The mapping between the name and bit value in an affinity is configured.
        
        There are 32 affinity bits in total. You can repeat this step to configure some or all affinity bits.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
        
        The interface view of the link through which the bypass LSP passes is displayed.
     5. Run [**mpls te link administrative group name**](cmdqueryname=mpls+te+link+administrative+group+name) *bit-name* &<1-32>
        
        An administrative group attribute is specified.
     6. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     7. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
        
        The tunnel interface view of the primary LSP is displayed.
     8. Run [**mpls te bypass-attributes affinity**](cmdqueryname=mpls+te+bypass-attributes+affinity) { **include-all** | **include-any** | **exclude** } *bit-name* &<1-32>
        
        An affinity is configured for the bypass LSP.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If an automatic bypass LSP that satisfies the specified affinity cannot be established, a node will bind a manual bypass LSP satisfying the specified affinity to the primary LSP.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.