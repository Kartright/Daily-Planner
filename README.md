# Daily-Planner
Python program for building and saving simple daily planners.
Events are sorted chronologically so there is no need to worry about the order in which events are added to planners.

**Creating Planners:**
When creating a planner you will be prompted to input how many days from today's date the intended planner date is.
This input should be a single integer. To create a planner for today's date simply input 0.

When creating an event for a planner there are two prompts:

1. The first prompt is the name of the event. This can be any string.

2. The second prompt is the time the event will take place.
   The time should be input in 24-hour time (HH:MM)

To stop adding events simply input 'exit'

New planners will be saved as simple text files to the working directory of the program file.

**Loading Planners:**
Loading a planner will display the desired planner in the console window.

When loading a planner it will prompt for the date of the desired planner.
The date should be input as 'Day Month Year' Where the day is in numerical form (00) and the month is written in full (e.g. January).

**Editing Planners:**
Editing a planner allows the user to add new events to a pre-existing planner.

When editing a planner it will prompt for the date of the desired planner.
The date should be input as 'Day Month Year' Where the day is in numerical form (00) and the month is written in full (e.g. January).

The user will then be prompted to add more events (See **Creating Planners** on how to input events)

when the user is finished adding events they will input 'exit' and the new edited planner will be displayed in the console.


