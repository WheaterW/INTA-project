Enabling Defense Against TCP SYN Flooding Attacks
=================================================

The TCP SYN flooding attack is a denial-of-service attack. Defense against TCP SYN flooding attacks protects the CPU by restricting the rate at which packets are sent to the CPU.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   The attack defense policy view is displayed.
3. Perform either of the following operations as required:
   * Run the [**tcpsyn-flood enable**](cmdqueryname=tcpsyn-flood+enable) command to enable defense against IPv4 TCP SYN flooding attacks.
   * Run the [**ipv6-tcpsyn-flood enable**](cmdqueryname=ipv6-tcpsyn-flood+enable) command to enable defense against IPv6 TCP SYN flooding attacks.
   
   
   
   The TCP SYN flooding attack is a denial-of-service attack in which an attacker sends a flood of TCP SYN packets to the target host, causing the target host to become too busy to answer legitimate requests. In extreme cases, the target host is suspended.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.