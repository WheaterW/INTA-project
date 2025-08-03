Enabling LSP Fragment Extension on an IPv6 IS-IS Device
=======================================================

Enabling LSP Fragment Extension on an IPv6 IS-IS Device

#### Prerequisites

Before enabling LSP fragment extension on an IPv6 IS-IS device, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

After LSP fragment extension is configured, an IPv6 IS-IS device can generate more LSP fragments to advertise more routing information.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) process-id
   ```
3. Enable LSP fragment extension for the IS-IS process.
   
   
   ```
   [lsp-fragments-extend](cmdqueryname=lsp-fragments-extend) [ [ level-1 | level-2 | level-1-2 ] | [ mode-1 | mode-2 ] ] *
   ```
   
   
   
   By default, LSP fragment extension is disabled for IS-IS processes.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If non-Huawei devices also exist on the network, set the working mode of LSP fragment extension to mode 1. Otherwise, the non-Huawei devices may fail to identify the LSPs sent by Huawei devices.
4. Configure a virtual system.
   
   
   ```
   [virtual-system](cmdqueryname=virtual-system) virtual-system-id
   ```
   
   To allow the device to generate extended LSP fragments, configure at least one virtual system ID. The system ID of the virtual system must be unique in the entire routing domain.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display isis statistics**](cmdqueryname=display+isis+statistics) [ **updated-lsp**  [ **history** ] ] [ **level-1** | **level-2** | **level-1-2** ] [ *process-id* | **vpn-instance** *vpn-instance-name* ] or [**display isis**](cmdqueryname=display+isis) *process-id* **statistics** [ [ [ **updated-lsp**  [ **history** ] ] [ **level-1** | **level-2** | **level-1-2** ] ] | [ **packet** ] ] command to check IS-IS process statistics.