Configuring an RD Set
=====================

RD sets are used to match the RD attributes of VPN routes.

#### Procedure

* Configure an RD set using the paragraph-by-paragraph editing mode.
  1. Run the [**edit xpl rd-list**](cmdqueryname=edit+xpl+rd-list) *rd-list-name* command to enter the RD set paragraph-by-paragraph editing view.
  2. Press **i** to enter the text editing mode.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Sets or route-filters can be configured only in the text editing mode. If you exit from the text editing mode, you can perform shortcut key operations only.
  3. Configure a start clause ([**xpl rd-list**](cmdqueryname=xpl+rd-list) *rd-list-name*) for an RD set.
  4. Configure elements (RDs of VPN routes) for the RD set in the RD set paragraph-by-paragraph editing interface view and separate every two neighboring elements with a comma (,). The elements can be configured in any of the following formats:
     
     
     + 16-bit AS number:32-bit user-defined number. For example, 101:3. The AS number ranges from 0 to 65535, and the user-defined number ranges from 0 to 4294967295.
     + Integral 4-byte AS number:2-byte user-defined number, for example, 0:3 or 65537:3. An AS number ranges from 0 to 4294967295. A user-defined number ranges from 0 to 65535.
     + 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 1 to 65535 and from 0 to 65535, respectively. A user-defined number ranges from 0 to 65535.
     + 32-bit IP address:16-bit user-defined number. For example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number ranges from 0 to 65535.
     + **regular** *regular-expression*: matches VPN routes with RDs in the specified regular expression.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       Regular expression processing is computing-intensive. When a large number of regular expressions are configured in an XPL policy to match a BGP route attribute and the length of the route attribute is long, the processing performance of the XPL policy deteriorates. To improve the processing performance of the routing policy, decrease the number of regular expressions or use a non-regular expression matching command.
       
       It is recommended that a maximum of 100 regular expressions be configured for each policy.
  5. Configure an end clause for the RD set using the [**end-list**](cmdqueryname=end-list) command in the RD set paragraph-by-paragraph editing interface view.
  6. Press **Esc** to exit from the text editing mode.
  7. Press **:wq** and **Enter** to save the configurations and exit from the global variable set paragraph-by-paragraph editing view.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A message is displayed for you to confirm whether to commit the configurations when you attempt to exit from the global variable set paragraph-by-paragraph editing view. To commit the configurations, press **Y**.
     
     To exit from the global variable set paragraph-by-paragraph editing view without saving the configurations, press **:q!** and **Enter**.
* Configure an RD set using the line-by-line editing mode.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**xpl rd-list**](cmdqueryname=xpl+rd-list) *rd-list-name* command to enter the RD set view.
  3. Configure elements for the RD set and separate every two neighboring elements with a comma (,). The elements can be configured in any of the following formats:
     
     
     + 16-bit AS number:32-bit user-defined number. For example, 101:3. The AS number ranges from 0 to 65535, and the user-defined number ranges from 0 to 4294967295.
     + Integral 4-byte AS number:2-byte user-defined number, for example, 0:3 or 65537:3. An AS number ranges from 0 to 4294967295. A user-defined number ranges from 0 to 65535.
     + 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 1 to 65535 and from 0 to 65535, respectively. A user-defined number ranges from 0 to 65535.
     + 32-bit IP address:16-bit user-defined number. For example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number ranges from 0 to 65535.
     + **regular** *regular-expression*: matches VPN routes with RDs in the specified regular expression.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       Regular expression processing is computing-intensive. When a large number of regular expressions are configured in an XPL policy to match a BGP route attribute and the length of the route attribute is long, the processing performance of the XPL policy deteriorates. To improve the processing performance of the routing policy, decrease the number of regular expressions or use a non-regular expression matching command.
       
       It is recommended that a maximum of 100 regular expressions be configured for each policy.
  4. Run the [**end-list**](cmdqueryname=end-list) command to conclude the configuration of the RD set, exit the RD set view, and return to the system view.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Example

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If only paragraph-by-paragraph editing is used as an example, the corresponding line editing is similar. To use the line editing mode, perform the operations described in paragraph-by-paragraph editing.

For detailed set and route-filter configuration steps, see [Configuration Procedures for Sets and Route-Filters Using the Paragraph-by-Paragraph Editing Mode](dc_vrp_xpl_cfg_0002.html#EN-US_CONCEPT_0000001793384325__section_dc_vrp_xpl_cfg_000102). For details about XPL clauses, see [XPL Paragraph Editing Clauses](dc_vrp_xpl_cfg_0014.html).

| **Objective** | Configure an RD set to match the VPN routes carrying the RD (100:1, 200:1, or 300:\*) in the format of 2-byte AS number:4-byte user-defined number. |
| --- | --- |
| **Configuration Example** | ``` <HUAWEI> edit xpl rd-list rd-list1  xpl rd-list rd-list1 100:1, 200:1, regular 300:* end-list ```  The RD set contains three elements and can match VPN routes carrying RD 100:1, 200:1, or 300:\*. |
| **Objective** | Configure a route-filter to allow only the VPN routes carrying the RDs contained in the set named **rd-list1** to match the route-filter. |
| **Reference Example** | ``` <HUAWEI> edit xpl route-filter r1  xpl route-filter r1 if rd in rd-list1 then approve else refuse endif end-filter ```  The route-filter references the set named **rd-list1** and allows only the VPN routes carrying the RDs contained in the set to match the route-filter. |