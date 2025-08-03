Configuring an SR-MPLS TE Policy
================================

SR-MPLS TE Policy is a tunneling technology developed based on SR.

#### Context

SR-MPLS TE Policies are used to direct traffic to traverse an SR-MPLS TE network. Each SR-MPLS TE Policy can have multiple candidate paths with different preferences. From the valid candidate paths, the one with the highest preference is selected as the primary path, and the one with the second highest preference is selected as the backup path.


#### Procedure

* Configure a segment list.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**segment-routing**](cmdqueryname=segment-routing)
     
     
     
     SR is enabled globally and the Segment Routing view is displayed.
  3. Run [**segment-list (Segment Routing view)**](cmdqueryname=segment-list+%28Segment+Routing+view%29) *list-name*
     
     
     
     A segment list is created for an SR-MPLS TE candidate path and the segment list view is displayed.
  4. Run [**index**](cmdqueryname=index) *index* **sid** **label** *label*
     
     
     
     A next-hop SID is configured for the segment list.
     
     
     
     You can run the command multiple times to configure multiple SIDs. The system generates a segment list with a label stack containing SIDs that are placed by index in ascending order. If a candidate path in the SR-MPLS TE Policy is preferentially selected, traffic is forwarded using the segment list of the candidate path. A maximum of 10 SIDs can be configured for each segment list.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an SR-MPLS TE Policy.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**segment-routing**](cmdqueryname=segment-routing)
     
     
     
     SR is enabled globally and the Segment Routing view is displayed.
  3. (Optional) Run [**sr-te-policy bgp-ls enable**](cmdqueryname=sr-te-policy+bgp-ls+enable)
     
     
     
     The SR-MPLS TE Policy is enabled to report information to BGP-LS.
     
     After the [**sr-te-policy bgp-ls enable**](cmdqueryname=sr-te-policy+bgp-ls+enable) command is run, the system sends the path information to BGP-LS with the candidate paths of the SR-MPLS TE Policy as the granularity.
  4. Run [**sr-te policy**](cmdqueryname=sr-te+policy) *policy-name*[ **endpoint** *ipv4-address* **color** *color-value* ]
     
     
     
     An SR-MPLS TE Policy is created, the endpoint and color value are configured for the SR-MPLS TE Policy, and the SR-MPLS TE Policy view is displayed.
  5. (Optional) Run [**binding-sid**](cmdqueryname=binding-sid) *label-value*
     
     
     
     A binding SID is configured for the SR-MPLS TE Policy.
     
     The value of *label-value* needs to be within the scope defined by the [**local-block**](cmdqueryname=local-block) *begin-value* *end-value* command.
  6. (Optional) Run [**mtu**](cmdqueryname=mtu) *mtu*
     
     
     
     An MTU is configured for the SR-MPLS TE Policy.
  7. (Optional) Run [**diffserv-mode**](cmdqueryname=diffserv-mode) { **pipe** *service-class* *service-color* | **uniform** }
     
     
     
     A DiffServ mode is configured for the SR-MPLS TE Policy to implement end-to-end QoS guarantee.
  8. Run [**candidate-path preference**](cmdqueryname=candidate-path+preference) *preference*
     
     
     
     A candidate path and its preference are configured for the SR-MPLS TE Policy.
     
     
     
     Each SR-MPLS TE Policy supports multiple candidate paths. A larger *preference* value indicates a higher preference. The candidate path with the highest preference takes effect.
  9. Run [**segment-list (candidate path view)**](cmdqueryname=segment-list+%28candidate+path+view%29) *list-name* [ **weight** *weight-value* ]
     
     
     
     A segment list is configured to reference the SR-MPLS TE candidate path.
     
     
     
     The segment list must have been created using the [**segment-list (Segment Routing view)**](cmdqueryname=segment-list+%28Segment+Routing+view%29) command.
     
     You can use the **weight** *weight-value* parameter to configure a weight for the segment list. If the weight configured for a segment list of a candidate path is less than the average weight, the segment list does not forward traffic. The average weight is calculated using the following formula: Average weight = Sum of weights of all segment lists of a candidate path/Maximum number of channels supported for load balancing For example, if the maximum number of channels supported for load balancing is M and a candidate path has a total of N segment lists, the average weight of the N segment lists is calculated as follows: (Weight 1 + Weight 2 + ... + Weight N)/M = X. In this example, X represents the average weight, and segment lists whose weights are less than X do not forward traffic.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Because UCMP for the headend of an SR-MPLS TE Policy is implemented among multiple segment lists of the SR-MPLS TE Policy, you only need to configure weights for the segment lists, without the need to run the [**load-balance unequal-cost enable**](cmdqueryname=load-balance+unequal-cost+enable) command. To implement UCMP for a transit P node of an SR-MPLS TE Policy, run the [**load-balance mpls unequal-cost enable**](cmdqueryname=load-balance+mpls+unequal-cost+enable) command.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.