Maintaining DNS
===============

Maintaining DNS

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

Dynamic DNS entries cannot be restored after being cleared. Exercise caution when you run the corresponding reset command.

Statistics on sent and received DNS packets cannot be restored after being cleared. Exercise caution when you run the corresponding reset command.

Clearing the DNS cache for applications may affect services. Exercise caution when performing this operation.



#### Procedure

* To perform DNS maintenance operations, run the corresponding commands listed in [Table 1](#EN-US_TASK_0000001513150530__table1043392113711) in the user view.
  
  **Table 1** DNS maintenance operations
  | Operation | Command | Description |
  | --- | --- | --- |
  | Clear dynamic IPv4 DNS entries. | [**reset dns dynamic-host**](cmdqueryname=reset+dns+dynamic-host) | N/A |
  | Clear dynamic IPv6 DNS entries. | [**reset dns ipv6 dynamic-host**](cmdqueryname=reset+dns+ipv6+dynamic-host) [ **vpn-instance** *vpn-instance-name* ] | NA |
  | Clear statistics about sent and received DNS packets. | [**reset dns statistics**](cmdqueryname=reset+dns+statistics) | NA |
  | Display statistics about DNS packets. | [**display dns statistics**](cmdqueryname=display+dns+statistics) | NA |
  | Clear the DNS cache for applications. | [**reset dns application cache**](cmdqueryname=reset+dns+application+cache) [ *domain-name* ] | The DNS cache for applications refers to that used by other modules (such as SIP and GRE) of the device to resolve domain names. |
  | Display the DNS cache for applications. | [**display dns application cache**](cmdqueryname=display+dns+application+cache) |
  | Display the DNS table for applications. | [**display dns application table**](cmdqueryname=display+dns+application+table) | The DNS table for applications refers to that used by other modules (such as SIP and GRE) of the device to resolve domain names. |
* Enable the filtering function of DNS debugging information. You can configure filter criteria to specify the debugging information that can be sent by the device. This ensures device performance and facilitates debugging information query.
  ```
  [dns debugging filter](cmdqueryname=dns+debugging+filter) { domain domain-name | client-ip ip-address | client-ipv6 ipv6-address }
  ```
  
  By default, no filter criteria are configured for DNS debugging information. To check the filter criteria configured for DNS debugging information, run the **[**display dns debugging filter**](cmdqueryname=display+dns+debugging+filter)** command.