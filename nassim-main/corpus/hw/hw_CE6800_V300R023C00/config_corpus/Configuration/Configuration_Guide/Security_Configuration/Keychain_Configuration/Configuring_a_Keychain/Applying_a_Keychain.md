Applying a Keychain
===================

Applying a Keychain

#### Context

A keychain itself manages just the encryption and authentication keys, and only takes effect when used in applications. Keychains can be used in applications running various protocols, as described in [Table 1](#EN-US_TASK_0000001176742371__table186034613278).

**Table 1** Using keychains in applications
| Transport Layer Protocol | Application | View | Application Scope | Configuration Reference |
| --- | --- | --- | --- | --- |
| Non-TCP | RIP | Interface view | Interface | IP Routing Configuration > RIP Configuration > Improving RIP Network Security > Configuring the Authentication Mode for RIP-2 Packets |
| IS-IS/IS-ISv6 | IS-IS view | IS-IS area | IP Route Configuration > IS-IS Configuration > Configuring IS-IS Authentication  IP Route Configuration > IS-ISv6 Configuration > Configuring IPv6 IS-IS Authentication |
| IS-IS view | IS-IS routing domain |
| Interface view | Interface |
| OSPF/OSPFv3 | OSPF area view | OSPF area | IP Route Configuration > OSPF Configuration > Configuring OSPF Authentication  IP Route Configuration > OSPFv3 Configuration > Configuring OSPFv3 Authentication |
| Interface view | Interface |
| OSPF area view | Virtual link |
| TCP | BGP/BGP4+ | BGP view and related views | Peer or peer group | IP Routing Configuration > BGP Configuration > Configuring BGP Authentication > Configuring Keychain Authentication  IP Route Configuration > BGP4+ Configuration > Configuring BGP4+ Authentication |

The following uses RIP as an example of how to apply a keychain.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Change the working mode of the interface from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure keychain authentication for RIP.
   
   
   ```
   [rip authentication-mode md5 nonstandard keychain](cmdqueryname=rip+authentication-mode+md5+nonstandard+keychain) keychain-name
   ```
5. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```