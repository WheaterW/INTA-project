Configuring User Priority Mapping in a Domain
=============================================

You need to configure the mappings among the user priority, CoS, and color to implement QoS on packets in a domain.

#### Context

You can configure the desired priorities for online users. To perform traffic scheduling according to the user priority, you can configure user priority mapping in a domain. After a user in this domain goes online, the priority of the user is mapped to the internal CoS of the device according to the configured mapping relationship.

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
4. Run [**user-priority**](cmdqueryname=user-priority) { **upstream** | **downstream** } { *priority* | **trust-8021p-inner** | **trust-8021p-outer** | **trust-dscp-outer** | **trust-dscp-inner** | **trust-exp-inner** | **trust-exp-outer** | **unchangeable** }
   
   
   
   The user priority is configured.
   
   
   
   The methods for configuring user priorities are as follows:
   
   * Directly specifying the user priority, which ranges from 0 to 7
   * Using the internal or external 802.1p value of Layer 2 packets of the user as the user priority (not applicable to packets sent from the network side to the user side)
   * Using the DSCP value of user packets as the user priority
   * Using the EXP value of MPLS packets as the user priority
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the AAA view.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**diffserv domain**](cmdqueryname=diffserv+domain) { *ds-domain-name* | **default** | **5p3d** } [ **domain-id** *domain-id* ]
   
   
   
   A DS domain is defined and the DS domain view is displayed.
8. (Optional) Run [**user-priority**](cmdqueryname=user-priority) *priority* **phb** { **af1** | **af2** | **af3** | **af4** | **be** | **cs6** | **cs7** | **ef** } [ **green** | **yellow** | **red** ]
   
   
   
   Priority mapping is configured for users in a domain.
   
   
   
   Before configuring the user priority mapping by running the [**user-priority phb**](cmdqueryname=user-priority+phb) command, you must specify the user priority that needs to be mapped by running the [**user-priority**](cmdqueryname=user-priority) command in the AAA domain. Otherwise, the mapping does not take effect.
   
   If the CoS is CS6, CS7, EF, or BE, packets can be marked only in green.
   
   **Table 1** Default mapping between user priorities and CoSs
   | User Priority | Service | Color |
   | --- | --- | --- |
   | 0 | BE | Green |
   | 1 | AF1 | Green |
   | 2 | AF2 | Green |
   | 3 | AF3 | Green |
   | 4 | AF4 | Green |
   | 5 | EF | Green |
   | 6 | CS6 | Green |
   | 7 | CS7 | Green |
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
10. Run [**aaa**](cmdqueryname=aaa)
    
    
    
    The AAA view is displayed.
11. Run [**domain**](cmdqueryname=domain) *domain-name*
    
    
    
    The AAA domain view is displayed.
12. To configure priority mapping for IP packets, MPLS packets, and multicast packets of a domain, run the [**trust upstream**](cmdqueryname=trust+upstream) *ds-domain-name* command to enable simple traffic classification in the domain.
13. (Optional) Run [**qos phb**](cmdqueryname=qos+phb) { **dscp** | **inner-8021p** | **outer-8021p** | **mpls-exp** } **disable**
    
    
    
    PHB for specific priorities of downstream packets in an AAA domain is disabled.
14. (Optional) Configure the function to redirect enterprise users to a specified BA classification domain.
    1. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the AAA view.
    2. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
    3. Run [**dhcp option**](cmdqueryname=dhcp+option) *option-code* **include** *option-include* **redirect ds-domain enable**
       
       
       
       The function to redirect enterprise users to a specified BA classification domain is enabled.
    4. Run [**aaa**](cmdqueryname=aaa)
       
       
       
       The AAA view is displayed.
    5. Run [**domain**](cmdqueryname=domain) *domain-name*
       
       
       
       The AAA domain view is displayed.
    6. Run [**redirect ds-domain**](cmdqueryname=redirect+ds-domain) *ds-domain-name*
       
       
       
       The function to redirect enterprise users in a DS domain to a specified BA classification domain is enabled.
15. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

Run the following commands to check the previous configuration.

* Run the [**display diffserv domain**](cmdqueryname=display+diffserv+domain) [ *ds-domain-name* ] [ **8021p** | **atm** | **dscp** | **exp** ] [ **inbound** | **outbound** ] command to display the configurations of a DS domain.
* Run the [**display diffserv domain application**](cmdqueryname=display+diffserv+domain+application) [ *ds-domain-name* ] command to display the interface list applied to a DS domain.