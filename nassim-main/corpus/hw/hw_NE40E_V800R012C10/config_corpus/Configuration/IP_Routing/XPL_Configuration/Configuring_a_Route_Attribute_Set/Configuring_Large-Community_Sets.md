Configuring Large-Community Sets
================================

Large-Community sets apply to BGP and are used to match the Large-Community attribute of BGP routes. This section describes how to configure Large-Community sets.

#### Procedure

* Configure a Large-Community set using the paragraph-by-paragraph editing mode.
  1. Run the [**edit xpl large-community-list**](cmdqueryname=edit+xpl+large-community-list) *large-community-list-name* command to enter the Large-Community set paragraph-by-paragraph editing view.
  2. Press **i** to enter the text editing mode.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Sets or route-filters can be configured only in the text editing mode. If you exit from the text editing mode, you can perform shortcut key operations only.
  3. Configure a start clause for the Large-Community set using the [**xpl large-community-list**](cmdqueryname=xpl+large-community-list) *large-community-list-name* command in the Large-Community set paragraph-by-paragraph editing view.
  4. Configure elements in the format of aa:bb:cc (100:1:1 for example) for the Large-Community set in the Large-Community set paragraph-by-paragraph editing view and separate every two neighboring elements with a comma (,). You can also configure elements in the **regular** *regular-expression* format to indicate that the Large-Community attribute of a route matches a specified regular expression, and *regular-expression* specifies a regular expression. An asterisk (\*) in an element can be used to match any digit; for example, an element can be set to 100:1:\*.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Regular expression processing is CPU computing-intensive. When a large number of regular expressions are configured in an XPL policy to match a BGP route attribute and the length of the route attribute is long, the processing performance of the XPL policy deteriorates. To improve the processing performance of the routing policy, decrease the number of regular expressions or use a non-regular expression matching command.
     
     It is recommended that a maximum of 100 regular expressions be configured for each policy.
  5. Configure an end clause for the Large-Community set using the [**end-list**](cmdqueryname=end-list) command in the Large-Community set paragraph-by-paragraph editing view.
  6. Press **Esc** to exit from the text editing mode.
  7. Press **:wq** and **Enter** to save the configurations and exit from the global variable set paragraph-by-paragraph editing view.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A message is displayed for you to confirm whether to commit the configurations when you attempt to exit from the global variable set paragraph-by-paragraph editing view. To commit the configurations, press **Y**.
     
     To exit from the global variable set paragraph-by-paragraph editing view without saving the configurations, press **:q!** and **Enter**.
* Configure a Large-Community set using the line-by-line editing mode.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**xpl large-community-list**](cmdqueryname=xpl+large-community-list) *large-community-list-name* command to enter the Large-Community set view.
  3. Configure elements in the format of aa:bb:cc (100:1:1 for example) for the Large-Community set and separate every two neighboring elements with a comma (,). You can also configure elements in the **regular** *regular-expression* format to indicate that the Large-Community attribute of a route matches a specified regular expression, and *regular-expression* specifies a regular expression. An asterisk (\*) in an element can be used to match any digit; for example, an element can be set to 100:1:\*.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Regular expression processing is CPU computing-intensive. When a large number of regular expressions are configured in an XPL policy to match a BGP route attribute and the length of the route attribute is long, the processing performance of the XPL policy deteriorates. To improve the processing performance of the routing policy, decrease the number of regular expressions or use a non-regular expression matching command.
     
     It is recommended that a maximum of 100 regular expressions be configured for each policy.
  4. Run the [**end-list**](cmdqueryname=end-list) command to conclude the configuration of the Large-Community set, exit the Large-Community set view, and return to the system view.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Example

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If only paragraph-by-paragraph editing is used as an example, the corresponding line editing is similar. To use the line editing mode, perform the operations described in paragraph-by-paragraph editing.

For detailed set and route-filter configuration steps, see [Configuration Procedures for Sets and Route-Filters Using the Paragraph-by-Paragraph Editing Mode](dc_vrp_xpl_cfg_0002.html#EN-US_CONCEPT_0000001793384325__section_dc_vrp_xpl_cfg_000102). For details about XPL clauses, see [XPL Paragraph Editing Clauses](dc_vrp_xpl_cfg_0014.html).

| **Objective** | Configure a Large-Community set to match Large-Community attribute values 100:1:1, 200:1:1, and 300:1:1. |
| --- | --- |
| **Configuration Example 1** | ``` <HUAWEI> edit xpl large-community-list aaa  xpl large-community-list aaa 100:1:1, 200:1:1, 300:1:1 end-list ```  This Large-Community set includes three elements and matches Large-Community attribute values 100:1:1, 200:1:1, and 300:1:1. |
| **Objective** | Configure a Large-Community set to match Large-Community attribute values 100:1:\*, 200:1:\*, and 300:1:1. |
| **Configuration Example 2** | ``` <HUAWEI> edit xpl large-community-list bbb  xpl large-community-list bbb regular 100:1:*, regular 200:1:*, 300:1:1 end-list ```  This Large-Community set includes three elements and matches Large-Community attribute values 100:1:\*, 200:1:\*, and 300:1:1. |
| **Objective** | Configure a route-filter to add Large-Community attribute values 100:1:1, 200:1:1, and 300:1:1 to the routes with a Local\_Pref value less than or equal to 100. |
| **Reference Example 1** | ``` <HUAWEI> edit xpl route-filter r1  xpl route-filter r1 if local-preference le 100 then apply large-community aaa additive endif end-filter ```  This route-filter references the Large-Community set **aaa** and adds Large-Community attribute values 100:1:1, 200:1:1, and 300:1:1 to the routes with a Local\_Pref value less than or equal to 100. |
| **Objective** | Configure a route-filter to set the next hop addresses of the routes whose Large-Community attribute values compose a subset of the set **bbb** to 1.1.1.1. |
| **Reference Example 2** | ``` <HUAWEI> edit xpl route-filter r2  xpl route-filter r2 if large-community matches-within bbb then apply ip next-hop 1.1.1.1 endif end-filter ```  This route-filter references the Large-Community set **bbb** and sets the next hop addresses of the routes whose Large-Community attribute values compose a subset of the set **bbb** to 1.1.1.1. |