Configuring a Route Target Set
==============================

Route target sets are used to match the RTs of VPN routes.

#### Procedure

* Configure a route target set using the paragraph-by-paragraph editing mode.
  1. Run the [**edit xpl extcommunity-list rt**](cmdqueryname=edit+xpl+extcommunity-list+rt) *rt-list-name* command to enter the route target set paragraph-by-paragraph editing view.
  2. Press **i** to enter the text editing mode.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Sets or route-filters can be configured only in the text editing mode. If you exit from the text editing mode, you can perform shortcut key operations only.
  3. Configure a start clause ([**xpl extcommunity-list rt**](cmdqueryname=xpl+extcommunity-list+rt) *rt-list-name*) for the route target set.
  4. Configure elements (RTs of VPN routes) for the route target set in the route target set paragraph-by-paragraph editing interface view and separate every two neighboring elements with a comma (,). The elements can be configured in any of the following formats:
     
     
     + 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number is an integer ranging from 0 to 65535, and the user-defined number is an integer ranging from 0 to 4294967295. The AS number and user-defined number must not be both 0s. Specifically, the RT must not be 0:0.
     + IPv4 address:2-byte user-defined number, for example, 192.168.122.15:1. The IPv4 address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number is an integer ranging from 0 to 65535.
     + Integral 4-byte AS number:2-byte user-defined number, for example, 0:3 or 65537:3. The integral 4-byte AS number ranges from 65536 to 4294967295, and the user-defined number is an integer ranging from 0 to 65535.
     + 4-byte AS number in dotted notation (*x*.*y*):2-byte user-defined number, for example, 0.0:3 or 0.1:0. The *x*, *y*, and user-defined number are integers ranging from 0 to 65535. The AS number and user-defined number must not be both 0s. Specifically, the RT must not be 0.0:0.
     + **regular** *regular-expression*: matches VPN routes with RTs in the specified regular expression.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       Regular expression processing is computing-intensive. When a large number of regular expressions are configured in an XPL policy to match a BGP route attribute and the length of the route attribute is long, the processing performance of the XPL policy deteriorates. To improve the processing performance of the routing policy, decrease the number of regular expressions or use a non-regular expression matching command.
       
       It is recommended that a maximum of 100 regular expressions be configured for each policy.
  5. Configure an end clause for the route target set using the [**end-list**](cmdqueryname=end-list) command in the route target set paragraph-by-paragraph editing interface view.
  6. Press **Esc** to exit from the text editing mode.
  7. Press **:wq** and **Enter** to save the configurations and exit from the global variable set paragraph-by-paragraph editing view.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A message is displayed for you to confirm whether to commit the configurations when you attempt to exit from the global variable set paragraph-by-paragraph editing view. To commit the configurations, press **Y**.
     
     To exit from the global variable set paragraph-by-paragraph editing view without saving the configurations, press **:q!** and **Enter**.
* Configure a route target set using the line-by-line editing mode.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**xpl extcommunity-list rt**](cmdqueryname=xpl+extcommunity-list+rt) *rt-list-name* command to enter the route target set view.
  3. Configure elements (RTs of VPN routes) for the route target set and separate every two neighboring elements with a comma (,). The elements can be configured in any of the following formats:
     
     
     + 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number is an integer ranging from 0 to 65535, and the user-defined number is an integer ranging from 0 to 4294967295. The AS number and user-defined number must not be both 0s. Specifically, the RT must not be 0:0.
     + IPv4 address:2-byte user-defined number, for example, 192.168.122.15:1. The IPv4 address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number is an integer ranging from 0 to 65535.
     + Integral 4-byte AS number:2-byte user-defined number, for example, 0:3 or 65537:3. The integral 4-byte AS number ranges from 65536 to 4294967295, and the user-defined number is an integer ranging from 0 to 65535.
     + 4-byte AS number in dotted notation (*x*.*y*):2-byte user-defined number, for example, 0.0:3 or 0.1:0. The *x*, *y*, and user-defined number are integers ranging from 0 to 65535. The AS number and user-defined number must not be both 0s. Specifically, the RT must not be 0.0:0.
     + **regular** *regular-expression*: matches VPN routes with RTs in the specified regular expression.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       Regular expression processing is computing-intensive. When a large number of regular expressions are configured in an XPL policy to match a BGP route attribute and the length of the route attribute is long, the processing performance of the XPL policy deteriorates. To improve the processing performance of the routing policy, decrease the number of regular expressions or use a non-regular expression matching command.
       
       It is recommended that a maximum of 100 regular expressions be configured for each policy.
  4. Run the [**end-list**](cmdqueryname=end-list) command to conclude the configuration of the route target set, exit the route target set view, and return to the system view.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Example

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If only paragraph-by-paragraph editing is used as an example, the corresponding line editing is similar. To use the line editing mode, perform the operations described in paragraph-by-paragraph editing.

For detailed set and route-filter configuration steps, see [Configuration Procedures for Sets and Route-Filters Using the Paragraph-by-Paragraph Editing Mode](dc_vrp_xpl_cfg_0002.html#EN-US_CONCEPT_0000001793384325__section_dc_vrp_xpl_cfg_000102). For details about XPL clauses, see [XPL Paragraph Editing Clauses](dc_vrp_xpl_cfg_0014.html).

| **Objective** | Configure a route target set to match the VPN routes with the RT 100:1, 200:1, or 300:1. |
| --- | --- |
| **Configuration Example** | ``` <HUAWEI> edit xpl extcommunity-list rt rt-list1  xpl extcommunity-list rt rt-list1 100:1, 200:1, 300:1 end-list ```  The route target set contains three elements and can match VPN routes carrying RT 100:1, 200:1, or 300:1. |
| **Objective** | Configure a route-filter to set the next hop IP addresses of the VPN routes carrying the RTs that are a subset of the set named **rt-list1** and the VPN routes carrying the RTs of which the set named **rt-list1** is a subset to 1.1.1.1 and 2.2.2.2, respectively. |
| **Reference Example** | ``` <HUAWEI> edit xpl route-filter r1  xpl route-filter r1 if extcommunity rt matches-within rt-list1 then apply ip next-hop 1.1.1.1 elseif extcommunity rt matches-all rt-list1 then apply ip next-hop 2.2.2.2 endif end-filter ```  The route-filter references the set named **rt-list1** and sets the next hop IP addresses of the VPN routes carrying the RTs that are a subset of this set and the VPN routes carrying the RTs of which this set is a subset to 1.1.1.1 and 2.2.2.2, respectively. |