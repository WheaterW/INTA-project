Configuring Standard RADIUS Attributes
======================================

Configuring Standard RADIUS Attributes

#### Context

For details about the RADIUS attributes supported by the device, see Description of RADIUS Attributes. The content, format, and encapsulation mode of some RADIUS attributes can be configured.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure standard RADIUS attributes in the system view as required.
   
   
   
   **Table 1** Configuring standard RADIUS attributes in the system view
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the No. 8 RADIUS attribute (Framed-IP-Address). | **[**radius-attribute**](cmdqueryname=radius-attribute)** **framed-ip-address** ****encapsulation-method**** **{** **version1** **|** **version2** **}** | Run this command to configure the encapsulation mode of the No. 8 RADIUS public attribute Framed-IP-Address. |
   | Configure the No. 22 RADIUS Attribute (Framed-route) | **[**radius-attribute**](cmdqueryname=radius-attribute+framed-route+support+default-route)** **framed-route** **support** **default-route** | Run this command to configure the device to generate a default route based on the route carried in the Framed-route attribute delivered by the RADIUS server. |
   | Configure the No. 32 RADIUS attribute (NAS-Identifier). | **radius-attribute nas-identifier max-length unlimited** | Run this command to remove the length limit of the No. 32 RADIUS public attribute NAS-Identifier. |
   | Configure the No. 55 RADIUS attribute (Event-Timestamp). | **[**radius-attribute event-timestamp encapsulation-type system-time**](cmdqueryname=radius-attribute+event-timestamp+encapsulation-type+system-time)** | Run this command to set the Event-Timestamp attribute value to the current system time. |
   | Configure the No. 99 RADIUS attribute (Framed-Ipv6-Route). | **[**radius-attribute**](cmdqueryname=radius-attribute+framed-route+support+default-route)** **framed-ipv6-route** **support** **default-route** | Run this command to configure the device to generate a default route based on the route carried in the Framed-IPv6-route attribute delivered by the RADIUS server. |
3. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
   
   
   
   The RADIUS server group view is displayed.
4. Configure standard RADIUS attributes in the RADIUS server group view as required.
   
   
   
   **Table 2** Configuring standard RADIUS attributes in the RADIUS server group view
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the No. 5 RADIUS attribute (NAS-Port). | [**radius-server format-attribute**](cmdqueryname=radius-server+format-attribute) **nas-port** *format-string* | Run this command to configure the format of the No. 5 RADIUS public attribute NAS-Port. |
   | Configure the No. 25 RADIUS attribute (Class). | [**radius-server class-as-car**](cmdqueryname=radius-server+class-as-car) **[ enable-pir ]** | Run this command to configure the No. 25 RADIUS public attribute Class to carry the CAR value. |
   | Configure the No. 25 RADIUS attribute (Class). | **[**radius-attribute assign class partial-match**](cmdqueryname=radius-attribute+assign+class+partial-match)** **string-value** **[**pppoe**](cmdqueryname=pppoe)** **[**motm**](cmdqueryname=motm)** [ ****encap-format**** **format-sting* *delimiter**  | ****exclude**** ****local**** ] \* | Run this command to configure the device to encapsulate the Class attribute into a PPP packet's MOTM field. |
   | Configure the No. 26 RADIUS attribute (Vendor-Specific). | [**radius-attribute vendor**](cmdqueryname=radius-attribute+vendor) { { **huawei** | **microsoft** | **3gpp2** | **redback** | **dslforum** | **other** }\* | **all** } **continuous** | Run this command to configure the device to encapsulate multiple proprietary attributes into the No. 26 RADIUS public attribute Vendor-Specific. |
   | Configure the No. 30 RADIUS attribute (Called-Station-Id). | [**radius-server called-station-id**](cmdqueryname=radius-server+called-station-id) **include** { **ap-ip** **account-request**  | [ **delimiter** *delimiter* ] { **ap-mac** [ **mac-format** *type1* ] [ **delimiter** *delimiter* ] | **ssid** [ **delimiter** *delimiter* ] } \* } | Run this command to configure the method of constructing the No. 30 RADIUS public attribute Called-Station-Id. |
   | Configure the No. 31 RADIUS attribute (Calling-Station-Id) in Huawei format. | [**radius-server calling-station-id**](cmdqueryname=radius-server+calling-station-id) **include** { **refer-option61** | **vlan-binding** | **vlan-description** | **line-id** | **llid** **user-type** { **ppp** | **lns** }\*} | Run this command to configure the method of generating the No. 31 RADIUS public attribute Calling-Station-Id. |
   | * [**radius-server calling-station-id include pevlan**](cmdqueryname=radius-server+calling-station-id+include+pevlan) [ { **delimiter** **delimiter-vlan** } [ **cevlan** ] ] * [**radius-server calling-station-id include cevlan**](cmdqueryname=radius-server+calling-station-id+include+cevlan) [ { **delimiter** **delimiter-vlan** } [ **pevlan** ] ] | Run this command to configure the device to construct the No. 31 RADIUS public attribute Calling-Station-Id based on the user PE-VLAN ID and CE-VLAN ID. |
   | [**radius-server calling-station-id**](cmdqueryname=radius-server+calling-station-id) **lns-default** **version1** | Run this command to configure the default format for constructing the Calling-Station-Id attribute on the LNS. The RADIUS authentication and accounting packets sent by the LNS carry a default Calling-Station-Id attribute, even if the LAC does not send the Calling-Number attribute to the LNS. |
   | [**radius-server calling-station-id**](cmdqueryname=radius-server+calling-station-id) **lns-default** **version1** **force** | Run this command to enable the LNS to construct the Calling-Station-Id attribute based on the version1 format. |
   | [**radius-server format-attribute calling-station-id**](cmdqueryname=radius-server+format-attribute+calling-station-id) **vendor** *vendor-id* [ **include** **option82** ] [ **version1** ] | The device is configured to encapsulate the No. 31 RADIUS public attribute Calling-Station-Id in the specified format. |
   | [**radius-server format-attribute calling-station-id user-defined version3**](cmdqueryname=radius-server+format-attribute+calling-station-id+user-defined+version3) | Run this command to configure the No. 31 RADIUS public attribute Calling-Station-Id to be encapsulated in the version 3 format. |
   | [**radius-server format-attribute include sub-slot**](cmdqueryname=radius-server+format-attribute+include+sub-slot) | Run this command to configure the device to encapsulate the subcard ID into the No. 31 RADIUS public attribute Calling-Station-Id and the Nas-Port-Id attribute. |
   | Configure the No. 87 RADIUS attribute (NAS-Port-Id). | [**radius-server format-attribute**](cmdqueryname=radius-server+format-attribute) **nas-port-id** { **vendor** { *vendor-id* [ *format-string* ] | **redback-simple** | **redback-addition** } | **version1** | **version2** } | Run this command to configure the format of the No. 87 RADIUS public attribute NAS-Port-Id. |
   | Configure the No. 87 RADIUS attribute (NAS-Port-Id). | [**radius-server nas-port-id lns**](cmdqueryname=radius-server+nas-port-id+lns) **include** [ **string** *string* | **ip** *delimiter* ] { **local-tunnel-ip** [ *delimiter* ] | **peer-tunnel-ip** [ *delimiter* ] | **local-tunnel-id** [ *delimiter* ] | **peer-tunnel-id** [ *delimiter* ] | **local-session-id** [ *delimiter* ] **peer-session-id** [ *delimiter* ] | **call-serial-number** [ *delimiter* ] } \* | Run this command to configure the format of the NAS-Port-Id attribute sent by the L2TP LNS to the RADIUS server. |
   | Configure the No. 87 RADIUS attribute (NAS-Port-Id). | [**radius-server nas-port-id**](cmdqueryname=radius-server+nas-port-id) **include** [ **delimiter** *delimiter-val* ] { **interface-description** [ **delimiter** *int-delimiter-val* ] | **pe-vlan** [ **delimiter** *pevlan-delimiter-val* ] | **ce-vlan** [ **delimiter** *cevlan-delimiter-val* ] } | Run this command to configure the non-L2TP LNS to send the NAS-Port-Id attribute in a user-defined format to the RADIUS server. |
   | Configure the No. 100 RADIUS attribute (Framed-Ipv6-Pool). | [**radius-attribute apply framed-ipv6-pool match pool-type**](cmdqueryname=radius-attribute+apply+framed-ipv6-pool+match+pool-type) | Run this command to configure an IPv6 address pool to be delivered by a RADIUS server using the No. 100 RADIUS public attribute Framed-Ipv6-Pool attribute to replace the IPv6 address pools of the same type configured in a domain. |
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.