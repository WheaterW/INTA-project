Configuring a Service Access Point
==================================

An EVC Layer 2 sub-interface is used as an EVC service access point, on which traffic encapsulation types and behaviors can be flexibly combined. A traffic encapsulation type and behavior are grouped into a traffic policy. Traffic policies help implement flexible Ethernet service access.

#### Context

For configuration notes about the traffic encapsulation types and behaviors, and their combinations, see [EVC Service Bearing](feature_0003992353.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2**
   
   
   
   An EVC Layer 2 sub-interface is created, and its view is displayed.
3. Run any of the following commands:
   
   
   * To configure default encapsulation, run the [**encapsulation**](cmdqueryname=encapsulation) **default** command.
   * To configure dot1q encapsulation, run the [**encapsulation dot1q**](cmdqueryname=encapsulation+dot1q) **vid** *pevid1* [ **to** *pevid2* ] command.
   * To configure dot1q encapsulation, run the [**encapsulation dot1q vid**](cmdqueryname=encapsulation+dot1q+vid) *pevid1* [ **to** *pevid2* ] **8021p** { *val8021p1* [ **to** *val8021p2* ] } &<1-8> command.
   * To configure QinQ encapsulation, run the [**encapsulation**](cmdqueryname=encapsulation) **qinq** **vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *high-ce-vid* ] | **default** } command.
   * To configure untagged encapsulation, run the [**encapsulation**](cmdqueryname=encapsulation) **untag** command.
4. Run any of the following commands:
   
   
   * To add a VLAN tag or an outer VLAN tag to each packet, run the [**rewrite push**](cmdqueryname=rewrite+push) **vid** *vid* [ **8021p** *8021p-value* ] command.
   * To add two VLAN tags to each packet, run the [**rewrite push**](cmdqueryname=rewrite+push) **vid** *vid* [ **8021p** *8021p-value* ] **ce-vid** *ce-vid* [ **ce-8021p** *ce-8021p-value* ] command.
   * To remove a VLAN tag or an outer VLAN tag from each packet, run the [**rewrite pop**](cmdqueryname=rewrite+pop) **single** command.
   * To remove two VLAN tags from each packet, run the [**rewrite pop**](cmdqueryname=rewrite+pop) **double** command.
   * To configure 1 to 1 mapping, run the [**rewrite map**](cmdqueryname=rewrite+map) **1-to-1** **vid** *pe-vid* **8021p** *pe-8021p-value* command.
   * To configure 1 to 2 mapping, run the [**rewrite map**](cmdqueryname=rewrite+map) **1-to-2** **vid** *pe-vid* [ **8021p** *peâ8021p-value* ] **ce-vid** *ce-vid* **ceâ8021p** *ceâ8021p-value* command.
   * To configure 2 to 1 mapping, run the [**rewrite map**](cmdqueryname=rewrite+map) **2-to-1** **vid** *pe-vid* [ **8021p** *pe-8021p-value* ] command.
   * To configure 2 to 2 mapping, run the [**rewrite map**](cmdqueryname=rewrite+map) **2-to-2** **vid** *pe-vid* [ **8021p** *peâ8021p-value* ] **ce-vid** *ce-vid* [ **ceâ8021p** *ceâ8021p-value* ] command.
   * To increase or reduce a tag value based on a specified offset in each packet, run the [**rewrite map**](cmdqueryname=rewrite+map) **offset** { **decrease** | **increase** } *offset-vid* command.
   * To swap the inner and outer VLAN tags carried in each packet, run the [**rewrite swap**](cmdqueryname=rewrite+swap) command.
   * To replace the outer VLAN tag in an outgoing service packet with the VLAN tag of the corresponding Layer 2 sub-interface, run the **[**rewrite map single outbound**](cmdqueryname=rewrite+map+single+outbound)** command.
5. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The EVC Layer 2 sub-interface is added to a BD.
   
   
   
   *bd-id* is the BD ID specified in [Creating a Bridge Domain](dc_vrp_evc_cfg_0004.html).
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.