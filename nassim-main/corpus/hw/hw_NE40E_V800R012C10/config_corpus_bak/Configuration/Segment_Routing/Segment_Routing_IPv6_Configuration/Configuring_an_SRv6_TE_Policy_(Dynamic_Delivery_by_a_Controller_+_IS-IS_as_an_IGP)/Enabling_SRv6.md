Enabling SRv6
=============

Other SRv6 TE Policy configurations can be performed only after SRv6 is enabled.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. (Optional) Run the [**evpn srv6 next-header-field**](cmdqueryname=evpn+srv6+next-header-field) { **59** | **143** } command to set a value for the Next Header field in an SRv6 extension header.
   
   
   
   If the value is 59 in earlier versions, you can perform this step to change the value to 59 to ensure compatibility with the earlier versions.
3. Run the [**te ipv6-router-id**](cmdqueryname=te+ipv6-router-id) *ipv6Addr* command to configure a global TE IPv6 router ID.
4. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) command to enable SRv6.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.