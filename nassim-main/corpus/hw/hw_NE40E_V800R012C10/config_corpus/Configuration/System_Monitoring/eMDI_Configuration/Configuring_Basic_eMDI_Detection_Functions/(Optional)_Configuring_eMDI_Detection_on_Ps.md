(Optional) Configuring eMDI Detection on Ps
===========================================

This section describes how to configure eMDI detection on Ps.

#### Context

Only NG MVPN networks support eMDI detection on video streams passing through Ps. eMDI detection is disabled by default. To enable eMDI detection on Ps, perform the following steps.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**emdi**](cmdqueryname=emdi)
   
   
   
   The eMDI view is displayed.
3. Run [**emdi match-mpls-label enable**](cmdqueryname=emdi+match-mpls-label+enable)
   
   
   
   eMDI detection on Ps is enabled.
4. Run [**emdi channel-group**](cmdqueryname=emdi+channel-group) *channel-group-name*
   
   
   
   An eMDI channel group is created or an existing channel group view is displayed.
5. Run [**emdi channel**](cmdqueryname=emdi+channel) *channel-name* **source** *source-address* **group** *group-address* **transit**
   
   
   
   A multicast channel is added to an eMDI channel group to enable eMDI detection on Ps.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   eMDI detection takes effect on Ps only after both the [**emdi match-mpls-label enable**](cmdqueryname=emdi+match-mpls-label+enable) and [**emdi channel**](cmdqueryname=emdi+channel) **source** *source-address* **group** *group-address* **transit** commands are run.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.