Configuring a Large-Community Filter
====================================

Configuring_a_Large-Community_Filter

#### Context

A Large-Community filter is used to filter BGP routes based on Large-Community attributes contained in BGP routes. The Large-Community attribute is an extended Community attribute. The Community attribute is a group of destination addresses with the same characteristics and consists of a set of 4-byte values, each of which specifies a community. Generally, the Community attribute on the NE40E is in the format of *aa:nn*, where *aa* specifies a 2-byte AS number and *nn* specifies the Community attribute ID defined by an administrator. The Community attribute is not flexible enough because it fails to carry a 4-byte AS number and contains only one Community attribute ID. To address this problem, the Large-Community attribute can be used instead. The Large-Community attribute consists of a set of 12-byte values and is in the format of *Global Administrator:LocalData1:LocalData2*.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The Large-Community filter is used to filter only BGP routes because it is a private BGP attribute.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run either of the following commands as needed:
   
   
   * To configure a basic Large-Community filter, run the [**ip large-community-filter**](cmdqueryname=ip+large-community-filter) **basic** *large-comm-filter-name* [ **index** *index-number* ] { **permit** | **deny** } { *aa:bb:cc* } &<1-16> command.
   * To configure an advanced Large-Community filter, run the [**ip large-community-filter**](cmdqueryname=ip+large-community-filter) **advanced** *large-comm-filter-name* [ **index** *index-number* ] { **permit** | **deny** } *regular-expression* command.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display ip large-community-filter**](cmdqueryname=display+ip+large-community-filter) [ *large-comm-filter-num* ] command to check information about the configured Large-Community filter.