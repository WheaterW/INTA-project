Configuring Regional Validation
===============================

Resource Public Key Infrastructure (RPKI) regional validation or regional confederation validation ensures BGP4+ security by validating route advertisers.

#### Usage Scenario

Regional validation: Users can manually combine multiple trusted ASs into a region and combine multiple regions into a regional confederation. Regional validation controls route selection results by checking whether the routes received from EBGP peers in an external region belong to the local region. This prevents intra-region routes from being hijacked by attackers outside the local region, and ensures that hosts in the local region can securely access internal services.

Regional validation applies to the following typical scenarios: regional validation scenario and regional confederation validation scenario.


#### Pre-configuration Tasks

Before configuring regional validation, complete the following tasks:

* [Configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rpki**](cmdqueryname=rpki)
   
   
   
   RPKI is started, and the RPKI view is displayed.
3. Run [**region-validation**](cmdqueryname=region-validation)
   
   
   
   Regional validation is enabled, and the region-validation view is displayed.
4. You can configure regions or regional confederation as required.
   
   
   * Create a region.
     1. Run [**region**](cmdqueryname=region) *region-id*
        
        A region is created.
     2. Run [**description**](cmdqueryname=description) *description-text*
        
        A description is configured for the region.
     3. Run [**as-number**](cmdqueryname=as-number) { *asn* } &<1-100>
        
        An AS number list is configured so that the AS numbers in it can be added to the region.
     4. Run [**quit**](cmdqueryname=quit)
        
        Exit the RPKI region-validation-region view.
     5. Run [**quit**](cmdqueryname=quit) Return to the system view.
   * Create a regional confederation.
     1. Run [**region**](cmdqueryname=region) *region-id*
        
        A region is created.
     2. Run [**quit**](cmdqueryname=quit)
        
        Exit the RPKI region-validation-region view.
     3. Run [**region-confederation**](cmdqueryname=region-confederation) *region-confederation-id*
        
        A regional confederation is created.
     4. Run [**description**](cmdqueryname=description) *description-text*
        
        A description is configured for the regional confederation.
     5. Run [**region**](cmdqueryname=region) { *region-id* } &<1-100>
        
        A region ID list is configured in the regional confederation so that regions in the list are added to the regional confederation.
     6. Run **quit**
        
        Exit the RPKI region-validation-confederation view.
     7. Run [**quit**](cmdqueryname=quit)
        
        The system view is displayed.
5. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
6. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
7. Enable the region or regional confederation function as required.
   
   
   * Run [**region-validation**](cmdqueryname=region-validation)
     
     BGP4+ regional validation is enabled.
   * Run [**region-validation confed-check strict**](cmdqueryname=region-validation+confed-check+strict)
     
     Strict BGP4+ regional validation is enabled.
8. Run [**bestroute region-validation**](cmdqueryname=bestroute+region-validation+allow-invalid) [ **allow-invalid** ]
   
   
   
   The device is configured to apply the BGP4+ regional validation results of RPKI to BGP4+ route selection.
   
   
   
   If regional validation succeeds, the route is valid and can participate in route selection. If regional validation fails, the route is invalid and cannot participate in route selection. To allow the routes that fail regional validation to be valid and participate in route selection, configure the **allow-invalid** parameter in the command. The priority of such routes is reduced during route selection.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display rpki session**](cmdqueryname=display+rpki+session+verbose) *ipv6-address* **verbose** command to check RPKI session configurations.