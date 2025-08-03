Configuring a BSR Administrative Domain
=======================================

By dividing a PIM-SM network into multiple BootStrap router (BSR) administrative domains and a global domain, the workload of a single BSR is reduced and private group addresses can be used for providing special services for users in specific domains.

#### Context

By default, one PIM-SM domain has only one BSR to manage the entire domain.

To manage networks effectively, configure multiple BSR administrative domains on a PIM-SM network. Each BSR administrative domain maintains only one BSR that serves a multicast group within a specific address range. The multicast group that does not belong to any BSR administrative domain belongs to the global domain. The global domain maintains a BSR that serves the other multicast groups.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

You can adjust the hash mask length and priority of the Candidate-BootStrap Router (C-BSR):

* Global configuration: See [Adjusting C-BSR Parameters](dc_vrp_multicast_cfg_0018.html). The global value takes effect in both the global domain and BSR administrative domains.
* BSR administrative domain configuration: The configuration for the BSR administrative domain takes precedence over the global configuration. If the configuration for the BSR administrative domain is not available, the global configuration is used.
* Global domain configuration: The configuration for the global domain takes precedence over the global configuration. If the configuration for the global domain is not available, the global configuration is used.


#### Procedure

1. Enable the BSR administrative domain function on all Routers.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
      
      
      
      The PIM view is displayed.
   3. Run [**c-bsr admin-scope**](cmdqueryname=c-bsr+admin-scope)
      
      
      
      The BSR administrative domain function is enabled.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Set the ranges of multicast groups that Candidate-BootStrap Routers (C-BSRs) in the BSR administrative domain serve and adjust the hash mask lengths and priorities of the C-BSRs in the BSR administrative domain on all C-BSRs.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
      
      
      
      The PIM view is displayed.
   3. Run [**c-bsr group**](cmdqueryname=c-bsr+group) *group-address* { *mask* | *mask-length* } [ **hash-length** *hash-length* | **priority** *priority* ] \*
      
      
      
      The range of the multicast groups that a C-BSR in the BSR administrative domain serves is set, and the hash mask length and priority of the C-BSR in the BSR administrative domain are adjusted.
      
      *group-address* { *mask* | *mask-length* }: specifies the range of the multicast groups that the C-BSR in the BSR administrative domain serves. The valid multicast groups range from 239.0.0.0 to 239.255.255.255. The ranges of multicast groups that C-BSRs in different BSR administrative domains serve can overlap. The multicast group takes effect only in the local administrative domain, that is, a private multicast group address is used.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. (Optional) Adjust the hash mask lengths and priorities of all the C-BSRs in the global domain.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
      
      
      
      The PIM view is displayed.
   3. Run [**c-bsr global**](cmdqueryname=c-bsr+global) [ **hash-length** *hash-length* | **priority** *priority* ] \*
      
      
      
      The hash mask length and priority of a C-BSR in the global domain are adjusted.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.