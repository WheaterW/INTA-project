Verifying the Configuration
===========================

After configuring a domain, you can check the domain configuration.

#### Prerequisites

The domain has been configured.
#### Procedure

1. Run the [**display domain**](cmdqueryname=display+domain) [ *domain-name* ] command to check the domain configuration.
2. Run the [**display user-flow-statistics**](cmdqueryname=display+user-flow-statistics) [ **domain** *domain-name* ] command in any view to check user upstream and downstream traffic statistics.
3. Run the [**display ip-pool usage-status**](cmdqueryname=display+ip-pool+usage-status) [ **domain** *domain-name* ] command to check the status of the public IP address pool in a specified domain.
4. Run the [**display ip-pool pool-usage**](cmdqueryname=display+ip-pool+pool-usage) [ **domain** *dname* | **pool-name** [ *pool-name* ] ] command to check the usage of the address pool bound to the domain.