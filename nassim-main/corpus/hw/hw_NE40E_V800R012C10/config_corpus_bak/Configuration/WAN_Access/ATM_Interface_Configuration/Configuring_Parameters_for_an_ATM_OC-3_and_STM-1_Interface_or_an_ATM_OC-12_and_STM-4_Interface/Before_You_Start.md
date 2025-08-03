Before You Start
================

Before configuring parameters for ATM interfaces, familiarize yourself with the usage scenario, complete the pre-configuration task, and obtain the required data. This can help you complete the configuration task quickly and accurately.

#### Usage Scenario

You can set these parameters according to the actual conditions of the ATM network so that these parameters can perfectly match the physical network.

The parameters of the ATM interface include the frame format, scramble function, loopback mode, and interval for traffic statistics collection. All these parameters have default configurations.

However, ATM sub-interface parameters, such as the frame format, scramble function,
and loopback mode, cannot be configured. If those parameters are configured on the ATM main interface, the sub-interface inherits the parameters automatically.

The configured interval for traffic statistics collection on the ATM main interface cannot be inherited by the sub-interface, and it needs to be configured on the sub-interface.

These parameters must be configured on an ATM interface that needs to be encapsulated with an upper layer protocol.


#### Pre-configuration Tasks

Before configuring an ATM interface, power on and start the Router normally.


#### Data Preparation

To configure an ATM interface, you need the following data.

| No. | Data |
| --- | --- |
| 1 | Number of the ATM interface |