Configuring a Delay in Delivering Forwarding Entries for a New Link in a Fault-triggered Switchback Scenario
============================================================================================================

Configuring a Delay in Delivering Forwarding Entries for a New Link in a Fault-triggered Switchback Scenario

#### Context

In a common Layer 3 multicast fault-triggered switchback scenario, to prevent packet loss caused by the delivery of new forwarding entries before traffic is diverted to the new forwarding link, you can change the maximum delay for delivering forwarding entries for the new forwarding link.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the PIM view.
   
   
   ```
   pim [ vpn-instance vpn-instance-name ]
   ```
3. Set the maximum delay in delivering forwarding entries for a new link after a switchback in PIM-SM or PIM-SSM mode.
   
   
   ```
   [rpf-switch-delay](cmdqueryname=rpf-switch-delay+max-time) mode { sm | ssm } max-time { smTimeValue | ssmTimeValue }
   ```
   
   By default, the maximum delays in delivering forwarding entries for a new link after a switchback in PIM-SM and PIM-SSM modes are 350s and 150s, respectively.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```