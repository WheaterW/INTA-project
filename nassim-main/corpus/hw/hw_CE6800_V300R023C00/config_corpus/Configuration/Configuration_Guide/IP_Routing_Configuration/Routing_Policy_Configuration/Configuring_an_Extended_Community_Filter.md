Configuring an Extended Community Filter
========================================

Configuring an Extended Community Filter

#### Context

An extended community filter is used to filter BGP routes based on extended community attributes. BGP extended community attributes are classified as follows:

* VPN target: VPN targets are used to control route learning between VPN instances, isolating routes of VPN instances from each other.
* Source of Origin (SoO): SoO attributes can be configured for VPN sites to distinguish routes from different VPN sites, preventing routing loops.
* Encapsulation: indicates the VXLAN encapsulation extended community attribute. In an EVPN VXLAN scenario, EVPN routes carry the VXLAN encapsulation extended community attribute. You can set the attribute value to 0:8 to filter EVPN routes in this scenario.

The matching conditions of extended community filters can be specified using extended community IDs or regular expressions.

![](public_sys-resources/note_3.0-en-us.png) 

Extended community filters are used to filter only BGP routes because extended community attributes are private attributes of BGP.



#### Procedure

* Configure VPN target extended community filters.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. VPN target extended community filters include basic and advanced VPN target extended community filters.
     
     
     + Configure a basic VPN target extended community filter.
       ```
       [ip extcommunity-filter](cmdqueryname=ip+extcommunity-filter) basic-extcomm-filter-num [ index index-number ] matchMode { rt extCmntyStr } &<1-16>
       [ip extcommunity-filter basic](cmdqueryname=ip+extcommunity-filter+basic) basic-extcomm-filter-name [ index index-number ] matchMode { rt extCmntyStr } &<1-16>
       ```
     + Configure an advanced VPN target extended community filter.
       ```
       [ip extcommunity-filter](cmdqueryname=ip+extcommunity-filter) advanced-extcomm-filter-num [ index index-number ] matchMode regular-expression
       [ip extcommunity-filter advanced](cmdqueryname=ip+extcommunity-filter+advanced) advanced-extcomm-filter-name [ index index-number ] matchMode regular-expression
       ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure SoO extended community filters.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. SoO extended community filters include basic and advanced SoO extended community filters.
     
     
     + Configure a basic SoO extended community filter.
       ```
       [ip extcommunity-list soo basic](cmdqueryname=ip+extcommunity-list+soo+basic) basic-extcomm-filter-name [ index index-number ] matchMode { site-of-origin } &<1-16>
       ```
     + Configure an advanced SoO extended community filter.
       ```
       [ip extcommunity-list soo advanced](cmdqueryname=ip+extcommunity-list+soo+advanced) advanced-extcomm-filter-name [ index index-number ] matchMode regular-expression
       ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure encapsulation extended community filters.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Encapsulation extended community filters include basic and advanced encapsulation extended community filters.
     
     
     + Configure a basic encapsulation extended community filter.
       ```
       [ip extcommunity-list encapsulation basic](cmdqueryname=ip+extcommunity-list+encapsulation+basic) encapsulation-name [ index index-value ] matchMode { encapsulation-value } &<1-16>
       ```
     + Configure an advanced encapsulation extended community filter.
       ```
       [ip extcommunity-list encapsulation advanced](cmdqueryname=ip+extcommunity-list+encapsulation+advanced) encapsulation-name [ index index-value ] matchMode regular
       ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the [**display ip extcommunity-filter**](cmdqueryname=display+ip+extcommunity-filter) command to check information about the configured extended community filters.
* Run the [**display ip extcommunity-list soo**](cmdqueryname=display+ip+extcommunity-list+soo) [ *eclSooName* ] command to check detailed information about a configured SoO extended community filter.
* Run the [**display ip extcommunity-list encapsulation**](cmdqueryname=display+ip+extcommunity-list+encapsulation) [ *name*] command to check detailed information about a configured encapsulation extended community filter.