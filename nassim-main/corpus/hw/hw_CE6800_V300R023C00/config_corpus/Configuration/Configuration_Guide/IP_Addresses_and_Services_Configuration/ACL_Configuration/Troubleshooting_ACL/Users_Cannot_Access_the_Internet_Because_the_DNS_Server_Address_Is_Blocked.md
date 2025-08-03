Users Cannot Access the Internet Because the DNS Server Address Is Blocked
==========================================================================

Users Cannot Access the Internet Because the DNS Server Address Is Blocked

#### Fault Symptom

An ACL is configured on the device to restrict destination addresses accessible to users; however, the DNS server address is blocked in the ACL. As a result, the query packets sent from users to the DNS server are discarded. The domain names cannot be resolved, so users cannot access the Internet.


#### Procedure

1. Check ACL rules in the system view.
   
   
   ```
   [display acl all](cmdqueryname=display+acl+all)
   ```
   
   The following rule is included:
   
   ```
   rule 100 deny ip destination 192.168.1.0 0.0.0.255  //Reject the packets destined for network segment 192.168.1.0/24.
   ```
   
   The DNS server address configured on user PCs is 192.168.1.68, which belongs to network segment 192.168.1.0/24. Therefore, packets sent from users to the DNS server are discarded. The domain names cannot be resolved, so users cannot access the Internet.
2. Run the [**rule**](cmdqueryname=rule) command in the ACL view to add a rule to permit the DNS server address.
   
   
   ```
   rule 99 permit ip destination 192.168.1.68 0.0.0.0  //Permit the packets destined for the DNS server.
   rule 100 deny ip destination 192.168.1.0 0.0.0.255  //Reject the packets destined for network segment 192.168.1.0/24.
   ```
   
   After rule 99 is added, the packets sent from users to the DNS server match rule 99 and pass. The domain names can be resolved, and users can access the Internet.