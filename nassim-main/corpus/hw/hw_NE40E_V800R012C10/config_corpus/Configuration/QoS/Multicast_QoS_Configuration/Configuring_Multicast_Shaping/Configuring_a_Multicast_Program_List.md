Configuring a Multicast Program List
====================================

A multicast program list contains one or more multicast addresses for identifying one or more IPTV channels or programs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run **[**multicast-list**](cmdqueryname=multicast-list)** *l*ist-name** [ **[**index**](cmdqueryname=index)** **list-index**] [****source-address**** **source-address** [ *source-mask-len* | **source-mask**] ] ****group-address**** **group-address**[ **group-mask-length** | **group-mask**] [****vpn-instance**** **vpn-instance-name**]
   
   
   
   A multicast program list is configured.
   
   
   
   The value of **group-address** *group-address* must be a multicast address.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.