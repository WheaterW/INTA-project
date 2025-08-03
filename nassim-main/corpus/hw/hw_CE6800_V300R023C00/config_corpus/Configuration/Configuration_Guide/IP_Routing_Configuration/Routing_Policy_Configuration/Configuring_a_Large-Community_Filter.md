Configuring a Large-Community Filter
====================================

Configuring a Large-Community Filter

#### Context

A Large-Community filter is used to filter BGP routes based on Large-Community attributes contained in BGP routes. The Large-Community attribute is an extended community attribute. The Community attribute is a group of destination addresses with the same characteristics and consists of a set of 4-byte values, each of which specifies a community. Generally, the Community attribute is in the format of *aa:nn*, where *aa* specifies a 2-byte AS number and *nn* specifies the Community attribute ID that is manually defined. The Community attribute is not flexible enough because it cannot carry a 4-byte AS number and contains only one Community attribute ID. To address this problem, the Large-Community attribute can be used instead. The Large-Community attribute consists of a set of 12-byte values and is in the format of *Global Administrator:LocalData1:LocalData2.*

![](public_sys-resources/note_3.0-en-us.png) 

The Large-Community filter is used to filter only BGP routes because it is a private BGP attribute.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a Large-Community filter.
   
   
   * Configure a basic Large-Community filter.
     ```
     [ip large-community-filter](cmdqueryname=ip+large-community-filter) basic large-comm-filter-name [ index index-number ] matchMode { cmntyStr } &<1-16>
     ```
   * Configure an advanced Large-Community filter.
     ```
     [ip large-community-filter](cmdqueryname=ip+large-community-filter) advanced large-comm-filter-name [ index index-number ] matchMode regular-expression
     ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ip large-community-filter**](cmdqueryname=display+ip+large-community-filter) [ *large-comm-filter-num* ] command to check information about the configured Large-Community filter.