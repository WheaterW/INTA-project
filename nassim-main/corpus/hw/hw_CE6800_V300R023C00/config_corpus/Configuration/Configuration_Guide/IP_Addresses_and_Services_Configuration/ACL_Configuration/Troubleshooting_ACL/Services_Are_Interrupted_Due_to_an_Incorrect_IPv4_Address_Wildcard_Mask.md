Services Are Interrupted Due to an Incorrect IPv4 Address Wildcard Mask
=======================================================================

Services Are Interrupted Due to an Incorrect IPv4 Address Wildcard Mask

#### Fault Symptom

A traffic policy has been configured on a device to redirect packets. To redirect the packets from a certain IPv4 address, the administrator adds a rule to the ACL used by the traffic policy following the ACL configuration guidelines. The new rule uses this source IP address as the matching condition. However, an incorrect IPv4 address wildcard mask is configured in the rule. As a result, BGP packets cannot be sent to the CPU, and most services are interrupted.


#### Procedure

1. Run the [**display this**](cmdqueryname=display+this) command in the ACL view to check the new rule.
   
   
   ```
   [display this](cmdqueryname=display+this)
   ```
   
   The new rule is as follows:
   
   ```
   rule 100 permit ip source 192.168.1.3 255.255.255.255
   ```
   
   The IPv4 address wildcard mask is 255.255.255.255, which is not an inverse mask. This rule is equivalent to **rule 100 permit ip** and **rule 100 permit ip source any**, meaning that packets from any IPv4 address are matched.
   
   The traffic policy using this ACL has been applied to a large number of interfaces, so all BGP packets received by these interfaces are redirected to other interfaces, but not sent to the CPU. As a result, a timeout occurs in processing protocol packets and in turn most services are interrupted.
2. Run the [**rule**](cmdqueryname=rule) command in the ACL view to change the IPv4 address wildcard mask in the new rule.
   
   
   
   The post-modification rule is as follows:
   
   ```
   rule 100 permit ip source 192.168.1.3 0.0.0.0 //This address is the IPv4 address of a single host only when the IPv4 address wildcard mask is 0.0.0.0.
   ```
   
   Services recover, and packets from the source IPv4 address of 192.168.1.3 are redirected correctly.