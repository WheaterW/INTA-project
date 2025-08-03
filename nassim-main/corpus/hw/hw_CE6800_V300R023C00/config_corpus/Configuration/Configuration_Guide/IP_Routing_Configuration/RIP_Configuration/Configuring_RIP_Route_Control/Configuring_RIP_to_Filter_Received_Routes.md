Configuring RIP to Filter Received Routes
=========================================

Configuring RIP to Filter Received Routes

#### Context

By specifying an ACL or IP prefix list, you can configure a routing policy to filter the received routes and allow only the RIP messages from a specific neighbor to pass.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIP process and enter the RIP view.
   
   
   ```
   [rip](cmdqueryname=rip) [ process-id ]
   ```
3. Configure RIP to filter received routes. [Table 1](#EN-US_TASK_0000001130782966__table13897184015814) lists the routing policies that can be used.
   
   
   
   **Table 1** Configuring RIP to filter received routes
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure RIP to filter received routes based on a numbered ACL. | [**filter-policy**](cmdqueryname=filter-policy) *acl-number* **import** [ *interface-type* *interface-number* ] | - |
   | Configure RIP to filter the routes advertised by a neighbor based on an IP prefix list. | [**filter-policy gateway**](cmdqueryname=filter-policy+gateway) *ip-prefix-name* **import** | - |
   | Configure RIP to filter the learned routes based on a named ACL. | [**filter-policy**](cmdqueryname=filter-policy) **acl-name** *acl-name* **import** [ *interface-type* *interface-number* ] | - |
   | Configure RIP to filter the routes learned by a specified interface based on an IP prefix list and a neighbor. | [**filter-policy ip-prefix**](cmdqueryname=filter-policy+ip-prefix) *ip-prefix-name* [ **gateway** *ip-prefix-name* ] **import** [ *interface-type* *interface-number* ] | - |
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```