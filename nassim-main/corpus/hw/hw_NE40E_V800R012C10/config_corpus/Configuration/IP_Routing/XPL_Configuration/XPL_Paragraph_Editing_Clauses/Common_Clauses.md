Common Clauses
==============

Common clauses are classified as logic, start, or end clauses. Logic clauses indicate logical relationships, the start clause begins a configuration in XPL, and the end clause concludes a configuration in XPL.

#### Logic Clauses

**eq**: equal to.

**ge**: greater than or equal to.

**le**: less than or equal to.

**in**: included in a set.

**if**: introductory condition clause.

**elseif**: introductory condition clause, used to filter the routes that fail to meet previous matching rules.

**else**: introductory condition clause, used to include all the routes that fail to meet previous matching rules.

**then**: introductory action clause, in the format of **if**+condition clause+**then** or **elseif**+condition clause+**then**. **else** is not followed by an introductory action clause in most cases.

**apply**: action implementation clause, in the format of **apply**+action clause. Action clauses (excluding **approve**, **refuse**, **finish**, **call route-filter** *route-filter-name*, and **break**) must follow **apply**.

**endif**: conclusive condition clause, following a condition and an action, and concluding all matching rules.


#### Configuration Start and End Clauses

| Configuration Start Clauses | Configuration End Clauses |
| --- | --- |
| [**xpl global-value**](cmdqueryname=xpl+global-value): begins the edition of a global variable set. | [**end-global-value**](cmdqueryname=end-global-value): concludes the edition of a global variable set. |
| [**xpl ip-prefix-list**](cmdqueryname=xpl+ip-prefix-list) *ip-prefix-list-name*: begins the edition of an IPv4 prefix set. | [**end-list**](cmdqueryname=end-list): concludes the edition of an IPv4 prefix set. |
| [**xpl ipv6-prefix-list**](cmdqueryname=xpl+ipv6-prefix-list) *ipv6-prefix-list-name*: begins the edition of an IPv6 prefix set. | [**end-list**](cmdqueryname=end-list): concludes the edition of an IPv6 prefix set. |
| [**xpl as-path-list**](cmdqueryname=xpl+as-path-list) *as-path-list-name*: begins the edition of an AS\_Path set. | [**end-list**](cmdqueryname=end-list): concludes the edition of an AS\_Path set. |
| **xpl community-list** *community-list-name*: begins the edition of a community set. | [**end-list**](cmdqueryname=end-list): concludes the edition of a community set. |
| [**xpl large-community-list**](cmdqueryname=xpl+large-community-list) *large-community-list-name*: starts the edition of a Large-community set. | [**end-list**](cmdqueryname=end-list): concludes the edition of a Large-community set. |
| [**xpl rd-list**](cmdqueryname=xpl+rd-list) *rd-list-name*: begins the edition of an RD set. | [**end-list**](cmdqueryname=end-list): concludes the edition of an RD set. |
| [**xpl extcommunity-list rt**](cmdqueryname=xpl+extcommunity-list+rt) *rt-list-name*: begins the edition of a route target set. | [**end-list**](cmdqueryname=end-list): concludes the edition of a route target set. |
| [**xpl extcommunity-list soo**](cmdqueryname=xpl+extcommunity-list+soo) *soo-list-name*: begins the edition of a site of origin (SoO) set. | [**end-list**](cmdqueryname=end-list): concludes the edition of an SoO set. |
| [**xpl route-filter**](cmdqueryname=xpl+route-filter) *route-filter-name*: begins the edition of a route-filter. | [**end-filter**](cmdqueryname=end-filter): concludes the edition of a route-filter. |
| [**xpl route-flow-group**](cmdqueryname=xpl+route-flow-group) *group-name*: begins the edition of a QPPB configuration group. | [**end-group**](cmdqueryname=end-group): concludes the edition of a QPPB configuration group. |


![](../../../../public_sys-resources/note_3.0-en-us.png) 

A configuration end clause concludes only the edition of a set or route-filter in the paragraph-by-paragraph editing view. To save the current configuration and exit this view, press **Ctrl+X**.