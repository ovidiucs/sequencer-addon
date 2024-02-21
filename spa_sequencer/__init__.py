# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2023, The SPA Studios. All rights reserved.

import bpy
import importlib

# List of submodule names as strings
submodules = [
    "editorial",
    "keymaps",
    "preferences",
    "render",
    "sequence",
    "shared_folders",
    "shot",
    "sync",
]

# Reload guard
for submodule in submodules:
    if submodule in locals():
        importlib.reload(locals()[submodule])
    else:
        exec(f"from . import {submodule}")

# Now, you can safely reference the modules directly
from spa_sequencer import (
    editorial,
    keymaps,
    preferences,
    render,
    sequence,
    shared_folders,
    shot,
    sync,
)

bl_info = {
    "name": "Sequencer",
    "author": "The SPA Studios",
    "description": "Toolset to improve the sequence workflow in Blender.",
    "blender": (4, 0, 0),
    "version": (1, 0, 1),
    "location": "",
    "warning": "",
    "category": "SPA",
}

packages = (
    sync,
    shot,
    sequence,
    render,
    editorial,
    shared_folders,
    preferences,
    keymaps,
)

def register():
    print("Starting addon registration")
    for package in packages:
        print(f"Registering package: {package.__name__}")
        package.register()
    print("Addon registration completed")

def unregister():
    print("Starting addon unregistration")
    for package in reversed(packages):
        print(f"Unregistering package: {package.__name__}")
        package.unregister()
    print("Addon unregistration completed")
