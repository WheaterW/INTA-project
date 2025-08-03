Configuring an IPv6 Prefix Set
==============================

IPv6 prefix sets apply to all dynamic routing protocols and can be used to match source, destination, and next hop IPv6 addresses.

#### Procedure

* Configure an IPv6 prefix set using the paragraph-by-paragraph editing mode.
  1. Run the [**edit xpl ipv6-prefix-list**](cmdqueryname=edit+xpl+ipv6-prefix-list) *ipv6-prefix-list-name* command to enter the paragraph-by-paragraph editing view of the IPv6 prefix set.
  2. Press **i** to enter the text editing mode.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Sets or route-filters can be configured only in the text editing mode. If you exit from the text editing mode, you can perform shortcut key operations only.
  3. Configure a start clause for the IPv6 prefix set using the [**xpl ipv6-prefix-list**](cmdqueryname=xpl+ipv6-prefix-list) *ipv6-prefix-list-name* command in the IPv6 prefix set paragraph-by-paragraph editing interface view.
  4. Configure elements (IPv6 addresses with a mask length, 2001:db8:0:1:: 64 for example) for the set in the IPv6 prefix set paragraph-by-paragraph editing interface view, and separate every two neighboring elements with a comma (,). You can use **eq**, **ge**, or **le** to specify the mask length.
  5. Configure an end clause for the IPv6 prefix set using the [**end-list**](cmdqueryname=end-list) command in the IPv6 prefix set paragraph-by-paragraph editing interface view.
  6. Press **Esc** to exit from the text editing mode.
  7. Press **:wq** and **Enter** to save the configurations and exit from the global variable set paragraph-by-paragraph editing view.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A message is displayed for you to confirm whether to commit the configurations when you attempt to exit from the global variable set paragraph-by-paragraph editing view. To commit the configurations, press **Y**.
     
     To exit from the global variable set paragraph-by-paragraph editing view without saving the configurations, press **:q!** and **Enter**.
* Configure an IPv6 prefix set using the line-by-line editing mode.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**xpl ipv6-prefix-list**](cmdqueryname=xpl+ipv6-prefix-list) *ipv6-prefix-list-name* command to enter the IPv6 prefix set view.
  3. Configure elements (IPv6 addresses with masks, such as 2001:db8:0:1::64) for the set and separate every two neighboring elements with a comma (,). You can use **eq**, **ge**, or **le** to specify the mask length.
  4. Run the [**end-list**](cmdqueryname=end-list) command to conclude the configuration of the IPv6 prefix set, exit the IPv6 prefix set view, and return to the system view.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Example

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If only paragraph-by-paragraph editing is used as an example, the corresponding line editing is similar. To use the line editing mode, perform the operations described in paragraph-by-paragraph editing.

For detailed set and route-filter configuration steps, see [Configuration Procedures for Sets and Route-Filters Using the Paragraph-by-Paragraph Editing Mode](dc_vrp_xpl_cfg_0002.html#EN-US_CONCEPT_0000001793384325__section_dc_vrp_xpl_cfg_000102). For details about XPL clauses, see [XPL Paragraph Editing Clauses](dc_vrp_xpl_cfg_0014.html).

| **Objective** | Configure an IPv6 prefix set to exactly match routes 2001:db8:0:1::/64, 2001:db8:1:1::/64, and 2001:db8:1:2::/64. |
| --- | --- |
| **Configuration Example 1** | ``` <HUAWEI> edit xpl ipv6-prefix-list aaa  xpl ipv6-prefix-list aaa 2001:db8:0:1:: 64, 2001:db8:1:1:: 64, 2001:db8:1:2:: 64 end-list ```  The IPv6 prefix set in configuration example 1 contains three elements and can exactly match routes 2001:db8:0:1::/64, 2001:db8:1:1::/64, and 2001:db8:1:2::/64. |
| **Objective** | Configure an IPv6 prefix set to match the routes in network segment 2001:db8:0:1::/64 with the mask length ranging from 96 to 100 bits, the routes in network segment 2001:db8:1:1::/64 with the mask length less than 100 bits, and the routes in network segment 2001:db8:1:2::/64 with the mask length of 96 bits. |
| **Configuration Example 2** | ``` <HUAWEI> edit xpl ipv6-prefix-list bbb  xpl ipv6-prefix-list bbb 2001:db8:0:1:: 64 ge 96 le 100, 2001:db8:1:1:: 64 le 100, 2001:db8:1:2:: 64 eq 96 end-list ```  This IPv6 prefix set includes three elements and matches the routes in network segment 2001:db8:0:1::/64 with the mask length ranging from 96 to 100 bits, the routes in network segment 2001:db8:1:1::/64 with the mask length less than 100 bits, and the routes in network segment 2001:db8:1:2::/64 with the mask length of 96 bits. |
| **Objective** | Configure an IPv6 prefix set to exactly match the route ::/64. |
| **Configuration Example 3** | ``` <HUAWEI> edit xpl ipv6-prefix-list ccc  xpl ipv6-prefix-list ccc :: 64 le 128 end-list ```  The IPv6 prefix set in configuration example 3 contains one element and can exactly match the route ::/64. |
| **Objective** | Configure an IPv6 prefix set to match all the routes with the mask length ranging from 64 to 128. |
| **Configuration Example 4** | ``` <HUAWEI> edit xpl ipv6-prefix-list ddd  xpl ipv6-prefix-list ddd :: 0 ge 64 le 128 end-list ```  The IPv6 prefix set configured in configuration example 4 contains one element and can match all the routes with the mask length ranging from 64 to 128. |
| **Objective** | Configure a route-filter to deny the routes that match set **bbb** and the routes that match neither set **aaa** nor **bbb** and permit the routes that do not match **bbb** but match **aaa** and increase their MED values by 10. |
| **Reference Example** | ``` <HUAWEI> edit xpl route-filter r1  xpl route-filter r1 if ipv6 route-destination in bbb then refuse elseif ipv6 route-destination in aaa then apply med + 10 else refuse endif end-filter ```  The route-filter references two IPv6 destination address prefix sets (**aaa** and **bbb**), denies the routes that match IPv6 destination address prefix set **bbb**, permits the routes that do not match **bbb** but match **aaa** and increases their MED values by 10, and denies all other routes. |