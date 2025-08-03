Configuring a Community Filter
==============================

Configuring a Community Filter

#### Context

A Community filter is used to filter BGP routes based on Community attributes contained in the BGP routes. A Community attribute is a set of destination addresses with the same characteristics. Filtering rules defined based on Community attributes can be used to filter BGP routes. Before advertising a route carrying a Community attribute to peers, a BGP device can be configured to change the original Community attribute of this route.

* The Community attribute is a 4-byte value in the format of *aa*:*nn*. According to standards, the most significant 2 bytes indicate an AS number, and the least significant 2 bytes indicate an identifier for management purposes.
* The Community attribute is a BGP route tag used to simplify the execution of route-policies. You can assign a specific Community attribute value to certain routes. Then, the routes can be filtered based on the Community attribute value and the corresponding policies can be executed.![](public_sys-resources/note_3.0-en-us.png) 
  
  Like an AS\_Path attribute, a Community attribute is used to filter only BGP routes because the Community attribute is also a private attribute of BGP.

**Figure 1** Application scenario of Community attributes  
![](figure/en-us_image_0000001176743451.png)

As shown in [Figure 1](#EN-US_TASK_0000001176743443__fig_dc_feature_route-policy_000801), a large number of routes in AS 100 are imported to the BGP routing table. These routes are used to transmit voice call and video surveillance services. The routes are advertised to AS 200 through BGP. Devices in AS 200 need to enforce different route-policies for routes used to transmit voice calls and video surveillance. ACLs or IP prefixes can be used to match routes one by one. However, there are a large number of route prefixes, which leads to heavy workload and low efficiency.

You can use the Community attribute to solve the problems. When a device in AS 100 imports these routes, the device adds the corresponding community values to distinguish the routes for voice calls from those for video surveillance. The routes for voice calls are assigned the community value of 100:1, and the routes for video surveillance are assigned the community value of 100:2. The attribute values are transmitted to AS 200 along with the routes. When route-policies need to be configured for the voice call and video surveillance routes on a device in AS 200, the device only needs to match the routes against the community values. For example, if routes match the community value of 100:1, routes for all voice services are filtered based on the policy.

BGP defines some well-known Community attributes, which can be directly used. [Table 1](#EN-US_TASK_0000001176743443__tab_001) describes common Community attributes.

**Table 1** Well-known Community attributes of BGP
| Community Attribute | Description |
| --- | --- |
| internet | By default, all routes belong to the Internet community. A route with this attribute can be advertised to all BGP peers. |
| no-advertise | After being received, a route with this attribute cannot be advertised to any other BGP peers. |
| no-export | After being received, a route with this attribute cannot be advertised outside the local AS. If a confederation is defined, the route with this attribute cannot be advertised to the ASs outside the confederation, but can be advertised to other sub-ASs in the confederation. |
| no-export-subconfed | After being received, a route with this attribute cannot be advertised outside the local AS or to other sub-ASs in the confederation. |



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a Community filter.
   
   
   * Configure a basic Community filter.
     ```
     [ip community-filter](cmdqueryname=ip+community-filter) basic basCfName [ index index-val ] matchMode [ cmntyStr ] &<1-20>
     ```
   * Configure an advanced Community filter.
     ```
     [ip community-filter](cmdqueryname=ip+community-filter) advanced comm-filter-name [ index index-number ] matchMode regular-expression
     ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ip community-filter**](cmdqueryname=display+ip+community-filter) [ *basic-comm-filter-num* | *adv-comm-filter-num* | *comm-filter-name* ] command to check information about the configured Community filter.