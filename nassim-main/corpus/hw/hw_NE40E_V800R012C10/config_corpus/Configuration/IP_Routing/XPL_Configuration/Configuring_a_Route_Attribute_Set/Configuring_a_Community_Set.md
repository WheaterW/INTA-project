Configuring a Community Set
===========================

Community sets apply only to BGP and are used to match the community attribute of BGP routes. This section describes how to configure community sets.

#### Procedure

* Configure a community set using the paragraph-by-paragraph editing mode.
  1. Run the [**edit xpl community-list**](cmdqueryname=edit+xpl+community-list) *community-list-name* command to enter the paragraph-by-paragraph editing view of the community set.
  2. Press **i** to enter the text editing mode.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Sets or route-filters can be configured only in the text editing mode. If you exit from the text editing mode, you can perform shortcut key operations only.
  3. Configure a start clause for a community set using the [**xpl community-list**](cmdqueryname=xpl+community-list) *community-list-name* command in the community set paragraph-by-paragraph editing interface view.
  4. Configure elements in the format of aa:nn (100:1 for example), a community number, or a known community attribute (**internet**, **no-export-subconfed**, **no-advertise**, or **no-export**) for the community set in the community set paragraph-by-paragraph editing interface view and separate every two neighboring elements with a comma (,). You can also configure elements in the **regular** *regular-expression* format to indicate that the community attribute of a route matches a specified regular expression, and *regular-expression* specifies a regular expression. An asterisk (\*) in an element can be used to match any digit. For example, 100:\* indicates that the element matches all community values with the AS number 100.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Regular expression processing is CPU computing-intensive. When a large number of regular expressions are configured in an XPL policy to match a BGP route attribute and the length of the route attribute is long, the processing performance of the XPL policy deteriorates. To improve the processing performance of the routing policy, decrease the number of regular expressions or use a non-regular expression matching command.
     
     It is recommended that a maximum of 100 regular expressions be configured for each policy.
  5. Configure an end clause for the community set using the [**end-list**](cmdqueryname=end-list) command in the community set paragraph-by-paragraph editing interface view.
  6. Press **Esc** to exit from the text editing mode.
  7. Press **:wq** and **Enter** to save the configurations and exit from the global variable set paragraph-by-paragraph editing view.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A message is displayed for you to confirm whether to commit the configurations when you attempt to exit from the global variable set paragraph-by-paragraph editing view. To commit the configurations, press **Y**.
     
     To exit from the global variable set paragraph-by-paragraph editing view without saving the configurations, press **:q!** and **Enter**.
* Configure a community set using the line-by-line editing mode.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**xpl community-list**](cmdqueryname=xpl+community-list) *community-list-name* command to enter the community set view.
  3. Configure elements in the format of aa:nn (100:1 for example), a community number, or a known community attribute (**internet**, **no-export-subconfed**, **no-advertise**, or **no-export**) for the community set and separate every two neighboring elements with a comma (,). You can also configure elements in the **regular** *regular-expression* format to indicate that the community attribute of a route matches a specified regular expression, and *regular-expression* specifies a regular expression. An asterisk (\*) in an element can be used to match any digit. For example, 100:\* indicates that the element matches all community values with the AS number 100.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Regular expression processing is CPU computing-intensive. When a large number of regular expressions are configured in an XPL policy to match a BGP route attribute and the length of the route attribute is long, the processing performance of the XPL policy deteriorates. To improve the processing performance of the routing policy, decrease the number of regular expressions or use a non-regular expression matching command.
     
     It is recommended that a maximum of 100 regular expressions be configured for each policy.
  4. Run the [**end-list**](cmdqueryname=end-list) command to conclude the configuration of the community set, exit the community set view, and return to the system view.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Example

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If only paragraph-by-paragraph editing is used as an example, the corresponding line editing is similar. To use the line editing mode, perform the operations described in paragraph-by-paragraph editing.

For detailed set and route-filter configuration steps, see [Configuration Procedures for Sets and Route-Filters Using the Paragraph-by-Paragraph Editing Mode](dc_vrp_xpl_cfg_0002.html#EN-US_CONCEPT_0000001793384325__section_dc_vrp_xpl_cfg_000102). For details about XPL clauses, see [XPL Paragraph Editing Clauses](dc_vrp_xpl_cfg_0014.html).

| **Objective** | Configure a community set to match the routes carrying community set 100:1, 200:1, 300:1, or no-export. |
| --- | --- |
| **Configuration Example 1** | ``` <HUAWEI> edit xpl community-list aaa  xpl community-list aaa 100:1, 200:1, 300:1, no-export end-list ```  This community set includes four elements and matches the routes carrying community set 100:1, 200:1, 300:1, or no-export. |
| **Objective** | Configure a community set to match the routes carrying community set 100:\*, 200:\*, or 300:1. |
| **Configuration Example 2** | ``` <HUAWEI> edit xpl community-list bbb  xpl community-list bbb regular 100:*, regular 200:*, 300:1 end-list ```  This community set includes three elements and matches the routes carrying community set 100:\*, 200:\*, or 300:1. |
| **Objective** | Configure a route-filter to add communities 100:1, 200:1, 300:1, and no-export to the routes with the Local\_Pref value less than 100. |
| **Reference Example 1** | ``` <HUAWEI> edit xpl route-filter r1  xpl route-filter r1 if local-preference le 100 then apply community aaa additive endif end-filter ```  This route-filter references community set **aaa** and adds communities 100:1, 200:1, 300:1, and no-export to the routes with the Local\_Pref value less than or equal to 100. |
| **Objective** | Configure a route-filter to set the next hop addresses of the routes whose communities are a subset of the community set **bbb** to 1.1.1.1. |
| **Reference Example 2** | ``` <HUAWEI> edit xpl route-filter r2  xpl route-filter r2 if community matches-within bbb then apply ip next-hop 1.1.1.1 endif end-filter ```  This route-filter references community set **bbb** and sets the next hop addresses of the routes whose communities are a subset of **bbb** to 1.1.1.1. |