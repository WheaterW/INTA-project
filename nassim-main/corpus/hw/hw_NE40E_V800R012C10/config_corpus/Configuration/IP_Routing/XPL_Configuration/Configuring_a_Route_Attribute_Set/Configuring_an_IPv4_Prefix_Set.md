Configuring an IPv4 Prefix Set
==============================

IPv4 prefix sets apply to all dynamic routing protocols and can be used to match source, destination, and next hop IP addresses.

#### Procedure

* Configure an IPv4 prefix set using the paragraph-by-paragraph editing mode.
  1. Run the [**edit xpl ip-prefix-list**](cmdqueryname=edit+xpl+ip-prefix-list) *ip-prefix-list-name* command to enter the IPv4 prefix set paragraph-by-paragraph editing view.
  2. Press **i** to enter the text editing mode.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Sets or route-filters can be configured only in the text editing mode. If you exit from the text editing mode, you can perform shortcut key operations only.
  3. Configure a start clause ([**xpl ip-prefix-list**](cmdqueryname=xpl+ip-prefix-list) *ip-prefix-list-name*) for an IPv4 prefix set.
  4. Configure elements (IPv4 addresses with masks, 1.1.1.0 24 for example) for the set and separate every two neighboring elements with a comma (,). You can use **eq**, **ge**, or **le** to specify the mask length.
  5. Configure an end clause (**end-list**) for the IPv4 prefix set.
  6. Press **Esc** to exit from the text editing mode.
  7. Press **:wq** and **Enter** to save the configurations and exit from the global variable set paragraph-by-paragraph editing view.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A message is displayed for you to confirm whether to commit the configurations when you attempt to exit from the global variable set paragraph-by-paragraph editing view. To commit the configurations, press **Y**.
     
     To exit from the global variable set paragraph-by-paragraph editing view without saving the configurations, press **:q!** and **Enter**.
* Configure an IPv4 prefix set using the line editing mode.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**xpl ip-prefix-list**](cmdqueryname=xpl+ip-prefix-list) *ip-prefix-list-name* command to enter the IPv4 prefix set view.
  3. Configure elements (IPv4 addresses with masks, such as 1.1.1.0 24) for the set and separate every two neighboring elements with a comma (,). You can use **eq**, **ge**, or **le** to specify the mask length.
  4. Run the [**end-list**](cmdqueryname=end-list) command to conclude the configuration of the IPv4 prefix set, exit the IPv4 prefix set view, and return to the system view.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Example

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If only paragraph-by-paragraph editing is used as an example, the corresponding line editing is similar. To use the line editing mode, perform the operations described in paragraph-by-paragraph editing.

For detailed set and route-filter configuration steps, see [Configuration Procedures for Sets and Route-Filters Using the Paragraph-by-Paragraph Editing Mode](dc_vrp_xpl_cfg_0002.html#EN-US_CONCEPT_0000001793384325__section_dc_vrp_xpl_cfg_000102). For details about XPL clauses, see [XPL Paragraph Editing Clauses](dc_vrp_xpl_cfg_0014.html).

| **Objective** | Configure an IPv4 prefix set to match the routes in 1.1.1.0/24, 2.2.2.0/24, and 3.3.3.3/32 network segments. |
| --- | --- |
| **Configuration Example 1** | ``` <HUAWEI> edit xpl ip-prefix-list aaa  xpl ip-prefix-list aaa 1.1.1.0 24, 2.2.2.0 24, 3.3.3.3 32 end-list ```  This prefix set includes three elements and matches the routes in 1.1.1.0/24, 2.2.2.0/24, and 3.3.3.3/32 network segments. |
| **Objective** | Configure an IPv4 prefix set to match the routes in network segment 1.1.1.0/24 with the mask length ranging from 26 to 30 bits, the routes in network segment 2.2.2.0/24 with the mask length greater than or equal to 28 bits, and the routes in network segment 3.3.3.0/24 with the mask length of 30 bits. |
| **Configuration Example 2** | ``` <HUAWEI> edit xpl ip-prefix-list bbb  xpl ip-prefix-list bbb 1.1.1.0 24 ge 26 le 30, 2.2.2.0 24 ge 28, 3.3.3.0 24 eq 30 end-list ```  This IPv4 prefix set includes three elements and matches the routes in network segment 1.1.1.0/24 with the mask length ranging from 26 to 30 bits, the routes in network segment 2.2.2.0/24 with the mask length greater than or equal to 28 bits, and the routes in network segment 3.3.3.0/24 with the mask length of 30 bits. |
| **Objective** | Configure a route-filter to set MED 60 for the routes that match IPv4 prefix set **bbb**, set MED 70 for the routes that do not match IPv4 prefix set **bbb** but match **aaa**, and set MED 80 for all other routes. |
| **Reference Example** | ``` <HUAWEI> edit xpl route-filter r1  xpl route-filter r1 if ip route-destination in bbb then apply med 60 elseif ip route-destination in aaa then apply med 70 else apply med 80 endif end-filter ```  The route-filter references two IPv4 destination address prefix sets (**aaa** and **bbb**) and sets MED 60 for the routes that match the set **bbb**, sets MED 70 for the routes that do not match the set **bbb** but match the set **aaa**, and sets MED 80 for all other routes. |