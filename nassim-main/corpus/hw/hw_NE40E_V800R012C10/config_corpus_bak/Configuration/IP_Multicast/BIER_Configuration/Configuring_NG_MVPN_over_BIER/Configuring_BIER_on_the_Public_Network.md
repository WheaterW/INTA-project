Configuring BIER on the Public Network
======================================

In the NG MVPN over BIER scenario, you need to configure all devices in each BIER sub-domain on the public network.

#### Context

Each edge node in a BIER sub-domain must be configured with a BFR-ID that is unique to the sub-domain. In the NG MVPN over BIER scenario, a BFR-ID needs to be configured for the sender PE and receiver PEs. Ps do not require BFR-IDs, but you need to enable BIER on the Ps.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bier**](cmdqueryname=bier)
   
   
   
   BIER is enabled, and the BIER view is displayed.
3. Run [**sub-domain**](cmdqueryname=sub-domain) *sub-domain-val*
   
   
   
   A BIER sub-domain is configured.
   
   
   
   * Run the [**bfr-id**](cmdqueryname=bfr-id) *bfr-id-val* command to configure a BFR-ID that is unique in the BIER sub-domain for the PE.
   * Run the [**encapsulation-type**](cmdqueryname=encapsulation-type) **mpls** **bsl** { **64** | **128** | **256** } **max-si** command to set the encapsulation type, BSL, and Max-SI of packets carried using BIER.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The values of *bfr-id-val*, [**bsl**](cmdqueryname=bsl), and *max-si-val* must meet the following formula:
     
     (*bfr-id-val* â 1)/[**bsl**](cmdqueryname=bsl) â¤ *max-si-val*
     
     If [**bsl**](cmdqueryname=bsl) and *max-si-val* are configured before *bfr-id-val*, *bfr-id-val* ranges from 1 to *bsl* x (*max-si-val* + 1).
   * Run the [**bfr-prefix**](cmdqueryname=bfr-prefix) **interface** { *interface-name* | *interface-type* *interface-number* } command to configure a BFR-prefix for the PE in the BIER sub-domain.
     
     A BFR-prefix is an IPv4 address in a sub-domain for the BFR. It must be a loopback interface address with a 32-bit mask. Therefore, the interface must be a loopback interface. The function takes effect only after IS-IS is enabled on the interface
   * Run the [**protocol**](cmdqueryname=protocol) *isis* command to configure the underlay protocol used to advertise BIER information.
   * (Optional) Run the [**max-load-balance**](cmdqueryname=max-load-balance) *number* command to configure the maximum number of BIER tunnels for load balancing.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.