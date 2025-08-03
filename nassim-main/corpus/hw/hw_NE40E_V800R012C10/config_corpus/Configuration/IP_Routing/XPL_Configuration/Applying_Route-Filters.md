Applying Route-Filters
======================

After a route-filter is created, it must be referenced
by a route-policy to take effect.

#### Context

Currently, route-filters apply to OSPF/OSPFv3, RIP/RIPng, IS-IS,
BGP/BGP4+. Perform one or more of the following configurations as
required:

* [Apply route-filters
  to OSPF.](#EN-US_TASK_0172366616__step_dc_vrp_xpl_cfg_001006)
* [Apply route-filters
  to RIP.](#EN-US_TASK_0172366616__step_dc_vrp_xpl_cfg_001004)
* [Apply route-filters
  to RIPng.](#EN-US_TASK_0172366616__step_dc_vrp_xpl_cfg_001005)
* [Apply
  route-filters to IS-IS.](#EN-US_TASK_0172366616__step_dc_vrp_xpl_cfg_001001)
* [Apply
  route-filters to BGP.](#EN-US_TASK_0172366616__step_dc_vrp_xpl_cfg_001002)
* [Apply
  route-filters to BGP4+.](#EN-US_TASK_0172366616__step_dc_vrp_xpl_cfg_001003)


#### Procedure

* Apply
  route-filters to OSPF.
  
  
  
  Route-filters can be used in OSPF route selection and interaction
  between OSPF and other routing protocols. [Table 1](#EN-US_TASK_0172366616__tab_dc_vrp_xpl_cfg_001006) lists
  usage scenarios and relevant configuration tasks.
  
  **Table 1** Route-filter application in OSPF
  | Usage Scenario | Relevant Configuration Task |
  | --- | --- |
  | Use a route-filter to filter the routes to be imported by OSPF. | [Configuring OSPF to Import External Routes](dc_vrp_ospf_cfg_2040.html) |
  | Use a route-filter to filter the default routes to be imported by OSPF. | [Configuring OSPF to Import a Default Route](dc_vrp_ospf_cfg_2041.html) |
  | Use a route-filter to filter LSAs in an Area. | [Configuring OSPF to Filter LSAs in an Area](dc_vrp_ospf_cfg_2044.html) |
  | Use a route-filter to filter the routes received by OSPF. | [Configuring OSPF to Filter Received Routes](dc_vrp_ospf_cfg_0044.html) |
* Apply
  route-filters to RIP.
  
  
  
  Route-filters can be used in RIP route selection and interaction
  between RIP and other routing protocols. [Table 2](#EN-US_TASK_0172366616__tab_dc_vrp_xpl_cfg_001004) lists
  usage scenarios and relevant configuration tasks.
  
  **Table 2** Route-filter application in RIP
  | Usage Scenario | Relevant Configuration Task |
  | --- | --- |
  | Use a route-filter to filter the routes to be imported by RIP. | [Configuring RIP to Import External Routes](dc_vrp_rip_cfg_0026.html) |
  | Use a route-filter to filter the default routes to be advertised by RIP. | [Configuring RIP to Advertise Default Routes](dc_vrp_rip_cfg_0025.html) |
* Apply
  route-filters to RIPng.
  
  
  
  Route-filters can be used in interaction between RIPng and
  other routing protocols. [Table 3](#EN-US_TASK_0172366616__tab_dc_vrp_xpl_cfg_001005) lists
  usage scenarios and relevant configuration tasks.
  
  **Table 3** Route-filter application in RIPng
  | Usage Scenario | Relevant Configuration Task |
  | --- | --- |
  | Use a route-filter to filter the routes to be imported by RIPng. | [Configuring RIPng to Import External Routes](dc_vrp_ripng_cfg_0019.html) |
* Apply route-filters to
  IS-IS.
  
  
  
  Route-filters can be used in IS-IS route selection and interaction
  between IS-IS and other routing protocols. [Table 4](#EN-US_TASK_0172366616__tab_dc_vrp_xpl_cfg_001001) lists
  usage scenarios and relevant configuration tasks.
  
  **Table 4** Route-filter application in IS-IS
  | Usage Scenario | Relevant Configuration Task |
  | --- | --- |
  | Use a route-filter to control IS-IS route leaking. | [Configure IPv4 IS-IS route leaking](dc_vrp_isis_cfg_1007.html)  [Configure IPv6 IS-IS route leaking](dc_vrp_isis_cfg_1030.html) |
  | Use a route-filter to control IS-IS default route generation. | [Configure IS-IS to generate default IPv4 routes](dc_vrp_isis_cfg_1011.html)  [Configure IS-IS to generate default IPv6 routes](dc_vrp_isis_cfg_1034.html) |
  | Use a route-filter to filter the routes to be imported by IS-IS. | [Configure IS-IS to import external IPv4 routes](dc_vrp_isis_cfg_1015.html)  [Configure IS-IS to import external IPv6 routes](dc_vrp_isis_cfg_1038.html) |
* Apply route-filters to
  BGP.
  
  
  
  Route-filters can be used to set BGP route attributes and
  filter the routes to be imported, advertised, or received. [Table 5](#EN-US_TASK_0172366616__tab_dc_vrp_xpl_cfg_001002) lists
  usage scenarios and relevant configuration tasks.
  
  **Table 5** Route-filter application in BGP
  | Usage Scenario | Relevant Configuration Task |
  | --- | --- |
  | Use a route-filter to set a priority for BGP routes. | [Setting a BGP Preference Value](dc_vrp_bgp_cfg_4011.html) |
  | Use a route-filter to filter the routes to be imported by BGP. | [Configuring BGP to Import Routes](dc_vrp_bgp_cfg_3007.html) |
  | Use a route-filter to filter the routes to be advertised by BGP. | [Using XPL to Filter the BGP Routes to Be Advertised](dc_vrp_bgp_cfg_3101.html) |
  | Use a route-filter to filter the routes to be received by BGP. | [Using XPL to Filter the BGP Routes to Be Received](dc_vrp_bgp_cfg_3102.html) |
* Apply route-filters to
  BGP4+.
  
  
  
  Route-filters can be used to set BGP4+ route attributes and
  filter the routes to be imported, advertised, or received. [Table 6](#EN-US_TASK_0172366616__tab_dc_vrp_xpl_cfg_001003) lists
  usage scenarios and relevant configuration tasks.
  
  **Table 6** Route-filter application in BGP4+
  | Usage Scenario | Relevant Configuration Task |
  | --- | --- |
  | Use a route-filter to set a priority for BGP4+ routes. | [Configuring BGP4+ to Import Routes](dc_vrp_bgp6_cfg_0010.html) |
  | Use a route-filter to filter the routes to be imported by BGP4+. | [Setting a BGP4+ Preference](dc_vrp_bgp6_cfg_0020.html) |
  | Use a route-filter to filter the routes to be advertised by BGP4+. | [Using XPL to Filter the BGP4+ Routes to Be Advertised](dc_vrp_bgp6_cfg_0088.html) |
  | Use a route-filter to filter the routes to be received by BGP4+. | [Using XPL to Filter the BGP4+ Routes to Be Received](dc_vrp_bgp6_cfg_0089.html) |