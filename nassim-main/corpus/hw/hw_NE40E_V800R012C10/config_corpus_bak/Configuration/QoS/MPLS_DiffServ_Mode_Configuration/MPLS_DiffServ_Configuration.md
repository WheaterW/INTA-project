MPLS DiffServ Configuration
===========================

MPLS_DiffServ_Configuration

#### BA and PHB

This section describes MPLS DiffServ configurations, which involve BA and PHB definitions. For details about BA and PHB definitions, see [BA and PHB](dc_ne_qos_feature_060.html).


#### BA and PHB Implementations in an MPLS DiffServ Scenario

Three modes are defined in MPLS DiffServ scenarios: Uniform, Pipe, and Short Pipe.

* In Uniform mode, the original priorities of packets are used for QoS implementation on an MPLS network. The original priorities of packets are reset when the packets are leaving the MPLS network.
* In Pipe or Short Pipe mode, packets are allocated a desired priority on the backbone network, regardless of their original priorities. After leaving the backbone network, the original priorities of packets remain unchanged.
  + In Pipe mode, the egress on the MPLS network processes a packet based on its re-allocated priorities.
  + In Short Pipe mode, the egress on the MPLS network processes a packet based on its original priorities.

**Figure 1** BA and PHB implementation on a PE  
![](images/fig_qos_feature_05702.png)

Both BA and PHB are required on the network-side interface of a PE. Therefore, run the **[**trust upstream**](cmdqueryname=trust+upstream)** command on the network-side interface.

On the user-side interface of a PE, implement BA for upstream traffic and perform one of the following operations for downstream traffic:

* Uniform mode: PHB needs to be performed. That is, in Uniform node, both BA and PHB are required on the network-side interface of a PE. Therefore, run the **[**trust upstream**](cmdqueryname=trust+upstream)** command on the network-side interface.
* In Pipe or Short Pipe mode, only BA is required on the user-side interface of the PE. PHB is not performed. The **[**diffserv-mode**](cmdqueryname=diffserv-mode)** and **[**trust upstream**](cmdqueryname=trust+upstream)** commands are mutually exclusive.

**Figure 2** BA and PHB implementation on a P  
![](images/fig_qos_feature_05703.png)

Both BA and PHB are required on the network-side interface of a P. Therefore, run the **trust upstream** command on the network-side interface.