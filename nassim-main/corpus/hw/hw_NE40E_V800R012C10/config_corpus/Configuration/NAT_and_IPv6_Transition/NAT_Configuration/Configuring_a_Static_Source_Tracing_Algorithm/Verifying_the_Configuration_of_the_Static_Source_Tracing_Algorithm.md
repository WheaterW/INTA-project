Verifying the Configuration of the Static Source Tracing Algorithm
==================================================================

After configuring a static NAT source tracing algorithm, check the configurations.

#### Procedure

* Run the [**display nat static-mapping**](cmdqueryname=display+nat+static-mapping) *static-mapping-id* command to check parameters of the static source tracing algorithm with a specified ID.
* Run the [**display nat static-mapping**](cmdqueryname=display+nat+static-mapping) { **global-pool** | **inside-pool** } *pool-id* command to check the public and private address pools of the static source tracing algorithm.
* Run the [**display nat static-mapping ipv4**](cmdqueryname=display+nat+static-mapping+ipv4) *ipv4-address* command to check the mapping between private IP address and public IP addresses/port range calculated based on the static source tracing algorithm.
* Run the [**display nat static-mapping global-ipv4**](cmdqueryname=display+nat+static-mapping+global-ipv4) *ipv4-address* **port** *port-value* command to check the private IP addresses of the static source tracing algorithm.