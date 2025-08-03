Enabling IPv6 Multicast Routing
===============================

Enable IPv6 multicast routing on a Router before you configure other IPv6 multicast features on the Router.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast ipv6 routing-enable**](cmdqueryname=multicast+ipv6+routing-enable)
   
   
   
   IPv6 multicast routing is enabled.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   Running the [**undo multicast ipv6 routing-enable**](cmdqueryname=undo+multicast+ipv6+routing-enable) command will delete all IPv6 multicast configurations and interrupt running IPv6 multicast services. If you want to restore the IPv6 multicast services, re-configure multicast commands for which configurations have been deleted.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.