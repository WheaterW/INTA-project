Using Tracert to Check a PW Path on a VPWS Network
==================================================

You can run the [**tracert**](cmdqueryname=tracert) command to obtain information about the SPEs and Ps through which packets pass from the source to the destination. Based on the command output, you can monitor PW connectivity and locate faulty nodes.

#### Prerequisites

Before testing PW connectivity using the [**tracert vc**](cmdqueryname=tracert+vc) command, ensure that the VPWS network has been configured correctly.

If the control word channel is used, you need to run the [**control-word**](cmdqueryname=control-word) command in the PW template view to enable the control word function.


#### Context

Perform the following steps on the PE of a VPWS network.


#### Procedure

1. Run any of the following commands to locate VPWS network faults through PW tracert as required:
   
   
   * Control-word mode:
     
     Run the [**tracert vc**](cmdqueryname=tracert+vc) *vc-type* *pw-id* [ *peer-address* ] [ **-exp** *exp-value* | **-f** *first-ttl* | **-m** *max-ttl* | **-r** *reply-mode* | **-t** *timeout-value* | **-g** ]\* **control-word** [ **remote** *remote-ip-address* ] [ **full-lsp-path** | **ptn-mode** ] [ **pipe** | **uniform** ] [ **detail** ] [ **bypass** **-si** *interface-name* | *interface-type* *interface-number* ] command.
     
     In a BGP-based scenario, run the [**tracert vc -vpn-instance**](cmdqueryname=tracert+vc+-vpn-instance) *vpn-name* *local-ce-id* *remote-ce-id* [ **-exp** *exp-value* | **-f** *first-ttl* | **-m** *max-ttl* | **-r** *reply-mode* | **-t** *timeout-value* | **-g** ]\* **control-word** [ **full-lsp-path** ] [ **detail** ] [ **bypass** **-si** *interface-name* | *interface-type* *interface-number* ] command to perform a test.
   * Label-alert mode:
     
     Run the [**tracert vc**](cmdqueryname=tracert+vc) *vc-type* *pw-id* [ *peer-address* ] [ **-exp** *exp-value* | **-f** *first-ttl* | **-m** *max-ttl* | **-r** *reply-mode* | **-t** *timeout-value* | **-g** ] \* **label-alert** [ **no-control-word** ] [ **full-lsp-path** ] [ **pipe** | **uniform** ] [ **detail** ] [ **bypass** **-si** *interface-name* | *interface-type* *interface-number* ] command.
     
     In a BGP scenario, run the [**tracert vc -vpn-instance**](cmdqueryname=tracert+vc+-vpn-instance) *vpn-name* *local-ce-id* *remote-ce-id* [ **-exp** *exp-value* | **-f** *first-ttl* | **-m** *max-ttl* | **-r** *reply-mode* | **-t** *timeout-value* | **-g** ]\* **label-alert** [ **no-control-word** ] [ **full-lsp-path** ] [ **detail** ] [ **bypass** **-si** *interface-name* | *interface-type* *interface-number* ] command to perform a test.
   * TTL mode:
     
     [**tracert vc**](cmdqueryname=tracert+vc) *vc-type* *pw-id* [ *peer-address* ] [ **-exp** *exp-value* | **-f** *first-ttl* | **-m** *max-ttl* | **-r** *reply-mode* | **-t** *timeout-value* | **-g** ] \* **normal** [ **no-control-word** ] [ **remote** *remote-ip-address* ] [ **full-lsp-path** ] [ **pipe** | **uniform** ] [ **detail** ] [ **bypass** **-si** *interface-name* | *interface-type* *interface-number* ]
   
   An example is as follows:
   ```
   <HUAWEI> tracert vc vlan 100 control-word remote 4.1.1.2 full-lsp-path
     TTL   Replier            Time    Type      Downstream
     0                                Ingress   1.1.1.2/[1025 ]
     1     1.1.1.2           230 ms  Transit    2.1.1.2/[1301 ]
     2     2.1.1.2           230 ms  Transit    3.1.1.2/[1208 ]
     3     3.1.1.2           100 ms  Transit    4.1.1.2/[3 ]
     4     4.1.1.2           150 ms  Egress
   ```
   
   An example based on BGP is as follows:
   ```
   <HUAWEI> tracert vc -vpn-instance vpn1 1 2 label-alert full-lsp-path
   TTL   Replier            Time    Type      Downstream   
   0                                Ingress   10.2.2.2/[21505 1026 ]   
   1     10.2.2.2           60 ms   Transit   10.3.3.3/[1026 ]   
   2     10.3.3.3           50 ms   Transit   10.4.4.4/[3 ]   
   3     10.1.1.1           70 ms   Egress 
   ```
   
   
   
   The preceding command output shows each node on the PW and the response time of each node.