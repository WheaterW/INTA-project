Configuring a Global Variable Set
=================================

A global variable set is a group of frequently used values that are defined as global variables. Global variables can be referenced by all route-filters configured on a device.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The data type of each value in a global variable set may vary with the route-filter that references the set.

The global variables on a device must be unique. A new global variable will override an existing global variable with the same name.

To enable a route-filter or a set to reference a global variable, enter $+variable name, for example, **$globvar**.



#### Procedure

* Configure a global variable set using the paragraph-by-paragraph editing mode.
  1. Run the [**edit xpl global-value**](cmdqueryname=edit+xpl+global-value) command to enter the global variable set paragraph-by-paragraph editing view.
  2. Press **i** to enter the text editing mode.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Sets or route-filters can be configured only in the text editing mode. If you exit from the text editing mode, you can perform shortcut key operations only.
  3. Configure a start clause (**xpl global-value**) for a global variable set.
  4. Configure set elements in the format of variable name+'value', for example, aaa '12', bbb'34', aaa '1.2.3.4'. Separate every two neighboring elements with a comma (,).
  5. Configure an end clause (**end-global-value**) for the global variable set.
  6. Press **Esc** to exit from the text editing mode.
  7. Press **:wq** and **Enter** to save the configurations and exit from the global variable set paragraph-by-paragraph editing view.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A message is displayed for you to confirm whether to commit the configurations when you attempt to exit from the global variable set paragraph-by-paragraph editing view. To commit the configurations, press **Y**.
     
     To exit from the global variable set paragraph-by-paragraph editing view without saving the configurations, press **:q!** and **Enter**.
* Configure a global variable set using the line editing mode.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**xpl global-value**](cmdqueryname=xpl+global-value) command to enter the global variable set view.
  3. Configure elements in the format of variable name+'value' in the global variable set view, for example, aaa'12', bbb'34', and aaa'1.2.3.4'. Separate every two neighboring elements with a comma (,).
  4. Run the [**end-global-value**](cmdqueryname=end-global-value) command to conclude the configuration of the global variable set.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Example

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If only paragraph-by-paragraph editing is used as an example, the corresponding line editing is similar. To use the line editing mode, perform the operations described in paragraph-by-paragraph editing.

For detailed set and route-filter configuration steps, see [Configuration Procedures for Sets and Route-Filters Using the Paragraph-by-Paragraph Editing Mode](dc_vrp_xpl_cfg_0002.html#EN-US_CONCEPT_0000001793384325__section_dc_vrp_xpl_cfg_000102). For details about XPL clauses, see [XPL Paragraph Editing Clauses](dc_vrp_xpl_cfg_0014.html).

| **Objective** | Configure a global variable set that includes two values: 100 and ip-prefix. |
| --- | --- |
| **Configuration Example** | ``` <HUAWEI> edit xpl global-value  xpl global-value aaa '100', bbb 'ip-prefix', end-global-value ```  The global variable set includes a set named **aaa** with value 100 and another set named **bbb** with value ip-prefix. |
| **Objective** | Configure a route-filter to permit only the routes with the MED value less than 100 and the routes that match the IPv4 prefix set named **bbb**. |
| **Reference Example** | ``` <HUAWEI> edit xpl ip-prefix-list r1  xpl route-filter r1 if ip med le $aaa then approve elseif ip route-destination in  $bbb  then approve else refuse endif end-filter ```  The route-filter uses two global variables (**aaa** and **bbb**), in which **aaa** represents a MED value and **bbb** represents an IPv4 destination address prefix set. The route-filter permits only the routes with the MED value less than 100 and the routes that match **bbb**. |