
# Maya Rigging Toolkit

## Repository
<https://github.com/Kaysumii/maya_rigging_toolkit.git>

## Description
I want to create a Python-based rigging toolkit for Autodesk Maya that helps automate repetitive tasks during the character rigging process. 
This program will allow user to generate controls, organize them into groups following proper naming functions, and connect them to the selected joints.
I also want to include customization options to make the tool easier to use. 
I chose this project because I'm interested in specializing in character rigging, and I know rigging requires a lot of repetitive tasks, so I wanted to make something to help move the process along.

## Features
- Automatic Control Creation
	- Generates NURBS curve controls for selected joints, automatically names and groups them, aligns and parent constrains them to their corresponding joints.
- Control Customization
	- Allow users to choose different control shapes, sizes and colors.
- Reset Controls
	- Create a function that resets selected controls to their default transformations.
## Challenges
- Learning how to use Maya's Python commands to automate different rigging tasks, as incorrect transforms and cause a rig to behave incorrectly.
- Making sure the script works correctly with different joint hierarchies and selections without errors

## Outcomes
Ideal Outcome:
- I hope to have a functioning Maya rigging toolkit that allows users to create, customize, and organize controls.
- I want the program to be useful for myself and other animation students who desire to do character rigging.
- To improve my understanding of python functions, loops, etc.

Minimal Viable Outcome:
- The code works correctly and effectively.
## Milestones

- Week 1 Research and Setup
  1. Research Maya's python commands
  2. Set up and test python scripts within Maya
  
- Week 2 Control Creation
  1. Create a function that generates controls for selected joints
  2. automatically name, group, align and connect controls to selected joints
  3. Test the functions on different joint hierarchies

- Week 3 Control Customization
  1. Add different control shapes, sizes, and colors.
  2. Test the customization options
  3. Create a reset control feature

- Week 4 (Final) 
  1. Test the toolkit on different character rigs
  2. Fix bugs related to alignment, parentin
