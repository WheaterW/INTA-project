Introduction to XPL Paragraph-by-Paragraph Editing
==================================================

The paragraph-by-paragraph editing mode is a new XPL configuration mode. For the comparison between the paragraph-by-paragraph and line-by-line editing modes, see [Overview of XPL](dc_vrp_xpl_cfg_0001.html). The following uses [Common Shortcut Keys](#EN-US_CONCEPT_0000001793384325__section54174564412), [Example of Paragraph-by-Paragraph Editing Operations](#EN-US_CONCEPT_0000001793384325__section1198951315912), and [Configuration Procedures for Sets and Route-Filters Using the Paragraph-by-Paragraph Editing Mode](#EN-US_CONCEPT_0000001793384325__section_dc_vrp_xpl_cfg_000102) as examples to describe the paragraph-by-paragraph editing mode.

The paragraph-by-paragraph editing interface functions as a text editor, in which users can edit XPL clauses to configure or modify sets and route-filters. After the configuration is complete, it can be committed by stage.

#### Common Shortcut Keys

Shortcut keys can be used in the paragraph-by-paragraph editing interface. [Table 1](#EN-US_CONCEPT_0000001793384325__table_001) lists common shortcut keys and their functions.

**Table 1** Shortcut keys commonly used in the paragraph-by-paragraph editing interface
| Shortcut Key | Function |
| --- | --- |
| **i** | Enters the text editing mode. Sets or route-filters can be configured only in the text editing mode. The shortcut key is the **i** key on the keyboard. |
| **Esc** | Exits the text editing mode. The shortcut key is the **Esc** key in the upper left corner of the keyboard. |
| **:q!** | Exits the paragraph-by-paragraph editing view without saving configurations. You need to press **Esc** to exit the text editing mode, and then enter the shortcut key manually. NOTE:  The shortcut key takes effect only after **Enter** is pressed. |
| **:wq** | Saves the configuration and exits from the paragraph-by-paragraph editing view. You need to press **Esc** to exit the text editing mode, and then enter the shortcut key manually. NOTE:  The shortcut key takes effect only after **Enter** is pressed. |

**Entering the paragraph-by-paragraph editing view**

The following lists the different XPL paragraph-by-paragraph editing views and the commands used to access them:

* Global variable set: Run the [**edit xpl global-value**](cmdqueryname=edit+xpl+global-value) command.
* IPv4 prefix set: Run the [**edit xpl ip-prefix-list**](cmdqueryname=edit+xpl+ip-prefix-list) *ip-prefix-list-name* command.
* IPv6 prefix set: Run the [**edit xpl ipv6-prefix-list**](cmdqueryname=edit+xpl+ipv6-prefix-list) *ipv6-prefix-list-name* command.
* AS\_Path set: Run the [**edit xpl as-path-list**](cmdqueryname=edit+xpl+as-path-list) *as-path-list-name* command.
* Community set: Run the [**edit xpl community-list**](cmdqueryname=edit+xpl+community-list) *community-list-name* command.
* Large-Community set: Run the [**edit xpl large-community-list**](cmdqueryname=edit+xpl+large-community-list) *large-community-list-name* command.
* Route-filter: Run the [**edit xpl route-filter**](cmdqueryname=edit+xpl+route-filter) *route-filter-name* command.


#### Example of Paragraph-by-Paragraph Editing Operations

**Table 2** Description of paragraph-by-paragraph editing operations
| No. | Item | Description | Picture |
| --- | --- | --- | --- |
| 1 | Enter the paragraph-by-paragraph editing view and the text editing mode. | For example, run the [**edit xpl ip-prefix-list**](cmdqueryname=edit+xpl+ip-prefix-list) *ip-prefix-list-name* command in the user view to enter the IPv4 prefix set paragraph-by-paragraph editing view, and press **i** to enter the text editing mode. **-- INSERT --** is displayed at the bottom of the interface, indicating that you can enter content, as shown in the figure on the right.  If you do not press **i**, content cannot be entered. |  |
| 2 | Configure XPL sets and route-filters. | In text editing mode, configure a start clause **xpl ip-prefix-list** *ip-prefix-list-name*, an element, and an end clause **end-list** for the IPv4 prefix set, and press **Esc** to exit the text editing mode.  After you press **Esc**, **-- INSERT --** at the bottom of the interface disappears. In this case, you cannot enter any content. If you need to continue your editing, press **i** again to return to the text editing mode.  Note that set elements must be separated by commas (,). Otherwise, an error is reported. | NOTE:   * In the preceding figure, **xpl ip-prefix-list** *prefixa* is the start clause, and **end-list** is the end clause. Both of them are mandatory. * After you run the [**edit xpl ip-prefix-list**](cmdqueryname=edit+xpl+ip-prefix-list) *prefixa* command to enter the paragraph-by-paragraph editing view, if [**edit xpl ip-prefix-list**](cmdqueryname=edit+xpl+ip-prefix-list) *prefixb* is entered as the start clause, the set elements of **prefixb** rather than **prefixa** are modified. Ensure that the input is correct. |
| 3 | Save configurations and exit from the paragraph-by-paragraph editing view. | After the configuration is complete, press **Esc**. **-- INSERT --** at the bottom of the interface disappears, indicating that you have exited the text editing mode. In this case, you can enter **:wq** and press **Enter** to save the configuration and exit the paragraph-by-paragraph editing view. You can also enter **:q!** and press **Enter** to exit the paragraph-by-paragraph editing view without saving the configuration. | * Save configurations and exit from the paragraph-by-paragraph editing view. A message is displayed, asking you whether to submit the configuration after the following operations: complete configuration, press **Esc** to exit the text editing mode, enter **:wq**, and press **Enter**. In this case, you can enter **y** to commit the configuration and press **Enter** to return to the user view. This indicats that the XPL configuration is saved successfully, as shown in the following figures.      If you enter **n**, the configuration is not saved. After you press **Enter**, the system returns to the user view too.      If you enter **c**, the configuration is not submitted. After you press **Enter**, the system returns to the paragraph-by-paragraph editing view. In this case, you can press **i** again to enter the text editing mode.      After you run the [**edit xpl ip-prefix-list**](cmdqueryname=edit+xpl+ip-prefix-list) *ip-prefix-list-name* command to enter the paragraph editing view, if you press **i** to enter the text editing mode and then press **Esc** to exit the text editing mode without entering any information, enter **:wq**, and press **Enter**, the system displays a message asking you whether to continue editing the configuration instead of whether to commit the configuration. You need to enter **n** to return to the user view. Determine the subsequent operations based on the displayed information. * Exit the paragraph-by-paragraph editing view without saving the configuration. After the configuration is complete, press **:q!** and press **Enter**. A message is displayed, asking you whether to continue the editing. In this case, you can enter **y** to return to the paragraph-by-paragraph editing view, and then press **i** to enter the text editing mode.      If you enter **n**, the system exits the paragraph-by-paragraph editing mode and returns to the user view. In this case, the configuration does not take effect. |
| 4 | The configuration is incorrect and cannot be saved. | If the configuration is incorrect, it cannot be submitted or saved. In this case, you can modify the configuration based on the error information and submit it again.  After the configuration is complete, enter **:wq** to save the configuration and exit the paragraph-by-paragraph editing view. Press **Enter**. A message is displayed asking you whether to commit the configuration. Enter **y** to commit the configuration. If the configuration is incorrect, an error message is displayed, as shown in the figure on the right.  In this case, you can continue to enter **y** to return to the paragraph-by-paragraph editing view. Press **i** again to enter the text editing mode. Based on the error information, use arrow keys on the keyboard to move the cursor to the corresponding position and modify the information. | * Incorrect configuration example 1 The configuration error is that the comma (,) is missing after 3.3.3.0 24.  In this case, you can enter **y** to return to the paragraph-by-paragraph editing view, and then press **i** to enter the text editing mode. Press arrow keys to move the cursor to the end of 3.3.3.0 24, supplement a comma (,), and then submit the configuration.  * Incorrect configuration example 2 The configuration error is invalid input. To exit the text editing mode, press **Esc** instead of typing **esc**.  If you encounter this issue, enter **y** to return to the paragraph-by-paragraph editing view, and then press **i** to enter the text editing mode. Press arrow keys to move the cursor to **esc** and delete it, and then continue to submit the configuration. |
| 5 | Change configuration. | To modify the existing configuration, run the [**edit xpl ip-prefix-list**](cmdqueryname=edit+xpl+ip-prefix-list) *ip-prefix-list-name* command to enter the IPv4 prefix set paragraph-by-paragraph editing view and press **i** to enter the text editing mode.  In this case, you can use arrow keys to move the cursor to the required position and delete or add set elements. Note that elements need to be separated by commas (,).  After the modification, press **Esc** to exit the text editing mode. Enter **:wq** and press **Enter** to save the configuration and exit the paragraph-by-paragraph editing view. | * Delete the set element 3.3.3.0 24 and save the configuration. * Add 5.5.5.0 24 to the original configuration and save the configuration. |



#### Configuration Procedures for Sets and Route-Filters Using the Paragraph-by-Paragraph Editing Mode

Sets and route-filters can be configured as follows:

* To configure a global variable set:
  1. Configure a start clause (**xpl global-value**) for a global variable set.
  2. Configure set elements in the format of variable name+'value' in the global variable set view.
     + The variable value range is The value is a string of 1 to 200 case-sensitive characters, spaces and question marks not supported. The string can contain letters, digits, underscores (\_), hyphens (-), dots (.), and colons (:). It must start with a letter, digit, or colon (:).The variable name must not be **abort**, **display**, **end-global-value**, or any abbreviation of the keywords, for example, **a**, **ab**, **abo**, **di**, **e**, or **end**.
     + Separate every two neighboring elements with a comma (,), for example, aaa '12', bbb '34', aaa '1.2.3.4'.
  3. Configure an end clause (**end-global-value**) for the global variable set.
* To configure an IPv4 prefix set:
  1. Configure a start clause (**xpl ip-prefix-list** *ip-prefix-list-name*) for an IPv4 prefix set.
  2. Configure elements (IPv4 addresses with masks, 1.1.1.0 24 for example) for the set and separate every two neighboring elements with a comma (,). You can use **eq**, **ge**, or **le** to specify the mask length. For example, **1.1.1.0 24 ge 26 le 30** matches the routes in network segment 1.1.1.0/24 with the mask length ranging from 26 to 30 bits.
  3. Configure an end clause (**end-list**) for the IPv4 prefix set.
* To configure an IPv6 prefix set:
  1. Configure a start clause (**xpl ipv6-prefix-list** *ipv6-prefix-list-name*) for an IPv6 prefix set.
  2. Configure elements (IPv6 addresses with masks, 2001:db8:0:1:: 64 for example) for the set and separate every two neighboring elements with a comma (,). You can use **eq**, **ge**, or **le** to specify the mask length. For example, **2001:db8:0:1:: 64 ge 96 le 100** matches the routes in network segment 2001:db8:0:1::/64 with the mask length ranging from 96 to 100 bits.
  3. Configure an end clause (**end-list**) for the IPv6 prefix set.
* To configure an AS\_Path set:
  1. Configure a start clause (**xpl as-path-list** *as-path-list-name*) for an AS\_Path set.
  2. Configure elements for the set and separate every two neighboring elements with a comma (,). The elements can be configured in any of the following formats:
     + **length** { **eq** | **ge** | **le** } *as-length*: matches BGP routes with AS\_Path length equal to (**eq**), greater than or equal to (**ge**), or less than or equal to (**le**) *as-length*. The value of *as-length* is an integer ranging from 0 to 2047.
     + **unique-length** { **eq** | **ge** | **le** } *as-length*: matches BGP routes with AS\_Path length equal to (**eq**), greater than or equal to (**ge**), or less than or equal to (**le**) *as-length* (duplicate AS numbers are counted as one). The value of *as-length* is an integer ranging from 0 to 2047.
     + **origin** *as-path* [ **whole-match** ]: matches BGP routes with AS\_Path whose rightmost AS numbers are the same as *as-path*. The *as-path* parameter is enclosed in single quotation marks, with every two neighboring AS numbers separated with a space. Duplicate AS numbers are counted as one unless **whole-match** is configured.
     + **peer-is** *as-path* [ **whole-match** ]: matches BGP routes with AS\_Path whose leftmost AS numbers are the same as *as-path*. The *as-path* parameter is enclosed in single quotation marks, with every two neighboring AS numbers separated with a space. Duplicate AS numbers are counted as one unless **whole-match** is configured.
     + **pass** *as-path* [ **whole-match** ]: matches BGP routes with AS\_Path whose contiguous AS numbers match *as-path*. The *as-path* parameter is enclosed in single quotation marks, with every two neighboring AS numbers separated with a space. Duplicate AS numbers are counted as one unless **whole-match** is configured.
     + **regular** *regular-expression*: matches BGP routes with AS\_Path in the specified regular expression.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       Regular expression processing is computing-intensive. When a large number of regular expressions are configured in an XPL policy to match a BGP route attribute and the length of the route attribute is long, the processing performance of the XPL policy deteriorates. To improve the processing performance of the routing policy, decrease the number of regular expressions or use a non-regular expression matching command.
       
       It is recommended that a maximum of 100 regular expressions be configured for each policy.
  3. Configure an end clause (**end-list**) for the AS\_Path set.
* To configure a community set:
  1. Configure a start clause (**xpl community-list** *community-list-name*) for a community set.
  2. Configure elements in the format of aa:nn (100:1 for example), a community number, or a known community (**internet**, **no-export-subconfed**, **no-advertise**, or **no-export**) for the community set and separate every two neighboring elements with a comma (,). Alternatively, configure elements in the format of **regular** *regular-expression*, which matches routes with community attributes in the specified regular expression.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Regular expression processing is computing-intensive. When a large number of regular expressions are configured in an XPL policy to match a BGP route attribute and the length of the route attribute is long, the processing performance of the XPL policy deteriorates. To improve the processing performance of the routing policy, decrease the number of regular expressions or use a non-regular expression matching command.
     
     It is recommended that a maximum of 100 regular expressions be configured for each policy.
     
     The community-based *regular expression* can be set to a character string in either the aa:nn format or integer format. The following are two examples:
     
     The regular ^1:1$ configuration matches routes that carry the community value of 65537 or 1:1.
     
     The regular ^65537$ configuration also matches routes that carry the community value of 65537 or 1:1.
  3. Configure an end clause (**end-list**) for the community set.
* Large-Community set:
  1. Configure a start clause (**xpl large-community-list** *large-community-list-name*) for the Large-Community set.
  2. Configure elements in the format of aa:bb:cc (100:1:1 for example) for the Large-Community set and separate every two neighboring elements with a comma (,). Alternatively, configure elements in the format of **regular** *regular-expression*, which matches routes with large-community attribute in the specified regular expression.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Regular expression processing is computing-intensive. When a large number of regular expressions are configured in an XPL policy to match a BGP route attribute and the length of the route attribute is long, the processing performance of the XPL policy deteriorates. To improve the processing performance of the routing policy, decrease the number of regular expressions or use a non-regular expression matching command.
     
     It is recommended that a maximum of 100 regular expressions be configured for each policy.
  3. Configure an end clause (**end-list**) for the Large-Community set.
* To configure a route-filter:
  1. Configure a start clause in the format of **xpl route-filter** *route-filter-name*($*var1*,$*var2*,...) for a route-filter. A maximum of eight parameters can be configured in a start clause, and the parameters can be used in condition or action clauses.
  2. Configure a condition clause in the format of **if**+condition clause+**then** and connect the conditions in the clause with the Boolean operator **NOT**, **AND**, or **OR**.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Route-filters can have only action clauses and can also be empty (configured with only a start clause and an end clause). In this case, the default action **refuse** is used. If an empty route-filter is specified in another route-filter using a **call** clause, the empty route-filter does not take effect.
  3. Configure an action clause.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + Multiple action clauses can be configured if they do not conflict with each other.
     + Action clauses (excluding **approve**, **refuse**, **finish**, **break**, and **call route-filter** *route-filter-name*) must follow **apply**.
  4. (Optional) Configure **elseif**+condition clause+**then** to filter the routes that fail to match the conditions specified in the **if** clause and specify an action clause for the **elseif** clause. You can configure multiple **elseif** clauses to filter the routes that fail to meet the previous matching rule or configure an **else** clause to match the routes that fail to meet all the previous matching rules. Each **if**, **elseif**, or **else** clause must be followed by an action clause.
  5. Configure a conclusive condition clause (**endif**).![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Steps 2 to 5 describe how to configure an **if** condition branch. One route-filter can have multiple **if** condition branches, and the **if** condition branches can be configured as follows:
     
     + One **if** condition branch is followed by another.
     + The **if**+condition clause+**then** or **elseif**+condition clause+**then** is followed by another **if** condition branch. Such a configuration further filters routes that match **if**+condition clause+**then** or **elseif**+condition clause+**then** against the second **if** condition branch.
     
     Regardless of the configuration mode, route filtering continues until **finish**, **break**, **refuse,** or the last **if** condition branch.
  6. Configure an end clause (**end-filter**) for the route-filter.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

An easy method to configure route-filters to reference route attribute sets is to use the format {element A, element B...}, **if ip route-source in { 1.1.1.0 24, 2.2.2.2 32 } then** for example. However, if a route-filter needs to reference a set multiple times, configure named route attribute sets. You can choose a configuration method as required.



#### Purpose

When advertising, receiving, or importing routes, the Router can use XPL based on actual networking requirements to filter routes and modify route attributes. XPL serves the following purposes:

* Controls route advertisement.
  
  Only matched routes are advertised.
* Controls route acceptance.
  
  Only necessary and valid routes are accepted, which reduces the routing table size and improves network security.
* Filters and controls imported routes.
  
  To enrich routing information, a routing protocol may import routes discovered by other routing protocols. A device can be configured to import only the routes that satisfy filtering conditions and set attributes for the imported routes as required.
* Modifies route attributes.
  
  Attributes of the routes that match the specified route-filter can be modified as required.
* Flexibly updates the policies for advertising and accepting routes
  
  XPL supports the paragraph-by-paragraph editing mode. Configurations can be performed in the paragraph editing UI and are committed together after the configurations of a paragraph are complete. Therefore, policy modification and update are relatively flexible.

#### Benefits

XPL offers the following benefits:

* Saves system resources by controlling the routing table size.
* Improves network security by controlling route advertisement and acceptance.
* Improves network performance by modifying route attributes for effective traffic planning.
* Simplifies routing policy configurations.