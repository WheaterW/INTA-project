Configuring OSPF to Advertise a Default Route
=============================================

Configuring OSPF to Advertise a Default Route

#### Prerequisites

Before configuring OSPF to advertise a default route, you have completed the following tasks:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).
* To use a route-policy to filter the default route, create the route-policy first.

#### Context

In actual networking scenarios, usually multiple devices are deployed on the area border and AS border of an OSPF network for next-hop backup or traffic load balancing. A default route can be configured to reduce routing entries and improve resource utilization on the OSPF network.

OSPF default routes are generally applied to the following scenarios:

1. An ABR in an area advertises Type 3 LSAs carrying the default route information within the area. Devices in the area use the received default route information to forward inter-area packets.
2. An ASBR in an AS advertises Type 5 or Type 7 LSAs carrying the default route information within the AS. Devices in the AS use the received default route information to forward AS external packets.

If no matching route is found, the default route can be used to forward packets.

The default route information carried in Type 3 LSAs takes precedence over that carried in Type 5 or Type 7 LSAs.

The rules for advertising default routes in different types of OSPF areas vary, as shown in [Table 1](#EN-US_TASK_0000001176742939__tab_dc_vrp_ospf_cfg_204101).

**Table 1** Default route advertising mode
| Area Type | Generation Condition | Advertised By | LSA Type | Flooding Area |
| --- | --- | --- | --- | --- |
| Common area | The [**default-route-advertise**](cmdqueryname=default-route-advertise) command is run. | ASBR | Type 5 LSA | Common area |
| Stub area | Automatically | ABR | Type 3 LSA | Stub area |
| NSSA | The [**nssa**](cmdqueryname=nssa) [ **default-route-advertise** ] command is run. | ASBR | Type 7 LSA | NSSA |
| Automatically | ABR | Type 7 LSA | NSSA |
| Totally NSSA | Automatically | ABR | Type 3 LSA | NSSA |

Perform the following steps on the ASBR running OSPF.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Import default routes to the OSPF process.
   
   
   ```
   [default-route-advertise](cmdqueryname=default-route-advertise) [ [ always | permit-calculate-other ] | cost costvalue | type typevalue | route-policy route-policy-name | distribute-delay delaytimer | tag tagvalue ] *
   ```
   
   Or
   
   ```
   [default-route-advertise](cmdqueryname=default-route-advertise) [ permit-calculate-other | cost costvalue | type typevalue | route-policy route-policy-name | distribute-delay delaytimer | tag tagvalue | permit-preference-less-than preference-val ] *
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   To prevent loops, you are advised to specify **permit-preference-less-than** to prevent low-priority active default routes from being imported. This parameter is used only when **always** is not specified.
   
   For details about how to configure the default route in an NSSA, see [Configuring an OSPF NSSA](vrp_ospf_cfg_0031.html).
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **routing** *ip-address* [ *mask* | *mask-length* ] command to check information about the default route advertised to a common OSPF area.