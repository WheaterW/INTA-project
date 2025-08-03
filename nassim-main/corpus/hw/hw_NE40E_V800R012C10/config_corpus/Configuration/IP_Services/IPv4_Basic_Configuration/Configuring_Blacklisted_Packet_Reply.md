Configuring Blacklisted Packet Reply
====================================

If TCP/UDP packets are denied by ACL rules, you can configure blacklisted packet reply to allow the system to respond to the source end with specified packets.

#### Usage Scenario

After ACLs are configured, you can configure the system to respond to the source end upon receipt of blacklisted packets, which are TCP/UDP packets denied by ACL rules. If TCP packets are denied, the system responds to the source end with TCP-RST packets; if UDP packets are denied, the system responds to the source end with Port Unreachable packets.


#### Prerequisites

None


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip blacklist packet permit**](cmdqueryname=ip+blacklist+packet+permit)
   
   
   
   The system is enabled to respond to the source end upon receipt of TCP/UDP packets denied by ACL rules.