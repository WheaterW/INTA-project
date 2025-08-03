Configuring the Rate at Which IGMP Packets Are Sent to the CPU
==============================================================

You can configure the rate at which IGMP packets are sent to the CPU to reduce CPU usage of a device and protect the device against attacks.

#### Context

Perform the following operations on an interface of the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Perform one of the following operations as required:
   
   
   * Run the [**cp-rate-limit igmp**](cmdqueryname=cp-rate-limit+igmp) **cir** *cir-value* [ **cbs** *cbs-value* ] command on an Ethernet sub-interface, GE sub-interface, or Eth-Trunk sub-interface to limit the rate at which IGMP packets are sent to the CPU.
   * Run the [**cp-rate-limit igmp**](cmdqueryname=cp-rate-limit+igmp) **cir** *cir-value* [ **cbs** *cbs-value* ] **vlan** *vlan-id1* [ **to** *vlan-id2* ] command on a Layer 2 Ethernet interface, Layer 2 GE interface, or Layer 2 Eth-Trunk interface, or sub-interface for dot1q VLAN tag termination to limit the rate at which IGMP packets are sent to the CPU.
   * Run the [**cp-rate-limit igmp**](cmdqueryname=cp-rate-limit+igmp) **cir** *cir-value* [ **cbs** *cbs-value* ] **pe-vid** *pe-vid* **ce-vid** *begin-vid* [ **to** *end-vid* ] command on an QinQ termination sub-interface to limit the rate at which IGMP packets are sent to the CPU.