Configuring a Community Filter
==============================

Configuring_a_Community_Filter

#### Context

A Community filter is used to filter BGP routes based on Community attributes contained in the BGP routes. A Community attribute is a set of destination addresses with the same characteristics. Filtering rules defined based on Community attributes can be used to filter BGP routes.

In addition to the well-known Community attributes, users can define community attributes using digits. The matching condition of a community filter can be specified using a community ID or a regular expression.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Like an AS\_Path attribute, a Community attribute is used to filter only BGP routes because the Community attribute is also a private attribute of BGP.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip community-filter**](cmdqueryname=ip+community-filter)
   
   
   
   A community filter is configured.
   
   
   
   * To configure a standard community filter, run the [**ip community-filter**](cmdqueryname=ip+community-filter) **basic** *comm-filter-name* [ **index** *index-number* ] { **permit** | **deny** } [ *community-number* | *aa:nn* | **internet** [ **strict-match** ] | **no-export-subconfed** | **no-advertise** | **no-export** ] &<1-20> or [**ip community-filter**](cmdqueryname=ip+community-filter) *basic-comm-filter-num* [ **index** *index-number* ] { **permit** | **deny** } [ *community-number* | *aa:nn* | **internet** | **no-export-subconfed** | **no-advertise** | **no-export** ] &<1-20> command.
   * To configure an advanced community filter, run the [**ip community-filter**](cmdqueryname=ip+community-filter) { **advanced** *comm-filter-name* | *adv-comm-filter-num* } [ **index** *index-number* ] { **permit** | **deny** } *regular-expression* command.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display ip community-filter**](cmdqueryname=display+ip+community-filter) [ *basic-comm-filter-num* | *adv-comm-filter-num* | *comm-filter-name* ] command to check information about the configured Community filter.