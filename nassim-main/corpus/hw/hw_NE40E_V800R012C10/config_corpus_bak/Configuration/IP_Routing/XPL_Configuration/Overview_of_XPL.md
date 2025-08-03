Overview of XPL
===============

This section describes the basic concepts of extended routing-policy language (XPL), comparison between XPL and routing policies, and two XPL configuration modes.

#### Definition

Extended routing-policy language (XPL) is a language used to filter routes and modify route attributes. By modifying route attributes (including reachability), XPL changes the path through which network traffic passes. XPL provides the same functions as routing policies do and can meet different customer requirements.

[Table 1](#EN-US_CONCEPT_0172366603__en-us_concept_0172354535_table_dc_vrp_xpl_feature_000101) compares XPL and routing policies.

**Table 1** Comparison between XPL and routing policies
| Item | Key Functions | Editing Method | Filtering Method | User Experience |
| --- | --- | --- | --- | --- |
| XPL | Filters routes and modifies route attributes. | Line-by-line or paragraph-by-paragraph editing | Uses sets or single elements to filter routes. | Policies can be flexibly configured and modified. |
| Routing policies | Filter routes and modify route attributes. | Line-by-line editing | Use filters or single elements to filter routes. | Users must follow strict command configuration rules. |


![](../../../../public_sys-resources/note_3.0-en-us.png) 

For details about routing policies, see "Routing Policies" in *HUAWEI NE40E-M2 seriesUniversal Service Router Feature Description â IP Routing*.



#### Line-by-Line and Paragraph-by-Paragraph Editing

XPL supports two configuration modes: line-by-line editing and paragraph-by-paragraph editing.

Line-by-line editing is the traditional configuration mode of a device, so is not expanded on in this section. For details about this mode, see the set or route-filter configuration process. Note that during line-by-line editing of a set or route-filter, you can run the [**abort**](cmdqueryname=abort) command to cancel the configurations that have not been committed in the current view and return to the system view or run the [**display this candidate**](cmdqueryname=display+this+candidate) command to check the configurations that have not been committed in the current view.

Paragraph-by-paragraph editing is a new method of configuring XPL. [Table 2](#EN-US_CONCEPT_0172366603__table_dc_vrp_xpl_feature_000102) compares the two editing modes. For details about paragraph-by-paragraph editing, see [Introduction to XPL Paragraph-by-Paragraph Editing](dc_vrp_xpl_cfg_0002.html).

For details about XPL paragraph-by-paragraph editing clauses, see [XPL Paragraph Editing Clauses](dc_vrp_xpl_cfg_0014.html).

**Table 2** Line-by-line and paragraph-by-paragraph editing comparison
| Item | Applicable to | Configuration Method | Help and Error Correction Mechanism |
| --- | --- | --- | --- |
| Line-by-line editing | Users who are familiar with the traditional configuration method or unfamiliar with XPL | Each command is run in a command view, and one command is presented in one line, which is considered a configuration unit.  NOTE:  To modify an existing global variable set, route attribute set, or route-filter using the line-by-line editing mode, you need to enter the specific command view. | You can get the desired command through the type-ahead function.  Configuration errors, if any, are reported after the command is configured. |
| Paragraph-by-paragraph editing | Users who are familiar with XPL clause configuration and want to simplify the configuration process | Configurations are performed in the paragraph editing UI and are committed together after the configurations of a paragraph are complete. Each paragraph is considered a configuration unit. | The type-ahead function is not supported, and complete clauses must be manually entered in the paragraph editing UI.  Configuration errors, if any, are reported after the configurations of the whole paragraph are committed. |



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