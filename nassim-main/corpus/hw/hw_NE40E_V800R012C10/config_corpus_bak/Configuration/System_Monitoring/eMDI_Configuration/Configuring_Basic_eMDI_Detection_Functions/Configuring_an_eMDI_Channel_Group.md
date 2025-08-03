Configuring an eMDI Channel Group
=================================

The channels to be detected need to be configured before the eMDI detection solution is used.

#### Context

Before configuring the multicast channels to be detected, create a channel group and add the multicast channels to the channel group.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**emdi**](cmdqueryname=emdi)
   
   
   
   eMDI detection is enabled and the eMDI view is displayed.
3. Run [**emdi channel-group**](cmdqueryname=emdi+channel-group) *channel-group-name*
   
   
   
   An eMDI channel group is created or the view of an existing eMDI channel group is displayed.
4. Run either of the following commands:
   
   
   * To add a specified multicast channel to the eMDI channel group in a BIER eMDI scenario, run the [**emdi channel**](cmdqueryname=emdi+channel) *channel-name* **source** *source-address* **group** *group-address* **vpn-instance** *vpn-instance-name* **sub-domain** *sub-domain-value* **bsl** *bsl-value* command.
   * To add a specified multicast channel to the eMDI channel group in other scenarios, run the [**emdi channel**](cmdqueryname=emdi+channel) *channel-name* **source** *source-address* **group** *group-address* [ **vpn-instance** *vpn-instance-name* | **vlan** *vlan-id* | **vsi** *vsi-name* | **bd** *bd-id* | **transit** ] [ **pt** *pt-value* ] [ **clock-rate** *clock-rate-value* ] [ **uncompressed** ] command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.