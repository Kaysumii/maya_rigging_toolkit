# Maya Rigging Toolkit

## Project Description

The Maya Rigging Toolkit is a Python-based tool designed to make the rigging process in Autodesk Maya easier and more efficient. Rigging involves repetitive tasks such as creating controls, aligning them with joints, and setting up constraints. This toolkit automates some of those tasks to save time.

The toolkit uses Python and Maya's `maya.cmds` library. Users manually create and position their joints before running the script. The toolkit can then generate controls, automatically color them based on their names, resize their CVs, and reset their transformations.

The project runs directly through Maya's Python Script Editor and does not require a separate user interface.

Optional: Users may set up this script as hotkeys in their rigging toolbar, so they don't have to run each script through the editor. 

## Project Links

**Demonstration Video:** [Add YouTube video URL]

**GitHub Repository:** [https://github.com/Kaysumii/maya_rigging_toolkit]

## Features

### 1. Automatic Control Creation

Creates NURBS circle controls for selected joints. Each control is automatically named, grouped, aligned with its corresponding joint, and connected using a Parent Constraint with Maintain Offset enabled.

### 2. Control Customization

The toolkit includes two customization options:

- **Automatic Coloring:** Controls beginning with `L_` are blue, controls beginning with `R_` are red, and all other controls are yellow.
- **CV Scaling:** Users can increase or decrease the size of selected controls by scaling their control vertices, cvs, without changing the control's transform scale.

### 3. Reset Controls

Resets the translation and rotation of selected controls to zero. This allows users to return controls to their original positions without changing their customized CV sizes.

## Requirements

- Autodesk Maya with Python scripting support
- Python (provided through Maya)
- Maya's built-in `maya.cmds` library

No additional pip-installable packages are required.

## Project Files

- `src/project.py` — Contains the toolkit's Python functions.
- `requirements.txt` — Lists external Python dependencies. None required for this project
- `README.md` — Contains project information and instructions.
- `proposal.md` — Contains the original project proposal, if included in the repository.

## How to Run the Toolkit

1. Open Autodesk Maya.
2. Create and position the joints you want to rig.
3. Open `src/project.py` in a text editor and copy the entire Python script.
4. In Maya, open **Windows → General Editors → Script Editor**. Or navigate to
the semicolon (;) located on the bottom right of the Maya window.
5. Switch to the Python tab.
6. Paste the script into the editor and execute it. Without anything being
selected
7. The Script Editor will display the available toolkit commands.

Once the script is loaded, you can execute individual functions in Maya's Python Script Editor.

### Available Commands

**Create Controls**

Select one or more joints and run:

```python
create_control()
```

**Color Controls**

Run the following command to automatically color existing controls based on their names:

```python
color_control()
```

**Increase Control Size**

Select one or more controls and run:

```python
scale_controls(1.1)
```

**Decrease Control Size**

Select one or more controls and run:

```python
scale_controls(0.9)
```

**Reset Controls**

Select one or more controls and run:

```python
reset_controls()
```

The controls should end with `_CON` for the scaling and reset functions to recognize them.

## Design Considerations

One of the main considerations was making the toolkit simple to use without creating a separate interface. Each feature was organized into its own function so users could run commands individually.

Another consideration was maintaining clean control transformations. Controls are placed inside groups that align with the joints, allowing their translation and rotation values to begin at zero. Scaling the CVs instead of the control transforms also helps preserve these values.

The toolkit uses loops to process multiple selected objects, conditional statements to check selections and control names, and function parameters to customize control sizes.

## Limitations

The toolkit currently creates circle-shaped controls only. Joints must be created and positioned manually before running the control creation function.

The script also does not automatically detect or remove existing controls and constraints, so users should avoid creating duplicate controls for the same joints.

## Future Improvements

Future improvements could include additional control shapes, automatic IK handle creation, hierarchy setup, and control mirroring. These features would allow the toolkit to support more advanced rigging tasks.

## Conclusion

This project has helped me practice using Python to automate tasks in Autodesk Maya. Through creating functions for control creation, coloring, scaling, and resetting, I gained more experience working with loops, conditionals, parameters, and Maya commands. The finished toolkit provides a simple way to complete repetitive rigging tasks more efficiently.