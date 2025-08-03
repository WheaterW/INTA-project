Configuring an AS\_Path Set
===========================

AS\_Path sets apply only to BGP and are used to match the AS\_Path attribute of BGP routes. This section describes how to configure AS\_Path sets.

#### Procedure

* Configure an AS\_Path set using the paragraph-by-paragraph editing mode.
  1. Run the [**edit xpl as-path-list**](cmdqueryname=edit+xpl+as-path-list) *as-path-list-name* command to enter the AS\_Path set paragraph-by-paragraph editing view.
  2. Press **i** to enter the text editing mode.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Sets or route-filters can be configured only in the text editing mode. If you exit from the text editing mode, you can perform shortcut key operations only.
  3. Configure a start clause for an AS\_Path set using the [**xpl as-path-list**](cmdqueryname=xpl+as-path-list) *as-path-list-name* command in the AS\_Path set paragraph-by-paragraph editing interface view.
  4. Configure elements in the format of regular+AS\_Path regular expression for the set in the AS\_Path set paragraph-by-paragraph editing interface view and separate every two neighboring elements with a comma (,). For example, regular 1\_2\_3\_4 represents an AS\_Path that contains AS numbers 1, 2, 3, and 4.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Regular expression processing is CPU computing-intensive. When a large number of regular expressions are configured in an XPL policy to match a BGP route attribute and the length of the route attribute is long, the processing performance of the XPL policy deteriorates. To improve the processing performance of the routing policy, decrease the number of regular expressions or use a non-regular expression matching command.
     
     It is recommended that a maximum of 100 regular expressions be configured for each policy.
  5. Configure an end clause for the AS\_Path set using the [**end-list**](cmdqueryname=end-list) command in the AS\_Path set paragraph-by-paragraph editing interface view.
  6. Press **Esc** to exit from the text editing mode.
  7. Press **:wq** and **Enter** to save the configurations and exit from the global variable set paragraph-by-paragraph editing view.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A message is displayed for you to confirm whether to commit the configurations when you attempt to exit from the global variable set paragraph-by-paragraph editing view. To commit the configurations, press **Y**.
     
     To exit from the global variable set paragraph-by-paragraph editing view without saving the configurations, press **:q!** and **Enter**.
* Configure an AS\_Path set using the line-by-line editing mode.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**xpl as-path-list**](cmdqueryname=xpl+as-path-list) *as-path-list-name* command to enter the AS\_Path set view.
  3. Configure elements in the format of regular+AS\_Path regular expression for the set and separate every two neighboring elements with a comma (,). For example, regular 1\_2\_3\_4 represents an AS\_Path that contains AS numbers 1, 2, 3, and 4.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Regular expression processing is CPU computing-intensive. When a large number of regular expressions are configured in an XPL policy to match a BGP route attribute and the length of the route attribute is long, the processing performance of the XPL policy deteriorates. To improve the processing performance of the routing policy, decrease the number of regular expressions or use a non-regular expression matching command.
  4. Run the [**end-list**](cmdqueryname=end-list) command to conclude the configuration of the AS\_Path set, exit the AS\_Path set view, and return to the system view.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Example

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If only paragraph-by-paragraph editing is used as an example, the corresponding line editing is similar. To use the line editing mode, perform the operations described in paragraph-by-paragraph editing.

For detailed set and route-filter configuration steps, see [Configuration Procedures for Sets and Route-Filters Using the Paragraph-by-Paragraph Editing Mode](dc_vrp_xpl_cfg_0002.html#EN-US_CONCEPT_0000001793384325__section_dc_vrp_xpl_cfg_000102). For details about XPL clauses, see [XPL Paragraph Editing Clauses](dc_vrp_xpl_cfg_0014.html).

| **Objective** | Configure an AS\_Path set to match the routes received from AS 100, the routes that pass through AS 200, and the routes that originate from AS 300. |
| --- | --- |
| **Configuration Example** | ``` <HUAWEI> edit xpl as-path-list aaa  xpl as-path-list aaa regular ^100_, regular _200_, regular _300$ end-list ```  This AS\_Path set includes three elements and matches the routes received from AS 100, the routes that pass through AS 200, and the routes that originate from AS 300. |
| **Objective** | Configure a route-filter to deny the routes received from AS 100, the routes that pass through AS 200, and the routes that originate from AS 300. |
| **Reference Example** | ``` <HUAWEI> edit xpl route-filter r1 ``` ``` xpl route-filter r1 if as-path in aaa then refuse else approve endif end-filter ```  The route-filter references AS\_Path set **aaa**, denies the routes that match **aaa**, and permits all other routes. |