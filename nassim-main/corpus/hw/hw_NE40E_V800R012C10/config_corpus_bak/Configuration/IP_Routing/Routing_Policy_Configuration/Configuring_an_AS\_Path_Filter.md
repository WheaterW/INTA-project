Configuring an AS\_Path Filter
==============================

Configuring_an_AS\_Path_Filter

#### Context

An AS\_Path filter is used to filter BGP routes by matching against AS\_Path attributes. The AS\_Path attribute records the numbers of all ASs through which a BGP route passes from the local end to the destination in the distance-vector (DV) order. In this case, AS\_Path attribute-based filtering rules can be defined to filter BGP routes.

The matching condition of an AS\_Path filter is specified using a regular expression. For example, ^30 indicates that only the AS\_Path attribute starting with 30 is matched. Using a regular expression can simplify configurations. For details on how to use regular expressions, see the command line description in the *Configuration Guide > Basic Configuration*.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The AS\_Path filter takes effect only on BGP routes because the AS\_Path attribute is a private attribute of BGP.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip as-path-filter**](cmdqueryname=ip+as-path-filter) { *as-path-filter-number* | *as-path-filter-name* } [ **index** *index-number* ] { **permit** | **deny** } *regular-expression*
   
   
   
   An AS\_Path filter is configured.
   
   
   
   *regular-expression* indicates that the AS\_Path filter uses regular expressions to define matching rules.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display ip as-path-filter**](cmdqueryname=display+ip+as-path-filter) [ *as-path-filter-number* | *as-path-filter-name* ] command to check information about the configured AS\_Path filter.