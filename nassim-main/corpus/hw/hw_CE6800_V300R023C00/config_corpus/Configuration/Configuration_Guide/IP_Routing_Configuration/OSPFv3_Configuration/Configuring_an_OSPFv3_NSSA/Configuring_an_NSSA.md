Configuring an NSSA
===================

Configuring an NSSA

#### Prerequisites

Before configuring an NSSA, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. (Optional) Enable the OSPFv3 forwarding address (FA) function.
   
   
   ```
   [lsa-forwarding-address](cmdqueryname=lsa-forwarding-address) { standard | zero-translate }
   ```
4. Enter the OSPFv3 area view.
   
   
   ```
   [area](cmdqueryname=area+%28OSPFv3+view%29) area-id
   ```
5. Configure the area as an NSSA.
   
   
   ```
   [nssa](cmdqueryname=nssa+%28OSPFv3+area+view%29) [ default-route-advertise [ backbone-peer-ignore | cost cost | type type | tag tag ] * | no-import-route | no-summary | translator-always | translator-interval translator-interval | set-n-bit | suppress-forwarding-address ] *
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```