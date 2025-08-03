Configuring Constraints for PCEP to Compute SR-MPLS TE Policy Paths
===================================================================

Before configuring PCEP to compute an SR-MPLS TE Policy path, you can perform the following steps to configure specific path constraints.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Set the SR-MPLS TE Policy path computation mode to PCEP.
   1. Run the [**segment-routing**](cmdqueryname=segment-routing) command to enable Segment Routing globally and enter the Segment Routing view.
   2. (Optional) Run the [**sr-te-policy pcep lsp-identifiers report**](cmdqueryname=sr-te-policy+pcep+lsp-identifiers+report) command to enable SR-MPLS TE Policy to report the IPV4-LSP-IDENTIFIERS TLV to PCEP.
      
      
      
      The IPv4-LSP-IDENTIFIERS TLV appears in the LSP object of a PCRpt message. In an interworking scenario with a third-party controller, you can enable this function to report information such as the tunnel ID and extended tunnel ID of a candidate path and the endpoint address of an SR-MPLS TE Policy.
   3. Perform either or both of the following configurations as required:
      
      
      * Set the global path computation mode to PCEP for all SR-MPLS TE Policies.
        
        Run the [**sr-te-policy dynamic-computation-seq**](cmdqueryname=sr-te-policy+dynamic-computation-seq)**pcep** command to set the dynamic path computation mode to PCEP.
      * Set a path computation mode for a single SR-MPLS TE Policy.
        1. Run the [**sr-te policy**](cmdqueryname=sr-te+policy) *policy-name*[ **endpoint** *ipv4-address* **color** *color-value* ] command to enter the SR-MPLS TE Policy view.
        2. Run the [**dynamic-computation-seq**](cmdqueryname=dynamic-computation-seq){ **pcep** | **none** } command to set the dynamic path computation mode to PCEP for the SR-MPLS TE Policy.
           
           If you specify the **none** parameter, the dynamic path computation mode set for the specified SR-MPLS TE Policy is canceled.
        3. Run the [**quit**](cmdqueryname=quit) command to return to the Segment Routing view.
      
      
      
      Note that the priority of global configurations is lower than that of single-policy configurations. If both configurations exist, single-policy configurations take effect. If single-policy configurations do not exist, global configurations are inherited.
      
      In real-world applications, there are typically the following three scenarios:
      1. To set the dynamic path computation mode to PCEP for all SR-MPLS TE Policies, run the [**sr-te-policy dynamic-computation-seq**](cmdqueryname=sr-te-policy+dynamic-computation-seq)**pcep** command to enable PCEP-based path computation globally.
      2. To set the dynamic path computation mode to PCEP for most SR-MPLS TE Policies, run the [**sr-te-policy dynamic-computation-seq**](cmdqueryname=sr-te-policy+dynamic-computation-seq)**pcep** command to enable PCEP-based path computation globally, and then run the [**dynamic-computation-seq**](cmdqueryname=dynamic-computation-seq) **none** command for each of the SR-MPLS TE Policies that do not require PCEP-based path computation.
      3. To set the dynamic path computation mode to PCEP for only a few SR-MPLS TE Policies, you do not need to run the [**sr-te-policy dynamic-computation-seq**](cmdqueryname=sr-te-policy+dynamic-computation-seq)**pcep** command. Instead, run the [**dynamic-computation-seq**](cmdqueryname=dynamic-computation-seq) **pcep** command for each of the SR-MPLS TE Policies that require PCEP-based path computation.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
3. (Optional) Configure SR-MPLS TE Policy path constraints.
   
   
   
   If SR-MPLS TE Policy path constraints need to be configured in subsequent steps, perform this step to configure the specific constraints in advance.
   
   
   
   1. Run the **segment-routing policy constraint-path** *path-name* command to create an SR-MPLS TE Policy path constraint and enter the path constraint view.
   2. Run the [**index**](cmdqueryname=index+address+ipv4)*index-value***address** **ipv4** *ipv4-address* [ **include** [ **strict** | **loose** ] | **exclude** ] command to specify the next-hop IP address in the path constraint.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
4. Configure SR-MPLS TE Policy creation constraints.
   
   
   
   Note that the priority of the configuration performed based on a constraint template is lower than that of the configuration performed directly on the specific SR-MPLS TE Policy. If both configurations exist, the configuration performed directly on the specific SR-MPLS TE Policy takes effect. If the configuration performed directly on the specific SR-MPLS TE Policy does not exist, the configuration performed based on a constraint template is inherited.
   
   
   
   * Perform the configuration based on an SR-MPLS TE Policy constraint template.
     1. Run the [**segment-routing policy constraint-template**](cmdqueryname=segment-routing+policy+constraint-template)*constraintName* command to create an SR-MPLS TE Policy constraint template and enter the constraint template view.
     2. Run the [**priority**](cmdqueryname=priority)*setup-priority* *hold-priority* command to configure the path setup priority and hold priority in the constraint template.
     3. Run the [**affinity**](cmdqueryname=affinity){ **include-all** | **include-any** | **exclude** } { *affinity-name* } &<1-32> command to configure affinity constraints in the constraint template.
     4. Run the [**bandwidth ct0**](cmdqueryname=bandwidth+ct0)*bandwidth-value* command to configure a bandwidth constraint in the constraint template.
     5. Run the [**constraint-path**](cmdqueryname=constraint-path)*constraint-path-name* command to configure a path constraint in the constraint template.
        
        The *constraint-path-name* parameter is configured using the **segment-routing policy constraint-path** *path-name* command, and its value is the same as the value of the *path-name* parameter.
     6. Run the [**link-bandwidth utilization**](cmdqueryname=link-bandwidth+utilization)*utilization-value* command to configure bandwidth usage in the constraint template.
     7. Run the [**metric-type**](cmdqueryname=metric-type){ **igp** | **te** | **delay** | **hop-count** } command to configure a metric type in the constraint template.
        
        After the configuration is complete, run the following commands to configure the corresponding constraint values:
        
        + Run the [**max-cumulation**](cmdqueryname=max-cumulation) **igp***max-igp-cost* command to configure the maximum IGP cost in the constraint template.
        + Run the [**max-cumulation te**](cmdqueryname=max-cumulation+te)*max-te-cost* command to configure the maximum TE cost in the constraint template.
        + Run the [**max-cumulation delay**](cmdqueryname=max-cumulation+delay)*max-delay* command to configure the maximum delay in the constraint template.
        + Run the [**max-cumulation hop-count**](cmdqueryname=max-cumulation+hop-count)*max-hop-count* command to configure the maximum number of hops in the constraint template.
     8. (Optional) Run the [**sid selection**](cmdqueryname=sid+selection){ **unprotected-preferred** | **protected-preferred** | **unprotected-only** | **protected-only** } command to configure a SID selection rule in the constraint template.
        
        The default SID selection rule in the constraint template is unprotected-SID-preferred (**unprotected-preferred**).
     9. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     10. Run the [**segment-routing**](cmdqueryname=segment-routing) command to enable Segment Routing globally and enter the Segment Routing view.
     11. Run the [**sr-te policy**](cmdqueryname=sr-te+policy) *policy-name*[ **endpoint** *ipv4-address* **color** *color-value* ] command to enter the SR-MPLS TE Policy view.
     12. Run the [**constraint-template**](cmdqueryname=constraint-template) *constraintName* command to specify the constraint template to be referenced by the SR-MPLS TE Policy.
     13. Run the [**quit**](cmdqueryname=quit) command to return to the Segment Routing view.
     14. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   * Perform the configuration directly on the specific SR-MPLS TE Policy.
     1. Run the [**segment-routing**](cmdqueryname=segment-routing) command to enable Segment Routing globally and enter the Segment Routing view.
     2. Run the [**sr-te policy**](cmdqueryname=sr-te+policy) *policy-name*[ **endpoint** *ipv4-address* **color** *color-value* ] command to enter the SR-MPLS TE Policy view.
     3. Run the [**candidate-path preference**](cmdqueryname=candidate-path+preference) *preference* command to configure a candidate path for the SR-MPLS TE Policy and specify a preference value for the path.
        
        Each SR-MPLS TE Policy supports multiple candidate paths. A larger *preference* value indicates a higher candidate path preference. If multiple candidate paths are configured, the one with the highest preference takes effect.
     4. Run the [**dynamic**](cmdqueryname=dynamic) command to configure the candidate path of the SR-MPLS TE Policy as a dynamic one.
     5. Run the [**affinity**](cmdqueryname=affinity){ **include-all** | **include-any** | **exclude** } { *affinity-name* } &<1-32> command to configure affinity constraints for the dynamic candidate path of the SR-MPLS TE Policy.
     6. Run the [**constraint-path**](cmdqueryname=constraint-path)*constraint-path-name* command to configure a path constraint for the dynamic candidate path of the SR-MPLS TE Policy.
        
        The *constraint-path-name* parameter is configured using the **segment-routing policy constraint-path** *path-name* command, and its value is the same as the value of the *path-name* parameter.
     7. Run the [**link-bandwidth utilization**](cmdqueryname=link-bandwidth+utilization)*utilization-value* command to configure bandwidth usage for the dynamic candidate path of the SR-MPLS TE Policy.
     8. Run the [**metric-type**](cmdqueryname=metric-type){ **igp** | **te** | **delay** | **hop-count** } command to configure a metric type for the dynamic candidate path of the SR-MPLS TE Policy.
        
        After the configuration is complete, run the following commands to configure the corresponding constraint values:
        
        + Run the [**max-cumulation**](cmdqueryname=max-cumulation) **igp***max-igp-cost* command to configure the maximum IGP cost for the dynamic candidate path of the SR-MPLS TE Policy.
        + Run the [**max-cumulation te**](cmdqueryname=max-cumulation+te)*max-te-cost* command to configure the maximum TE cost for the dynamic candidate path of the SR-MPLS TE Policy.
        + Run the [**max-cumulation delay**](cmdqueryname=max-cumulation+delay)*max-delay* command to configure the maximum delay for the dynamic candidate path of the SR-MPLS TE Policy.
        + Run the [**max-cumulation hop-count**](cmdqueryname=max-cumulation+hop-count)*max-hop-count* command to configure the maximum number of hops for the dynamic candidate path of the SR-MPLS TE Policy.
     9. (Optional) Run the [**sid selection**](cmdqueryname=sid+selection){ **unprotected-preferred** | **protected-preferred** | **unprotected-only** | **protected-only** } command to configure a SID selection rule for the candidate path of the SR-MPLS TE Policy.
        
        The default SID selection rule in the constraint template is unprotected-SID-preferred (**unprotected-preferred**).
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.