Configuring an SoO Set
======================

Site of origin (SoO) sets are used to match the SoOs of VPN routes.

#### Procedure

* Configure an SoO set using the paragraph-by-paragraph editing mode.
  1. Run the [**edit xpl extcommunity-list soo**](cmdqueryname=edit+xpl+extcommunity-list+soo) *soo-list-name* command to enter the SoO set paragraph-by-paragraph editing view.
  2. Press **i** to enter the text editing mode.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Sets or route-filters can be configured only in the text editing mode. If you exit from the text editing mode, you can perform shortcut key operations only.
  3. Configure a start clause ([**xpl extcommunity-list soo**](cmdqueryname=xpl+extcommunity-list+soo) *soo-list-name*) for an SoO set.
  4. Configure elements (SoOs of VPN routes) for the SoO set in the SoO set paragraph-by-paragraph editing interface view and separate every two neighboring elements with a comma (,). The elements can be configured in any of the following formats:
     
     
     + 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number is an integer ranging from 0 to 65535, and the user-defined number is an integer ranging from 0 to 4294967295. The AS number and user-defined number must not be both 0s. Specifically, the SoO must not be 0:0.
     + IPv4 address:2-byte user-defined number, for example, 192.168.122.15:1. The IPv4 address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number is an integer ranging from 0 to 65535.
     + Integral 4-byte AS number:2-byte user-defined number, for example, 0:3 or 65537:3. The integral 4-byte AS number ranges from 65536 to 4294967295, and the user-defined number is an integer ranging from 0 to 65535.
     + 4-byte AS number in dotted notation (*x*.*y*):2-byte user-defined number, for example, 0.0:3 or 0.1:0. The *x*, *y*, and user-defined number are integers ranging from 0 to 65535. The AS number and user-defined number must not be both 0s. Specifically, the SoO must not be 0.0:0.
     + **regular** *regular-expression*: matches VPN routes with SoO in the specified regular expression.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       Regular expression processing is computing-intensive. When a large number of regular expressions are configured in an XPL policy to match a BGP route attribute and the length of the route attribute is long, the processing performance of the XPL policy deteriorates. To improve the processing performance of the routing policy, decrease the number of regular expressions or use a non-regular expression matching command.
       
       It is recommended that a maximum of 100 regular expressions be configured for each policy.
  5. Configure an end clause for the SoO set using the [**end-list**](cmdqueryname=end-list) command in the SoO set paragraph-by-paragraph editing interface view.
  6. Press **Esc** to exit from the text editing mode.
  7. Press **:wq** and **Enter** to save the configurations and exit from the global variable set paragraph-by-paragraph editing view.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A message is displayed for you to confirm whether to commit the configurations when you attempt to exit from the global variable set paragraph-by-paragraph editing view. To commit the configurations, press **Y**.
     
     To exit from the global variable set paragraph-by-paragraph editing view without saving the configurations, press **:q!** and **Enter**.
* Configure an SoO set using the line-by-line editing mode.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**xpl extcommunity-list soo**](cmdqueryname=xpl+extcommunity-list+soo) *soo-list-name* command to enter the SoO set view.
  3. Configure elements (SoOs of VPN routes) for the SoO set and separate every two neighboring elements with a comma (,). The elements can be configured in any of the following formats:
     
     
     + 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number is an integer ranging from 0 to 65535, and the user-defined number is an integer ranging from 0 to 4294967295. The AS number and user-defined number must not be both 0s. Specifically, the SoO must not be 0:0.
     + IPv4 address:2-byte user-defined number, for example, 192.168.122.15:1. The IPv4 address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number is an integer ranging from 0 to 65535.
     + Integral 4-byte AS number:2-byte user-defined number, for example, 0:3 or 65537:3. The integral 4-byte AS number ranges from 65536 to 4294967295, and the user-defined number is an integer ranging from 0 to 65535.
     + 4-byte AS number in dotted notation (*x*.*y*):2-byte user-defined number, for example, 0.0:3 or 0.1:0. The *x*, *y*, and user-defined number are integers ranging from 0 to 65535. The AS number and user-defined number must not be both 0s. Specifically, the SoO must not be 0.0:0.
     + **regular** *regular-expression*: matches VPN routes with SoO in the specified regular expression.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       Regular expression processing is computing-intensive. When a large number of regular expressions are configured in an XPL policy to match a BGP route attribute and the length of the route attribute is long, the processing performance of the XPL policy deteriorates. To improve the processing performance of the routing policy, decrease the number of regular expressions or use a non-regular expression matching command.
       
       It is recommended that a maximum of 100 regular expressions be configured for each policy.
  4. Run the [**end-list**](cmdqueryname=end-list) command to conclude the configuration of the SoO set, exit the SoO set view, and return to the system view.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Example

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If only paragraph-by-paragraph editing is used as an example, the corresponding line editing is similar. To use the line editing mode, perform the operations described in paragraph-by-paragraph editing.

For detailed set and route-filter configuration steps, see [Configuration Procedures for Sets and Route-Filters Using the Paragraph-by-Paragraph Editing Mode](dc_vrp_xpl_cfg_0002.html#EN-US_CONCEPT_0000001793384325__section_dc_vrp_xpl_cfg_000102). For details about XPL clauses, see [XPL Paragraph Editing Clauses](dc_vrp_xpl_cfg_0014.html).

| **Objective** | Configure an SoO set to match the VPN routes carrying the SoO (100:1, 200:1, or 300:1). |
| --- | --- |
| **Configuration Example** | ``` <HUAWEI> edit xpl extcommunity-list soo soo-list1  xpl extcommunity-list soo soo-list1 100:1, 200:1, 300:1 end-list ```  The SoO set contains three elements and can match VPN routes carrying SoO 100:1, 200:1, or 300:1. |
| **Objective** | Configure a route-filter to overwrite the SoOs of the VPN routes carrying at least one of the SoOs specified in the set named **soo-list1** with 100:1 and 200:1. |
| **Reference Example** | ``` <HUAWEI> edit xpl route-filter r1  xpl route-filter r1 if extcommunity soo matches-any soo-list1 then apply extcommunity soo { 100:1,200:1 } overwrite endif end-filter ```  The route-filter references the set named **soo-list1** and overwrites the SoOs of the VPN routes carrying at least one of the SoOs specified in the set with 100:1 and 200:1. |