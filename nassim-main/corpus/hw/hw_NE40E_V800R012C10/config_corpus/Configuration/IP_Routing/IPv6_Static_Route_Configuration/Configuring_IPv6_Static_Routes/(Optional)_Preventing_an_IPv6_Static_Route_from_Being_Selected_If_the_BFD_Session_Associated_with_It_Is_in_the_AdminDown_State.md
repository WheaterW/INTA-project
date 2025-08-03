(Optional) Preventing an IPv6 Static Route from Being Selected If the BFD Session Associated with It Is in the AdminDown State
==============================================================================================================================

This section describes how to configure the Router not to select an IPv6 static route if the BFD session associated with it is in the AdminDown state. This ensures that Huawei devices can interwork with non-Huawei devices.

#### Context

By default, an IPv6 static route can still be selected by Huawei devices even though the BFD session associated with it is in the AdminDown state, but not by non-Huawei devices. As a result, Huawei devices cannot interwork with non-Huawei devices.

To address this problem, run the [**ipv6 route-static track bfd-session admindown invalid**](cmdqueryname=ipv6+route-static+track+bfd-session+admindown+invalid) command to configure the Router not to select the IPv6 static route if the BFD session associated with it is in the AdminDown state.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 route-static track bfd-session**](cmdqueryname=ipv6+route-static+track+bfd-session) **session-name** *bfd-name* **admindown invalid**
   
   
   
   The Router has been configured not to select the IPv6 static route if the BFD session associated with it is in the AdminDown state.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.