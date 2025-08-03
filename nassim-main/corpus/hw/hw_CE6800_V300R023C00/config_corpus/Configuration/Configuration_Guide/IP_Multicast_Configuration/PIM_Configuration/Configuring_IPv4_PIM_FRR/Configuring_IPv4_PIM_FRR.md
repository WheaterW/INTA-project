Configuring IPv4 PIM FRR
========================

Configuring IPv4 PIM FRR

#### Prerequisites

Before configuring IPv4 PIM FRR, you have completed the following tasks:

* Configure a unicast routing protocol to ensure that devices are reachable through IP routes.
* Configure unicast IGP FRR.
* Configure basic PIM-SM functions.

#### Context

Generally, when a multicast link is faulty, multicast traffic convergence depends on unicast route convergence, which is time-consuming. This is unacceptable for multicast networks with high requirements on real-time transmission. To solve this problem, you can configure IPv4 PIM FRR. After FRR is configured, PIM sets up primary and backup MDTs based on unicast backup FRR routes, allowing multicast traffic to be transmitted through both the primary and backup links. The forwarding plane of the device with primary and backup routes accepts multicast traffic from the primary link and discards traffic from the backup link. If the primary link fails, the forwarding plane accepts multicast traffic from the backup link immediately, which accelerates multicast traffic convergence.

![](public_sys-resources/note_3.0-en-us.png) 

IPv4 PIM FRR can be configured only in IPv4 multicast scenarios.

This function is only supported by the following: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the PIM view.
   
   
   ```
   [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
   ```
3. Enable IPv4 PIM FRR.
   
   
   ```
   [rpf-frr](cmdqueryname=rpf-frr) [ policy { acl-number | acl-name acl-name } ]
   ```
4. (Optional) Set a delay in sending Prune messages upstream.
   
   
   ```
   [rpf-prune-delay](cmdqueryname=rpf-prune-delay) delay-time [ policy { acl-number | [acl-name](cmdqueryname=acl-name) acl-name } ]
   ```
5. (Optional) Set a delay in generating forwarding entries on interfaces connected to backup upstream devices.
   
   
   ```
   [backup-rpf-switchover-delay](cmdqueryname=backup-rpf-switchover-delay) interval hold-time [ policy { acl-number | acl-name acl-name } ]
   ```
6. (Optional) Set the maximum delay in delivering forwarding entries on a new link after a switchback in PIM-SM or PIM-SSM mode.
   
   
   ```
   [rpf-switch-delay](cmdqueryname=rpf-switch-delay+max-time) mode { sm | ssm } max-time { smTimeValue | ssmTimeValue }
   ```
   
   By default, the maximum delays in delivering forwarding entries on a new link after a switchback in PIM-SM and PIM-SSM modes are 350s and 150s, respectively.
7. (Optional) Set the WTR time for multicast forwarding entries.
   
   
   1. Return to the system view.
      ```
      [quit](cmdqueryname=quit)
      ```
   2. Set the WTR time for multicast forwarding entries.
      ```
      [multicast rpf-frr fib-wtr](cmdqueryname=multicast+rpf-frr+fib-wtr) wtr-time
      ```
      
      By default, the WTR time for multicast forwarding entries is 10s.
8. (Optional) Configure a PIM ECMP priority.
   
   
   1. Return to the system view.
      ```
      [quit](cmdqueryname=quit)
      ```
   2. Enter the interface view.
      ```
      [interface](cmdqueryname=interface) interface-type interface-number
      ```
   3. Switch the interface working mode from Layer 2 to Layer 3.
      ```
      [undo portswitch](cmdqueryname=undo+portswitch)
      ```
   4. Set a PIM ECMP priority for the interface.
      ```
      [pim ecmp-priority](cmdqueryname=pim+ecmp-priority) priorityValue
      ```
      
      The PIM ECMP priority takes effect only after it is configured on both the primary and backup inbound interfaces.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display multicast routing-table**](cmdqueryname=display+multicast+routing-table) or [**display multicast vpn-instance routing-table**](cmdqueryname=display+multicast+vpn-instance+routing-table) command to check the IP multicast routing table.
* Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) command to check the PIM routing table.
* Run the [**display pim join-prune**](cmdqueryname=display+pim+join-prune) command to check information about Join/Prune messages sent upstream by the device.