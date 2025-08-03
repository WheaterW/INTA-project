Understanding a Feature Software Package
========================================

A feature software package provides component-based service capabilities for specific valuable features based on a basic software package. One package corresponds to one feature and can be independently installed or uninstalled. See [Figure 1](#EN-US_CONCEPT_0000001513049246__fig1185745144612). Feature software packages can be installed, uninstalled, or upgraded on an in-service device. To add new features or implement in-service incremental upgrade of features based on service requirements, you can install or upgrade feature software packages separately without requiring the basic software package to be upgraded.

**Figure 1** Feature software package  
![](figure/en-us_image_0000001512690122.png)
A feature software package supports the following basic functions:

* Online installation/uninstallation of a feature software package: After a device starts, you can install a new feature software package (\*.ccx) or uninstall a loaded feature software package based on service requirements, such as new features. After a feature software package is installed, its function is automatically enabled. Similarly, after it is uninstalled, its function is automatically disabled.
* In-service upgrade of a feature software package: Huawei releases later versions of a feature software package to enhance feature capabilities, optimize feature performance, or resolve feature package problems. You can upgrade a feature software package based on service requirements.
* Rollback of a feature software package: If an exception occurs during the upgrade of a feature software package, this package will be automatically rolled back to the source version. After a feature software package is upgraded, if the related features become abnormal or the package cannot meet service requirements, you can roll back the package to the source version. For details about the rollback process, see [Configuring In-Service Upgrade of a Feature Software Package](gx_upgrade_cfg_0012.html) and [Specifying the Feature Software Package That Takes Effect at the Next Startup](gx_upgrade_cfg_0014.html). Use the feature software package of the source version.

This document describes only key upgrade operations. For details about a device upgrade and each released version, obtain the corresponding upgrade guide.

#### Obtaining a Feature Software Package

1. Visit [Huawei enterprise technical support website](https://support.huawei.com/enterprise/en/index.html) and select the corresponding product in the software download area.
2. Select the desired feature software package.
3. Click **Download** next to the ***XXX*****.ccx** file (named in the format of product name + version number + feature name) of the required version.

![](public_sys-resources/note_3.0-en-us.png) 

The version of a feature software package must match that of the system software. Otherwise, the package cannot be successfully loaded.