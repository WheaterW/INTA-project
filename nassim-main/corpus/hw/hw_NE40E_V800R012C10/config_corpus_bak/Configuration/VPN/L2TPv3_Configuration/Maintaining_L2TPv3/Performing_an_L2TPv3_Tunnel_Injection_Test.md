Performing an L2TPv3 Tunnel Injection Test
==========================================

An L2TPv3 tunnel injection test is used to test traffic forwarding in the upstream and downstream directions.

#### Pre-configuration Tasks

* A working tunnel has been configured.

#### Procedure

1. Configure basic L2TPv3 functions (see [Configuring Basic L2TPv3 over IPv6 Functions](dc_vrp_l2tpv3_cfg_000005.html)) but do not bind the L2TPv3 tunnel to any services.
2. Configure the L2TPv3 tunnel as an injection tunnel.
   1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
   2. Run the [**l2tpv3 instance**](cmdqueryname=l2tpv3+instance) *instance-name* command to configure an L2TPv3 instance on the interface and enter the L2TPv3 instance view.
   3. Run the [**l2tpv3 static binding pw**](cmdqueryname=l2tpv3+static+binding+pw) *pwname* **injected** command to bind an L2TPv3 tunnel to the L2TPv3 instance and specify the tunnel as an injection tunnel.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

Run the [**display l2tpv3 pw**](cmdqueryname=display+l2tpv3+pw) *pwname* command to check whether the L2TPv3 PW is correctly configured.

Run the [**display l2tpv3 statistics pw**](cmdqueryname=display+l2tpv3+statistics+pw) *pwname* command to check packet statistics about the L2TPv3 PW.