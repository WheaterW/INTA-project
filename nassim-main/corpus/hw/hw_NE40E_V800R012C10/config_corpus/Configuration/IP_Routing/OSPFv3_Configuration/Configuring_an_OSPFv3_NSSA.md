Configuring an OSPFv3 NSSA
==========================

By configuring a non-backbone area on the border of an autonomous system (AS) as a not-so-stubby area (NSSA), you can reduce the size of the routing table and the amount of routing information to be transmitted.

#### Usage Scenario

An excessive number of entries in a routing table wastes network resources and causes high CPU usage. To reduce the number of entries in a routing table and the amount of routing information to be transmitted, configure a non-backbone area on the border of an AS as a stub area or an NSSA. For details about how to configure an OSPFv3 stub area, see [Configuring an OSPFv3 Stub Area](dc_vrp_ospfv3_cfg_2080.html).

OSPFv3 stub areas cannot import external routes from outside an AS, nor can they learn the external routes imported by the other areas in the same AS. To import external routes to an area and minimize resource consumption, configure the area as an NSSA. NSSAs can import the external routes (outside an AS) and advertise them within the entire AS, without learning external routes from the other areas in the AS. This reduces the consumption of bandwidth and storage resources on the Router.

NSSA attributes must be configured on all Routers in an NSSA.


#### Pre-configuration Tasks

Before configuring an OSPFv3 NSSA, complete the following tasks:

* Configure an IP address for each interface to ensure that neighboring devices can communicate with each other at the network layer.
* [Configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. (Optional) Run [**lsa-forwarding-address**](cmdqueryname=lsa-forwarding-address) { **standard** | **zero-translate** }
   
   
   
   The OSPFv3 forwarding address (FA) function is enabled.
4. Run [**area**](cmdqueryname=area) *area-id*
   
   
   
   The OSPFv3 area view is displayed.
5. Run [**nssa**](cmdqueryname=nssa) [ { **default-route-advertise** [ **backbone-peer-ignore** | **cost** *cost-value* | **type** *type-value* | **tag** *tag-value* ] \* } | **no-import-route** | **no-summary** | **translator-always** | **translator-interval** *interval-value* | **set-n-bit** | **suppress-forwarding-address** ] \*
   
   
   
   The specified area is configured as an NSSA.
   
   The usage scenarios of the [**nssa**](cmdqueryname=nssa) command parameters are as follows:
   
   * To allow default Type 7 LSA generation, specify [**default-route-advertise**](cmdqueryname=default-route-advertise). After this parameter is specified, a Type 7 LSA default route will be generated on an ABR, regardless of whether the route ::/0 exists in the ABR's routing table. On an ASBR, however, a Type 7 LSA default route can be generated only if the route ::/0 exists in the ASBR's routing table.
   * If an ASBR also functions as an ABR, specifying **no-import-route** prevents OSPFv3 from advertising the external routes imported using the [**import-route**](cmdqueryname=import-route) command to the NSSA.
   * To reduce the number of LSAs to be transmitted to the NSSA, specify **no-summary** on an ABR. This prevents the ABR from transmitting Summary LSAs (Type 3 LSAs) to the NSSA.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After the [**nssa**](cmdqueryname=nssa) **default-route-advertise** **backbone-peer-ignore** **no-summary** command is run, the ABR generates both the default Type 7 LSA and default Type 3 LSA as long as the backbone area contains interfaces that are up, regardless of whether neighbor relationships in Full state exist. In this case, the default Type 3 LSA preferentially takes effect.
   * After **set-n-bit** is set, the DD packets sent by the Router carry the N-bit of 1.
   * If multiple ABRs are deployed in the NSSA, OSPFv3 automatically selects an ABR (generally the ABR with the largest router ID) as a translator to translate Type 7 LSAs into Type 5 LSAs. Each change of a translator causes LSA flooding. To prevent this issue, specify **translator-always** on an ABR to configure the ABR as a fixed translator. To allow two ABRs to participate in load balancing, configure **translator-always** on the ABRs.
   * To ensure service continuity during translator switching, specify the **translator-interval** parameter. The value of *interval-value* must be greater than the flooding interval.
   * To disable translated Type 5 LSAs from carrying an FA, specify the **suppress-forwarding-address** parameter.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **routing** [ [ *ipv6-address* *prefix-length* ] | **abr-routes** | **asbr-routes** | **ase-routes** | **inter-routes** | **intra-routes** | **nssa-routes** ] [ **verbose** ] command to check the OSPFv3 routing table information.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **lsdb** [ **area** *area-id* ] [ [ **originate-router** *advertising-router-id* | **hostname** *hostname* ] | **self-originate** ] { **grace** | **inter-prefix** | **inter-router** | **intra-prefix** | **link** | **network** | **router** | **router-information** | **nssa** } [*link-state-id* ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ] command to check the OSPFv3 LSDB information.