Configuring RIP to Filter Received Routes
=========================================

You can configure an import policy for a device so that
the device receives only required routes.

#### Context

You can configure an import policy by specifying an ACL
or IP prefix list to filter received routes. You can also configure
a device to receive only the RIP packets from a specified neighbor.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run **rip** [ *process-id* ]
   
   
   
   A RIP process is created, and the RIP view is displayed.
3. Configure RIP to filter received routes.
   
   
   * Run [**filter-policy**](cmdqueryname=filter-policy) *acl-number* **import** [ *interface-type* *interface-number* ]
     
     The learned routes are filtered based on the ACL.
   * Run [**filter-policy gateway**](cmdqueryname=filter-policy+gateway) *ip-prefix-name* **import**
     
     The routes advertised by neighbors are filtered based
     on the IP prefix list.
   * Run [**filter-policy**](cmdqueryname=filter-policy) **acl-name** *acl-name* **import** [ *interface-type* *interface-number* ]
     
     The learned routes
     are filtered based on the named ACL.
   * Run [**filter-policy ip-prefix**](cmdqueryname=filter-policy+ip-prefix) *ip-prefix-name* [ **gateway** *ip-prefix-name* ] **import** [ *interface-type* *interface-number* ]
     
     The routes learned from the specified interface are
     filtered based on the IP prefix list or interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.