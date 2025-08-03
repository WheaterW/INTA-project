Configuration Management Configuration
======================================

The system provides two configuration validation modes to ensure configuration reliability.

#### Context

As increasingly new types of services emerge, higher requirements are imposed on devices. For example, it is required that services take effect after being configured, invalid configurations be discarded, and impact on the existing services be minimized.

To ensure reliable user configurations, the system allows two-phase configuration validation. In the first phase, the system performs syntax and semantics checks. In the second phase, configurations take effect and are used for services.


[Overview of Configuration Management](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfgm_cfg_0001.html)

The system supports two configuration validation modes: immediate validation and two-phase validation. By default, the two-phase validation mode takes effect. The system also supports offline configuration, which means that you can change interface configurations after a board is removed.

[Configuration Precautions for Configuration Management](../../../../software/nev8r10_vrpv8r16/user/spec/Configuration_Management_limitation.html)



[Configuring a Validation Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfgm_cfg_0002.html)

You can configure the immediate or two-phase validation mode for different reliability requirements.

[Disabling the Re-confirmation Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfgm_cfg_0050.html)

Some device commands may result in serious consequences if operations are not properly performed. To avoid misoperations, re-confirmation is required by default.

[Performing Configuration Rollback](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfgm_cfg_0044.html)

Configuration rollback allows the system to roll back to a specified historical configuration state. This section describes how to roll the system back to a previous configuration.

[Managing Configuration Files](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfgm_cfg_0020.html)

You can manage configuration files, for example, set the configuration file to be loaded at the next startup or save the configuration file.

[Configuration Examples for Configuration Management](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfgm_cfg_0031.html)

This section provides configuration management examples.