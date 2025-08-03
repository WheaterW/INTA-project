Configuring BGP to Detect the Status Changes of an Eth-Trunk Interface
======================================================================

Configuring BGP to Detect the Status Changes of an Eth-Trunk Interface

#### Prerequisites

Before configuring BGP to detect the status changes of an Eth-Trunk interface, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

In a BGP over M-LAG networking scenario, you can configure this function on an M-LAG device. It allows BGP to detect the status changes of an Eth-Trunk interface connected to a specified peer and adjust the priority of BGP routes received from the peer accordingly. If a single Eth-Trunk interface is specified (by running this command once) and fails, this configuration allows BGP to detect the Eth-Trunk interface fault and change the priority of the routes received from the peer to the lowest (by setting the MED to the maximum value and the Local\_Pref to the minimum value). If multiple Eth-Trunk interfaces are specified (by running this command multiple times), BGP changes the priority of the received routes to the lowest only if all these Eth-Trunk interfaces go faulty.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the BGP-IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
4. Configure BGP to detect the status changes of an Eth-Trunk interface.
   
   
   ```
   [peer](cmdqueryname=peer+route-priority-track) peerIpv6Addr route-priority-track interface { interface-name | localIfType localIfNum }
   ```
   
   This command configuration takes precedence over the configuration of applying a route-policy to routes received from or to be advertised to a peer (using the [**peer route-policy**](cmdqueryname=peer+route-policy) command). If both commands are run, the **peer route-priority-track interface** command configuration takes effect in the case of a link fault.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) **peer** *ipv4-address* **received-routes** command to check information about routes received by BGP from the specified peer.