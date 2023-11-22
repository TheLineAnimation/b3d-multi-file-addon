<a href="https://thelineanimation.com/">
    <img src="https://thelineanimation.github.io/playblast-plus/_static/thelinelogo.png" alt="Aimeos logo" title="Aimeos" height="60" />
</a>

<br>

# Blender - Multi-File Addon Template


### Addon Boilerplate Code

Writing a blender add-on can be confusing, especially when you want to start adding more complex modules and operators that have their own dependencies. 

It's much easier to manage these in separate files rather than one big, long .py file that's impossible to update and understand.

- This example is inspired by the following Blender Add-ons :
    - Flamenco
    - Magic UV

### To Use

Clone the repo and adjust the code as required! 

### How it works

The module `init.py` call the register functions on the addon global preferences, any properties needed by the add-on, and the operator and secondary utilities.
```
.
📁── b3d-multi-file-addon
    📁── op
    │   📄── op_one.py
    │   📄── op_two.py
    │   ├── [add extra operators here and register their names in init.py]
    │   📄── __init__.py
    📁── utils
    │   📄── __init__.py
    │   └── [add custom python modules here]
    📄── preferences.py
    📄── properties.py
    📄── ui.py
    📄── __init__.py
    
```

### Pre-Requisites

You'll need to know Python, and how Blender's code ecosystem functions, otherwise it
won't make much sense.

Will work in any Blender version over 2.8. (Properties syntax changed prior to this)