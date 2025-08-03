Configuring Dynamic Bandwidth Reservation
=========================================

This section describes how to configure dynamic bandwidth reservation on an MPLS TE interface. This configuration enables the MPLS TE interface to dynamically reserve bandwidth for an MPLS TE tunnel to account for the fact that physical bandwidth is variable.

#### Usage Scenario

The reservable bandwidth values configured on the interfaces along an MPLS TE tunnel are used by the MPLS TE module to check whether a link meets all tunnel bandwidth requirements. If a fixed bandwidth value is configured on an interface and the physical bandwidth of the interface changes, the MPLS TE module cannot correctly evaluate link bandwidth resources when the actual reservable bandwidth differs from the configured bandwidth value. For example, the actual physical bandwidth of a trunk interface on an MPLS TE tunnel is 1 Gbit/s. The maximum reservable bandwidth is set to 800 Mbit/s, and the BC0 bandwidth is set to 600 Mbit/s for the interface. If a member of the trunk interface fails, the trunk interface has its physical bandwidth reduced to 500 Mbit/s, which does not meet the requirements for the maximum reservable bandwidth and BC0 bandwidth. However, the MPLS TE module still attempts to reserve the bandwidth as configured. As a result, bandwidth reservation fails.

To address this issue, you can configure the maximum reservable dynamic bandwidth and BC dynamic bandwidth. The former is the proportion of the maximum reservable bandwidth to the actual physical bandwidth, and the latter is the proportion of the BC bandwidth to the maximum reservable bandwidth. Based on the two proportions, the MPLS TE module can quickly detect physical bandwidth changes along links and preempt the bandwidth of any MPLS TE tunnel that requires more than the available interface bandwidth. If soft preemption is supported by the preempted tunnel, traffic on the tunnel can be smoothly switched to another links with sufficient bandwidth. The smooth traffic switchover is also performed when an interface fails, which minimizes traffic loss.


#### Pre-configuration Tasks

Before configuring dynamic bandwidth reservation, enable MPLS TE on the interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of an MPLS TE-enabled interface is displayed.
3. Run [**mpls te bandwidth max-reservable-bandwidth dynamic**](cmdqueryname=mpls+te+bandwidth+max-reservable-bandwidth+dynamic) *max-dynamic-bw-value*
   
   
   
   The maximum reservable dynamic bandwidth is configured for the link.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If this command is run in the same interface view as the [**mpls te bandwidth max-reservable-bandwidth**](cmdqueryname=mpls+te+bandwidth+max-reservable-bandwidth) command, the latest configuration overrides the previous one.
4. (Optional) Run [**mpls te bandwidth max-reservable-bandwidth dynamic baseline remain-bandwidth**](cmdqueryname=mpls+te+bandwidth+max-reservable-bandwidth+dynamic+baseline+remain-bandwidth)
   
   
   
   The device is configured to use the remaining bandwidth of the interface when calculating the maximum reservable dynamic bandwidth for TE.
   
   
   
   In scenarios such as channelized sub-interface and bandwidth lease, the remaining bandwidth of an interface changes, but the physical bandwidth does not. In this case, the actual forwarding capability of the interface decreases. If the maximum reservable dynamic bandwidth of the TE tunnel is still calculated based on the physical bandwidth, the calculated TE bandwidth is greater than the actual bandwidth, and the actual forwarding capability of the interface does not meet the bandwidth requirement of the tunnel.
5. Run [**mpls te bandwidth dynamic**](cmdqueryname=mpls+te+bandwidth+dynamic) **bc0** *bc0-bw-percentage*
   
   
   
   The BC0 dynamic bandwidth is configured for the link.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If this command is run in the same interface view as the [**mpls te bandwidth bc0**](cmdqueryname=mpls+te+bandwidth+bc0) command, the latest configuration overrides the previous one.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display mpls te link-administration bandwidth-allocation**](cmdqueryname=display+mpls+te+link-administration+bandwidth-allocation) [ **interface** *interface-type interface-number* ] command to check bandwidth information on a specified or all MPLS TE interfaces.