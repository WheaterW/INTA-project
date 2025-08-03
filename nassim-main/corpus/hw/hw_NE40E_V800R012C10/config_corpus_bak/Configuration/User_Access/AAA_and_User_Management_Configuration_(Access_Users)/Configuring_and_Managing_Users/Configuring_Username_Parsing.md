Configuring Username Parsing
============================

The sequence of a domain name and a username and the position of the delimiter between them can be flexibly configured to meet different requirements.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain-name-delimiter**](cmdqueryname=domain-name-delimiter) *delimiter*
   
   
   
   The domain name delimiter is configured.
4. Run [**domain-location**](cmdqueryname=domain-location) { **after-delimiter** | **before-delimiter** }
   
   
   
   The position of the domain name is set.
5. Run [**domainname-parse-direction**](cmdqueryname=domainname-parse-direction) { **left-to-right** | **right-to-left** }
   
   
   
   The direction in which the domain name is parsed is set.
6. (Optional) Run [**realm-name-delimiter**](cmdqueryname=realm-name-delimiter) *delimiter*
   
   
   
   The realm name delimiter is configured.
7. (Optional) Run [**realm-location**](cmdqueryname=realm-location) { **after-delimiter** | **before-delimiter** }
   
   
   
   The position of the realm name is configured.
8. (Optional) Run [**realmname-parse-direction**](cmdqueryname=realmname-parse-direction) { **left-to-right** | **right-to-left** }
   
   
   
   The direction in which the realm name is parsed is configured.
9. Run [**parse-priority**](cmdqueryname=parse-priority) { **domain-first** | **realm-first** } A parsing priority is configured.
   
   
   * If the realm name delimiter is configured and the **domain-first** keyword is specified, the system first parses the realm name according to the realm name delimiter, realm name parsing direction, and realm name position. The system then parses the remaining character string based on the domain name delimiter, domain name position, and domain name parsing direction.
   * If no realm name delimiter is configured and the **domain-first** keyword is specified, the system parses the domain name based on the domain name delimiter, domain name position, and domain name parsing direction.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.