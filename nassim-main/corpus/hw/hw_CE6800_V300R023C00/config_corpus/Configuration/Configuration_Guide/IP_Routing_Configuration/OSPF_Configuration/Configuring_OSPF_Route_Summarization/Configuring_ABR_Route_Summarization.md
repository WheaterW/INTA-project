Configuring ABR Route Summarization
===================================

Configuring ABR Route Summarization

#### Prerequisites

Before configuring ABR route summarization, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Enter the OSPF area view.
   
   
   ```
   [area](cmdqueryname=area) area-id
   ```
4. Configure OSPF ABR route summarization.
   
   
   ```
   [abr-summary](cmdqueryname=abr-summary) ip-address mask [ [ advertise | [ cost { cost-value | inherit-minimum } ] | [ generate-null0-route ] ] * | [ not-advertise | [ cost { cost-value | inherit-minimum } ] ] * | [ generate-null0-route | [ advertise ] | [ cost { cost-value | inherit-minimum } ] ] * ]
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```