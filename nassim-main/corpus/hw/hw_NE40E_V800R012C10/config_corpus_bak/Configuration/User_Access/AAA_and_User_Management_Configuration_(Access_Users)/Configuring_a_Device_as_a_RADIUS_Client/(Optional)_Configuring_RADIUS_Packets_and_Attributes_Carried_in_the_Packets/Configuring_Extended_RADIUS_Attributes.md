Configuring Extended RADIUS Attributes
======================================

Configuring_Extended_RADIUS_Attributes

#### Context

The content or format of some Huawei proprietary RADIUS attributes can be configured.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure extended RADIUS attributes in the system view as required.
   
   
   
   **Table 1** Configuring extended RADIUS attributes in the system view
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure Huawei No. 181 extended RADIUS attribute (HW-Acct-terminate-subcause). | [**radius-attribute hw-acct-terminate-subcause encapsulation-type**](cmdqueryname=radius-attribute+hw-acct-terminate-subcause+encapsulation-type) { **string** | **integer** } | Run this command to configure the device to encapsulate the Huawei proprietary No. 181 attribute HW-Acct-terminate-subcause of a specified type into a RADIUS packet. |
3. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
   
   
   
   The RADIUS server group view is displayed.
4. Configure extended RADIUS attributes in the RADIUS server group view as required.
   
   
   
   **Table 2** Configuring extended RADIUS attributes in the RADIUS server group view
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure Huawei No. 31 extended RADIUS attribute (HW-QOS-Profile-Name). | [**radius-attribute case-sensitive qos-profile-name**](cmdqueryname=radius-attribute+case-sensitive+qos-profile-name) | Run this command to configure the Huawei No. 31 extended RADIUS attribute HW-QOS-Profile-Name to be case-sensitive. The QoS profile name on the device is case-sensitive. If the QoS profile name delivered by the RADIUS server is also case-sensitive, the QoS profile names must be of the same case. Otherwise, the QoS policy may be incorrect. |
   | Configure Huawei No. 153 extended RADIUS attribute (HW-User-Mac). | [**radius-attribute usermac-as-option61**](cmdqueryname=radius-attribute+usermac-as-option61) | Run this command to configure the device to encapsulate Huawei No. 153 extended RADIUS attribute HW-User-Mac based on the Option 61 attribute. If you also run the [**client-option82**](cmdqueryname=client-option82) **version1** command on the BAS interface, the client-id information (DHCPv4 Option61/DHCPv6 Option1/PPPoE PADR Tag 0x0103 Host-unique) is encapsulated into the Class attributes in RADIUS accounting packets. |
   | Configure Huawei No. 167 extended RADIUS attribute (HW-PCP-Server-Name). | **[**radius-attribute assign hw-pcp-server-name**](cmdqueryname=radius-attribute+assign+hw-pcp-server-name)**  { **dhcp** *dhcp-option-code* | **dhcpv6** *dhcpv6-option-code* } | Run this command to configure the device to encapsulate Huawei No. 167 extended RADIUS attribute HW-PCP-Server-Name into a specified DHCP/DHCPv6 option. |
   | Configure Huawei No. 196 extended RADIUS attribute (HW-MNG-IPv6). | **[**radius-attribute assign hw-mng-ipv6 pppoe motm**](cmdqueryname=radius-attribute+assign+hw-mng-ipv6+pppoe+motm)** [ ****encap-format**** **format-sting* *delimiter** | **exclude** **local** ] \* | The device is configured to encapsulate Huawei No. 196 extended RADIUS attribute (HW-MNG-IPv6) delivered by the RADIUS server into the MOTM field of PPP packets. |
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.