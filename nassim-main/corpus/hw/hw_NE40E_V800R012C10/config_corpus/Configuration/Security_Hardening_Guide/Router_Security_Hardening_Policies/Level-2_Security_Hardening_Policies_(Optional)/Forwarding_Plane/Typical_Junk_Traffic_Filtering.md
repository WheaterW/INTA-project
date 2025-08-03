Typical Junk Traffic Filtering
==============================

Typical Junk Traffic Filtering

#### Security Policy

Interface-based ACLs can be used to effectively prevent abnormal traffic from entering user terminals or prevent terminals' abnormal traffic from entering a network. The traffic to be blocked mainly includes common viruses and Trojan horse ports.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The ports to be blocked must be determined based on site requirements and confirmed by users. The following configurations and examples are for reference only.



#### Configuring Maintenance

1. Define an ACL to discard invalid packets matching viruses or Trojan horse ports.
   1. Run [**acl**](cmdqueryname=acl) { **name** *interface-based-acl-name* { **interface** | [ **interface** ] **number** *interface-based-acl-number* } | [ **number** ] *interface-based-acl-number* }
      
      The interface-based ACL view is displayed.
      
      The interface-based ACL number ranges from 1000 to 1999.
   2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } **interface** { *interface-type* *interface-number* | **any** } [ **time-range** *time-name* ] \*
      
      An interface-based ACL rule is configured.
2. Configure a traffic policy.
   1. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
      
      A traffic classifier is configured, and the traffic classifier view is displayed.
   2. Run [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **acl** { *acl-number* | **name** *acl-name* }
      
      An ACL rule is configured.
3. Define a traffic behavior.
   1. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behaviorâname*
      
      A traffic behavior is configured, and the traffic behavior view is displayed.
   2. Run [**permit | deny**](cmdqueryname=permit+%7C+deny)
      
      Packets are allowed to pass or are discarded.
4. Configure a traffic policy.
   1. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
      
      A traffic policy is configured, and the traffic policy view is displayed.
   2. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name*
      
      A traffic behavior is specified for the traffic classifier in the traffic policy.
5. Apply the traffic policy to a specified interface.
   1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      The interface view is displayed.
   2. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* { **inbound** | **outbound** }The traffic policy is applied to the specified interface.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      You can apply different traffic policies to the inbound and outbound directions of an interface.

#### Configuration Example

Configure ACL 3300 and ACL IPv6 3400 to match packets with viruses and Trojan horse ports and discard the packets.
```
acl number 3300
 rule 5 deny udp source-port range 135 netbios-ssn 
 rule 10 deny udp destination-port range 135 netbios-ssn
 rule 15 deny udp source-port eq 445
 rule 20 deny udp destination-port eq 445
 rule 25 deny tcp source-port eq 445  
 rule 30 deny tcp destination-port eq 445

acl ipv6 number 3400
 rule 5 deny udp source-port range 135 netbios-ssn 
 rule 10 deny udp destination-port range 135 netbios-ssn
 rule 15 deny udp source-port eq 445
 rule 20 deny udp destination-port eq 445
 rule 25 deny tcp source-port eq 445  
 rule 30 deny tcp destination-port eq 445
```

Filter out invalid incoming packets on the upstream interface of the device.
```
traffic classifier tcAntivirusIn operator or
 if-match acl 3300
 if-match ipv6 acl 3400
traffic behavior tbAntivirusIn

traffic policy tpAntivirusIn
 share-mode
 statistics enable
 classifier tcAntivirusIn behavior tbAntivirusIn precedence 1

//Apply the traffic policy to the inbound direction of the upstream interface.
interface GigabitEthernet0/1/0
 undo shutdown
 traffic-policy tpAntivirusIn inbound
```

Filter out invalid outgoing packets on the upstream interface of the device.
```
traffic classifier tcAntivirusOut operator or
 if-match acl 3300
 if-match ipv6 acl 3400
traffic behavior tbAntivirusOut

traffic policy tpAntivirusOut
 share-mode
 statistics enable
 classifier tcAntivirusOut behavior tbAntivirusOut precedence 1

//Apply the traffic policy to the outbound direction on the upstream interface of the device.
interface GigabitEthernet0/1/0
 undo shutdown
 traffic-policy tpAntivirusOut outbound
```


#### Verifying the Security Hardening Result

* Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command to check interface traffic information.
* Run the [**display traffic behavior**](cmdqueryname=display+traffic+behavior) { **system-defined** | **user-defined** } [ *behavior-name* ] command to check the traffic behavior configuration.
* Run the [**display traffic classifier**](cmdqueryname=display+traffic+classifier) { **system-defined** | **user-defined** } [ *classifier-name* ] command to check the traffic classifier configuration.
* Run the [**display traffic policy**](cmdqueryname=display+traffic+policy) [ [ **name** ] *policy-name* ] **statistics** **interface** *interface-type* *interface-number* [ .*sub-interface* ] { **inbound** | **outbound** } [ **verbose** { **classifier-based** [ **class** *class-name* ] | **rule-based** [ **class** *class-name* ] [ **filter** ] } ] command to check traffic policy statistics about an interface.